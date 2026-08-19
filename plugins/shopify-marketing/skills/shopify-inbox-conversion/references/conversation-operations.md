# Shopify Inbox conversation operations

## Staff conversations

Staff can reply directly in Shopify Inbox. Current capabilities include sharing product links, discount codes, images, and videos. The conversation view can display cart context when available.

If a customer leaves the site, a staff reply may be delivered to the customer's email when an email is available/linked according to Inbox behavior.

## AI-generated suggested replies

Suggested replies are separate from the automatic Inbox agent. They assist staff composing a response.

Current requirements include an English online store/admin and Inbox eligibility conditions. Shopify states that staff remain responsible for accuracy and should review/edit generated replies before sending.

If a suggested reply is factually wrong, editing that reply provides style/response feedback but does not fix the underlying source information. Fix the product/policy/page source.

## Staff handoff

The Inbox agent can hand off when:

- customer requests a person;
- agent determines staff attention is needed;
- it lacks sufficient confidence.

If staff handoff is available, the conversation moves to staff with the AI context. If handoff is unavailable, the agent can provide the store's sender email; the agent does not send the email on the customer's behalf.

Ensure that sender email is monitored before relying on this fallback.

## Customer sign-in

New customer accounts can require sign-in before messaging staff depending on settings. The Inbox agent itself can converse without sign-in, but order lookup requires sign-in. Never bypass this boundary by asking the customer to paste sensitive order/account data that should be handled through supported authentication.

## Product links and discounts

Staff can share products published to the Inbox sales channel. A product unavailable to that sales channel may not be shareable through Inbox.

Staff can share existing valid discount codes; the discount can apply to the cart when clicked. Do not create, change, or promise a discount solely to close a chat unless business policy and approval support it.

## Conversation status and assignment

Conversations can be open or closed and assigned/unassigned to staff with appropriate permissions. Current Shopify documentation states that Inbox conversations cannot be deleted.

Use assignment intentionally so one customer does not receive competing staff replies.

## Agent performance metrics

Current overview metrics:

- Assisted sessions
- Assisted orders
- Satisfaction rate
- Average response time

Build a manual quality layer because these metrics do not directly measure factual correctness.

## Operational dashboard additions

Track manually or in a reporting system where feasible:

- handoff count/rate;
- handoff reason;
- unanswered topic;
- factual error;
- policy error;
- unsafe/medical escalation;
- product recommendation accepted/clicked if measurable;
- repeat contact for same question;
- support versus sales topic mix.
