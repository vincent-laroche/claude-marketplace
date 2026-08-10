---
name: hs-forecast
description: Generate a Hair Solutions revenue forecast with best/likely/worst scenarios across product and service revenue streams. Covers Shopify e-commerce, treatment bookings, subscriptions, and wholesale. Use for "quarterly forecast", "monthly revenue projection", "gap to target", or "pipeline coverage check".
---

# HS Forecast

Merged from: `forecast` (Anthropic base) + `analytics-ads` (HS) + `hubspot-business-ops` (HS)

## Trigger

User wants a revenue forecast, a gap-to-target assessment, or a coverage check against the monthly/quarterly plan.

## Inputs

- Current period (month or quarter)
- Revenue target for the period
- Actual revenue to date (from Shopify or provided by user)
- Open HubSpot pipeline value (deals in active stages)
- Historical conversion rates if known

## Revenue Streams

| Stream | Source | Notes |
| --- | --- | --- |
| E-commerce products | Shopify GA4 | Main volume driver |
| Treatment bookings | HubSpot deals | Appointment-driven |
| Subscriptions | Shopify | Predictable MRR |
| Wholesale / B2B | HubSpot deals | Lumpy, larger ASP |

## Forecast Build

1. **Actual to date**: revenue already recognized.
2. **Committed pipeline**: deals at late stage (Proposal Accepted or Closed pending payment). Apply 85–90% confidence.
3. **Upside pipeline**: deals at mid-stage (Consultation Booked, Demo/Trial). Apply 40–60% confidence.
4. **Run-rate projection**: if Shopify product revenue is on a clear trajectory, extrapolate to period end.
5. **Scenarios**:
   - **Best case**: committed + all upside converts + run-rate holds.
   - **Likely**: committed + 50% upside + run-rate holds.
   - **Worst case**: committed only + run-rate 10% below trend.
6. **Gap analysis**: likely forecast vs. target → gap amount and what would close it.

## Output

- Scenario table (Best / Likely / Worst)
- Gap-to-target and required pipeline to close it
- Top 3 deals or Shopify actions that would most improve the forecast
- Confidence notes and data quality flags

## Guardrails

- Label all projections as estimates. Do not present forecasts as guarantees.
- If input data is incomplete, state what is missing and its impact on confidence.
