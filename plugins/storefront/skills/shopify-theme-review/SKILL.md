---
name: shopify-theme-review
description: Reviews Hair Solutions Co. Shopify theme source or live pages for brand compliance, SEO, accessibility, mobile UX, performance, theme-editor safety, release risk, and implementation defects. Use when Vincent asks for a review, audit, critique, QA, verification, or pass/fail check. Do not use when the request is to implement or ship a change.
---

# Shopify Theme Review

1. Identify the exact page, URL, template, section, block, snippet, asset, or change under review.
2. Read `../../references/theme-map.md` and the narrow reference matching the surface.
3. Inspect source and rendered behavior needed for evidence.
4. Return findings first, ordered by severity, with exact file, line, URL, or rendered-page evidence.
5. Separate source-confirmed issues from live-page inferences.

## Review Scope

- Brand and design system fit.
- One H1, heading order, metadata, canonical tags, JSON-LD, FAQ parity, and internal links.
- Keyboard access, focus, labels, contrast, touch targets, reduced motion, mobile overflow.
- LCP, CLS, INP risk, image dimensions, loading attributes, and console/network errors.
- Theme-editor compatibility, dynamic sources, app blocks, and Shopify object safety.

## Error Handling

- If browser access fails, complete source review and state the missing rendered evidence.
- If no issues are found, say that clearly and list residual test gaps.
