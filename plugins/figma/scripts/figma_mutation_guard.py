#!/usr/bin/env python3
"""Require confirmation before destructive or externally visible Figma operations."""

import json
import re
import sys

payload = json.load(sys.stdin)
serialized = json.dumps(payload.get("tool_input") or payload.get("toolInput") or {}).lower()
markers = (r"\bpublish\b", r"\bshare\b", r"\bpermission\b", r"\bdelete\b", r"\.remove\(", r"\bbulk\b")

if any(re.search(marker, serialized) for marker in markers):
    print(
        json.dumps(
            {
                "hookSpecificOutput": {"permissionDecision": "ask"},
                "systemMessage": "Figma publishing, sharing, deletion, or bulk mutation requires explicit approval for the exact file/node and intended effect.",
            }
        ),
        file=sys.stderr,
    )
    sys.exit(2)
