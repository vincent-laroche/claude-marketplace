# Storefront Abnormality Audit Model

## Terms To Recognize

This skill combines established web-review practices:

- UX audit: systematic evaluation of usability, navigation, content, accessibility, and business-impact barriers.
- Heuristic evaluation: expert review against usability principles such as visibility, match with user expectations, consistency, error prevention, recognition over recall, and minimalist design.
- Design audit: consistency and quality review across layout, typography, color, components, spacing, and brand expression.
- Content audit / content analysis: review of usefulness, clarity, duplication, structure, claims, and maintenance burden.
- QA testing: verification that links, forms, states, and responsive layouts work.
- Visual regression testing: screenshot-based detection of unintended visual changes, layout defects, overlap, hidden elements, and style drift.
- Structural anomaly detection: custom layer for detecting repeated modules, duplicate functions, competing CTAs, stale blocks, and similar sections that render but should not exist together.

## Page Contracts

Use these as starting points, then adjust to the actual page.

### Contact / Help / FAQ

Expected job: route the visitor to the right support path, answer urgent common questions, set response expectations, reduce repetitive support demand, and provide one clear escalation path.

High-risk abnormalities:

- Duplicate contact-card groups or support-routing grids.
- Contact options without channel purpose or expected response timing.
- Fake or stale phone numbers, hours, WhatsApp links, chat promises, or email claims.
- Form plus external form link plus card link all competing without hierarchy.
- FAQ content hardcoded when Vincent expects editor control.
- FAQ schema that does not exactly match visible questions and answers.

### Home

Expected job: explain the category, establish trust, guide product discovery, show realism/craft, answer next-step uncertainty, and move visitors toward shopping or education.

High-risk abnormalities:

- Multiple heroes or multiple primary narratives.
- Product-path modules repeated under different names.
- Trust/proof blocks repeated without new evidence.
- Editorial sections that say the same thing in different words.
- CTAs that compete before the visitor understands the product.

### Collection

Expected job: help visitors compare products and narrow choices.

High-risk abnormalities:

- Filters or sort that are hidden, broken, misleading, or too low on mobile.
- Product cards with insufficient differentiators.
- Educational sections repeated above the grid before product discovery.
- Collection intro copy that does not match the actual product set.

### Product

Expected job: support confident purchase by explaining product, variants, price, availability, fit, realism, lifespan, care, shipping/returns, and help paths.

High-risk abnormalities:

- Variant controls that are unclear, clipped, non-functional, or visually disconnected from price/add-to-cart.
- Repeated purchase panels, repeated specs, repeated accordions, or repeated guarantee blocks.
- Copy that hides material differences or overpromises results.
- Sticky elements covering checkout-adjacent controls on mobile.

### About

Expected job: establish human credibility, craft, mission, operational truth, and trust.

High-risk abnormalities:

- Generic manifesto copy without proof.
- Repeated founder/story sections.
- Decorative imagery without credibility value.
- Claims that sound like medical, rescue, or hype positioning.

## Abnormality Passes

### 1. Structural Anomaly

Ask:

- Are there repeated sections with the same layout immediately adjacent?
- Do two sections perform the same page job?
- Are there two card grids, two form areas, two FAQ areas, or two intro/hero blocks?
- Does the page look like multiple versions were stacked instead of edited?
- Are there hidden sections in the template that are still carrying stale content?

Flag even when each section is individually well designed.

### 2. Semantic Similarity And Redundancy

Ask:

- Do headings use different words for the same promise?
- Do descriptions repeat the same support path, product value, or trust claim?
- Do CTAs point to the same destination with no journey reason?
- Are users being asked to make the same decision twice?

Similar does not mean identical. "You've got questions? We've got answers" and "Still need a hand?" can be the same support-routing intent.

### 3. Visual Rhythm And Hierarchy

Ask:

- Does the page establish a clear first, second, third priority?
- Are sections too similar in density, shape, or rhythm?
- Is the page dominated by cards, badges, icons, or repeated grids?
- Does spacing imply relationships correctly?
- Does anything look like a leftover default theme section?

### 4. Interaction And State

Test:

- Primary and secondary CTAs.
- Forms, external forms, chat triggers, WhatsApp links, account links.
- Accordions, tabs, filters, menus, localization controls.
- Hover, focus, loading, success, error, and empty states when possible.

Flag controls that exist but do not produce the promised action.

### 5. Content Integrity

Check:

- Facts: hours, phone, email, shipping promises, returns, production timing, stock/custom distinctions.
- Claims: avoid unsupported guarantees, medical implications, or shame/pity language.
- Maintenance: content hardcoded in Liquid when it should live in schema, metafields, pages, or metaobjects.
- Specificity: vague support copy should be replaced with concrete route, expectation, or next step.

### 6. Accessibility And Responsive Behavior

Check:

- One H1 and logical heading order.
- Keyboard focus and visible focus states.
- Labels, field names, error text, ARIA where required.
- Mobile widths 320, 375, 390, 430 when changing or auditing mobile.
- No overlap, horizontal scroll, clipped text, or tap targets below 44px.
- Contrast meets WCAG AA for meaningful text and controls.

### 7. SEO And Schema

Check:

- Title and meta match the page.
- Visible content supports search intent.
- Internal links point to relevant help, products, collections, policies, or guides.
- FAQ schema only exists when exact visible FAQs exist.
- ContactPage/Organization schema does not contain stale or fake contact data.

### 8. Shopify Editor And Maintainability

Check:

- Section names are meaningful in the editor.
- Settings affect rendered output.
- Merchant-editable content is not unnecessarily hardcoded.
- Reusable patterns are not duplicated across separate sections.
- Blocks preserve `block.shopify_attributes`.
- App-managed files are not modified unless explicitly requested.

### 9. Brand And Design-System Fit

For Hair Solutions Co.:

- Use the current storefront `DESIGN.md` and `/Users/vMac/08_brand/brand-design-system/tokens/tokens.css` as the current color source, not stale bundled skill colors.
- Voice: calm, plain, adult, no pity, no hype, no emoji, no exclamation marks.
- Visual language: restrained, editorial, warm-neutral, useful photography, minimal decoration.
- Clay/copper accent should be controlled and never become general body text or decorative noise.

## Severity Examples

- P0: broken checkout-adjacent control, privacy leak, legal/policy contradiction, exposed customer data, false refund/shipping promise.
- P1: duplicate primary contact-routing sections, broken contact form or chat link, fake phone number, mobile CTA covers form, page has two H1s that confuse structure.
- P2: repeated CTA cluster, too many similar cards, hardcoded FAQ content, weak heading hierarchy, card-grid fatigue, poor mobile rhythm.
- P3: minor spacing inconsistency, slightly stale label, inconsistent capitalization, non-critical hover mismatch.
