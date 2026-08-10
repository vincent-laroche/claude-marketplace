# Evidence Frameworks For Website UX Audits

Use this reference to ground audits in established rules instead of taste alone.

## Usability Heuristics

Use Nielsen Norman Group's 10 usability heuristics as the behavioral baseline:

- visibility of system status;
- match between system and real-world language;
- user control and freedom;
- consistency and standards;
- error prevention;
- recognition rather than recall;
- flexibility and efficiency of use;
- aesthetic and minimalist design;
- help users recognize and recover from errors;
- help and documentation.

Apply heuristics to actual tasks, not as abstract checklist scoring.

## Interaction Science

- **Fitts's Law**: frequently used controls should be large enough and easy to reach, especially on mobile and in sticky UI.
- **Hick's Law**: excessive equally weighted choices slow decisions; group, prioritize, or progressively disclose.
- **Cognitive load**: reduce memory burden, unclear state, repeated decisions, ambiguous labels, and unnecessary visual competition.
- **Recognition over recall**: expose key options, status, and comparison cues instead of hiding them behind memory-dependent flows.
- **Feedback loops**: user actions need immediate visible feedback, especially add-to-cart, filters, forms, accordions, drawers, and async states.

## Visual Composition

Assess composition through:

- clear first-viewport purpose;
- hierarchy by size, weight, spacing, contrast, and position;
- predictable scan path;
- balance between dense information and breathing room;
- proximity and grouping;
- alignment and grid discipline;
- figure/ground clarity;
- repetition and rhythm;
- restrained emphasis, with one primary action per decision moment.

Flag pages where everything competes equally or the most important object is not visually dominant.

## Accessibility

Use WCAG 2.2 as the compliance floor:

- keyboard navigation and visible focus;
- semantic structure and heading order;
- name, role, and value for controls;
- contrast for text and essential non-text boundaries;
- labels, errors, and instructions for forms;
- target size and spacing for touch;
- no content hidden from assistive tech when it is visually required;
- no reliance on color alone for state or meaning.

Automated checks are incomplete. Pair them with keyboard, screen-reader semantics, viewport, motion, and comprehension review.

## Performance UX

Use Core Web Vitals as the measurable performance-experience layer:

- LCP at or below 2.5 seconds for good loading experience;
- INP at or below 200 milliseconds for good interaction responsiveness;
- CLS at or below 0.1 for stable layout.

Treat field data as stronger than lab data. Use Lighthouse as a diagnostic snapshot, not the final truth.

## Brand And Design-System Discipline

A strong website UI should:

- make page roles and component roles repeatable;
- use consistent spacing, type scale, color roles, radius, shadows, and motion;
- avoid one-off components unless the page job requires them;
- make primary, secondary, and contextual actions visually distinct;
- match brand tone without sacrificing task clarity;
- reserve decorative elements for actual attention or trust value.

For Hair Solutions Co., customer-facing reviews should preserve calm editorial restraint, warm-neutral visual language, realistic media, no hype, and relief-not-rescue positioning.

## Source Anchors

- Nielsen Norman Group usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
- Nielsen Norman Group visual design principles: https://www.nngroup.com/articles/principles-visual-design/
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Core Web Vitals: https://web.dev/articles/vitals
- Material Design accessibility and layout guidance: https://m3.material.io/
