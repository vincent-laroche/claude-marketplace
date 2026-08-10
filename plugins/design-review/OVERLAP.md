# design-review — overlap map

This plugin consolidates **four previously separate stacks** that all did some form of
"look at a design and judge it":

| Former plugin / location | Skills brought in |
| --- | --- |
| `visual-design-review` | design-fidelity-qa, designer-eye-review, frontend-craft-review, product-design-audit, visual-polish-review |
| `open-design-plugin` | build-test, clone-audit, critique-theater, design-extract, design-system-package, diff-review, figma-extract, token-map |
| `~/.claude/skills` (standalone) | website-ux-science-audit, brand-identity |

Collapsing four plugins into one removes the plugin-level duplication. **The skill-level
overlap has deliberately not been cut** — that judgement is yours, and deleting is harder
to undo than keeping.

## Where the real redundancy is

### Cluster 1 — "judge a live interface for quality" (4 skills, heavy overlap)

- `designer-eye-review` — designer-eye audit of a live interface; visual QA, spacing, hierarchy
- `visual-polish-review` — whether a page/screen/Figma frame/email looks polished
- `frontend-craft-review` — frontend interfaces for distinctive craft and design-system quality
- `critique-theater` — critique workflow from open-design

These answer nearly the same question. **Recommend: keep one.** `website-ux-science-audit`
is arguably stronger than all four — it has a P0–P3 severity ladder, a measured-vs-heuristic
evidence rule, and real tooling (`scripts/audit_page.py` running Lighthouse, axe, Pa11y,
Wallace). The other four are prose-only.

### Cluster 2 — genuinely distinct jobs (keep all)

- `design-fidelity-qa` — compares a **rendered implementation against a source** (Figma frame,
  mockup). No other skill does this.
- `product-design-audit` — audits a **flow** (onboarding, checkout, multi-step), not a screen.
- `website-ux-science-audit` — evidence-backed audit with live tooling and severity ranking.
- `brand-identity` — **designs** an identity system rather than critiquing one. Different verb.
  Note: generic, no Hair Solutions specifics — tagged `Needs Adaptation` in Notion.

### Cluster 3 — design-system extraction (4 skills, possible overlap)

- `design-extract`, `design-system-package`, `token-map`, `figma-extract`

These form a pipeline (extract → map tokens → package) rather than four competing takes,
so they may all earn their place. But `figma-extract` overlaps the separate `figma` plugin,
and `token-map` overlaps `brand`'s Atelier Zero token authority — which is the **canonical**
source. Any token extraction must defer to `brand`, never override it.

### Cluster 4 — not really design review

- `build-test`, `clone-audit`, `diff-review` — engineering-flavoured. Consider moving to
  `storefront` or dropping.

## Also overlapping, outside this plugin

- `storefront/storefront-abnormality-audit` — page-level QA for Shopify specifically. Distinct
  enough to keep separate, but it and `website-ux-science-audit` will both fire on
  "audit this page". Their descriptions should be sharpened so routing is unambiguous.
- `marketing/social-media-design-science-audit` — same family, social surfaces only.
- `brand/atelier-zero-brand-compliance` — brand-specific audit; the canonical one for anything
  customer-facing.

## Suggested end state

Roughly **6–8 skills**: one live-interface reviewer, `design-fidelity-qa`,
`product-design-audit`, `brand-identity`, and the extraction pipeline — with the redundant
critique skills retired once you've confirmed which voice you prefer.
