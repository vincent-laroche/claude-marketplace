---
name: hs-account-research
description: Research a Hair Solutions Co. prospect or existing client — Shopify purchase history, treatment records, hair profile, HubSpot contact data, social presence, and LTV — to produce actionable sales intel before outreach or a consultation. Use for "research [client]", "look up [prospect]", "tell me about [contact]", or "intel on [company/person]".
---

# HS Account Research

Merged from: `account-research` (Anthropic base) + `hubspot-crm-model` (HS)

## Trigger

User asks to research a client, prospect, or account before outreach, a consultation booking, or a partnership conversation.

## Inputs

- Name, email, or phone of the person or company
- Research depth: quick scan, standard, or deep dive
- Optional: Shopify order ID, HubSpot contact URL

## Research Sequence

1. **HubSpot contact lookup** — use `hubspot-crm-model` to pull: contact properties, lifecycle stage, last activity date, associated deals, email engagement history, and any notes on previous interactions.
2. **Shopify purchase history** — query order history: total spend, products purchased, average order value, last order date, return rate, subscription status.
3. **Hair profile synthesis** — from notes and purchase history, infer: hair type/concern (if logged), preferred treatments, product loyalty, referral source.
4. **Web / social presence** (for B2B or influencer prospects) — search LinkedIn, Instagram, and the web for professional context, audience size, and brand fit.
5. **LTV and segment** — calculate or estimate: total lifetime value, segment (prospect / active / lapsed / VIP), and risk of churn.

## Output

**Account Brief** (shareable):

- Name, contact info, lifecycle stage
- Hair profile and key concerns
- Purchase history summary and LTV
- Last interaction and open threads
- Recommended next action and talking points
- Risks and open questions

## Guardrails

- Use only first-party HS data (HubSpot, Shopify) and public information. Do not use data brokers.
- Do not share personally identifiable details outside the team.
- Verify HubSpot records before citing them — duplicates and stale data are common.
