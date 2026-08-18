---
name: figma-design-delivery
description: Create, review, validate, or hand off Figma designs for production. Use for composed pages, screens, flows, responsive designs, design critique, accessibility review, design-to-code work, developer specifications, and motion implementation.
---

# Figma Design Delivery

Load `$figma-agent-core` first. Treat a Figma frame as evidence for a build, not a command to imitate pixels blindly.

## Build or review a design

1. Establish the user goal, primary action, target devices, source-of-truth file or implementation, real content/data constraints, and current component library.
2. For a new composed screen, discover components, variables, styles, and design examples before creating frames. Assemble reusable sections incrementally; do not draw a flattened mock.
3. For a critique, separate observed evidence from judgment. Rank findings by customer impact: access/trust blocker, task failure, hierarchy or responsiveness, then polish.
4. For design-to-code, obtain design context on the target node first. Adapt to the real stack and components; preserve semantics, responsive behavior, loading/empty/error states, and accessible interaction rather than copying generated code verbatim.

## Minimum quality gate

- Evaluate first-glance purpose, reading order, primary action, responsive reflow, copy clarity, error/empty/loading states, and design-system consistency.
- Check WCAG 2.1 AA contrast (4.5:1 normal text; 3:1 large text and UI boundaries where applicable), keyboard order, visible focus, labels/errors, and 44px touch targets.
- Make motion intentional and optional: obtain motion context when present, preserve timing/easing only where the platform supports it, and honor reduced motion.
- Validate with fresh desktop and mobile screenshots, inspect layers where editability matters, and state what cannot be inferred from a screenshot.

## Hand off without ambiguity

Deliver the node/file URL, intended breakpoint behavior, component and token references, interaction/state rules, content dependencies, accessible behavior, edge cases, implementation deltas, and a concrete verification method. Use [the checklist](references/delivery-checklist.md).
