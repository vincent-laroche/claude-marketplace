---
name: hs-pipeline-review
description: Analyze the Hair Solutions HubSpot sales pipeline — prioritize open deals, flag stale or at-risk opportunities, audit hygiene issues, and produce a weekly action plan. Use for "weekly pipeline review", "which deals to focus on", "stale deals", "pipeline health", or "deal stage audit".
---

# HS Pipeline Review

Merged from: `pipeline-review` (Anthropic base) + `hubspot-crm-model` (HS) + `hubspot-business-ops` (HS)

## Trigger

User wants to review the current deal pipeline, prioritize focus for the week, or audit CRM hygiene.

## Inputs

- Pipeline data: paste a HubSpot pipeline export, or connect via `hubspot-api` to pull live deals.
- Current date (auto-detected)
- Optional: revenue target and current attainment

## Review Passes

### 1. Stage Distribution

Count deals by stage. Flag: top-heavy (too many early-stage deals), bottom-light (no near-close deals), or a single-stage cluster.

### 2. Staleness Audit

Flag any deal with no activity in the last:

- 3+ days (at Consultation Booked or later)
- 7+ days (at any stage)

### 3. Hygiene Issues

Check for:

- Missing close date
- Close date in the past without a Won/Lost outcome
- No associated contact or company
- Deal value is $0 or blank
- Stage has not moved in 14+ days

### 4. Risk Flags

- Single-threaded deals (only one contact touched)
- Deals where last activity was client-initiated with no HS response
- Deals with a competitor mentioned in notes

### 5. Priority Ranking

Rank top 5 deals by: deal value × stage probability × days-since-last-activity (recency penalty).

## Output

- Stage distribution summary
- Staleness and hygiene issue list (with deal names and recommended fixes)
- Risk-flagged deals
- Top 5 priority deals with recommended next action for each
- One-paragraph pipeline health verdict

## Guardrails

- Do not update deal stages or contact records while generating the review — read-only pass first.
- Present hygiene fixes as a list for the user to approve before applying in HubSpot.
