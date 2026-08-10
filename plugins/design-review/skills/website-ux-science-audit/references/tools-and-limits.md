# Tools And Limits

Use tools to collect evidence, not to replace judgment.

## Local Tool Stack

- `lighthouse`: performance, accessibility, SEO, best-practice, and page diagnostics.
- `axe` from `@axe-core/cli`: accessibility rule checks with JSON output.
- `pa11y`: CLI-friendly accessibility backup and WCAG runner.
- `playwright`: screenshots, viewport QA, interaction checks, ARIA snapshots, and visual regression setup.
- `wallace`: CSS analytics and color/design-token drift evidence.
- `@projectwallace/css-design-tokens`: programmable extraction of color, type, radii, durations, easing, shadows, and other tokens from CSS.
- `color-science-palette-audit`: companion skill for palette compatibility, contrast, and brand-color decisions.

## What Each Tool Can Prove

- Lighthouse can reveal likely performance, SEO, accessibility, and best-practice issues in a lab run.
- axe and Pa11y can catch many accessibility rule violations.
- Playwright can verify page state, screenshots, responsive layouts, keyboard flows, and ARIA snapshots.
- Wallace can reveal CSS complexity, color inventory, and implementation drift.
- Visual regression tools such as Percy, Chromatic, and Playwright snapshots can detect UI changes, not whether the design is good.
- Microsoft Clarity, Hotjar, GA4, Search Console, and funnel analytics can show real behavior when installed and connected.
- AI attention tools such as Attention Insight, EyeQuant, and 3M VAS can estimate attention patterns, but should be treated as pre-launch directional evidence.

## What Tools Cannot Prove

- A Lighthouse score does not prove the page persuades, educates, or converts.
- An axe pass does not prove the experience is accessible for all users.
- A heatmap does not prove user intent without task and traffic context.
- A screenshot does not prove interactive state, keyboard access, or mobile ergonomics.
- A style-library match does not prove brand fit.

## Recommended Evidence Strength

1. Direct user behavior or usability-test evidence.
2. Field performance and analytics data.
3. Tool output from Lighthouse, axe, Pa11y, Playwright, and Wallace.
4. Source inspection and semantic review.
5. Expert heuristic and composition review.
6. AI attention prediction or aesthetic preference.

Report evidence strength with findings when stakes are high.

## Current Source Anchors

- Lighthouse: https://developer.chrome.com/docs/lighthouse/overview
- Web Vitals: https://web.dev/articles/vitals
- axe-core: https://github.com/dequelabs/axe-core
- axe CLI: https://github.com/dequelabs/axe-core-npm
- Pa11y: https://pa11y.org/
- Playwright ARIA snapshots: https://playwright.dev/docs/aria-snapshots
- Project Wallace: https://www.projectwallace.com/
- Storybook accessibility testing: https://storybook.js.org/docs/writing-tests/accessibility-testing
- Microsoft Clarity: https://clarity.microsoft.com/
- Hotjar heatmaps: https://www.hotjar.com/
- Attention Insight: https://attentioninsight.com/
