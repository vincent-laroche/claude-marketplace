---
name: hs-incident-response
description: Handle operational incidents at Hair Solutions Co. — storefront down, Shopify/Cloudflare outage, order processing failure, customer data issue, ad account suspension, or critical supplier problem. Structured triage, communication, resolution, and post-incident review. Use for "site is down", "orders not processing", "Cloudflare issue", "emergency", or "something is broken".
---

# HS Incident Response

Merged from: `incident-response` (Anthropic engineering base) + `hair-solutions-cloudflare-ops` (HS) + `shopify-theme-dev` (HS)

## Trigger

An operational issue is impacting Hair Solutions customers, revenue, or brand — or may do so imminently.

## Incident Classification

| Severity | Definition | Response Time |
| --- | --- | --- |
| P0 — Critical | Storefront completely down, orders not processing, payment failure, data breach | Immediate |
| P1 — High | Checkout errors, Cloudflare routing broken, HubSpot not syncing, major display bug | Within 1 hour |
| P2 — Medium | Partial feature broken, email sending delayed, slow page load, ad account flagged | Within 4 hours |
| P3 — Low | Minor visual bug, non-critical content error, delayed fulfillment notification | Next business day |

## Response Sequence

### 1. Triage (first 5 minutes)

- Confirm the issue is real: check hairsolutions.co directly, check Shopify Admin, check the Cloudflare dashboard.
- Classify severity (P0–P3).
- Identify the affected system(s): Shopify, Cloudflare, HubSpot, GA4/GTM, ad platforms, Notion.
- Estimate customer impact: how many users affected? Revenue risk per hour?

### 2. Immediate Containment (P0/P1 only)

- If the issue is Cloudflare: use `hair-solutions-cloudflare-ops` to inspect routing, DNS, and Access rules.
- If the issue is the Shopify theme: switch to a safe backup theme in Shopify Admin to restore the storefront while diagnosing.
- If the issue is a failed deployment: roll back to the last known-good GitHub commit.
- Do not attempt a fix if you cannot confirm the root cause — containment first.

### 3. Diagnosis

- Pull error logs (Shopify, Cloudflare, browser console, GTM preview).
- Identify: when did it start, what changed recently (code push, app install, DNS change, campaign launch)?
- Document findings as you go.

### 4. Fix and Verify

- Apply the minimum change needed to restore service.
- Verify on a non-production URL or staging view before pushing to live.
- Confirm resolution: check the specific user-facing flow that was broken.

### 5. Communication

- For P0/P1: notify the team immediately; draft a brief customer-facing notice if orders were affected (Atelier Zero voice — factual, calm, no hype).
- For all incidents: log a timeline note in HubSpot or the incident log page.

### 6. Post-Incident Review (within 48 hours for P0/P1)

- What happened?
- What was the customer and revenue impact?
- What caused it?
- What will prevent recurrence?
- What monitoring or guardrail would have caught it earlier?

## Guardrails

- Do not deploy a fix to production without testing it first.
- Do not expose API keys, tokens, or secrets in any log, message, or document.
- Use `hair-solutions-cloudflare-ops` for all Cloudflare token and Worker operations — do not use raw token values directly.
- For data breaches or suspected customer data exposure: stop, do not investigate further without legal guidance, escalate immediately.
