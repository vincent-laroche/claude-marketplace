---
name: figma-library-engineering
description: Build, audit, document, or repair production-quality Figma design systems. Use for variables and tokens, component libraries, variants, styles, responsive patterns, library governance, and Code Connect readiness.
---

# Figma Library Engineering

Build systems from evidence, not generic UI defaults. Load `$figma-agent-core` first.

## Discovery before construction

1. Inspect the target file, pages, libraries, variables, styles, components, properties, and representative product screens.
2. Establish authority for every value: an approved design system, existing production implementation, or an explicitly approved new decision. Do not manufacture a token ramp to fill a gap.
3. Inventory the missing responsibility: foundation, component, pattern, documentation, binding, responsive behavior, or code mapping. Fix the narrowest layer that resolves it.

## Build in dependency order

1. Create or reconcile collections, modes, semantic aliases, and styles before consuming components.
2. Build components from auto-layout primitives. Bind supported fills, strokes, text, effects, radii, and spacing to variables rather than raw values.
3. Use variant properties only for stable visual axes such as size, layout, surface, or state. Keep dynamic content and feature composition in exposed instances or properties rather than exploding variants.
4. Preserve named component families, existing consumers, and editor discoverability. Document purpose, variants, states, responsive rules, accessibility notes, and known constraints.

## Audit and verify

- Check token naming and alias direction; no circular aliases, orphan collections, or duplicate semantic values without reason.
- Check components for broken/remote instances, missing states, unbound raw styling, hidden primary instances, accidental detachment, and unlinked non-variant properties.
- Check desktop and mobile examples at intended widths. Verify the actual Layers tree and component bindings, not only pixels.
- For Code Connect, require a published component, a URL with `node-id`, and a matching implementation. Write parserless `.figma.ts` templates only when code props prove a mapping; never invent props or use `.figma.tsx` for this workflow.
- Do not publish a library as a side effect. Report publish state separately.

See [the finish gate](references/library-finish-gate.md).
