---
name: shopify-lifecycle-automation
description: Design, audit, implement, and optimize Shopify-native lifecycle marketing using Shopify Messaging automations, Shopify Flow, Shopify Forms, customer segments, ShopifyQL, metafields, and Growth analytics. Use for welcome, abandoned browse/cart/checkout, post-purchase, upsell, win-back, birthday, VIP, replenishment, customer-joined-segment, consent-driven journeys, custom Flow workflows, automation troubleshooting, lifecycle maps, segment design, form strategy, duplicate-workflow audits, or any request about how Shopify marketing automations work in the current 2026 admin.
---

# Shopify Lifecycle Automation

Use this skill to build a coherent lifecycle system for Hair Solutions Co instead of isolated automations.

## Current 2026 architecture

As verified on 2026-08-19:

- Shopify Messaging manages native email and SMS marketing automations.
- Marketing automations that use Shopify Messaging email moved to Shopify Messaging on 2026-03-24.
- Automations with marketing activities from other apps are available in Shopify Flow.
- Shopify Messaging provides pre-built lifecycle templates.
- Shopify Flow is the custom workflow and third-party integration layer.
- Shopify Forms captures native email/SMS/WhatsApp consent and customer data.
- Customers > Segments provides dynamic customer audiences using ShopifyQL-style filters.
- Growth contains Campaigns, Attribution, and related marketing performance views.

Read `references/architecture-and-catalog.md` before relying on an older tutorial or admin path.

## Change-control rules

1. Inspect all active Messaging automations, Flow workflows, and relevant third-party journeys before proposing a new automation.
2. Never activate, disable, delete, edit, or replace a live automation without explicit approval.
3. Never change customer subscription states, lifecycle/customer fields, tags, metafields, consent configuration, discounts, billing, or production workflow logic without explicit approval.
4. Do not silently migrate a workflow from Flow to Messaging or vice versa. Explain the reason, behavioral differences, and cutover risk first.
5. Never create duplicate abandoned-cart, welcome, win-back, or post-purchase journeys across Messaging, Flow, HubSpot, or another app.
6. Do not invent Hair Solutions Co purchase cycles, product lifetime, reorder cadence, policies, discounts, margins, customer tiers, or medical/product claims.
7. Build plans and exact implementation specs first. Require approval before any production activation.

## Freshness rule

Re-check official Shopify documentation before using any fact that can change, including:

- automation template availability;
- channel support;
- Flow limits;
- plan restrictions;
- Forms limits;
- segment filters/functions;
- consent behavior;
- pricing;
- admin navigation;
- early-access functionality.

Use `references/source-index.md` as the source map.

## Lifecycle design sequence

Always design in this order:

1. **Business outcome** - define the revenue, conversion, retention, or customer-experience objective.
2. **Event/state** - identify the actual Shopify event or customer state that should trigger eligibility.
3. **Consent** - confirm the customer can legally and technically receive the intended channel.
4. **Audience** - define a dynamic customer segment or trigger condition.
5. **Exclusions** - define who must not enter or continue.
6. **Trigger** - choose Messaging native trigger/template or Flow trigger.
7. **Conditions** - add only conditions that prevent meaningful mistakes or improve relevance.
8. **Waits** - define timing with a business reason. Do not use arbitrary delays.
9. **Message/action** - define each communication or operational action.
10. **Exit logic** - stop when the desired action occurs or the customer becomes ineligible.
11. **Overlap check** - compare against every related active journey.
12. **Measurement** - define success, guardrails, attribution limits, and review window.
13. **Test** - validate trigger, conditions, wait behavior, data fallbacks, links, discounts, and suppression.
14. **Approval** - require explicit approval before activation.
15. **Post-launch review** - check performance and operational exceptions.

## Decide: Messaging or Flow

Use **Shopify Messaging** when a supported native marketing automation template covers the need and the primary outcome is email/SMS marketing. Prefer the native path for simplicity, reporting, and editor compatibility.

Use **Shopify Flow** when:

- the automation is custom beyond a Messaging template;
- a third-party app must participate;
- operational actions, tags, metafields, notifications, or external services are required;
- branching logic is more complex than the Messaging template supports;
- a Flow-specific trigger/action is needed.

Do not use Flow merely because older documentation says automations live there. Read `references/flow-design.md`.

## Native Messaging automation catalog

Read `references/architecture-and-catalog.md` for current details.

The current native catalog includes major families:

### Recover site visitors

- Convert abandoned product browse - email and SMS
- Recover abandoned cart - email and SMS
- Recover abandoned checkout - email and SMS

Abandoned checkout email has special behavior and currently does not count toward Messaging email billing. By default, marketing automations generally send to subscribed customers. Shopify currently allows the abandoned checkout email recipient setting to be changed to All customers. Treat that setting as legally and reputationally sensitive. Never recommend switching to All customers without a jurisdiction/consent review and explicit merchant decision.

### Welcome new subscribers

- Welcome/discount automation
- Welcome discount series with follow-up brand-building/reminder messages

### Post-purchase

- Thank customers after first/second purchase
- Upsell after first purchase
- Win back customers
- Retail-location-related post-purchase journeys when applicable

### Customer appreciation

- Birthday discount
- VIP/customer milestone journeys

Do not activate every available template. Each automation must fill a distinct customer need and have a measurable business case.

## Hair Solutions Co recommended lifecycle build order

Use this as a sequencing recommendation, not as permission to activate.

### Phase 1 - revenue protection and foundation

1. Abandoned checkout
2. Abandoned cart
3. Welcome new subscribers
4. Post-purchase thank-you/education
5. Engaged-subscriber segmentation and list-health suppression

### Phase 2 - incremental lifecycle revenue

6. Browse abandonment if volume and consent justify it
7. First-purchase cross-sell/education based on verified product relationships
8. Win-back based on observed repurchase distribution, not guessed timing
9. VIP/appreciation based on an explicit value definition

### Phase 3 - enrichment and channel expansion

10. Forms for preference/profile enrichment
11. SMS versions for high-intent journeys in supported markets
12. Birthday or other metafield-driven journeys if data quality is adequate
13. Custom Flow/HubSpot coordination when Shopify-native logic is insufficient

Do not build a generic replenishment automation until actual order data or a verified product lifecycle supports a timing rule.

## Automation specification format

For every automation, return this exact core spec:

### [Automation name]

- Objective:
- Platform: Shopify Messaging / Shopify Flow / hybrid
- Channel:
- Trigger:
- Eligibility:
- Consent requirement:
- Exclusions:
- Wait/timing:
- Steps/messages:
- Exit conditions:
- Data dependencies:
- Discount dependencies:
- Overlap risks:
- Failure/edge cases:
- Primary KPI:
- Guardrail metrics:
- Test cases:
- Approval required before:

If the user asks for multiple journeys, add a conflict matrix showing where customers could enter more than one journey.

## Customer segmentation workflow

Read `references/forms-and-segments.md`.

1. Describe the audience in plain language.
2. Identify the minimum Shopify data fields required.
3. Confirm those fields exist and are reliable.
4. Prefer native filters/functions over tags created only for segmentation.
5. Write the ShopifyQL WHERE logic using documented filter names/operators.
6. Run/validate the query in Shopify before treating it as correct.
7. Review Shopify's generated segment description against the intended audience.
8. Check sample members and exclusions.
9. Save with a durable naming convention.

### Segment naming

Use a structure such as:

`MKT | [channel/consent] | [lifecycle state] | [qualifier]`

Examples:

- `MKT | Email | Engaged | 6m`
- `MKT | Email | Customers | 2+ Orders`
- `MKT | Email | Winback Eligible | Verified Window`

Do not encode a date window in the name unless it is actually in the query.

## Safe starter segment patterns

Validate all syntax in the current Shopify segment editor.

### Email subscribers

`email_subscription_status = 'SUBSCRIBED'`

### Recently added subscribers

`email_subscription_status = 'SUBSCRIBED' AND customer_added_date >= -30d`

### Engaged list pattern

Shopify's deliverability docs use a pattern that combines current subscription status with recent acquisition or evidence of an order/click. See `references/forms-and-segments.md` for the source pattern.

### Product purchase segments

Use Shopify's documented product-purchase functions and select actual product IDs in the editor. Never type a guessed product ID or infer product equivalence by name.

## Forms strategy

Use Shopify Forms for native audience growth and enrichment when its capabilities fit.

A form should have one primary purpose:

- email signup;
- SMS signup;
- WhatsApp signup;
- preference capture;
- customer-profile/metafield enrichment;
- campaign/lead capture.

Do not create fields merely because the data might be useful someday. Every field must have a current segmentation, personalization, support, or analytics use.

Before building a form:

1. Define the downstream segment/automation that will use each field.
2. Choose local form data versus customer metafield based on whether the data must persist/reuse.
3. Confirm supported field and metafield types.
4. Confirm behavior for existing customers; do not assume submitting a form overwrites email/phone or every consent field.
5. Define tags only when a tag is the right durable state, not as a substitute for proper structured data.
6. Define form success metrics: views, submissions, completion rate, qualified subscriber rate, downstream conversion.
7. Require approval before publishing the form or changing live consent collection.

## Flow design rules

Read `references/flow-design.md`.

### Keep Flow deterministic

A production Flow should make its decision path obvious from the canvas:

Trigger -> eligibility conditions -> waits -> actions -> exit/terminal state.

Use explicit names for workflows, conditions, and branch purpose. Avoid deeply nested branches when multiple smaller workflows are easier to reason about and do not create race conditions.

### Customer joined segment

Use the Customer joined segment trigger when the desired lifecycle state is most naturally represented by a dynamic segment, such as VIP or win-back eligibility. Remember that membership changes dynamically. Test how existing versus newly qualifying customers behave before activation.

### Customer subscribed to email marketing

Use the documented subscription trigger only for the events it actually observes. Shopify documents behavior tied to supported subscription actions such as forms/theme signup. Do not assume every external subscription-state change triggers the workflow identically.

### Wait actions

Use waits for meaningful customer timing. Shopify Flow currently has documented workflow limits including a maximum number of Wait steps. Re-check the current limit; at skill build time, Shopify documents up to 40 Wait steps in a workflow.

Do not create a workflow near a platform limit unless there is a compelling reason.

### External actions

Grow, Advanced, and Plus currently support Flow's Send HTTP Request action. Basic does not. Re-verify plan restrictions before designing integrations around HTTP requests.

## Duplicate and collision audit

Before any activation, build a matrix with rows for lifecycle events and columns for Shopify Messaging, Shopify Flow, HubSpot, and other sending apps.

Check at least:

- new subscriber;
- browse abandonment;
- cart abandonment;
- checkout abandonment;
- first purchase;
- second/repeat purchase;
- product-specific purchase;
- win-back/lapse;
- VIP milestone;
- birthday;
- back in stock;
- promotion campaign overlap.

Flag:

- two messages within an unreasonably short window;
- two discounts competing;
- contradicting policies/offers;
- a transactional notification plus marketing message that reads as duplicate;
- email and SMS triggered simultaneously without intentional channel orchestration;
- a Flow path and Messaging template triggered by the same customer action.

## Turning off automations

Turning off a Messaging automation can affect customers currently in wait stages. Shopify documents that customers in the wait stage of a deactivated automation can have their pending path canceled. Before disabling a live automation:

1. Review active/pending volume if available.
2. Determine whether a replacement will start immediately.
3. Decide how to handle customers between old and new paths.
4. Avoid double entry during cutover.
5. Require explicit approval.

## Measurement

Read `references/measurement-and-qa.md`.

Messaging automation analytics can include reach, sessions, orders, conversion rate, and sales. Do not optimize an automation solely for attributed revenue if the purpose is customer education or trust.

For each journey define:

- primary KPI;
- secondary KPI;
- list-health/customer-experience guardrail;
- minimum evaluation window;
- attribution caveat;
- next test if performance is weak.

## QA test suite

Before activation, test at least:

1. Eligible subscribed customer.
2. Ineligible/unsubscribed customer.
3. Customer missing optional personalization.
4. Customer already purchased before a delayed recovery message.
5. Customer qualifying for an overlapping journey.
6. Discount expired/ineligible/missing if a discount is used.
7. Product unavailable or changed if product content is dynamic.
8. Mobile email/SMS rendering.
9. Link/UTM tracking.
10. Workflow turned off during a wait, if relevant to cutover planning.

## Reference loading guide

- `references/architecture-and-catalog.md` - 2026 surfaces and native Messaging automation catalog.
- `references/forms-and-segments.md` - Shopify Forms, metafields, customer segments, ShopifyQL patterns.
- `references/flow-design.md` - Flow triggers, conditions, actions, waits, custom workflows, current plan boundaries.
- `references/measurement-and-qa.md` - analytics, collision audits, testing, lifecycle optimization.
- `references/source-index.md` - official Shopify source map verified 2026-08-19.
