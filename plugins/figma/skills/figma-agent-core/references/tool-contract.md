# Tool Contract

| Need | First tool surface | Verify with |
| --- | --- | --- |
| Inspect a Design file/node | metadata, screenshot, or design context | fresh screenshot and returned node IDs |
| Inspect a FigJam board | FigJam context | section/node IDs and screenshot |
| Write in one Figma file | file-context mutation tool | metadata/layers plus screenshot |
| Create a Figma file | account/plan lookup, then file creation | returned file URL and key |
| Build code from Figma | design context | target-repo checks and visual comparison |
| Need unattended/cross-file work | Figma REST after endpoint verification | read-only smoke test or post-write read |
| Need a Shopify fact | Shopify Admin read tool | returned Admin object/query |
| Change Shopify | explicit approval plus narrow mutation tool | post-write Admin read and repo checks |

Always query available tools at task start. Tool names, account entitlements, and write capability can change between sessions.
