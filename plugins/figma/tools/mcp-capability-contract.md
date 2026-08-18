# Figma Shopify MCP Capability Contract

The host runtime must expose the applicable tools; the plugin does not install, authenticate, or broaden MCP access.

| Capability | Required live surface | Write boundary |
| --- | --- | --- |
| Figma inspection | account, metadata, screenshot, design/FigJam context | read-only |
| Figma file work | file creation, assets, variables, libraries, file-context mutation | explicit edit scope; publish/share/delete/bulk work needs approval |
| Figma engineering | REST, Plugin API, Code Connect, motion, diagram/deck tools | scopes/permissions and endpoint support must be verified |
| Shopify fact finding | Shopify Admin shop/theme/product/collection/inventory/order/customer/GraphQL reads | read-only |
| Shopify change | Admin mutation, theme-file, inventory, product/collection/asset tools | explicit approval for exact object/effect plus read-back |

At session start, dynamically inspect tool availability and schemas. Never substitute tool presence for access to a specific Figma file, Shopify shop, API scope, plan entitlement, or mutation authority.
