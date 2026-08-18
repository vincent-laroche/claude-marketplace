#!/usr/bin/env python3
"""Find theme code that bypasses native Shopify theme settings.

Seven scans, each answering one question a merchant would ask after changing a
setting and seeing nothing happen. Read-only: nothing here writes, commits, or
contacts a store.

    scan_native_settings.py [--root DIR] [--baseline REV] [scan ...]

Scans: overrides, dead-tokens, schema-defaults, section-controls, literals,
strings, orphan-settings. Default runs all.

Exit code is 1 when any scan reports a finding, so it can gate a commit.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

RUNTIME_DIRS = ("assets", "blocks", "layout", "sections", "snippets", "templates", "config")
SOURCE_SUFFIXES = (".liquid", ".css", ".json", ".js")

# The snippets that turn theme settings into CSS custom properties. A variable
# declared here is settings-derived: whatever the merchant picks in the editor
# arrives through it.
SETTINGS_LAYER = (
    "snippets/theme-styles-variables.liquid",
    "snippets/color-palette.liquid",
)

ROOT_BLOCK = re.compile(r":root[^{]*\{")
# A value that carries its own literal, once var() references are removed.
VALUE_LITERAL = re.compile(
    r"#[0-9a-fA-F]{3,8}\b|\d+(?:\.\d+)?(?:px|rem|em|vw|vh|%|s|ms)\b|[\"'][^\"']+[\"']")
# Scoped cascade resets, not overrides.
RESET_VALUES = {"inherit", "initial", "unset", "revert", "none", "0"}

DECL = re.compile(r"(--[a-zA-Z][\w-]*)\s*:")
VAR_USE = re.compile(r"var\(\s*(--[a-zA-Z][\w-]*)")
SCHEMA = re.compile(r"\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}", re.S)
JS_BLOCK = re.compile(r"\{%-?\s*javascript\s*-?%\}(.*?)\{%-?\s*endjavascript\s*-?%\}", re.S)
STYLE_LIKE = re.compile(r"(?:\{%-?\s*stylesheet\s*-?%\}|\{%-?\s*style\s*-?%\})(.*?)"
                        r"(?:\{%-?\s*endstylesheet\s*-?%\}|\{%-?\s*endstyle\s*-?%\})", re.S)
TEXT_NODE = re.compile(r">([^<>{}]*[A-Za-z][^<>{}]*)<")
JS_LITERAL = re.compile(r"'([A-Z][a-z][^']{3,})'|\"([A-Z][a-z][^\"]{3,})\"")

# A colour written out rather than referenced. rgb(var(--token) / 0.5) is
# token-driven and does NOT count -- var() references are stripped first, and
# what remains must still name a colour.
COLOR_LITERAL = re.compile(
    r"#[0-9a-fA-F]{3,8}\b|\brgba?\(\s*\d|\bhsla?\(\s*\d", re.I)
PX = re.compile(r"(?<![\w-])(\d+(?:\.\d+)?)px\b")

# Properties where a literal shadows a control the merchant already has. A
# literal width on an icon is not a finding; a literal page width is.
SETTING_SHADOWS = {
    "max-width": "Theme settings > Layout > Page width",
    "border-radius": "Theme settings > corner-radius controls",
    "padding-block": "the section's Padding controls",
    "padding-block-start": "the section's Padding controls",
    "padding-block-end": "the section's Padding controls",
    "font-size": "Theme settings > Typography sizes",
}
# Below these, a literal is component detail rather than a shadowed setting.
SHADOW_MIN_PX = {"max-width": 600, "border-radius": 0, "padding-block": 24,
                 "padding-block-start": 24, "padding-block-end": 24, "font-size": 0}

# Cart/HTTP plumbing, not customer copy.
JS_LITERAL_ALLOW = {"Content-Type", "Accept"}


def read(p: pathlib.Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def source_files(root: pathlib.Path) -> list[pathlib.Path]:
    out = []
    for d in RUNTIME_DIRS:
        base = root / d
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.suffix in SOURCE_SUFFIXES:
                out.append(p)
    return out


def changed_files(root: pathlib.Path, baseline: str) -> list[pathlib.Path] | None:
    """Files that deviate from the upstream baseline -- where hardcoding lives."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "diff", "--name-only", f"{baseline}..HEAD", "--", *RUNTIME_DIRS],
            capture_output=True, text=True, check=True).stdout.split()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return [root / f for f in out if (root / f).is_file() and (root / f).suffix in SOURCE_SUFFIXES]


def rel(root: pathlib.Path, p: pathlib.Path) -> str:
    try:
        return str(p.relative_to(root))
    except ValueError:
        return str(p)


def line_of(text: str, idx: int) -> int:
    return text.count("\n", 0, idx) + 1


# --------------------------------------------------------------------------- scans

def _settings_layer_vars(root):
    """Exact names and template stems the settings layer emits.

    Horizon builds some names from a `[placeholder]` template
    ('--font-size--[font_size]'), so the literal token never appears in source.
    Harvesting the stem is what catches an override of --font-size--h2.
    """
    exact, stems = set(), set()
    for f in SETTINGS_LAYER:
        p = root / f
        if not p.is_file():
            continue
        t = read(p)
        exact |= {m.group(1) for m in DECL.finditer(t)}
        stems |= {m.group(1) for m in re.finditer(r"(--[a-zA-Z][\w-]*)\[", t)}
    return exact, stems


def _root_spans(s):
    for m in ROOT_BLOCK.finditer(s):
        i, depth = m.end(), 1
        while i < len(s) and depth:
            depth += (s[i] == "{") - (s[i] == "}")
            i += 1
        yield m.end(), i


def scan_overrides(root, files):
    """A settings-derived variable redefined at :root with its own literal.

    Scope is the whole signal. A redefinition inside a component class is
    ordinary cascade work; one at :root replaces the merchant's choice
    everywhere, and nothing in the editor says so.
    """
    exact, stems = _settings_layer_vars(root)
    if not exact:
        return ["settings layer not found — is --root a Horizon theme?"]
    out = []
    for p in files:
        if p.suffix not in (".liquid", ".css") or rel(root, p) in SETTINGS_LAYER:
            continue
        s = read(p)
        for a, b in _root_spans(s):
            for m in re.finditer(r"(--[a-zA-Z][\w-]*)\s*:\s*([^;{}\n]+)", s[a:b]):
                name, val = m.group(1), m.group(2).strip()
                if not (name in exact or any(name.startswith(x) for x in stems)):
                    continue
                if val in RESET_VALUES:
                    continue
                if not VALUE_LITERAL.search(re.sub(r"var\([^)]*\)", "", val)):
                    continue
                out.append(f"{rel(root, p)}:{line_of(s, a + m.start())}"
                           f"  :root override  {name} = {val[:60]}")
    return out


def scan_dead_tokens(root, files, prefix):
    """Custom properties declared and never read.

    Matches declarations ANYWHERE on a line. A line-start anchor misses every
    token declared second on a shared line, which under-reports silently.
    """
    declared, used = {}, set()
    for p in files:
        if p.suffix == ".json":
            continue
        s = read(p)
        for m in DECL.finditer(s):
            if m.group(1).startswith(prefix):
                declared.setdefault(m.group(1), rel(root, p))
        used |= {m.group(1) for m in VAR_USE.finditer(s)}
    dead = sorted(t for t in declared if t not in used)
    missing = sorted(t for t in used if t.startswith(prefix) and t not in declared)
    out = [f"{declared[t]}  {t} declared, never read" for t in dead]
    out += [f"(nowhere)  {t} read, never declared" for t in missing]
    return out


def _schema_of(text):
    m = SCHEMA.search(text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except ValueError:
        return None


def _walk_settings(node):
    if isinstance(node, dict):
        for s in node.get("settings", []) or []:
            yield s
        for b in node.get("blocks", []) or []:
            yield from _walk_settings(b)


def scan_schema_defaults(root, files):
    """`default:` on a text/textarea input.

    Shopify re-seeds these on theme update and they cannot be translated. A
    `t:` key is fine -- that is Shopify's own translatable convention.
    """
    out = []
    for p in files:
        if p.suffix != ".liquid":
            continue
        d = _schema_of(read(p))
        if not d:
            continue
        for s in _walk_settings(d):
            if s.get("type") in ("text", "textarea") and "default" in s:
                val = str(s["default"])
                if val.startswith("t:"):
                    continue
                out.append(f"{rel(root, p)}  {s.get('id')}  default={val[:60]!r}")
    return out


def scan_section_controls(root, files):
    """Sections offering no colour, width, or padding control."""
    out = []
    for p in files:
        if p.suffix != ".liquid" or p.parent.name != "sections":
            continue
        d = _schema_of(read(p))
        if not d or "settings" not in d:
            continue
        types = {s.get("type") for s in d.get("settings", [])}
        ids = {s.get("id") for s in d.get("settings", [])}
        missing = []
        if not types & {"color", "color_scheme"}:
            missing.append("colour")
        if "section_width" not in ids:
            missing.append("width")
        if "padding-block-start" not in ids:
            missing.append("padding")
        if missing:
            out.append(f"{rel(root, p)}  no {', '.join(missing)} control")
    return out


def scan_literals(root, files):
    """Literal values that shadow a native setting.

    Deliberately narrow. Flagging every literal buries the few that matter and
    teaches the reader to skim past all of them.
    """
    out = []
    for p in files:
        if p.suffix not in (".liquid", ".css"):
            continue
        s = read(p)
        blocks = ([(0, s)] if p.suffix == ".css"
                  else [(m.start(1), m.group(1)) for m in STYLE_LIKE.finditer(s)])
        for offset, css in blocks:
            for dm in re.finditer(r"(?m)^[^\S\n]*([a-z-]+)\s*:\s*([^;{}\n]+);", css):
                prop, val = dm.group(1), dm.group(2).strip()
                if prop.startswith("--") or "{{" in val or "{%" in val:
                    continue
                bare = re.sub(r"var\([^)]*\)", "", val)
                ln = line_of(s, offset + dm.start())
                if COLOR_LITERAL.search(bare):
                    out.append(f"{rel(root, p)}:{ln}  hardcoded colour  "
                               f"{prop}: {val[:60]}  -> the Color palette")
                    continue
                if prop in SETTING_SHADOWS and "var(" not in val:
                    px = [float(x) for x in PX.findall(bare)]
                    if px and max(px) >= SHADOW_MIN_PX[prop]:
                        out.append(f"{rel(root, p)}:{ln}  shadows a setting  "
                                   f"{prop}: {val[:50]}  -> {SETTING_SHADOWS[prop]}")
    return out


def scan_strings(root, files):
    """Customer-facing strings baked into section markup or a javascript block.

    A section javascript block is served as a static asset and cannot read
    `section.settings`; its strings need a rendered JSON bridge.
    """
    out = []
    for p in files:
        if p.suffix != ".liquid" or p.parent.name not in ("sections", "blocks", "snippets"):
            continue
        s = read(p)
        markup = SCHEMA.sub("", STYLE_LIKE.sub("", JS_BLOCK.sub("", s)))
        n = sum(1 for m in TEXT_NODE.finditer(markup) if len(m.group(1).strip()) > 2)
        js_hits = []
        for jm in JS_BLOCK.finditer(s):
            for lm in JS_LITERAL.finditer(jm.group(1)):
                lit = lm.group(1) or lm.group(2)
                if lit not in JS_LITERAL_ALLOW:
                    js_hits.append(lit)
        if n or js_hits:
            bits = []
            if n:
                bits.append(f"{n} markup string(s)")
            if js_hits:
                bits.append(f"{len(js_hits)} script string(s): "
                            + ", ".join(sorted(set(js_hits))[:4]))
            out.append(f"{rel(root, p)}  {'; '.join(bits)}")
    return out


def scan_orphan_settings(root):
    """settings_schema.json entries never referenced in source.

    Horizon builds some keys dynamically ('type_size_[h]'), so a hit here is a
    lead to confirm by hand, not a finding. Reported separately for that reason.
    """
    schema_path = root / "config" / "settings_schema.json"
    if not schema_path.is_file():
        return []
    try:
        groups = json.loads(read(schema_path))
    except ValueError:
        return [f"{rel(root, schema_path)}  does not parse"]
    ids = [(g.get("name", "?"), s["id"])
           for g in groups if isinstance(g, dict)
           for s in g.get("settings", []) if s.get("id")]
    corpus = "".join(read(p) for p in source_files(root))
    return [f"[{g}] {i}  never referenced (confirm: may be built dynamically)"
            for g, i in ids
            if f"settings.{i}" not in corpus and f"settings['{i}']" not in corpus]


SCANS = {
    "overrides": "Theme code redefining a Horizon custom property",
    "dead-tokens": "Custom properties declared and never read",
    "schema-defaults": "`default:` on a text/textarea input",
    "section-controls": "Sections with no colour, width, or padding control",
    "literals": "Literal colours and sizes in style blocks",
    "strings": "Customer-facing strings baked into markup or script",
    "orphan-settings": "Schema settings never referenced (leads, not findings)",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scans", nargs="*", choices=sorted(SCANS), default=None,
                    metavar="SCAN", help="One or more of: " + ", ".join(sorted(SCANS)))
    ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    ap.add_argument("--baseline", help="Upstream baseline rev; limits scans to files that deviate")
    ap.add_argument("--prefix", default="--az-", help="Custom-property prefix for dead-tokens")
    args = ap.parse_args()

    scans = args.scans or sorted(SCANS)
    root = args.root.resolve()
    everything = source_files(root)
    if not everything:
        print(f"no theme source under {root}", file=sys.stderr)
        return 2

    scoped = everything
    if args.baseline:
        c = changed_files(root, args.baseline)
        if c is None:
            print(f"warning: baseline {args.baseline!r} unreachable; scanning all files\n",
                  file=sys.stderr)
        else:
            scoped = c
            print(f"scoped to {len(scoped)} file(s) deviating from {args.baseline}\n")

    findings = 0
    for name in scans:
        if name == "overrides":
            rows = scan_overrides(root, scoped)
        elif name == "dead-tokens":
            rows = scan_dead_tokens(root, everything, args.prefix)
        elif name == "schema-defaults":
            rows = scan_schema_defaults(root, scoped)
        elif name == "section-controls":
            rows = scan_section_controls(root, scoped)
        elif name == "literals":
            rows = scan_literals(root, scoped)
        elif name == "strings":
            rows = scan_strings(root, scoped)
        else:
            rows = scan_orphan_settings(root)

        print(f"## {name} — {SCANS[name]}")
        if rows:
            for r in rows:
                print(f"  {r}")
            print(f"  ({len(rows)} finding(s))\n")
            if name != "orphan-settings":
                findings += len(rows)
        else:
            print("  clean\n")

    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
