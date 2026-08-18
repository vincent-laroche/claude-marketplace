#!/usr/bin/env python3
"""Report drift between installed marketplace caches and their remotes.

`~/.claude/plugins/marketplaces/<name>/` is a cache Claude Code clones and
manages. It is not an authoring checkout, but nothing about it says so: a
`git commit` there succeeds, looks exactly like a real commit, and reaches
nobody. That is not hypothetical — the `figma-import-html-to-sites` skill was
committed only into that cache during a repository rename and sat unpublished
until it was found by accident weeks later, at which point the cache was four
commits ahead and six behind its own remote.

This script makes that condition visible instead of accidental.

The hazard is narrower than the directory. A third-party marketplace is pure
consumption: you never commit into it, so it cannot strand anything, and being
900 commits behind is staleness rather than data loss. A marketplace you *own*
is the one that can hold work nobody else can see. So owned repositories are
judged (unpushed commits or a dirty tree is a failure) and the rest are only
reported.

Standard-library only, no writes unless --install-guards is passed.

    marketplace_doctor.py                  # fetch and report, exit 1 on drift
    marketplace_doctor.py --no-fetch       # offline, uses last-known remote refs
    marketplace_doctor.py --install-guards # (re)install the pre-commit guards
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

CACHE_ROOT = Path.home() / ".claude" / "plugins" / "marketplaces"

# A remote containing this owns-marker is treated as yours, and therefore
# judged rather than merely reported.
DEFAULT_OWNER = "vincent-laroche"

# Where an authoring checkout of an owned marketplace plausibly lives. Used
# only to name the right path in the guard message — a miss degrades the
# message, it never blocks the guard.
AUTHORING_ROOTS = (
    Path.home() / "03_agents",
    Path.home() / "07_design" / "brand",
    Path.home() / "02_dev",
    Path.home() / "01_projects",
)

GUARD_HOOK = """#!/bin/sh
# Installed by claude-marketplace scripts/marketplace_doctor.py --install-guards
#
# This repository is a Claude Code managed cache, not an authoring checkout.
# A commit here succeeds and reaches nobody: the cache is reset and re-pulled
# by the plugin system, so the work is silently discarded rather than pushed.
echo "BLOCKED: this is a managed marketplace cache, not an authoring checkout." >&2
echo "  cache:  $(pwd)" >&2
echo "  author: {authoring}" >&2
echo "" >&2
echo "Commit there and push; the cache updates itself from the remote." >&2
exit 1
"""


def git(repo: Path, *args: str, check: bool = False) -> str:
    """Run git in `repo`, returning stripped stdout ('' on failure)."""
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except (OSError, subprocess.SubprocessError):
        return ""
    if check and result.returncode != 0:
        return ""
    return result.stdout.strip()


def find_authoring_checkout(remote_url: str) -> str | None:
    """Locate a non-cache checkout sharing this remote, for the guard message."""
    if not remote_url:
        return None
    target = remote_url.rstrip("/").removesuffix(".git")
    for root in AUTHORING_ROOTS:
        if not root.is_dir():
            continue
        # One level deep, then two — deep enough for 07_design/brand/<repo>
        # without walking an entire home directory.
        for depth in (root.glob("*/.git"), root.glob("*/*/.git")):
            for dot_git in depth:
                candidate = dot_git.parent
                url = git(candidate, "remote", "get-url", "origin")
                if url.rstrip("/").removesuffix(".git") == target:
                    return str(candidate)
    return None


def inspect(repo: Path, fetch: bool, owner: str) -> dict:
    """Collect the drift facts for one cache directory."""
    info: dict = {"name": repo.name, "path": repo}

    if not (repo / ".git").exists():
        info["state"] = "not-a-git-repo"
        return info

    remote = git(repo, "remote", "get-url", "origin")
    info["remote"] = remote
    info["owned"] = owner.lower() in remote.lower()

    if fetch:
        git(repo, "fetch", "--quiet", "origin")

    upstream = git(repo, "rev-parse", "--abbrev-ref", "@{u}")
    if not upstream:
        info["state"] = "no-upstream"
        return info

    ahead = git(repo, "rev-list", "--count", f"{upstream}..HEAD")
    behind = git(repo, "rev-list", "--count", f"HEAD..{upstream}")
    dirty = git(repo, "status", "--porcelain")

    info["ahead"] = int(ahead) if ahead.isdigit() else 0
    info["behind"] = int(behind) if behind.isdigit() else 0
    info["dirty"] = len([ln for ln in dirty.splitlines() if ln.strip()])
    info["state"] = "ok"
    # Only an owned repository can strand work; the rest are informational.
    info["stranded"] = bool(info["owned"] and (info["ahead"] or info["dirty"]))
    return info


def install_guard(repo: Path, remote_url: str) -> str:
    """Write the pre-commit guard into an owned cache. Returns a status word."""
    hooks_dir = repo / ".git" / "hooks"
    if not hooks_dir.is_dir():
        return "no-hooks-dir"
    authoring = find_authoring_checkout(remote_url) or (
        "your local checkout of " + (remote_url or "this repository")
    )
    hook = hooks_dir / "pre-commit"
    body = GUARD_HOOK.format(authoring=authoring)
    if hook.exists() and hook.read_text() == body:
        return "current"
    hook.write_text(body)
    hook.chmod(0o755)
    return "installed"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-fetch", action="store_true",
                        help="skip git fetch; use last-known remote refs")
    parser.add_argument("--install-guards", action="store_true",
                        help="(re)install the pre-commit guard in owned caches")
    parser.add_argument("--owner", default=DEFAULT_OWNER,
                        help=f"remote substring marking a repo as yours (default: {DEFAULT_OWNER})")
    args = parser.parse_args()

    if not CACHE_ROOT.is_dir():
        print(f"No marketplace cache at {CACHE_ROOT} — nothing to check.")
        return 0

    caches = sorted(p for p in CACHE_ROOT.iterdir() if p.is_dir())
    reports = [inspect(p, fetch=not args.no_fetch, owner=args.owner) for p in caches]

    owned = [r for r in reports if r.get("owned")]
    others = [r for r in reports if not r.get("owned")]
    stranded = [r for r in reports if r.get("stranded")]

    def line(r: dict) -> str:
        if r["state"] == "not-a-git-repo":
            return f"  {r['name']:<26} (not a git repo)"
        if r["state"] == "no-upstream":
            return f"  {r['name']:<26} no upstream branch"
        mark = "  <-- UNPUSHED WORK" if r.get("stranded") else ""
        return (f"  {r['name']:<26} ahead {r['ahead']:<4} behind {r['behind']:<5} "
                f"dirty {r['dirty']:<4}{mark}")

    print(f"Marketplace caches under {CACHE_ROOT}\n")
    print(f"Yours ({args.owner}) — judged:")
    print("\n".join(line(r) for r in owned) if owned else "  (none)")
    print("\nThird-party — reported only, staleness is expected:")
    print("\n".join(line(r) for r in others) if others else "  (none)")

    if args.install_guards:
        print("\nPre-commit guards:")
        for r in owned:
            if r["state"] == "not-a-git-repo":
                continue
            status = install_guard(r["path"], r.get("remote", ""))
            print(f"  {r['name']:<26} {status}")

    if stranded:
        print("\nFAIL: work exists only in a managed cache and has not been pushed.")
        for r in stranded:
            print(f"  {r['path']}")
            if r["ahead"]:
                print(f"    {r['ahead']} unpushed commit(s)")
            if r["dirty"]:
                print(f"    {r['dirty']} uncommitted file(s)")
            author = find_authoring_checkout(r.get("remote", ""))
            if author:
                print(f"    authoring checkout: {author}")
        print("\nA cache is reset and re-pulled by the plugin system. Move this work")
        print("to the authoring checkout and push it, or it will be discarded.")
        return 1

    print("\nPASS: no marketplace cache holds unpushed work.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
