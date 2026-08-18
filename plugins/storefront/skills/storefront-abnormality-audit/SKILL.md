---
name: storefront-abnormality-audit
description: Ruthless storefront page audit for detecting structural, semantic, visual, interaction, content, accessibility, SEO, Shopify editor, and brand abnormalities. Use when asked to inspect, audit, review, QA, critique, or find what is wrong with a Hair Solutions Co. storefront page, especially issues that render normally but feel duplicated, unfinished, confusing, stale, or accidentally assembled.
---

# Storefront Abnormality Audit

## Purpose

Use this skill to audit a rendered storefront page like a senior UX QA, content strategist, Shopify theme reviewer, and visual designer at the same time.

Do not stop at "does the page broadly work?" A page can fulfill its purpose and still contain unacceptable abnormalities: duplicate modules, repeated card grids, competing CTAs, leftover blocks, semantic repetition, broken visual rhythm, stale support details, hardcoded content, or controls that exist but do not actually work.

## Required Inputs

Work from evidence, not impression:

1. Inspect the rendered public page or provided screenshot.
2. Inspect the relevant Shopify template, sections, snippets, CSS, and schema when available.
3. If live inspection is possible, capture at least desktop and mobile evidence.
4. Use the storefront's current `DESIGN.md`, current brand token source, and live rendered behavior over stale memory or older skill files.

For Hair Solutions Co., `shopify theme dev` and local preview are permitted and are a good source of rendered evidence (Vincent's ruling, 2026-08-17). `theme push` and `publish` are also permitted (2026-08-18) — but `atelier-zero-storefront/main` is the live theme, so a CLI push goes straight to hairsolutions.co with no GitHub record. `theme delete` remains gated.

## Audit Workflow

1. **Classify the page**
   Identify the page type: home, collection, product, contact, help center, article, policy, cart, account, or other.

2. **Infer the page contract**
   State the jobs the page should perform for the visitor and the business. Keep this brief; it is the baseline, not the whole audit.

3. **Run abnormality passes**
   Read `references/audit-model.md` when doing a full page audit. Apply the passes in this order:
   - structural anomaly
   - semantic similarity and redundancy
   - visual rhythm and hierarchy
   - interaction and state
   - content integrity
   - accessibility and responsive behavior
   - SEO and schema integrity
   - Shopify editor and maintainability
   - brand and design-system fit

4. **Fail what should not pass**
   Flag an issue if it looks accidental, duplicated, misleading, non-functional, stale, unfinished, editor-hostile, or inconsistent with the page's role, even if it technically renders.

5. **Score severity**
   Use:
   - `P0`: revenue, checkout, legal, privacy, customer-data, or severe trust risk.
   - `P1`: obvious customer-facing mistake, broken core interaction, duplicate primary module, fake/stale contact detail, or page-level confusion.
   - `P2`: meaningful UX, visual, content, accessibility, or maintainability issue that weakens confidence.
   - `P3`: polish, consistency, minor rhythm, copy, or implementation cleanup.

6. **Write findings first**
   For each finding include:
   - severity and title
   - evidence from the rendered page and/or source
   - why it matters
   - recommended fix
   - owner: code, theme editor, content, design, app/integration, or policy

7. **Separate fixes from audit**
   Unless the user explicitly asks for implementation, return the audit and recommended fix order. If implementation is requested, make the smallest safe changes and verify them.

## Mandatory Abnormality Tests

Always actively search for:

- Adjacent sections with the same functional job.
- Repeated section types, repeated card grids, repeated form blocks, repeated FAQs, repeated hero-like intros.
- Headings with different wording but the same intent.
- CTA destinations that repeat without a deliberate top/bottom journey reason.
- Two modules competing for the same visitor decision.
- Sections that feel like leftover drafts from a previous version.
- Hardcoded merchant content that should be editable.
- Settings that appear in the theme editor but do not affect the rendered page.
- Broken anchors, chat links, forms, accordions, filters, variant controls, or menu controls.
- Fake placeholders, fake phone numbers, stale hours, or unsupported operational claims.
- Mobile-only failures: overlap, horizontal scroll, clipped text, tiny tap targets, sticky elements covering content.

## Output Shape

Use this structure:

```markdown
**Verdict**
One blunt paragraph: pass, conditional pass, or fail.

**Findings**
- P1 - Finding title
  Evidence: ...
  Why it matters: ...
  Fix: ...
  Owner: ...

**Fix Order**
1. ...
2. ...

**Checks Performed**
Rendered pages, viewport sizes, files inspected, tools/checks run.

**Residual Risk**
Anything not verified.
```

Keep the answer direct. Do not cushion obvious mistakes.
