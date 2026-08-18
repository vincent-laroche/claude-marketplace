#!/usr/bin/env python3
"""Validate the Email Marketing custom-agent definitions."""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

REQUIRED_FIELDS = ("name", "description", "developer_instructions")
ALLOWED_SANDBOX_MODES = {"read-only", "workspace-write", "danger-full-access"}
EXPECTED_AGENT_COUNT = 8


def validate_agent_files(agent_dir: Path) -> list[str]:
    errors: list[str] = []
    files = sorted(agent_dir.glob("*.toml"))

    if len(files) != EXPECTED_AGENT_COUNT:
        errors.append(
            f"{agent_dir}: expected {EXPECTED_AGENT_COUNT} TOML files, found {len(files)}"
        )

    names: dict[str, Path] = {}
    for path in files:
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path}: invalid TOML: {exc}")
            continue

        for field in REQUIRED_FIELDS:
            value = data.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path}: missing non-empty {field!r}")

        name = data.get("name")
        if isinstance(name, str) and name.strip():
            normalized_name = name.casefold()
            if normalized_name in names:
                errors.append(f"{path}: duplicate name also used by {names[normalized_name]}")
            else:
                names[normalized_name] = path

        sandbox_mode = data.get("sandbox_mode")
        if sandbox_mode not in ALLOWED_SANDBOX_MODES:
            errors.append(
                f"{path}: sandbox_mode must be one of {sorted(ALLOWED_SANDBOX_MODES)}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "agent_dir",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "agents",
    )
    args = parser.parse_args()

    errors = validate_agent_files(args.agent_dir)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {EXPECTED_AGENT_COUNT} Email Marketing custom agents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
