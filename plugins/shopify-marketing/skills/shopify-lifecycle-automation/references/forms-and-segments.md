# Shopify Forms and customer segmentation

## Shopify Forms

Shopify Forms is the native form app for popup and inline forms. It can collect contact and marketing-consent data and can feed customer segments/automations.

### Current capability snapshot

Verified 2026-08-19:

- Popup and inline forms.
- Email, SMS, and WhatsApp marketing consent options depending on configuration/availability.
- Discounts can be part of signup experiences.
- Form analytics include views, submissions, and completion rate.
- Forms can apply customer tags.
- Custom fields can store local form data or supported customer/company metafields.
- Customer metafield data can be used later for segmentation when the data type is supported.
- Current Shopify docs state a maximum of 25 forms per store.
- Forms do not currently provide a general multi-step/conditional-logic form builder.

Re-check these limits before designing around them.

### Existing-customer caveat

Do not assume a form submission overwrites every field on an existing customer. Shopify documents cases where email/phone and some data are not modified the same way for existing customers. Test the exact field and consent behavior before using a form as a profile-update mechanism.

### Custom field design

Use a customer metafield when the answer should persist as structured customer data and support future segmentation. Use local form data when persistence/reuse is unnecessary.

Shopify Forms supports common field types such as text, dropdown, radio, multi-line text, multiple choice, date, number, and file input depending on context. Customer-segment metafield filtering supports only certain data types. Verify the current supported type before creating a field solely for segmentation.

### Form build standard

For each form document:

- Form purpose
- Placement/trigger
- Audience
- Fields
- Consent channel(s)
- Required/optional status
- Metafield/tag mapping
- Discount behavior
- Success state
- Downstream segment
- Downstream automation
- Analytics target
- Existing-customer test
- Mobile QA
- Approval gate

## Customer segments

Shopify customer segments are dynamic. Customers enter and leave as their data changes.

The segment editor uses ShopifyQL-style queries with fixed FROM/SHOW scaffolding and a WHERE clause for filters. Current default structure resembles:

```
FROM customers
SHOW customer_name, note, subscription_status, location, orders, amount_spent
WHERE [filters, operators, values]
ORDER BY updated_at
```

The admin provides templates and Sidekick can generate a segment from plain-language intent. Always run the query and review the generated description/members before saving.

## Reliable filter examples

Use only filters that appear in the live editor/reference.

### Email subscription

`email_subscription_status = 'SUBSCRIBED'`

Possible documented states include subscribed, not subscribed, pending, invalid, unsubscribed, and redacted.

### Customer added date

Examples:

`customer_added_date >= -7d`

`customer_added_date > -8m`

### Country

`customer_countries CONTAINS 'US'`

### Email events

Shopify customer segments support Shopify Messaging email event functions such as delivered, opened, clicked, bounced, marked as spam, and unsubscribed, with parameters such as activity ID, date, and count depending on event/filter.

Examples from Shopify's reference include patterns such as:

`shopify_email.opened MATCHES (activity_id = 135195754518)`

Do not copy placeholder activity IDs into production. Select the actual marketing activity in the editor.

### Engaged list starting pattern

Shopify's deliverability documentation gives an example:

`email_subscription_status = 'SUBSCRIBED' AND (customer_added_date > -6m OR (customer_added_date <= -6m AND (number_of_orders > 0 OR shopify_email.clicked() = true)))`

Use it as a starting concept, then tune to Hair Solutions Co's actual cycle and engagement distribution.

### Product purchase functions

Shopify supports product-purchase segment functions. Build these through the editor so Shopify inserts actual product IDs. Do not rely on product-title text where the function expects an ID.

## Segment quality checklist

- Uses current documented filters/functions
- Consent state is explicit when used for marketing
- Date window matches the stated name
- AND/OR precedence reflects intent
- Product IDs are selected from Shopify
- Query runs without error
- Segment size is plausible
- Sample members are correct
- Known exclusions are absent
- AI-generated description matches intent
- Segment name is durable and understandable
