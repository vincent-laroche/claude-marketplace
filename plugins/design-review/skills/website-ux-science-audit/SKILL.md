---
name: website-ux-science-audit
description: Audits websites, ecommerce pages, UI flows, layouts, information architecture, visual composition, accessibility, performance UX, and brand-system discipline with evidence-backed UX rules and local audit tools. Use when reviewing websites, landing pages, Shopify storefronts, UI/UX science, composition, conversion friction, Core Web Vitals, WCAG, heuristic evaluation, or tool-assisted page QA. Do not use for pure code implementation, generic design inspiration, image/video color grading, or palette-only analysis.
---

# Website UX Science Audit

## Workflow

1. Define the audit target: full site, page type, page section, user flow, component, or design mockup.
2. Classify the audit mode:
   - **Expert review**: screenshots, source, or page description only.
   - **Tool-assisted audit**: live URL or local page can be tested.
   - **Behavioral audit**: analytics, heatmaps, recordings, or funnel data are provided.
3. Read the relevant references just in time:
   - `references/evidence-frameworks.md` for UX laws, heuristics, accessibility, performance, and composition.
   - `references/tools-and-limits.md` for Lighthouse, axe, Pa11y, Playwright, Wallace, heatmaps, and AI attention tools.
   - `references/ecommerce-ux.md` for ecommerce, Shopify, product pages, collections, cart, checkout, and mobile commerce.
4. If a URL or CSS file is available, run or prepare local checks:

```bash
python3 scripts/audit_page.py --url https://example.com --css path/to/styles.css --out /tmp/ux-audit --run
```

5. Evaluate the page across the core audit lenses:
   - user intent and page job;
   - information architecture and page structure;
   - visual hierarchy and composition;
   - interaction ergonomics and cognitive load;
   - accessibility and inclusive usability;
   - performance UX and Core Web Vitals risk;
   - mobile and responsive behavior;
   - ecommerce trust, selection, and conversion flow when relevant;
   - brand discipline and design-system consistency;
   - evidence quality: measured, heuristic, behavioral, or inference.
6. Separate measured facts from expert judgment. Never present a heuristic observation as field data.
7. When the issue is color-specific, invoke `color-science-palette-audit`. When the issue is Hair Solutions customer-facing brand implementation, invoke `atelier-zero-design-system`.

## Output Standard

1. Start with a verdict: pass, pass with fixes, or fail for the target user/job.
2. Lead with ranked findings, not general praise. Use severity labels:
   - **P0 revenue or access blocker**
   - **P1 conversion, trust, or accessibility risk**
   - **P2 usability, clarity, or mobile friction**
   - **P3 polish, consistency, or optimization**
3. For each finding include: evidence type, affected area, issue, user/business impact, specific fix, and verification method.
4. Include a concise section map when auditing a page: keep, revise, remove, add, or test.
5. Finish with the next validation step: browser screenshot, Lighthouse, axe, Pa11y, Playwright viewport pass, analytics review, or live-user test.

## Guardrails

1. Do not equate beautiful UI with usable UX. Usability requires task fit, clarity, accessibility, and feedback.
2. Do not overfit to generic heuristics when ecommerce intent, page type, or brand positioning changes the correct answer.
3. Do not claim analytics or heatmap behavior unless real behavioral evidence was provided.
4. Do not rely on Lighthouse or axe as complete UX proof; automated tools are necessary but incomplete.
5. Do not recommend wholesale redesigns when a small structural, copy, spacing, or interaction change solves the risk.

## Error Handling

1. If no URL, screenshot, code, or page description is provided, ask for the smallest artifact needed to audit the target.
2. If a live audit tool fails, report the exact failed tool, keep the remaining evidence, and give the next diagnostic.
3. If a page is behind login, customer data, checkout, or production-sensitive flows, avoid write actions and request safe read-only access or screenshots.
4. If automated scores conflict with visible UX defects, explain the conflict and prioritize user-impact evidence.
5. If the user asks for implementation after the audit, switch to the appropriate build skill and preserve the audit findings as requirements.

## Resources

- `scripts/audit_page.py`: checks installed audit tools, plans commands, and can run Lighthouse, axe, Pa11y, and Wallace.
- `references/evidence-frameworks.md`: science-backed UX, accessibility, performance, and composition criteria.
- `references/tools-and-limits.md`: current tool stack, uses, outputs, and limits.
- `references/ecommerce-ux.md`: ecommerce and Shopify-specific audit criteria.
