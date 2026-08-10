#!/usr/bin/env python3
"""Validate the Atelier Zero converter's single-file HTML output contract."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path


class ContractParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype_html = False
        self.tags: set[str] = set()
        self.has_viewport = False
        self.external_stylesheets: list[str] = []
        self.external_scripts: list[str] = []

    def handle_decl(self, decl: str) -> None:
        if decl.strip().lower() == "doctype html":
            self.doctype_html = True

    def handle_starttag(self, tag: str, attrs) -> None:
        tag = tag.lower()
        self.tags.add(tag)
        attributes = {str(key).lower(): value for key, value in attrs}

        if tag == "meta" and str(attributes.get("name", "")).lower() == "viewport":
            self.has_viewport = True

        if tag == "link" and "stylesheet" in str(attributes.get("rel", "")).lower():
            self.external_stylesheets.append(str(attributes.get("href", "<missing href>")))

        if tag == "script" and attributes.get("src"):
            self.external_scripts.append(str(attributes["src"]))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate that a conversion is one complete HTML file with embedded CSS and JavaScript."
    )
    parser.add_argument("html_file", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.html_file.expanduser().resolve()
    errors: list[str] = []

    if not path.is_file():
        errors.append(f"File does not exist: {path}")
    elif path.suffix.lower() != ".html":
        errors.append("Primary deliverable must use the .html extension.")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    try:
        source = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        print(f"FAIL: Could not read UTF-8 HTML: {exc}")
        return 1

    parser = ContractParser()
    parser.feed(source)

    if not parser.doctype_html:
        errors.append("Missing <!doctype html>.")

    for tag in ("html", "head", "title", "style", "body"):
        if tag not in parser.tags:
            errors.append(f"Missing required <{tag}> element.")

    if not parser.has_viewport:
        errors.append("Missing responsive viewport metadata.")

    if parser.external_stylesheets:
        errors.append(
            "CSS must be embedded in the HTML; external stylesheet(s): "
            + ", ".join(parser.external_stylesheets)
        )

    if parser.external_scripts:
        errors.append(
            "Required JavaScript must be embedded in the HTML; external script(s): "
            + ", ".join(parser.external_scripts)
        )

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print(f"PASS: {path} satisfies the standalone HTML output contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
