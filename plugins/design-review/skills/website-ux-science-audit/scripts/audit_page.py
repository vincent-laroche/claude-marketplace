#!/usr/bin/env python3
"""Plan or run a local website UX audit tool stack."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Sequence


@dataclass
class ToolStatus:
    name: str
    available: bool
    path: str | None


@dataclass
class CommandResult:
    name: str
    command: list[str]
    cwd: str | None
    exit_code: int | None
    output_path: str | None
    stderr_path: str | None
    skipped: bool
    note: str


def tool_status(name: str) -> ToolStatus:
    path = shutil.which(name)
    return ToolStatus(name=name, available=path is not None, path=path)


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def run_command(name: str, command: Sequence[str], out_dir: Path, timeout: int, cwd: Path | None = None) -> CommandResult:
    stdout_path = out_dir / f"{name}.stdout.txt"
    stderr_path = out_dir / f"{name}.stderr.txt"
    try:
        completed = subprocess.run(
            list(command),
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
            cwd=str(cwd) if cwd else None,
        )
    except subprocess.TimeoutExpired as exc:
        write_text(stdout_path, exc.stdout or "")
        write_text(stderr_path, (exc.stderr or "") + f"\nTimed out after {timeout}s\n")
        return CommandResult(name, list(command), str(cwd) if cwd else None, None, str(stdout_path), str(stderr_path), False, "timed out")

    write_text(stdout_path, completed.stdout)
    write_text(stderr_path, completed.stderr)
    return CommandResult(
        name=name,
        command=list(command),
        cwd=str(cwd) if cwd else None,
        exit_code=completed.returncode,
        output_path=str(stdout_path),
        stderr_path=str(stderr_path),
        skipped=False,
        note="completed",
    )


def planned_commands(url: str | None, css: str | None, out_dir: Path) -> list[tuple[str, list[str], str | None, Path | None]]:
    commands: list[tuple[str, list[str], str | None, Path | None]] = []
    if url:
        commands.append(
            (
                "lighthouse",
                [
                    "lighthouse",
                    url,
                    "--quiet",
                    "--chrome-flags=--headless",
                    "--output=json",
                    f"--output-path={out_dir / 'lighthouse.json'}",
                ],
                "lighthouse",
                None,
            )
        )
        commands.append(("axe", ["axe", url, "--stdout", "--timeout", "90"], "axe", None))
        commands.append(("pa11y", ["pa11y", url, "--reporter", "json", "--timeout", "90000"], "pa11y", None))
    if css:
        css_path = Path(css).expanduser()
        if css_path.exists():
            resolved = css_path.resolve()
            commands.append(("wallace", ["wallace", resolved.name, "--json"], "wallace", resolved.parent))
        else:
            commands.append(("wallace", ["wallace", css, "--json"], "wallace", None))
    return commands


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", help="URL to audit with Lighthouse, axe, and Pa11y")
    parser.add_argument("--css", help="CSS file to audit with Wallace")
    parser.add_argument("--out", default="ux-audit-output", help="Output directory")
    parser.add_argument("--run", action="store_true", help="Run commands. Default only prints plan and tool availability")
    parser.add_argument("--timeout", type=int, default=180, help="Per-command timeout in seconds")
    args = parser.parse_args()

    tools = [tool_status(name) for name in ["lighthouse", "axe", "pa11y", "playwright", "wallace"]]
    out_dir = Path(args.out).expanduser().resolve()
    commands = planned_commands(args.url, args.css, out_dir)
    command_plan = [
        {
            "name": name,
            "command": command,
            "required_tool": required_tool,
            "cwd": str(cwd) if cwd else None,
        }
        for name, command, required_tool, cwd in commands
    ]

    if not args.run:
        print(json.dumps({"tools": [asdict(tool) for tool in tools], "planned_commands": command_plan}, indent=2))
        return 0

    if not args.url and not args.css:
        print("Provide --url, --css, or both when using --run.", file=sys.stderr)
        return 2

    out_dir.mkdir(parents=True, exist_ok=True)
    results: list[CommandResult] = []
    for name, command, required_tool, cwd in commands:
        if required_tool and shutil.which(required_tool) is None:
            results.append(CommandResult(name, command, str(cwd) if cwd else None, None, None, None, True, f"missing {required_tool}"))
            continue
        results.append(run_command(name, command, out_dir, args.timeout, cwd))

    summary = {"tools": [asdict(tool) for tool in tools], "results": [asdict(result) for result in results]}
    write_text(out_dir / "summary.json", json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
