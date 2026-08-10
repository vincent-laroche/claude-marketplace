#!/usr/bin/env python3
"""Read-only scanner for likely visual-identity residue in conversion targets."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


TEXT_EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".html", ".htm", ".liquid",
    ".hubl", ".mjml", ".jsx", ".tsx", ".js", ".ts", ".vue",
    ".svelte", ".json", ".md", ".txt", ".xml", ".svg",
}

SKIP_DIRS = {
    ".git", "node_modules", "dist", "build", ".next", ".vinext",
    ".wrangler", "coverage", "vendor",
}

ATELIER_HEX = {
    "#EFE7D2", "#ECE4CF", "#DDD2B6", "#15140F", "#2A2620", "#5A5448",
    "#8B8676", "#ED6F5C", "#F08E7C", "#E9B94A", "#6E7448", "#F7F1DE",
}

RETIRED_HEX = {
    "#0F0F0F": "Ink role now resolves through the current Atelier Zero source",
    "#1B1B1B": "retired Body Black",
    "#2A2929": "retired Soft Black",
    "#14213D": "retired Harbor Navy",
    "#FAFAFA": "retired Off White",
    "#E5E5E5": "retired Soft Silver",
    "#D6D6D6": "retired Muted Silver",
    "#A63E1B": "retired Copper Clay",
}

LEGACY_FONTS = (
    "Instrument Serif", "Geist Mono", "Geist", "Roboto", "Montserrat",
    "Poppins", "Helvetica Neue",
)

HEX_RE = re.compile(r"(?<![\w-])#[0-9a-fA-F]{3,8}\b")
FUNCTION_COLOR_RE = re.compile(r"\b(?:rgb|rgba|hsl|hsla)\s*\([^)]*\)", re.I)
FONT_DECL_RE = re.compile(r"font-family\s*:\s*([^;}{]+)", re.I)
GRADIENT_RE = re.compile(r"\b(?:linear|radial|conic)-gradient\s*\(", re.I)
SHADOW_RE = re.compile(r"box-shadow\s*:\s*([^;}{]+)", re.I)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan source files for likely non-Atelier colors, fonts, and effects."
    )
    parser.add_argument("targets", nargs="+", type=Path)
    parser.add_argument(
        "--surface", choices=("web", "email", "social"), default="web"
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 when findings exist. Default is report-only exit 0.",
    )
    return parser.parse_args()


def iter_files(targets: list[Path]):
    seen: set[Path] = set()
    for target in targets:
        target = target.expanduser().resolve()
        if target.is_file():
            candidates = (target,)
        elif target.is_dir():
            candidates = (
                path for path in target.rglob("*")
                if path.is_file()
                and path.suffix.lower() in TEXT_EXTENSIONS
                and not any(part in SKIP_DIRS for part in path.parts)
            )
        else:
            raise FileNotFoundError(f"Target does not exist: {target}")

        for path in candidates:
            if path not in seen:
                seen.add(path)
                yield path


def add_finding(findings, path: Path, line: int, kind: str, value: str, message: str):
    findings.append({
        "file": str(path),
        "line": line,
        "kind": kind,
        "value": value,
        "message": message,
    })


def scan_file(path: Path, surface: str, findings: list[dict[str, object]]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return

    for line_number, line in enumerate(text.splitlines(), 1):
        for match in HEX_RE.finditer(line):
            value = match.group(0).upper()
            if value in RETIRED_HEX:
                add_finding(
                    findings, path, line_number, "retired-color", value,
                    RETIRED_HEX[value],
                )
            elif surface in {"email", "social"} and value not in ATELIER_HEX:
                add_finding(
                    findings, path, line_number, "non-atelier-color", value,
                    "Literal color is outside the current Atelier Zero palette; inspect its role.",
                )
            elif surface == "web":
                add_finding(
                    findings, path, line_number, "raw-color", value,
                    "Web source should normally use a current token; token definitions and required platform config are exceptions.",
                )

        for match in FUNCTION_COLOR_RE.finditer(line):
            add_finding(
                findings, path, line_number, "functional-color", match.group(0),
                "Inspect RGB/HSL color residue and map it to a current semantic role.",
            )

        lower_line = line.lower()
        for font in LEGACY_FONTS:
            if font.lower() in lower_line:
                if any(
                    font.lower() in longer.lower()
                    and len(longer) > len(font)
                    and longer.lower() in lower_line
                    for longer in LEGACY_FONTS
                ):
                    continue
                add_finding(
                    findings, path, line_number, "legacy-font", font,
                    "Replace the selected type role unless this is historical documentation or a fallback explicitly allowed by the current platform spec.",
                )

        for match in FONT_DECL_RE.finditer(line):
            add_finding(
                findings, path, line_number, "font-declaration", match.group(1).strip(),
                "Inventory this declaration and verify it against the current platform-specific type contract.",
            )

        if GRADIENT_RE.search(line):
            add_finding(
                findings, path, line_number, "gradient", line.strip(),
                "Only the currently documented Atelier Zero texture/effect is allowed; inspect before retaining.",
            )

        for match in SHADOW_RE.finditer(line):
            value = match.group(1).strip()
            if "var(--" not in value and value.lower() != "none":
                add_finding(
                    findings, path, line_number, "raw-shadow", value,
                    "Map hand-rolled elevation to a current documented token or remove it.",
                )


def main() -> int:
    args = parse_args()
    findings: list[dict[str, object]] = []
    files = list(iter_files(args.targets))
    for path in files:
        scan_file(path, args.surface, findings)

    counts = Counter(str(item["kind"]) for item in findings)
    result = {
        "surface": args.surface,
        "files_scanned": len(files),
        "findings": findings,
        "summary": dict(sorted(counts.items())),
    }

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        for item in findings:
            print(
                f"{item['file']}:{item['line']} [{item['kind']}] "
                f"{item['value']} :: {item['message']}"
            )
        print(f"Scanned {len(files)} file(s); {len(findings)} finding(s).")
        if counts:
            print("Summary: " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))

    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
