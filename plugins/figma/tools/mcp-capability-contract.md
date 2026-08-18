# Figma Shopify MCP Capability Contract

The plugin **declares** the Figma MCP server in `plugins/figma/.mcp.json`
(`https://mcp.figma.com/mcp`, HTTP), so enabling the plugin is enough to get
`use_figma` and the rest of the Figma surface. Changed 2026-08-18 — the plugin
previously declared nothing and relied on the host already having a Figma
server, which left its skills inert whenever it was enabled on its own.

Declaring is not authenticating. The server still runs its own OAuth on first
use, and the plugin never widens a scope: it does not grant access to a specific
Figma file, plan entitlement, or mutation authority. Shopify tools remain the
host's to provide — this plugin declares no Shopify server.

| Capability | Required live surface | Write boundary |
| --- | --- | --- |
| Figma inspection | account, metadata, screenshot, design/FigJam context | read-only |
| Figma file work | file creation, assets, variables, libraries, file-context mutation | explicit edit scope; publish/share/delete/bulk work needs approval |
| Figma engineering | REST, Plugin API, Code Connect, motion, diagram/deck tools | scopes/permissions and endpoint support must be verified |
| Shopify fact finding | Shopify Admin shop/theme/product/collection/inventory/order/customer/GraphQL reads | read-only |
| Shopify change | Admin mutation, theme-file, inventory, product/collection/asset tools | explicit approval for exact object/effect plus read-back |

At session start, dynamically inspect tool availability and schemas. Never substitute tool presence for access to a specific Figma file, Shopify shop, API scope, plan entitlement, or mutation authority.
