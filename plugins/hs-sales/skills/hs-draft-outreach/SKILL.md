---
name: hs-draft-outreach
description: Research a Hair Solutions prospect or lapsed client and draft personalized outreach — re-engagement emails, product recommendation messages, treatment follow-ups, and partnership pitches. Voice must follow Atelier Zero v7 rules. Use for "draft outreach to [contact]", "write re-engagement email", or "reach out to [prospect]".
---

# HS Draft Outreach

Merged from: `draft-outreach` (Anthropic base) + `hs-email-sequence` (HS)

## Trigger

User wants to contact a prospect, lapsed client, or partner with a personalized message.

## Outreach Types

| Type | Use when |
| --- | --- |
| Re-engagement | Client has not purchased or booked in 90+ days |
| Product recommendation | Client's purchase history suggests a natural next product |
| Treatment follow-up | Client attended a consultation but did not book |
| Win-back | Client churned to a competitor or cancelled |
| Partnership pitch | Influencer, salon, or brand collaboration |
| Cold outreach | New prospect from web research or referral |

## Drafting Sequence

1. Run `hs-account-research` (quick scan) to gather personalization context.
2. Select the outreach type and confirm the one goal of this message.
3. Draft: opening hook (specific to this person) → one clear value statement → one low-friction ask. Three paragraphs maximum.
4. Apply Atelier Zero voice:
   - Warm, specific, adult. "We" to "you."
   - No urgency, scarcity, hype, or exclamation marks.
   - No emoji.
   - Never fabricate results or claims.
5. Write 2–3 subject line variants.
6. Write a short PS line with a secondary soft prompt if appropriate.

## Output

- Subject line options (2–3)
- Email body (ready to send, not yet sent)
- Optional: LinkedIn message variant (shorter)
- Personalization notes: what you used and what to verify before sending

## Guardrails

- Do not send the email — present drafts for approval.
- Do not use consent-required customer media (before/afters, DMs, testimonials) without confirmed exact-use consent.
- Route to `hs-brand-review` for any outreach that will be used as a template at scale.
