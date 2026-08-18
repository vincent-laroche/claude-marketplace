#!/usr/bin/env python3
"""Emit the Figma plugin's minimal safety context at session start."""

import json

print(
    json.dumps(
        {
            "systemMessage": (
                "Figma plugin: confirm live Figma/Shopify MCP access and the exact target before acting. "
                "Planning/audit/handoff is read-only; publishing, sharing, deletes, bulk edits, "
                "Shopify mutations, theme uploads, and webhook registration need explicit approval."
            )
        }
    )
)
