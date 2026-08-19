# Current Shopify Messaging architecture - verified 2026-08-19

## Product map

Shopify Messaging is the current Shopify-native multi-channel marketing app and was formerly named Shopify Email. It supports email, SMS, and WhatsApp marketing campaigns. It also manages email and SMS marketing automations.

The Shopify admin Marketing tab was renamed Growth on 2026-06-17. Growth contains Campaigns, Attribution, and Campaign Autopilot. Marketing automations that use Shopify Messaging emails moved into Shopify Messaging on 2026-03-24. Automations with marketing activities from other apps are available through Shopify Flow.

Use this map:

- Apps > Messaging: email/SMS/WhatsApp campaigns, templates, email/SMS automations, Messaging settings, channel analytics.
- Growth: Campaigns, Attribution, Campaign Autopilot.
- Customers > Segments: audience definitions.
- Shopify Forms: native contact capture and customer data collection.
- Shopify Flow: custom workflows and third-party actions.
- Shopify Inbox: live chat and Inbox agent, not outbound campaign marketing.

## Requirements

As of verification, Shopify Messaging is available to Basic, Grow, Advanced, and Shopify Plus merchants. Shopify Messaging requires Shopify Network Intelligence to be enabled. Sending also depends on store eligibility and the requirements on the current Shopify Messaging requirements page.

## Email pricing snapshot

Verified 2026-08-19:

- 10,000 free emails per calendar month on eligible plans.
- $1 USD per 1,000 additional emails up to 300,000.
- $0.65 USD per 1,000 after 300,000.
- $0.55 USD per 1,000 after 750,000.
- Messaging email automations count toward the monthly allowance except abandoned checkout automations, which are free.
- Unused free emails do not roll over.

Always re-check current pricing before budgeting or promising a cost.

## 2026 changes that invalidate older tutorials

1. "Shopify Email" may appear in older documentation, screenshots, apps, blog posts, or Liquid examples. Treat it as legacy naming unless the current admin still uses the label in a specific place.
2. Do not direct users to Marketing > Automations as the primary management surface for Messaging automations after the March 2026 migration.
3. Growth is the current marketing-growth surface after the June 2026 rename.
4. SMS marketing automations became available in Shopify Messaging in May 2026, so older guidance that says SMS automations require a third-party app may be obsolete.
5. WhatsApp marketing is a current Shopify Messaging channel in August 2026 and has its own Meta requirements, consent, pricing, templates, and regional restrictions.

## Freshness-sensitive fields

Re-verify before acting:

- plan eligibility;
- pricing;
- supported SMS countries;
- WhatsApp regional restrictions;
- early-access status of Campaign Autopilot;
- message or test limits;
- channel verification requirements.
