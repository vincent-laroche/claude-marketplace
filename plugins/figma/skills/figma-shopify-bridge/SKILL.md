---
name: figma-shopify-bridge
description: Translate Figma design intent into a safe, native-first Shopify implementation plan or change set. Use for Figma-to-Liquid work, storefront visual-parity audits, Horizon section and block mapping, responsive commerce UI, Shopify Admin context checks, and design-to-theme handoff.
---

# Figma Shopify Bridge

Load `$figma-agent-core` and inspect the design context before mapping it to Shopify. Translate responsibilities, not CSS selectors or static pixels.

## Establish the boundary

1. Confirm the theme repository, branch, target template/section, current schema, viewport evidence, and whether the request is planning, local implementation, or release.
2. Read Shopify Admin only when it resolves a real data, theme, or configuration question. Treat customer, order, product, inventory, theme-file, and mutation tools as production-sensitive.
3. Keep design values and content claims tied to their current authority. A Figma mock cannot authorize new catalog data, metafields, assets, or customer behavior.

## Assign each design responsibility

Use the first valid owner in this order:

1. Native global setting or palette.
2. Stock section or block setting.
3. JSON template composition.
4. Shopify object, dynamic source, or an existing metafield.
5. Small custom block or section with schema and editor ownership.
6. A documented implementation delta when no safe native equivalent exists.

Do not add a custom selector, hidden markup, duplicate per-template CSS, or hardcoded storefront value until the relevant schema and owner have been inspected and ruled out.

## Preserve commerce behavior

- Keep product cards, purchase options, variants, filters, search, cart, and account behavior in native mechanisms unless an approved gap requires extension.
- Map Figma responsiveness to the theme's actual breakpoints and containers. Record a delta if native settings cannot express it cleanly.
- Validate Liquid/schema/JSON/CSS/JavaScript with repository checks and inspect desktop plus narrow mobile. Check overflow, console errors, focus behavior, images, and data states.
- Never publish, upload a theme, alter Shopify data, change checkout-adjacent behavior, or call an Admin mutation without explicit approval. Do not use Shopify CLI or a theme-dev server.

Report the intent inventory, owner chosen for each material responsibility, unresolved deltas, checks run, and release state. See [the ownership table](references/shopify-ownership.md).
