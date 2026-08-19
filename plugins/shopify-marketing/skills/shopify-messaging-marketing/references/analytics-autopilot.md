# Analytics, Shopify Campaigns, attribution, and Campaign Autopilot

## Shopify Messaging analytics

Messaging reports can include performance, orders, funnel behavior, and link activity. Interpret metrics in context.

### Open tracking

Shopify provides multiple open-tracking privacy settings, including an optimized/recommended mode and more or less restrictive tracking choices. Open rate can be affected by mailbox privacy behavior and the store's tracking configuration. Never use opens as the sole optimization target.

### UTM defaults

Shopify Messaging can append UTM parameters. Current defaults include a Shopify email source/medium and campaign identifier derived from the email/campaign activity. Stores can customize UTM behavior at the activity or shop level. Setting changes may apply to future activities rather than retroactively to existing campaigns.

Define a stable convention before scaling campaigns so historical reporting remains readable.

Suggested naming convention:

- Campaign internal name: `YYYY-MM-DD | objective | audience | offer/theme`
- `utm_source`: `shopify_email`, `shopify_sms`, or another intentional source convention
- `utm_medium`: channel-specific medium
- `utm_campaign`: durable campaign family or launch identifier
- `utm_content`: creative/CTA variant only when useful

Do not overwrite Shopify defaults casually if other reporting depends on them.

## Analytics caveat

Messaging activity reporting does not capture every downstream purchase path. For example, a recipient can read an email, later return directly without clicking, and purchase without the order appearing as a Messaging-attributed conversion. Distinguish platform attribution from total incrementality.

## Shopify Campaigns in Growth

Use Shopify Campaigns to group activities that belong to a single commercial push across channels. Campaigns can use:

- marketing activities;
- shareable links;
- short links;
- QR codes;
- auto-match rules based on UTM or channel/type fields.

Avoid deleting or editing tracking links after distribution when that can break attribution. Prefer creating a new link when a distributed tracking asset must change.

Shopify Campaign metrics can include sales, orders, AOV, and sessions. Review current documentation for calculation details; returns may not be incorporated in all campaign calculations.

## Attribution

Shopify marketing performance reporting supports multiple attribution models. Current documentation includes last non-direct, last, first, any click, and linear views.

For material decisions:

1. Review at least two models.
2. Compare Shopify's first-party view with ad-platform self-attribution when paid media is involved.
3. Do not force exact agreement between systems.
4. Note the conversion window used by the specific report/activity.
5. Pair attributed revenue with list-health and customer-quality indicators.

## Campaign Autopilot

Campaign Autopilot is an early-access Growth feature as of 2026-08-19 and may not be available to every merchant.

Current behavior:

- Requires Shopify Messaging and an active subscriber list.
- Can recommend one-time email campaigns and ongoing marketing automations.
- Recommendations can include abandoned browse/cart/checkout, welcome, product launch, and promotional tactics.
- Shopify generates branded content and chooses an audience for the tactic.
- The merchant reviews and approves or dismisses the recommendation before it goes live.
- Some content can be edited. The audience may not be directly changeable within the Autopilot recommendation flow.
- Autopilot-generated assets are identifiable in Messaging.

### Autopilot review rubric

Score each proposed tactic:

- Incremental value: does it fill a real lifecycle/campaign gap?
- Duplicate risk: is another Messaging/Flow/third-party automation already covering the same event?
- Audience quality: is the proposed audience commercially and legally appropriate?
- Economics: expected margin/revenue versus message cost/discount cost.
- Claim/policy accuracy: are all product and policy statements verified?
- Brand fit: does the copy match Hair Solutions Co without pressure or medical overstatement?
- Measurement: is the tactic named/tagged so results can be isolated?

Reject or revise tactics that fail a high-risk criterion even if Shopify recommends them.
