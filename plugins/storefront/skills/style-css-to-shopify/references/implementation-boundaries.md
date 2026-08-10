# Implementation boundaries and verification

## Architecture rules

- Keep global values in theme settings or shared variable/mapping output.
- Keep page composition in JSON templates and reusable behavior in sections/blocks.
- Keep catalog, page, blog, cart, and customer facts in Shopify objects or approved metafields.
- Add custom CSS only for a capability the theme demonstrably lacks; scope it to the owning component.
- Never target a theme's undocumented internal selectors, use `!important`, or use template-specific CSS to simulate a global system.

## Liquid and schema safeguards

- Inspect a block's schema before writing JSON settings; do not assume a setting ID, type, or option exists.
- Use valid public block IDs. In Horizon, IDs derived from underscore-prefixed private block types are rejected if the underscore is retained.
- Use integer values for range controls; encode fractional visual ratios with the nearest supported integer proportions.
- Preserve settings defaults so an additive change does not silently change unrelated template consumers.
- When filtering in a Liquid loop, count rendered items. Do not use `forloop.last` for separators after skipped entries; guard empty output and align carousel counts with the rendered count.
- Preserve native form submission, validation, cart behavior, and accessible error associations when extending an interaction.

## Fidelity claims

Call a result "structurally aligned" when section order, component responsibility, dynamic data bindings, and responsive constraints have been verified. Call it "visually verified" only after rendered checks of computed values and interaction states. Do not call it pixel-perfect when native limits were accepted or only static boards were compared.

## Minimum verification matrix

| Layer | Check |
|---|---|
| Source | Inventory source tokens, components, responsive changes, and data dependencies |
| Theme | Parse JSON/JSONC and Liquid schemas; confirm every referenced section/block resolves |
| Styles | Check CSS syntax and reachability; ensure no obsolete parallel class system remains |
| Runtime | Check desktop plus narrow mobile for overflow, broken assets, console errors, focus, reduced motion, and requested interactions |
| Data | Exercise representative populated and empty states with real/approved Shopify data |
| Release | Keep local checks, GitHub delivery, development-theme upload, and live publication as separate states |

## Stop conditions

Stop before implementation or release when any of these is true:

- The project instructions, source authority, or target theme version are unclear.
- The project instructions explicitly conflict with the requested work; the project instruction takes precedence until the user resolves the conflict.
- Source CSS/HTML is absent, malformed, empty, or lacks a source viewport/breakpoint baseline for a fidelity claim.
- A required schema, settings file, or template is missing, malformed, incompatible with the installed theme version, or contradictory.
- The target is legacy/non-OS-2.0 and has no verified equivalent for the proposed JSON-template, group, or block mechanism.
- The request requires publishing, theme upload, catalog/customer mutations, asset upload, or checkout changes without explicit approval.
- The design needs absent metafields, product copy, or media and there is no approved data/asset source.
- The only proposed path is an undocumented internal override or a broad custom CSS replacement for native theme behavior.
