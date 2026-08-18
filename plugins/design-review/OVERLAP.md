# design-review — overlap map

This plugin consolidates **four previously separate stacks** that all did some form of
"look at a design and judge it":

| Former plugin / location | Skills brought in |
| --- | --- |
| `visual-design-review` | design-fidelity-qa, designer-eye-review, frontend-craft-review, product-design-audit, visual-polish-review |
| `open-design-plugin` | build-test, clone-audit, critique-theater, design-extract, design-system-package, diff-review, figma-extract, token-map |
| `~/.claude/skills` (standalone) | website-ux-science-audit, brand-identity |

Collapsing four plugins into one removed the plugin-level duplication. The skill-level
overlap cut was **executed on 2026-08-10**, taking the plugin from 15 skills to 8.

## What was cut

### Cluster 1 — "judge a live interface for quality" (4 removed, 1 kept)

Removed: `designer-eye-review`, `visual-polish-review`, `frontend-craft-review`,
`critique-theater`.

All four answered nearly the same question in prose only. `website-ux-science-audit` was
kept in their place — it has a P0–P3 severity ladder, a measured-vs-heuristic evidence
rule, and real tooling (`scripts/audit_page.py` running Lighthouse, axe, Pa11y, Wallace).

### Cluster 4 — not really design review (3 removed)

Removed: `build-test`, `clone-audit`, `diff-review`. Engineering-flavoured, not design
review. These were dropped rather than moved to `storefront`; if any of them turns out to
be wanted, recover it from git history rather than rewriting.

## What was kept (8)

### Genuinely distinct jobs

- `design-fidelity-qa` — compares a **rendered implementation against a source** (Figma frame,
  mockup). No other skill does this.
- `product-design-audit` — audits a **flow** (onboarding, checkout, multi-step), not a screen.
- `website-ux-science-audit` — evidence-backed audit with live tooling and severity ranking.
- `brand-identity` — removed 2026-08-18, see below.

### Design-system extraction pipeline — removed 2026-08-18

`design-extract`, `design-system-package`, `token-map` and `brand-identity` were
removed from this plugin. A design system does not live in the marketplace: the
authority is `vincent-laroche/brand-design-system`, and carrying extraction and
identity tooling here invited a second copy that would drift from it. The caveat
this file already recorded — that `token-map` overlapped the canonical Atelier
Zero token authority and had to defer to it — was the warning sign.

`figma-extract` stays; it reads a Figma file and overlaps the separate `figma`
plugin, not the brand authority.

All four are recoverable from git history (`git log --diff-filter=D --  'plugins/design-review/skills/*'`).

## Still overlapping, outside this plugin

- `storefront/storefront-abnormality-audit` — page-level QA for Shopify specifically. Distinct
  enough to keep separate, but it and `website-ux-science-audit` will both fire on
  "audit this page". Their descriptions should be sharpened so routing is unambiguous.
- `marketing/social-media-design-science-audit` — same family, social surfaces only.
- `brand/atelier-zero-brand-compliance` — brand-specific audit; the canonical one for anything
  customer-facing.

## Recovery

Every removed skill is in git history. To restore one:

```bash
git checkout 200dd9a -- plugins/design-review/skills/<name>
```
