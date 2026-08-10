# Atelier Zero source map

Use the live repository at `/Users/vMac/08_brand/brand-design-system` as the only brand authority. Resolve paths from the current filesystem on every run; do not copy values from older installed skills or memory.

## Required reading order

1. `PROJECT.md` — current status, known gaps, and unfinished brand assets.
2. `AGENTS.md` — repository, safety, and coding rules.
3. `README.md` — source hierarchy and current stack.
4. `SKILL.md` — binding Atelier Zero brand mandate.
5. `DESIGN.md` — operating model, brand position, and visual foundations.
6. `styles/system-v3.css` — canonical CSS tokens and base atoms.
7. `tokens/tokens.css` and `tokens/tokens.json` — portable CSS and structured token exports.
8. `specs/ATELIER_ZERO_RULEBOOK_V1.md` — palette roles, contrast, surface recipes, CTA rules, migration map, and QA.
9. `specs/COMPONENT_CONTRACTS.md` — components and states used by the target.
10. `specs/COMPOSITION_RULES.md` and `specs/DECISION_TREES.md` — layout, spacing, alignment, cards, surfaces, imagery, and motion.
11. `specs/brand_voice.md` — canonical voice, claims, replacement rules, and channel adaptation when copy is present.

## Platform routing

- Shopify or general storefront work: read `specs/PLATFORM_SHOPIFY.md`.
- Email or HubSpot module work: read `specs/PLATFORM_EMAIL.md`.
- Social graphic, carousel, story, reel, or video-cover work: read `specs/PLATFORM_SOCIAL.md`.
- Mixed-channel work: read every applicable platform spec and keep channel outputs separate.

## Asset routing

Inspect the current identity status before selecting a logo or font asset:

- `app/identity/page.tsx`
- `assets/logos/`
- `public/brand-assets/`
- `Hair Solutions Co - Logo (aterlier-zero)/`
- `fonts/`

Do not assume a filename containing `current`, `Atelier Zero`, `ink`, `silver`, or another brand term proves approval. Check `PROJECT.md`, `DESIGN.md`, the identity page, and the asset itself. If the source of truth says a current export is pending, report the gap rather than recoloring an old raster or inventing a substitute.

## Target-project authority

Read the target project's own `PROJECT.md`, `AGENTS.md`, `CLAUDE.md`, `README.md`, and relevant implementation files before conversion. Preserve its framework, editor contracts, data bindings, and release rules unless they conflict with a current Atelier Zero requirement or the user explicitly asks to change them.

When the target contains embedded or copied brand guidance, treat it as downstream and potentially stale. The brand repository wins.
