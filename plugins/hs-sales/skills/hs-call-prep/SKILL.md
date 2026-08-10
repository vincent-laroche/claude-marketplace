---
name: hs-call-prep
description: Prepare for a Hair Solutions client consultation, sales call, or partnership meeting. Reviews client history, current hair goals, open deals, recommended products or treatments, and suggested agenda. Use for "prep my call with [client]", "consultation prep", or "get me ready for [meeting]".
---

# HS Call Prep

Merged from: `call-prep` (Anthropic base)

## Trigger

User has an upcoming client consultation, sales call, trade partnership meeting, or influencer conversation and wants to walk in prepared.

## Inputs

- Client name or contact URL
- Meeting type: consultation, product review, partnership, check-in
- Date and duration
- Any specific topics the client raised in advance

## Prep Sequence

1. Run `hs-account-research` for the contact (quick scan if time is short, standard otherwise).
2. Review open HubSpot deals or active quotes for this contact.
3. Pull last 3 email/call notes from the HubSpot timeline.
4. Review last Shopify order and any pending items (abandoned cart, subscription renewal).
5. Identify the most relevant treatment or product recommendation based on hair profile.
6. Check whether any active promotions or seasonal offers apply.
7. Draft a 3-point agenda: (a) understand current state and goals, (b) present recommendation, (c) agree on next step.

## Output

**Call Prep Brief**:

- Client snapshot (name, segment, LTV, last interaction)
- Open threads and outstanding items
- Recommended talking points (max 3)
- Suggested agenda
- Potential objections and responses
- Ideal next step to commit before ending the call

## Guardrails

- Do not promise treatments, prices, or timelines not confirmed with the team.
- Keep the prep brief to one page — depth comes from the conversation, not the prep doc.
