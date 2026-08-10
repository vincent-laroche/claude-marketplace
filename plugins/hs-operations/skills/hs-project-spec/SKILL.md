---
name: hs-project-spec
description: Write a clear, actionable spec for a Hair Solutions project — new storefront feature, marketing campaign, operational improvement, or integration. Covers goals, success metrics, scope, open questions, and a phased delivery plan. Use for "write a spec", "define the project", "document requirements", "what are we building", or "project brief".
---

# HS Project Spec

Merged from: `feature-spec` (Anthropic product-management base)

## Trigger

User wants to define, document, or plan a project before starting work.

## Spec Template

### 1. Title and Owner

- Project name (short, specific)
- Owner and key stakeholders
- Target start and completion date

### 2. Problem Statement

One paragraph: what pain or opportunity does this address? What happens if we do nothing?

### 3. Goals and Success Metrics

| Goal | Metric | Target | Measurement Source |
| --- | --- | --- | --- |
| | | | |

Keep to 2–3 goals maximum. Each must be measurable.

### 4. Scope

**In scope** (what this project will deliver):

- List each deliverable specifically.

**Out of scope** (what this project will NOT do):

- Explicitly list common misunderstandings or related work to exclude.

### 5. HS Stack Touchpoints

For each system the project touches, note what changes:

- **Shopify**: theme changes, metafields, product config, app additions
- **HubSpot**: workflow changes, new properties, automation, email
- **Cloudflare**: Worker changes, subdomain, access rules
- **Figma**: design deliverables required
- **Notion**: documentation or database changes
- **Marketing channels**: social, paid, email involvement

### 6. Open Questions

List unknowns that must be resolved before or during the project. Assign each an owner.

### 7. Risks

List top 2–3 risks. For each: likelihood (H/M/L), impact (H/M/L), mitigation plan.

### 8. Phased Delivery Plan

| Phase | Description | Output | Timeline |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |

### 9. Approval

- Decision required from: [name]
- Approved / Not approved / Needs revision

## Guardrails

- Do not start building before the spec is approved.
- Keep the spec short enough to fit one page unless complexity genuinely requires more.
- Route to the relevant domain plugin for detailed technical planning (e.g. `shopify-theme-dev` for Liquid work, `hubspot-developer` for API integrations).
