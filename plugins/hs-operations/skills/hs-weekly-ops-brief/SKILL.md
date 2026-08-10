---
name: hs-weekly-ops-brief
description: Produce a weekly Hair Solutions business health check — bookings and revenue vs. target, top marketing metrics, open support items, team or project priorities, and three focus areas for the coming week. Use for "weekly brief", "weekly review", "how did we do this week", "weekly business summary", or "week in review".
---

# HS Weekly Ops Brief

Merged from: `small-business` weekly-brief skill (Anthropic base) + `hubspot-business-ops` (HS) + `analytics-ads` (HS)

## Trigger

End of working week (Friday afternoon), or the user requests a weekly business review.

## Inputs

- Week date range (auto-detected or provided)
- Optional: revenue target for the week / month
- Optional: any specific areas to focus on

## Brief Sections

### 1. Revenue and Bookings

- Shopify net revenue for the week vs. prior week and vs. weekly target.
- Number of treatment/service bookings confirmed.
- New vs. returning customer split.

### 2. Marketing Performance

- Top-performing channel this week (organic, paid, email, social).
- Email: open rate and click rate for any sends this week.
- Paid: total ad spend and ROAS.
- Social: reach or engagement highlights (if tracked).
- Any campaign that launched or ended this week.

### 3. Support and Operations

- Open support tickets (count and oldest unresolved).
- Unfulfilled Shopify orders older than 48 hours.
- Any site, Cloudflare, or Shopify issues flagged this week.

### 4. HubSpot Pipeline

- New deals entered this week.
- Deals moved to Closed Won / Closed Lost.
- Pipeline value change week-over-week.

### 5. Project and Team Priorities

- Status of active projects (in-flight: on track / at risk / blocked).
- Any decisions or approvals needed from the owner.

### 6. Three Focus Areas for Next Week

Derive from the above: the three highest-leverage actions to move the business forward.

## Output

A scannable brief, each section max 5 bullets. Total length: fits one screen. Ends with the three focus areas.

## Guardrails

- Read-only data pass — do not take actions in HubSpot, Shopify, or ad platforms while generating the brief.
- If live data is unavailable for a section, say so rather than omitting the section.
