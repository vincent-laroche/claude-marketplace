---
name: style-css-to-shopify
description: Converts an existing CSS/design-system implementation into a native-first Shopify Online Store 2.0 plan or change set, with Horizon as the primary target. Use when handling HTML/CSS-to-Liquid work, visual-parity audits, editable-theme-customizer rebuilds, section/block/schema mapping, or decisions about whether a style belongs in theme settings, JSON templates, dynamic Shopify data, or a custom Liquid component. Do not use for publishing, checkout changes, arbitrary Shopify themes without inspecting their schemas, or literal pixel-cloning that bypasses native controls.
---

# Style CSS to Shopify

Use this skill to translate design responsibilities, not to mechanically port selectors. Preserve theme-editor ownership and Shopify data behavior while pursuing the closest justified visual result.

## 1. Establish the boundary

1. Read the project instructions, current project log, and the live theme's local `AGENTS.md` before touching source.
2. Confirm the exact theme repository, branch, theme version, source CSS/HTML or Figma evidence, source viewport/breakpoint measurements, representative data fixtures, and whether the request is planning, local implementation, or release.
3. For customer-facing work, inspect the current brand authority before using any old token, asset, font, or design artifact.
4. Treat publishing, theme upload, GitHub delivery, Shopify-data changes, asset upload, and checkout behavior as separate approval boundaries.
5. Treat project instructions as higher priority than this skill. Stop and request direction if they conflict with the requested work.
6. Stop and request direction if the source is only a screenshot; source CSS/HTML is missing, malformed, or empty; the target theme cannot be inspected; or a proposed solution requires invented catalog content or an unapproved data mutation.

## 2. Build an intent inventory

1. Inventory each source responsibility: tokens, type roles, surfaces, spacing, layout, components, interaction states, responsive changes, and content/data dependencies.
2. Run `scripts/css_class_reachability.py` when a CSS bundle and theme markup are available. Treat its output as a diagnostic, not proof: Liquid may emit classes dynamically.
3. Separate reusable visual primitives from route-specific composition. Record the desired visual behavior rather than only CSS selectors or pixel values.
4. Create a row for every unresolved responsibility using `assets/parity-delta-ledger.md`.

## 3. Inspect the target before proposing an equivalent

1. Parse and read the relevant section/block `{% schema %}` and the matching group in `config/settings_schema.json`; inspect active values in `config/settings_data.json` where applicable.
2. Read `references/horizon-native-equivalences.md` for the Horizon-first mapping and `references/implementation-boundaries.md` before editing Liquid, JSON, CSS, or JavaScript.
3. Select the first applicable owner in this order:

   1. native global setting or palette;
   2. stock section/block setting;
   3. JSON template composition of stock sections/blocks;
   4. native Shopify object, dynamic source, or existing metafield;
   5. small custom block/section with schema and editor ownership;
   6. documented delta when no safe native equivalent exists.

4. Stop before mapping or editing if a required schema/settings file is missing, malformed, incompatible with the active theme version, or contradicts the intended setting. Resolve the source of truth first.
5. Do not add a custom class, layout block, or stylesheet rule until the relevant native schema has been inspected and ruled out.

## 4. Map design intent to Shopify responsibilities

1. Use `section` for page bands and `group` for grids, splits, stacks, cards, and nested layout where the target is Horizon.
2. Keep buttons, fields, swatches, product cards, collection cards, filters, cart, search, and commerce flows in their native mechanisms unless a documented capability is genuinely absent.
3. Build custom Liquid only for distinctive behavior or visual language the theme cannot own. Give every custom block a schema, preset, `block.shopify_attributes`, and a minimal reachable style surface.
4. Bind real product, collection, blog, customer, cart, and page data through Shopify's native objects or approved metafields. Never hardcode prototype copy merely to fill a band.
5. Preserve template section keys, order, defaults, and existing consumers unless the approved change explicitly changes them.

## 5. Handle non-equivalence explicitly

1. Record native limits—slider caps, discrete setting steps, unsupported font roles, shared desktop/mobile values, and native interaction behavior—as deltas rather than hidden overrides.
2. Prefer the clean native result when a board and the theme conflict. Explain the visual effect, the reason, and the lowest-risk alternative.
3. Escalate rather than guess when a design requires new metafields, catalog content, assets, customer data, app behavior, or a theme-upgrade-sensitive stock-file change.
4. Do not use internal Horizon selectors, `!important`, duplicated per-template CSS, hardcoded remote URLs, or hidden markup to impersonate a native feature.

## 6. Implement in ownership order

1. Apply global palette, typography, geometry, and shared settings before route templates.
2. Add or refine custom primitives before composing routes.
3. Update JSON templates as composition and configuration, not as a place to repeat presentation logic.
4. Implement dynamic content contracts before cosmetic filler; leave a band visibly absent or use the native empty state rather than inventing claims.
5. Keep every change small and reversible. Do not publish or alter Shopify data as part of this workflow.

## 7. Verify outcomes

1. Validate Liquid schemas, JSON/JSONC, template references, CSS syntax, and JavaScript syntax with the repository's existing checks.
2. Confirm custom CSS is reachable and remove obsolete styles rather than preserving parallel systems.
3. Check desktop and mobile at the source-design breakpoints plus a narrow mobile width. Verify no horizontal overflow, broken assets, console errors, inaccessible validation, or unwanted motion.
4. Verify dynamic routes with representative data: product, collection, blog/article, cart, search, contact, and empty states as applicable.
5. Capture a source baseline at each target viewport and compare it with the rendered target: computed typography, spacing, radii, colors, hierarchy, interaction state, focus, and reduced-motion behavior. State the measurement/tolerance for each accepted delta; do not close fidelity claims from a screenshot alone.
6. Update the parity/delta ledger with observed evidence, accepted differences, and any release blocker.

## 8. Deliver and hand off

1. State the mapping decisions, files changed, verification run, and exact accepted deltas.
2. Separate local verification from GitHub delivery, development-theme upload, and live publication.
3. Record a compact session handoff in the project's `PROJECT.md` when meaningful work was performed.

## Error Handling

- If CSS classes are mostly unreachable, stop adding selectors; inspect the emitted markup and replace duplicate styling with native ownership where possible.
- If a setting exists but cannot represent the source exactly, keep the setting and log the nearest clean result before proposing an override.
- If content fidelity depends on missing data, define the data contract and request approval; do not fabricate text or point Liquid at nonexistent metafields.
- If a stock-file edit is required, identify its upgrade risk, make it additive where possible, and validate it against the exact current theme version.
- If the requested theme is not Horizon, first establish that it is OS 2.0 and identify its actual layout/composition primitives. Treat the Horizon reference as a pattern, not a schema catalog. If the theme lacks a safe equivalent or is a legacy/non-OS-2.0 theme, stop and provide a migration or scoped custom-build recommendation instead of assuming JSON templates, groups, or app-block support.
