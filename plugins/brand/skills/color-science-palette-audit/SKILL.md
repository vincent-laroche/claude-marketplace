---
name: color-science-palette-audit
description: Audits brand color palettes with modern color science. Use when evaluating hex palettes, color compatibility, contrast, perceptual distance, temperature, harmony, role fit, accessibility, brand discipline, CSS color-token drift, or whether colors work well together. Do not use for image color grading, video color correction, generic graphic design moodboards, or CSS implementation work without a palette-evaluation question.
---

# Color Science Palette Audit

## Purpose

Use this skill to turn color science into a practical brand-system decision: whether a palette is coherent, accessible, role-ready, and enforceable in CSS/design tokens. Treat the six evaluation lenses as required checks, not the whole skill.

## Workflow

1. Identify the decision being made: approve a palette, assign semantic roles, compare alternatives, audit CSS drift, or diagnose accessibility.
2. Normalize supplied colors to uppercase hex unless the user requests another output format.
3. For modern color-science context, read `references/color-science-current.md` before making claims about OKLCH, APCA, CSS Color 4/5, or current browser/standards status.
4. For a palette of hex codes, run:

```bash
python3 scripts/audit_palette.py '#111111' '#F8F4EE' '#C96A4A'
```

5. Evaluate and report these six dimensions:
   - **Contrast**: WCAG 2.x contrast ratios for text/background pairings, plus where low-contrast pairs may still work as borders, fills, or decorative surfaces.
   - **Perceptual distance**: OKLCH/OKLab-space distance between colors; flag near-duplicates, weak differentiation, and overly large jumps.
   - **Temperature and harmony**: hue family, warm/cool balance, chroma consistency, and whether accents feel intentional.
   - **Role fit**: assign candidate roles such as ink, body text, surface, paper, border, muted fill, accent, warning, success, or disabled state.
   - **Accessibility**: WCAG 2.x text thresholds as the compliance floor; treat APCA/WCAG 3 as useful supplemental analysis only when a reliable implementation is available.
   - **Brand discipline**: judge whether the palette supports a small, repeatable system with clear semantic roles and limited off-brand one-off colors.
6. Apply the current-web-color discoveries from `references/color-science-current.md`:
   - Use OKLCH/OKLab internally for perceptual reasoning, then return uppercase hex when the brand system is hex-first.
   - Use CSS Color 4/5 features such as `oklch()`, `color-mix()`, and relative color syntax as authoring options only after checking project/browser constraints.
   - Use WCAG 2.x contrast as the compliance floor; describe APCA/WCAG 3 as supplemental and still developing.
   - Use Project Wallace for CSS/design-token extraction and drift checks when auditing implementation, not for standalone aesthetic judgment.
7. Separate measured facts from design judgment. Label computations as measured; label harmony, role-fit, and brand-discipline conclusions as recommendations.
8. When auditing a CSS file or Shopify theme, first extract colors with Project Wallace when available, then compare the extracted set against the approved palette. Do not assume a color is approved because it appears in production CSS.

## Project Wallace Integration

1. Use `wallace <file.css> --json` for CSS metrics and raw color inventory when the CLI is available.
2. Use `@projectwallace/css-design-tokens` when a script or app needs design-token objects from CSS.
3. Compare extracted colors against the approved palette, semantic token names, and allowed derived values.
4. Report drift as specific unapproved values, usage contexts, and suggested token replacements.

## Output Standard

1. Start with a clear verdict: approve, approve with changes, or do not approve.
2. Show the recommended role map for each color.
3. List color pairs that are safe for normal text, large text only, or not suitable for text.
4. Flag colors to merge, adjust, reserve as accents, or remove.
5. Give concrete next steps: revised hex values, role naming, CSS token names, or a Project Wallace drift check.

## Guardrails

1. Do not claim that a palette is accessible because it is aesthetically harmonious; accessibility requires measured contrast.
2. Do not use APCA as the sole compliance answer while WCAG 3 contrast methods remain in progress.
3. Do not recommend more brand colors when fewer semantic colors solve the design problem.
4. Do not convert a hex-only brand system to OKLCH in user-facing documentation unless explicitly asked; use OKLCH internally for analysis and return hex recommendations by default.
5. For Hair Solutions Co. customer-facing work, invoke `atelier-zero-design-system` and read the live canonical brand repository before recommending or implementing any palette decision.

## Error Handling

1. If supplied colors are missing, malformed, or mixed with non-color text, stop and ask for the exact hex list or extract only unambiguous hex values after stating the assumption.
2. If a browser-support, WCAG, APCA, or CSS Color 4/5 claim could affect implementation, verify the current source before presenting it as current.
3. If Project Wallace is unavailable, continue with `scripts/audit_palette.py` for standalone palette analysis and state that CSS drift extraction was not performed.
4. If a palette passes contrast but fails role clarity or brand discipline, report it as technically usable but not approved as a brand system.
5. If a user asks for production CSS changes, switch to the relevant implementation skill and preserve the palette-audit result as input, not as an edit instruction.

## Resources

- `scripts/audit_palette.py`: deterministic CLI for hex palette analysis.
- `references/color-science-current.md`: current standards and practical color-science guidance.
