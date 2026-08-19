# Current Shopify Inbox and Inbox agent - verified 2026-08-19

## Inbox

Shopify Inbox provides online-store chat managed by staff or, for eligible early-access merchants, an Inbox agent.

Staff can respond on desktop/mobile, share product links, share valid discount codes, and send images/videos. Conversations can be assigned to staff and searched by customer or keywords/order information as supported.

## Inbox agent status

The Inbox agent is early access and available only to certain merchants as of verification.

Current requirements include:

- Shopify Inbox installed;
- active online store;
- new customer accounts, not legacy customer accounts;
- eligible Shopify plan (Basic, Grow, Advanced, Plus documented at build time).

Re-check eligibility before planning activation.

## Agent capabilities

Current documented capabilities include:

- answer product questions;
- recommend products from the store catalog;
- help with order lookups after customer authentication;
- add items to cart;
- reply in the customer's language;
- use product catalog, policies, published pages/guides, and Shopify Knowledge Base as sources;
- use cited web search as a secondary source for qualitative reviews/social proof for a specific catalog product.

The agent bases product recommendations on the store catalog. Store sources, not generic web search, are authoritative for product facts, care, usage, and styling guidance.

## Assignment modes

Current modes:

- All conversations
- Only when staff are unavailable
- Never

Only when staff are unavailable uses the configured staff availability hours. Assignment-mode changes apply to new conversations immediately.

## Authentication/customer data

Customers can chat with the agent without signing in. Order lookups require sign-in. Staff-chat sign-in/contact requirements are configured separately.

The agent handles customer data independently per store and does not share customer information/conversation data across stores.

## AI disclosure and privacy

When the Inbox agent is active, Shopify automatically displays a notice that chat is powered by Shopify and that the customer is chatting with AI. The disclosure cannot be removed/customized.

Shopify states that customer chat communications are processed to generate responses and improve the agent. Merchants using a custom privacy policy should review it for disclosures about Shopify-powered AI chat and processing of chat data. Treat this as a privacy/legal review item before activation.

## Limits and built-in protections

Current documented conversation limits:

- Up to 100 agent responses in a conversation for unsigned customers.
- Up to 1,000 agent responses for signed-in customers.
- Up to 50 conversations per customer per day.

Built-in protections include rate limiting, bot/spam detection, and blocked-sender/IP filtering.

When a limit is reached, the agent stops and hands off if staff handoff is available; otherwise it provides the store sender email.

Re-check these limits before designing operational assumptions around them.
