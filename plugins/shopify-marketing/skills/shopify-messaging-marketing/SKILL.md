---
name: shopify-messaging-marketing
description: Operate, audit, plan, and optimize Shopify Messaging for email, SMS, and WhatsApp marketing, including the 2026 Shopify Email-to-Messaging transition, campaign creation, reusable templates, custom Liquid, sender authentication, deliverability, subscriber consent, segmentation, testing, scheduling, UTM tracking, analytics, Shopify Campaigns, and Campaign Autopilot. Use for Shopify marketing campaign strategy or implementation, email/SMS/WhatsApp setup, template design, deliverability troubleshooting, campaign QA, campaign measurement, or any request involving Shopify Messaging, Shopify Email legacy terminology, Growth marketing campaigns, or Shopify-native outbound marketing.
---

# Shopify Messaging Marketing

Use this skill as the operating manual for Shopify-native outbound campaigns for Hair Solutions Co. Treat Shopify's current admin and official documentation as the source of truth.

## Core operating rule

Shopify Messaging is the current multi-channel app and was formerly Shopify Email. Do not send a user toward legacy admin paths without checking whether they still exist. As verified on 2026-08-19:

- Email, SMS, and WhatsApp campaigns are created in Shopify Messaging.
- Email and SMS marketing automations are managed in Shopify Messaging.
- Growth contains Campaigns, Attribution, and Campaign Autopilot.
- Shopify Flow remains the custom workflow layer and is handled by the `shopify-lifecycle-automation` skill.
- Shopify Inbox is a customer chat surface and is handled by the `shopify-inbox-conversion` skill.

Read `references/current-architecture.md` when platform location, plan eligibility, pricing, channel support, or 2026 migration history matters.

## Safety and change control

Protect revenue, customer trust, and deliverability.

1. Inspect before changing. Establish the current sender setup, segments, active automations, campaign calendar, and existing templates before recommending structural changes.
2. Never send, schedule, publish, activate, disable, or materially edit a live campaign without explicit approval.
3. Never change sender DNS, DMARC, domain authentication, consent settings, privacy text, subscription state, discounts, billing, or live storefront content without explicit approval.
4. Never invent Hair Solutions Co product facts, policies, replacement intervals, guarantees, refund promises, medical claims, before/after claims, or expected hair-loss outcomes.
5. When copy depends on product specifications, shipping, refunds, discounts, inventory, or customer promises, use verified store data or ask for the missing fact.
6. Treat email, SMS, and WhatsApp consent independently. A subscriber to one channel is not automatically subscribed to another.
7. Prefer a draft, plan, QA report, or exact change list before a production action.

## Freshness rule

Shopify changes quickly. Before relying on a value that can change, verify it against official Shopify Help Center, Shopify Changelog, or Shopify developer documentation. This includes:

- pricing and free allowances;
- supported countries and regions;
- plan eligibility;
- early-access status;
- message limits and quiet hours;
- admin navigation;
- template or personalization limits;
- Autopilot behavior;
- analytics and attribution behavior.

Use `references/source-index.md` as the starting source map. If a current official page conflicts with this skill, follow the current official page and state the change.

## Choose the operating mode

Classify the request before working:

- **Foundation audit**: sender authentication, consent capture, list health, channel eligibility, branding, UTM conventions, measurement.
- **Campaign build**: audience, offer/message, channel, template, links, personalization, test, schedule, approval.
- **Template system**: reusable email structure, content modules, dynamic/static products, discount blocks, custom Liquid.
- **Deliverability**: authentication, volume, Smart delivery, complaints, bounces, engagement, list cleaning.
- **SMS/WhatsApp**: country eligibility, consent, quiet hours or Meta approval, character/message economics, tests.
- **Measurement**: Messaging report, Shopify Campaign, attribution model, UTM hygiene, post-send diagnosis.
- **Autopilot review**: evaluate Shopify-generated tactic, audience, duplicate risk, copy, economics, and compliance before approval.

## Foundation audit workflow

Run this before building a new marketing system.

1. Confirm Shopify plan and that Shopify Messaging is installed and available.
2. Confirm the sender email and branded domain.
3. Confirm SPF/DKIM authentication and exactly one valid DMARC record for the sender domain.
4. Confirm a monitored reply address; avoid no-reply style addresses.
5. Inventory subscriber sources: checkout, customer accounts/sign-in if used, theme newsletter forms, Shopify Forms, imports, and any third-party sync.
6. Confirm consent settings by channel and market. Note whether double opt-in is enabled where appropriate.
7. Inventory active customer segments and define a naming convention.
8. Inventory active campaigns, scheduled sends, Messaging automations, Flow workflows, and third-party sends to detect overlap.
9. Record normal email send volume and recent engagement/bounce/complaint behavior before increasing cadence.
10. Define campaign naming and UTM conventions before the first production send.
11. Confirm brand settings, reusable email templates, footer identity/address, accessibility basics, and test process.
12. Confirm analytics baseline and attribution model used for decision-making.

Return a prioritized audit with: blocker, risk, recommended change, owner/system, and approval required.

## Email campaign workflow

Read `references/email-playbook.md` for detailed editor capabilities and current limits.

For every campaign:

1. Define the business objective in one sentence.
2. Define the audience using a saved Shopify customer segment whenever possible.
3. State exclusions and suppression logic explicitly.
4. Decide whether the message is promotional, educational, launch, replenishment/reorder, win-back, cross-sell, announcement, or service-adjacent marketing.
5. Choose a reusable template before composing. Avoid changing templates late because Shopify deletes prior draft content when switching templates.
6. Build a mobile-first hierarchy: primary message and CTA in the first two mobile scrolls.
7. Use one dominant CTA. Add secondary links only when they reduce friction rather than split intent.
8. Use personalization only when the fallback is safe and the data is reliable.
9. Verify every product, discount, policy, deadline, price, stock statement, and URL against current store data.
10. Apply UTM parameters using the store convention.
11. Send tests to representative inboxes. Shopify supports multiple test addresses; use at least one mobile and one desktop review path operationally.
12. Check spelling manually because Shopify does not provide a reliable final spellcheck guarantee.
13. Check alt text, contrast, link clarity, unsubscribe/footer, and reply address.
14. Estimate recipient count and incremental email cost.
15. Check recent volume against normal baseline before a large send.
16. Present the final send brief and require approval before sending or scheduling.
17. After the send, review performance at a reasonable delay and compare against the campaign objective, not only opens.

## Hair Solutions Co campaign guardrails

Apply these rules whenever the campaign concerns hair systems, hair loss, appearance, or customer outcomes:

- Do not diagnose hair loss or imply medical treatment.
- Do not imply a hair system will produce biological hair growth.
- Do not invent wear duration, maintenance intervals, adhesive performance, lifespan, density, color match, base durability, or styling compatibility.
- Do not create a guarantee, refund, replacement, or delivery promise that is not in current policy.
- Do not use before/after or transformation claims unless the underlying media, permissions, and claim are verified.
- Use product-history segmentation only when the products and customer data actually support the inference.
- If proposing replenishment timing, label the timing as a hypothesis until order history or a verified product policy supports it.
- Prefer education, product-fit clarity, care confidence, social proof with source, and friction reduction over pressure tactics.

## Template system

Build a small reusable system instead of a large template library. A practical default is:

1. **Editorial/Product Education** - education-led with one product or collection CTA.
2. **Offer/Promotion** - clear offer, urgency only when factual, discount block if relevant.
3. **Launch/Back in Stock** - product-led with product or collection section.
4. **Lifecycle** - compact automation template with context-specific dynamic blocks.

Use Shopify sections before custom code. Use Custom Liquid only when the standard editor cannot produce the required result.

For a reusable template, specify:

- purpose;
- eligible audiences;
- required sections;
- optional sections;
- CTA hierarchy;
- product section mode: Dynamic or Static;
- fallback behavior for personalization;
- mobile QA;
- accessibility QA;
- UTM behavior;
- claims/policy verification points.

## Custom Liquid rule

Read `references/email-playbook.md` before writing Liquid for Messaging.

- Use only Shopify-supported variables and filters for Messaging.
- Preserve required unsubscribe behavior.
- Preserve open tracking variables when the store's open tracking configuration requires them.
- Respect Shopify's current size limits for Custom Liquid sections and fully custom-coded emails.
- Prefer small, testable snippets over an entire custom-coded email.
- Never assume storefront Liquid objects are available in Shopify Messaging.

## Deliverability workflow

Read `references/deliverability-consent.md`.

Diagnose in this order:

1. Sender authentication and DMARC.
2. Consent provenance and list quality.
3. Bounce, unsubscribe, complaint, and spam trends.
4. Recent sending frequency and volume spikes.
5. Engagement recency and inactive subscriber share.
6. Segment size and Smart delivery behavior.
7. Copy/link/domain risk factors.
8. Inbox-provider or platform-specific issue.

Do not solve weak deliverability by sending more volume. If warming or rebuilding reputation, use the most engaged audience first and increase volume gradually.

## SMS workflow

Read `references/sms-whatsapp.md` before recommending SMS.

Always confirm:

- recipient countries are currently supported;
- SMS-specific opt-in exists;
- required terms/privacy disclosures exist;
- toll-free or local verification is complete where applicable;
- quiet hours for recipient local time;
- final GSM-7/UCS-2 character count and number of billed message segments;
- shortened-link setting when appropriate for tracking and cost;
- test send result;
- estimated campaign and automation spend.

Use SMS for high-intent, time-sensitive communication. Do not mirror every email into SMS.

## WhatsApp workflow

Read `references/sms-whatsapp.md` before recommending WhatsApp.

Always confirm:

- current regional support and exclusions;
- WhatsApp-specific explicit consent;
- connected eligible WhatsApp Business Account;
- Meta template approval status;
- daily/new-account sending limits;
- message cost by recipient region;
- content and button behavior;
- keyword replies if used;
- test result before scheduling.

Do not assume U.S. WhatsApp marketing is supported. Verify current Shopify/Meta rules first.

## Campaign Autopilot workflow

Read `references/analytics-autopilot.md`.

Treat Autopilot as a proposal generator, not an autonomous marketing owner.

1. Confirm the store has access and that Shopify Messaging is connected.
2. Review the proposed objective and audience.
3. Check whether an equivalent campaign or automation already exists.
4. Review offer economics and product/policy accuracy.
5. Review copy, brand fit, claims, links, and discounts.
6. Review channel cost and send volume.
7. Review audience suitability. If Autopilot does not permit direct audience editing, decide whether to accept the tactic rather than trying to force it.
8. Require approval before publishing/activating.
9. Tag or document the tactic as Autopilot-generated for later performance comparison.

## Measurement workflow

Read `references/analytics-autopilot.md`.

Use a hierarchy:

1. **Primary business outcome**: sales, orders, qualified sessions, or another defined objective.
2. **Conversion efficiency**: conversion rate, revenue per recipient/session, AOV where relevant.
3. **Click behavior**: CTR and link activity.
4. **List health**: unsubscribe, bounce, complaint/spam signals.
5. **Opens**: directional only; interpret cautiously based on tracking/privacy settings.

Use Shopify Campaigns to group related activities when a broader promotion spans email, social, QR/shareable links, or other channels. Review more than one attribution model for material decisions.

## Default output formats

### Campaign brief

Return:

1. Objective
2. Audience and exclusions
3. Channel and rationale
4. Message angle
5. Offer/claim verification needed
6. Template structure
7. Subject/preview or SMS/WhatsApp draft parameters
8. CTA and destination
9. UTM/campaign mapping
10. Estimated reach/cost
11. QA checklist
12. Approval gate
13. Post-send KPI plan

### Audit

Return a table or compact sections with:

- Finding
- Evidence/current state
- Risk
- Recommendation
- Priority
- Approval required

### Post-send analysis

Return:

- Goal and audience
- Delivery/reach
- Click/conversion behavior
- Revenue/orders if attributable
- List-health signals
- Attribution caveat
- What worked
- What likely constrained performance
- One to three changes for the next test

## Reference loading guide

- `references/current-architecture.md` - current 2026 product surfaces, eligibility, pricing overview, migration notes.
- `references/email-playbook.md` - email campaign editor, templates, personalization, Custom Liquid, content best practices.
- `references/deliverability-consent.md` - sender authentication, Smart delivery, list growth, consent, volume, complaints.
- `references/sms-whatsapp.md` - SMS and WhatsApp eligibility, rules, limits, economics, testing.
- `references/analytics-autopilot.md` - Messaging analytics, UTMs, Shopify Campaigns, attribution, Campaign Autopilot.
- `references/source-index.md` - official Shopify source map verified on 2026-08-19.
