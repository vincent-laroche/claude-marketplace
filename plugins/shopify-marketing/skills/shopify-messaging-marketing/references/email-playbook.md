# Shopify Messaging email campaign and template playbook

## Campaign editor capabilities

Current Shopify Messaging email campaigns support:

- branded Shopify templates;
- reusable custom templates;
- fully custom-coded HTML email;
- saved customer segments or all email subscribers;
- subject line and preview text;
- personalization;
- editable UTM parameters;
- tests to multiple addresses;
- immediate or scheduled sending;
- Shopify-suggested future send time based on click-through optimization.

Changing the template of an existing draft deletes content from the previous template. Do not use template switching as an exploratory design step after substantial copy has been written.

## Personalization

Current supported personalization includes common customer fields such as first name, last name, email, city, region, and country. Shopify currently limits personalization values in subject/preview and body. Verify the current limit before a high-complexity template; as of this skill build, Shopify documents up to 2 personalized values across subject/preview and up to 10 in the email body.

Always define a safe default. If no default is supplied and the field is missing, the personalized space may be blank.

Do not personalize with inferred sensitive attributes or unsupported assumptions.

## Standard template sections

Shopify Messaging supports a broad section library. Important sections include:

- Button
- Collection
- Countdown
- Custom Liquid
- Discount
- Express checkout
- Footer
- Gift card
- Header
- Image and GIF
- Image with text
- Multi-column
- Product
- Text
- Video

Automation-specific sections include abandoned browse, cart, and checkout content.

### Product section

A Product section can be Dynamic or Static. Dynamic can resolve products at send time such as best sellers or newest products. Static selects fixed products. Current documentation permits up to 9 products in a product section. Re-check if designing around this maximum.

### Collection section

Current documentation permits up to 9 products from a collection in the section.

### Countdown section

Shopify can render a live countdown as an animated image. Use only for a real deadline. Never create false urgency.

## Custom templates

Use reusable custom templates when the layout will recur. Keep the reusable template generic enough that editors do not need to delete product-specific or promotion-specific remnants each time.

Recommended Hair Solutions Co template anatomy:

1. Brand header
2. One-line context or category label
3. Headline
4. Brief body copy
5. Primary CTA
6. Optional product/collection proof block
7. Optional education or reassurance block
8. Optional secondary CTA
9. Footer/unsubscribe

## Writing defaults from Shopify guidance

Shopify's own email guidance favors concise, store-driving marketing:

- Put important information high in the email, particularly within the first two mobile scrolls.
- Include at least one clear link back to the store.
- Keep copy compact; Shopify's guidance suggests roughly 200 words or 20 lines as a useful ceiling for many marketing emails.
- Avoid excessive capitalization and punctuation.
- Keep subject lines concise; Shopify guidance suggests 3-6 words and under 50 characters as a useful target.
- Use accurate alt text and sufficient contrast.
- Test all links and discounts.
- Send consistently rather than disappearing for long periods and returning with a major volume spike.

Treat these as defaults, not rigid laws. Conversion context overrides arbitrary word counts.

## Accessibility QA

Check:

- logical heading/content order;
- descriptive alt text for meaningful images;
- non-image text for essential offer terms;
- readable mobile type size;
- sufficient color contrast (Shopify guidance references 4.5:1 for normal text);
- CTA text that communicates destination/action;
- no dependence on color alone;
- test with images disabled when the campaign is important.

## Custom Liquid

Shopify Messaging Custom Liquid is not equivalent to theme Liquid.

Rules:

1. Use only supported Messaging variables.
2. If open tracking is active and a custom-coded email requires Shopify's tracking variable, preserve it.
3. Preserve unsubscribe URL/link behavior.
4. Current documented limits: 50 KB per Custom Liquid section and 500 KB for a fully custom-coded email. Verify current limits before building near them.
5. Avoid brittle logic that depends on unavailable storefront objects.
6. Use conditional output with clear fallbacks.
7. Test representative customers/data states.

Useful variable families include customer, shop, email, customer tags/orders, store credit, and automation-specific objects. Consult the live Custom Liquid reference before writing non-trivial code because the supported object list is large and can change.

## Pre-send QA

- Correct segment and exclusion logic
- Sender and reply address
- Subject and preview
- Personalization fallbacks
- Mobile first-screen hierarchy
- Every link
- Discount eligibility/date/value
- Product availability and price
- Policy/claim accuracy
- UTM values
- Image alt text
- Contrast and text legibility
- Footer address and unsubscribe
- Test inbox rendering
- Spelling and grammar
- Recipient count
- Incremental cost
- Volume spike risk
- Approval recorded before send/schedule
