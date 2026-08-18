#!/usr/bin/env python3
"""Block prohibited Shopify CLI and local theme-server commands."""

import json
import re
import sys

payload = json.load(sys.stdin)
command = str(payload.get("tool_input", {}).get("command", ""))
blocked = (
    r"\bshopify\s+theme\s+(dev|serve|push|pull|publish|share)\b",
    r"\bnpm\s+run\s+dev(?::\S+)?\b",
    r"\b(?:start|status|stop)-theme-dev\.sh\b",
    r"127\.0\.0\.1:9292",
)

if any(re.search(pattern, command, flags=re.IGNORECASE) for pattern in blocked):
    print(
        json.dumps(
            {
                "hookSpecificOutput": {"permissionDecision": "deny"},
                "systemMessage": "This plugin does not permit Shopify CLI/theme-server workflows. Use local repository inspection and GitHub delivery only.",
            }
        ),
        file=sys.stderr,
    )
    sys.exit(2)
