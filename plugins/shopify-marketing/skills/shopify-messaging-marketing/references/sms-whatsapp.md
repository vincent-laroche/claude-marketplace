# Shopify Messaging SMS and WhatsApp playbook - verified 2026-08-19

## SMS

### Current supported recipient countries

Shopify currently documents native Messaging SMS marketing support for recipients in:

Austria, Canada, Denmark, Finland, Italy, Luxembourg, Poland, Portugal, Spain, Sweden, United Kingdom, and United States excluding Puerto Rico.

Re-verify before every new market launch.

### Consent and policy

SMS requires SMS-specific opt-in and compliance with applicable privacy and telecommunications laws. Shopify's requirements page calls out examples including GDPR, CPRA, TCPA, ePrivacy, and UK PECR depending on market. Terms/privacy content must cover collection/use of phone numbers, data sharing, frequency, possible data rates, opt-out, and support/contact information as applicable.

### Character economics

Current Shopify Messaging SMS behavior:

- GSM-7 style standard characters: 160 characters per message segment.
- Non-standard/UCS-2 style content: 70 characters per message segment, including many emoji and accented characters.
- Longer campaigns are split for billing even when they display as one continuous message in most supported countries.
- Personalization can change the actual character encoding/length.
- Link shortening can reduce length and preserve Messaging click/sales tracking.

Always calculate billed segments, not just visible character count.

### Quiet hours

Shopify enforces recipient-local quiet hours and retries messages later. Current documented windows include:

- Canada, EU, UK: 20:00-08:00 local time.
- U.S.: generally 21:00-08:00, with state exceptions.

Shopify also applies a buffer before quiet hours due to carrier delays. Verify the current quiet-hour table for state-level exceptions before scheduling U.S. campaigns.

### SMS price snapshot

Current per-message pricing varies materially by country and can change. There may also be a monthly toll-free number fee for U.S./Canada. Shopify currently offers up to 25 test SMS messages per week for free. Automations can have a monthly spending-threshold alert, but the alert does not cap charges.

Never copy old pricing into a budget. Re-open the live SMS pricing page.

## WhatsApp

### Eligibility and connection

WhatsApp marketing in Shopify Messaging requires:

- Shopify Messaging eligibility;
- a connected WhatsApp Business Account through Meta onboarding;
- compliance with WhatsApp Business terms/policy;
- explicit WhatsApp marketing consent;
- a Meta-approved marketing template.

If an existing WhatsApp Business Account is connected to another provider, migration/setup requirements can differ. Follow the live setup guide.

### Regional restrictions

As of 2026-08-19, Shopify states that WhatsApp marketing messages cannot be sent to recipients in the United States or China, and are unavailable in certain sanctioned regions. U.S.-based stores can still market via WhatsApp to supported non-U.S. recipients.

Brazil and Indonesia have additional cross-border scaling/verification considerations.

Always re-verify regional support before recommending a market.

### Template behavior

Current Shopify Messaging WhatsApp templates include examples such as:

- Back in stock
- Blank WhatsApp
- Upcoming sale
- Product showcase
- VIP exclusive

Templates are submitted to Meta for approval. Current campaigns can use text, image, or product headers and buttons including URL, phone, discount, or quick reply depending on configuration. Shopify includes store identity/unsubscribe behavior in the campaign flow.

### Limits and costs

Current documentation states:

- 1,024-character WhatsApp message limit.
- Up to 25 test messages per week for free.
- New WhatsApp Business Accounts can start with a business-initiated daily sending cap until they progress through Meta trust tiers.
- Pricing is per message and varies by recipient region.
- A customer reply opens a 24-hour customer-service window in which qualifying utility/customer-service messages can be free, while marketing/authentication messages remain billed.

Re-check limits and pricing before launch.

## Channel selection rule

Use email as the default broad owned-marketing channel. Add SMS or WhatsApp when:

- the audience has explicit channel consent;
- the market is supported;
- urgency or conversational relevance justifies the higher marginal cost/intrusiveness;
- the message is concise enough for the channel;
- frequency is controlled across channels.

Do not send the same promotion through all channels by default. Coordinate frequency at the customer level when possible.
