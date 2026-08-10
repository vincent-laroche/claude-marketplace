---
name: hs-month-end-close
description: Run the Hair Solutions Co. monthly financial close — reconcile Shopify revenue against HubSpot deals, review expenses, produce a P&L summary, flag anomalies, and prepare a brief for the next planning cycle. Use for "month-end close", "reconcile revenue", "monthly P&L", "financial summary", or "close the books".
---

# HS Month-End Close

Merged from: `month-end-close` (Anthropic finance base) + `hubspot-business-ops` (HS) + `analytics-ads` (HS)

## Trigger

End of calendar month, or the user requests a financial summary, revenue reconciliation, or close-the-books workflow.

## Inputs

- Month and year
- Shopify revenue report (export or paste)
- HubSpot deals closed-won during the period (export or connect)
- Expense summary (if available)
- Prior month actuals (for comparison)

## Close Sequence

### 1. Revenue Reconciliation

- Pull Shopify gross revenue, returns/refunds, and net revenue for the period.
- Pull HubSpot closed-won deals for the same period.
- Reconcile: Shopify (e-commerce) vs. HubSpot (service/treatment bookings). Identify and explain any gap.
- Verify subscriptions: expected MRR vs. actual charges.

### 2. Revenue Breakdown

| Stream | Gross | Refunds | Net | vs. Prior Month |
| --- | --- | --- | --- | --- |
| E-commerce (Shopify) | | | | |
| Treatments / Services | | | | |
| Subscriptions | | | | |
| Wholesale / B2B | | | | |
| **Total** | | | | |

### 3. Expense Review

- List known recurring expenses (Shopify, HubSpot, Cloudflare, ad spend, fulfilment).
- Flag any unrecognised or unusually large charges.
- Calculate gross margin if COGS data is available.

### 4. Anomaly Flags

- Revenue more than 15% above or below the 3-month average → investigate before closing.
- Refund rate above 5% → flag for product or fulfilment review.
- A single order representing more than 20% of monthly revenue → note for risk awareness.

### 5. Close Summary

Produce a one-page brief:

- Net revenue vs. target
- Month-over-month change
- Top revenue driver
- Key anomaly or risk
- Recommended action for next period

## Guardrails

- Do not post or file any financial records — produce drafts only.
- Do not make tax or accounting judgments. Flag items that require an accountant's review.
- Label all figures as unaudited until confirmed by the owner.
