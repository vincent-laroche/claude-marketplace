#!/usr/bin/env python3
"""Report prefixed CSS classes defined in CSS versus mentioned in theme markup."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CSS_EXTENSIONS = {".css", ".scss", ".sass", ".less"}
MARKUP_EXTENSIONS = {".liquid", ".json", ".html", ".htm", ".js", ".ts", ".jsx", ".tsx"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare prefixed CSS selectors with mentions in Liquid/theme markup."
    )
    parser.add_argument("--prefix", required=True, help="Class prefix to inspect, e.g. az-")
    parser.add_argument("--css", nargs="+", required=True, help="CSS file(s) or directory/directories")
    parser.add_argument(
        "--markup", nargs="+", required=True, help="Markup file(s) or directory/directories"
    )
    parser.add_argument("--strict", action="store_true", help="Exit 1 if any defined class is not mentioned")
    return parser.parse_args()


def collect(paths: list[str], extensions: set[str]) -> list[Path]:
    files: set[Path] = set()
    for raw_path in paths:
        path = Path(raw_path).expanduser()
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        if path.is_file():
            if path.suffix.lower() in extensions:
                files.add(path)
        else:
            files.update(candidate for candidate in path.rglob("*") if candidate.is_file() and candidate.suffix.lower() in extensions)
    return sorted(files)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        raise RuntimeError(f"Could not read {path}: {error}") from error


def main() -> int:
    args = parse_args()
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_-]*", args.prefix):
        print("error: --prefix must be a valid class-name prefix", file=sys.stderr)
        return 2

    try:
        css_files = collect(args.css, CSS_EXTENSIONS)
        markup_files = collect(args.markup, MARKUP_EXTENSIONS)
    except (FileNotFoundError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    class_pattern = re.compile(r"(?<![A-Za-z0-9_-])\.([A-Za-z_][A-Za-z0-9_-]*)")
    mention_pattern = re.compile(rf"(?<![A-Za-z0-9_-])({re.escape(args.prefix)}[A-Za-z0-9_-]+)")
    defined: set[str] = set()
    mentioned: set[str] = set()

    for path in css_files:
        defined.update(
            name for name in class_pattern.findall(read_text(path)) if name.startswith(args.prefix)
        )
    for path in markup_files:
        mentioned.update(mention_pattern.findall(read_text(path)))

    unreachable = sorted(defined - mentioned)
    report = {
        "prefix": args.prefix,
        "css_files": len(css_files),
        "markup_files": len(markup_files),
        "defined": sorted(defined),
        "mentioned": sorted(mentioned),
        "unreachable": unreachable,
        "note": "Mentions are text matches only; inspect dynamic Liquid output before deleting CSS.",
    }
    print(json.dumps(report, indent=2))
    if args.strict and unreachable:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
