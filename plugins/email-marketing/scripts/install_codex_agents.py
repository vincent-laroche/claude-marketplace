#!/usr/bin/env python3
"""Install the bundled Email Marketing agents into Codex's personal agent directory."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

from validate_agents import EXPECTED_AGENT_COUNT, validate_agent_files

SOURCE_DIR = Path(__file__).resolve().parent.parent / "agents"
DEFAULT_TARGET_DIR = Path.home() / ".codex" / "agents"
DESTINATION_PREFIX = "email-marketing-"


def destination_for(source: Path, target_dir: Path) -> Path:
    return target_dir / f"{DESTINATION_PREFIX}{source.name}"


def install_agents(target_dir: Path) -> int:
    errors = validate_agent_files(SOURCE_DIR)
    if errors:
        raise SystemExit("\n".join(errors))

    target_dir.mkdir(parents=True, exist_ok=True)
    installed = 0
    unchanged = 0

    for source in sorted(SOURCE_DIR.glob("*.toml")):
        destination = destination_for(source, target_dir)
        content = source.read_bytes()
        if destination.is_file() and destination.read_bytes() == content:
            unchanged += 1
            continue

        with tempfile.NamedTemporaryFile(dir=target_dir, delete=False) as temporary:
            temporary.write(content)
            temporary_path = Path(temporary.name)
        os.chmod(temporary_path, 0o644)
        os.replace(temporary_path, destination)
        installed += 1

    print(
        f"Email Marketing agents ready in {target_dir}: "
        f"{installed} installed or updated, {unchanged} unchanged."
    )
    print("Start a new Codex chat before invoking them.")
    return 0


def check_agents(target_dir: Path) -> int:
    missing_or_stale: list[Path] = []
    for source in sorted(SOURCE_DIR.glob("*.toml")):
        destination = destination_for(source, target_dir)
        if not destination.is_file() or destination.read_bytes() != source.read_bytes():
            missing_or_stale.append(destination)

    if missing_or_stale:
        for destination in missing_or_stale:
            print(f"Missing or stale: {destination}")
        return 1

    print(f"Verified {EXPECTED_AGENT_COUNT} installed Email Marketing agents.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET_DIR)
    args = parser.parse_args()
    return check_agents(args.target) if args.check else install_agents(args.target)


if __name__ == "__main__":
    raise SystemExit(main())
