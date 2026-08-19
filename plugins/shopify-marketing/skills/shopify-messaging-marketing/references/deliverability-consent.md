# Deliverability, authentication, list health, and consent

## Sender email and authentication

Shopify distinguishes Store email from Sender email. Sender email is customer-facing and is used for marketing and many notifications/replies.

For a branded third-party sender domain, authenticate it. Shopify uses CNAME records for DKIM and SPF. DMARC is also required by major mailbox providers for branded sending. Shopify's current setup documentation says automatic authentication for certain domain providers can configure CNAME records for DKIM/SPF but may still require a manual DMARC record.

Shopify documents a default DMARC example of:

`v=DMARC1; p=none;`

Do not blindly add it. Check whether a DMARC record already exists. A domain must not have multiple DMARC TXT records. If an existing policy is managed elsewhere, preserve the intended policy and coordinate changes.

Avoid no-reply style sender addresses because they can reduce trust and some hosts may reject them.

## List acquisition and consent

Only market to people with valid permission for the specific channel and applicable jurisdiction. Shopify can collect email opt-in through checkout, sign-in/customer account surfaces, theme newsletter forms, Shopify Forms, and imports.

Rules:

- Never purchase a list.
- Preserve source/provenance where possible.
- Use double opt-in when legal requirements, list quality, or risk justify it.
- Do not treat an order email address as marketing consent by default.
- Do not convert email consent into SMS or WhatsApp consent.
- Review role-based addresses and stale imported lists carefully.
- Regularly remove or suppress invalid, bounced, or unengaged contacts according to platform behavior and policy.

Shopify automatically handles unsubscribe/spam states and suppresses some bounced addresses. Do not try to route around those protections.

## Smart delivery and list-health filtering

Shopify Messaging includes list-health and bot filtering. Smart delivery can filter unengaged recipients on larger sends; current documentation describes Smart delivery behavior for segments over 1,000 recipients. Verify current thresholds before relying on exact behavior.

Do not disable protective filtering merely to maximize raw reach without a specific business reason.

## Complaint rate

Shopify references Gmail/Yahoo complaint enforcement around 0.3% and recommends keeping complaint rate below 0.1%. Use the current deliverability page for the latest thresholds.

If complaints rise:

1. Stop expanding volume.
2. Isolate the acquisition source and campaign type.
3. Tighten to recently engaged subscribers.
4. Check frequency, expectations, subject/copy mismatch, and opt-in quality.
5. Fix the cause before scaling again.

## Volume consistency

Shopify advises against sudden large increases, including sends many times larger than normal daily volume. Current guidance suggests gradually ramping volume roughly 20-30% per week and starting a seasonal ramp several weeks ahead of a major event.

Use this operationally:

- Establish the normal weekly volume.
- If the target audience is materially larger, segment and batch.
- Start with highest engagement.
- Observe bounce, complaint, unsubscribe, and click quality before the next step.
- Avoid long periods of inactivity followed by a full-list blast.

## Example engaged segment

Shopify's deliverability documentation provides an engagement-oriented pattern similar to:

`email_subscription_status = 'SUBSCRIBED' AND (customer_added_date > -6m OR (customer_added_date <= -6m AND (number_of_orders > 0 OR shopify_email.clicked() = true)))`

Treat this as a starting pattern, not a universal definition. Validate syntax in the live segment editor and tune the recency window to the business's actual purchase cycle and send history.

## Legal/compliance boundary

Shopify provides tools, not legal clearance. The merchant remains responsible for consent, required disclosures, physical address/footer rules, privacy laws, telecom rules, and regional requirements. For material uncertainty in a regulated market, flag it for legal review rather than inventing an answer.
