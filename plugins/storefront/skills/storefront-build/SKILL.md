---
name: storefront-build
description: Write or edit Liquid sections, blocks and snippets for the hairsolutions.co storefront against the current Hair Solutions Co. design system. Use for any .liquid section, block, snippet, schema, or theme-editor wiring. Single Color Palette, design tokens, and the theme-editor wiring that carries them.
---

# Storefront build

Everyday skill for writing theme code. Read `references/theme-map.md` for the
section/template/collection map.

**Resolve the target repository's own contract first.** Read its `AGENTS.md`, `DESIGN.md` and
`THEME-BASELINE.md` for the Horizon version it is actually built on, its custom-file prefix,
and its authorization rules. Those differ between the current theme and the superseded one —
never carry a version or prefix over from this document or from another repo.

If the repository ships its own project-local rules under `.claude/rules/`, they load
automatically for the paths you touch and they govern.

Design authority is `/Users/vMac/08_brand/brand-design-system` — its `tokens/` and `specs/`.
Never hardcode a token value that already exists as a custom property.

## Horizon rules

- ONE **Color Palette** (colour schemes are gone): use `settings.color_palette.background` /
  `settings.color_palette.foreground`. Do not add scheme settings.
- OS 2.0 architecture: sections plus theme blocks (`{% content_for 'blocks' %}`), `{% schema %}`
  with stable setting IDs and presets. Preserve `{{ block.shopify_attributes }}` on every
  rendered block root.
- New custom components use the prefix the target repository documents. Reuse existing blocks
  and snippets (see theme-map) before inventing.
- Liquid: `.value` on metaobject and metafield values; never pipe inside `[ ]` (assign first);
  whitespace control on every tag (`{%- -%}`); `render` not `include`.
- Schema: `placeholder:` never `default:` on `text` and `textarea` inputs. Never rename or
  reuse an existing setting `id` — merchants' saved values are keyed by it.
- Liquid comments are plain text only. No `====` or ASCII art; it crashes the parser.
- Inspect nearby files first; make small focused diffs. Never modify app-managed `ecom-*`,
  `ss-*` or `foxify-*` files unless the request names them.

## Definition of Done (check every item before committing)

- **Radii:** use the `--r-*` tokens by role — pill for buttons and badges, large for cards
  and panels, medium for nested surfaces, small for inputs. The values behind them are
  brand authority and live in `foundations/spacing.md`; never inline a px radius.
- **Colour:** design-system tokens only, never a hardcoded hex. The palette itself is
  brand authority and is not restated here — `foundations/color.md` owns it, including
  the CTA fill, its required text colour, and how sparingly the accent may be used.
- **Type:** the four families and their roles are owned by `foundations/typography.md`.
  Use the token, not a font name.
- **Backgrounds:** flat token fills. No gradients, patterns or glass. Never two dark sections
  adjacent, never Ink as the global page background. Keep the paper grain.
- **Grids:** column counts and their responsive collapse are owned by
  `foundations/spacing.md`, which also records the carve-outs. Read it rather than
  assuming a maximum.
- **Spacing:** the token scale; `clamp()` for fluid sizing.
- **Mobile:** side padding 20–28px, no horizontal scroll, touch targets at least 44×44px.
  QA at 320/375/390/430. Mobile styles are part of the deliverable, not a follow-up.
- **Motion:** honour `prefers-reduced-motion`. No scroll-triggered reveals, spinners, skeleton
  shimmers, or chevron SVGs — the accordion uses a rotating `+`.
- **Imagery:** no AI-generated imagery. Placeholders are flat token fills with a mono caption,
  aspect locked: product 3/4, article 16/10, hero 4/5.
- **Voice:** no exclamation marks, no emoji, no hype, urgency or scarcity. Say "system", never
  "wig" or "toupee". Never reference balding or hair loss unprompted. Never invent product,
  pricing, shipping, return, support or timing claims.
- Schema and IDs stable, dynamic sources intact, theme-editor compatible.
- SEO: one H1, logical headings, semantic HTML, metadata / JSON-LD / internal links preserved,
  FAQ schema only for a visibly rendered FAQ.

## Media

Cloudinary only — see the `cloudinary-media` skill. AssetLink for products, collections and
blogs; Files CDN for pages. Never duplicate media into theme `assets/`.

## Validate

Run the target repository's own validator if it has one (for example
`./scripts/claude/validate.sh`). Otherwise run `shopify theme check` — local static analysis
that never contacts the store.

When done, ship via `storefront-release`. Never publish without separate explicit approval.
