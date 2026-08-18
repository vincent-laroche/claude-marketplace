#!/usr/bin/env python3
"""Require confirmation before Shopify Admin mutations."""

import json
import sys

payload = json.load(sys.stdin)
tool_name = str(payload.get("tool_name") or payload.get("toolName") or "").lower()
serialized = json.dumps(payload.get("tool_input") or payload.get("toolInput") or {}).lower()
mutation_markers = (
    "graphql_mutation",
    "_create_",
    "_update_",
    "_upsert_",
    "_upload_",
    "set_inventory",
    "add_to_collection",
    "bulk_update",
)

if any(marker in tool_name for marker in mutation_markers) or '"mutation' in serialized:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {"permissionDecision": "ask"},
                "systemMessage": "Shopify Admin mutation requires explicit approval for the exact object and intended effect.",
            }
        ),
        file=sys.stderr,
    )
    sys.exit(2)
