# Lifecycle measurement and QA

## Messaging automation analytics

Shopify Messaging automation reporting currently includes metrics such as reach, sessions, orders, conversion rate, and sales, with activity-level reports for individual messages/steps.

Use the metric closest to the actual objective. Examples:

- Recovery journey: recovered orders/revenue plus unsubscribe/complaint guardrails.
- Welcome: first-purchase conversion, click quality, list retention.
- Post-purchase education: support friction, repeat sessions/clicks, downstream repeat purchase over a longer horizon.
- Win-back: reactivation orders/revenue, discount cost, unsubscribe rate.

## Attribution caution

Attributed automation sales are not identical to incremental sales. A customer might have purchased without the automation. For major decisions:

- compare against historical baseline;
- use holdouts/tests if practical;
- review timing from message to purchase;
- inspect offer cost and margin;
- watch whether one automation is cannibalizing another.

## Collision matrix

Create a table:

| Customer state/event | Messaging email | Messaging SMS | Flow | HubSpot/other | Conflict? | Resolution |
|---|---|---|---|---|---|---|

At minimum include subscriber signup, browse, cart, checkout, first order, repeat order, win-back, VIP, birthday, and campaign periods.

## Pre-launch QA

### Data

- Trigger data exists
- Segment query validated
- Consent state correct
- Metafields/tags populated as expected
- Product IDs/current references correct

### Logic

- Trigger fires once as intended
- Conditions have correct AND/OR logic
- Wait duration correct
- Exit/suppression works after purchase
- Customer cannot loop unexpectedly
- Duplicate protections present

### Content

- Subject/message accurate
- Personalization fallback safe
- Product and policy claims verified
- Discount valid and scoped
- Links/UTMs correct
- Mobile rendering checked

### Operations

- Owner named
- Monitoring metric named
- Error/handoff path named
- Deactivation effect understood
- Existing customers in wait/segment considered
- Production activation explicitly approved

## Post-launch review cadence

Do not overreact to tiny samples. Review in layers:

1. First technical check: trigger/sends/errors only.
2. Early quality check: delivery, clicks, obvious unsubscribe/complaint issues.
3. Conversion check after enough customer time has elapsed.
4. Cohort/economic review after a full purchase-cycle-relevant window.

Document one change hypothesis at a time where possible.
