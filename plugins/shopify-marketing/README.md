# Shopify Marketing

Shopify-native marketing operations for Hair Solutions Co. (`one-head-hair.myshopify.com`) on the
2026 **Shopify Messaging** platform — the app that replaced Shopify Email.

This plugin is the counterpart to `email-marketing` (MailerLite) and `crm` (HubSpot). It owns
everything that runs *inside* Shopify: campaigns, lifecycle automations, and the Inbox chat surface.

## Skills

| Skill | Owns | Read it for |
|---|---|---|
| `shopify-messaging-marketing` | Outbound campaigns | Email/SMS/WhatsApp campaigns, reusable templates, custom Liquid, sender authentication, deliverability, consent, segmentation, scheduling, UTM tracking, Growth analytics, Campaign Autopilot |
| `shopify-lifecycle-automation` | Triggered journeys | Welcome, abandoned browse/cart/checkout, post-purchase, upsell, win-back, replenishment, VIP; Shopify Flow workflows, Shopify Forms, customer segments, ShopifyQL, measurement and QA |
| `shopify-inbox-conversion` | Chat | Inbox setup, the early-access Inbox agent, persona design, Shopify Knowledge Base, staff handoff, quick replies, conversation ops, safety QA |

Each skill carries its own `references/` for progressive disclosure, plus an `agents/openai.yaml`
Codex agent definition.

## Platform boundaries

The three skills are deliberately scoped so they don't overlap:

- **Shopify Messaging** creates and sends campaigns, and manages native email/SMS marketing
  automations. Marketing automations using Shopify Messaging email moved here on 2026-03-24.
- **Shopify Flow** is the custom workflow and third-party integration layer. Available on any paid
  plan. Use it when a journey needs logic Messaging templates can't express.
- **Shopify Inbox** is a customer chat surface, not an outbound channel.

## Non-negotiable rules

These are enforced in every skill and matter more than speed:

1. **Inspect before changing.** Establish current senders, segments, active automations, and
   templates before proposing structural change.
2. **Never send, schedule, publish, activate, disable, or materially edit a live campaign or
   automation without explicit approval.**
3. **Never change** sender DNS, DMARC, domain authentication, consent settings, privacy text,
   subscription state, discounts, or billing without explicit approval.
4. **Never invent** product facts, replacement intervals, guarantees, refund promises, medical
   claims, or expected hair-loss outcomes. Hair replacement is a trust-sensitive category.
5. **Treat email, SMS, and WhatsApp consent independently.** A subscriber to one channel is not
   subscribed to another.
6. **Never create duplicate journeys** across Messaging, Flow, HubSpot, or MailerLite. Duplicate
   abandoned-cart or welcome flows are the most common and most expensive failure here.
7. **Verify anything that can change** — pricing, free allowances, plan eligibility, admin
   navigation, message limits — against the Shopify Help Center or Changelog before relying on it.
   Shopify moves fast and these skills were verified on 2026-08-19.

## Account facts

Verified 2026-08-19 against the live store:

- Store: Hair Solutions Co, `one-head-hair.myshopify.com` / hairsolutions.co
- Plan: **Basic** — Shopify Messaging email is available; Shopify Flow is available
- 3,958 customers, 3,780 email-subscribed
- Shopify Messaging free allowance: 10,000 emails/month, then $1 per 1,000
- **Abandoned checkout automation emails do not count toward the allowance**

## Related plugins

- `email-marketing` — MailerLite, for landing-page lead capture and prospect nurture
- `crm` — HubSpot portal 50966981, the outgoing lifecycle platform
- `storefront` — Horizon theme engineering
- Brand authority lives in the **brand-design-marketplace**, not here
