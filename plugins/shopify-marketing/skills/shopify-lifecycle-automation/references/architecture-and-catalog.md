# Shopify lifecycle architecture and native automation catalog - verified 2026-08-19

## Architecture

Shopify marketing automation is now split by purpose:

- Shopify Messaging: native email/SMS marketing campaigns and automations.
- Shopify Flow: custom ecommerce workflows, operational automation, and third-party app activities.
- Shopify Forms: native signup, consent, and structured customer-data capture.
- Customer Segments: dynamic audience/state definitions.
- Growth: Campaigns, Attribution, Autopilot, and marketing performance surfaces.

The 2026 migration matters. Shopify announced on 2026-03-05 that on 2026-03-24, marketing automations using Shopify Messaging emails would move into Shopify Messaging, while automations with marketing activities from other apps would be available in Flow. Shopify then renamed the Marketing admin tab to Growth on 2026-06-17.

## Messaging automation requirements

Shopify Messaging automations require Shopify Messaging eligibility. Full automation functionality can require Shopify Flow to be installed and appropriate Marketing/Flow permissions. Check the live requirements page before implementation.

## Native automation families

### Recover site visitors

#### Convert abandoned product browse

Trigger concept: customer views at least one product but leaves without adding to cart or purchasing.

Channels currently documented: Email, SMS.

Use when browse volume and subscriber identity are sufficient. Avoid aggressive timing for low-intent browsing.

#### Recover abandoned cart

Trigger concept: customer adds products to cart but does not start checkout.

Channels: Email, SMS.

Check collision with checkout abandonment and any third-party cart recovery app.

#### Recover abandoned checkout

Trigger concept: customer starts checkout but does not complete order.

Channels: Email, SMS.

Important current behavior:

- Abandoned checkout email does not count toward Messaging email charges/allowance.
- Marketing automations normally target marketing subscribers by default.
- Shopify currently allows the email recipient setting for abandoned checkout to be changed to All customers.

Treat the All customers option as a compliance-sensitive merchant decision, not a default recommendation.

### Welcome new subscribers

Shopify provides welcome templates including a single discount welcome and a series. The series can include an initial message plus follow-up brand-building and discount-reminder messages depending on the template.

Use the smallest sequence that earns its place. Do not send a three-message series because the template exists; define the role of every message.

### Post-purchase

Current documented templates include:

- Encourage online customers to visit retail locations in relevant setups.
- Thank customers after their first and second purchases.
- Upsell customers after their first purchase.
- Win back customers after a defined period since last order.

Win-back uses dynamic customer-state logic such as Customer joined segment. Base timing on actual reorder behavior where possible.

### Customer appreciation

Current examples include:

- Celebrate customer birthday, using a birth-date standard metafield and optionally Shopify Forms to collect it.
- VIP/customer appreciation journeys driven by customer segment membership.

## SMS automations

Shopify added native SMS marketing automations to Messaging in May 2026. Pre-built templates include abandoned carts, abandoned checkouts, and browse abandonment, with custom options also available. SMS costs are per message and automation spending thresholds are alerts rather than hard caps.

## Activation and editing

Messaging automations are managed in Apps > Messaging > Automations. Editing the workflow logic and editing the message template are distinct activities in the UI.

When an automation is turned off, customers in a wait stage can have pending sends canceled. Plan cutovers intentionally.
