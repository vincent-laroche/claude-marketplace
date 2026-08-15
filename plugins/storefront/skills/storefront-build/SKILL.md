---
name: storefront-build
description: Write or edit Liquid sections, blocks and snippets for the hairsolutions.co storefront against the current Hair Solutions Co. design system. Use for any .liquid section, block, snippet, schema, or theme-editor wiring. Single Color Palette, design tokens, Inter Tight and Inter.
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

- **Radii:** `--r-pill` `999px` buttons, badges, chips, avatars; `--r-lg` `20px` cards, panels,
  dialogs; `--r-md` `12px` nested small surfaces; `--r-sm` `4px` inputs and multiline fields.
- **Colour:** design-system tokens only, no hardcoded hex. Coral `#ED6F5C` is the only CTA
  fill and its text is Ink `#15140F` — never white on Coral. Papers `#EFE7D2` `#ECE4CF`
  `#DDD2B6`, bone `#F7F1DE`, ink scale `#15140F` `#2A2620` `#5A5448` `#8B8676`.
- **Coral discipline:** under roughly 10% of a composition, once per view where possible,
  never on body text, never repeated decorative trim across a grid or list.
- **Type:** Inter Tight (headings, controls), Inter (body), JetBrains Mono (prices, specs,
  eyebrows), Playfair Display **italic inline emphasis inside a heading only** — never a
  standalone Playfair heading. Nothing else.
- **Backgrounds:** flat token fills. No gradients, patterns or glass. Never two dark sections
  adjacent, never Ink as the global page background. Keep the paper grain.
- **Grids:** three columns desktop maximum, two at 768–1024, one on mobile. Never four.
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
