# Horizon-native equivalences

Read this reference after inspecting the target theme's current schemas. It records a proven Horizon-first decision pattern; it is not a substitute for the installed version's source.

| Design responsibility | Prefer in Horizon | Avoid |
|---|---|---|
| Site palette, text colors, CTA treatment, control geometry | Global palette and theme settings | Literal colors repeated in templates or component CSS |
| Page band | `sections/section.liquid` and template order | A custom section only to add padding, background, or width |
| Stack, grid, split, card composition | `blocks/group.liquid`: direction, child width, gap, background, border, radius, padding, nested `@theme` blocks | Parallel `grid`, `split`, `container`, or `card` layout classes |
| Text rhythm | Group gaps and text block padding | Spacer markup, negative margins, page-specific CSS |
| Buttons, fields, chips, tiles, swatches | Native control settings and stock blocks | Rebuilt controls solely for visual treatment |
| Collections and products | Stock collection/product card blocks and Shopify objects | Prototype-only cards or hardcoded catalog details |
| Blog and article context | `closest.blog`, `article.*`, current route-aware settings | A fixed blog handle reused on every route |
| Cart, search, contact, 404, password | Native sections and states | Bespoke replacements that lose Shopify behavior |
| Editorial signature unavailable natively | Small schema-backed custom blocks | A broad CSS framework for every source class |

## Custom-component threshold

Create a custom component only after confirming the theme lacks the capability. Historically justified Horizon exceptions included:

- a thin Coral tick before an eyebrow;
- uppercase mono metadata where no mono role exists;
- registration/corner marks on a panel;
- a rule row with a Coral italic index;
- an oversized statistic with an italic fragment;
- locked before/after aspect across states;
- a display type tier above the native scale;
- a required interaction behavior that stock accordion controls cannot express.

Each exception must expose editor-owned settings and use styles that its own markup reaches.

## Known native limits worth logging

- Theme controls can be discrete or capped; a board value may be unreachable without taking ownership away from the editor.
- Some typography roles are not selectable through a native font picker. Self-hosted fonts or a targeted variable override can be justified, but must be checked in rendered output.
- A setting can apply at every breakpoint while the design calls for mobile-specific values. Do not add breakpoint CSS automatically; accept the clean native value unless the responsive treatment itself is an approved custom capability.
- Native controls can have different state semantics from a design system, such as a plus becoming a minus rather than rotating into a cross.

## Data-equivalence rule

Visual sections may look complete while their content responsibilities are not available in Shopify. Map every content area to an existing native object or approved metafield. If the map requires new definitions, content population, or customer data, create a data contract and stop for approval.
