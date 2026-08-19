# Persona and knowledge architecture

## Persona controls behavior, not facts

Shopify's current Inbox persona is for tone, wording, personality, and service style. It should not be used as the only place to store shipping rates, return terms, support hours, discounts, sizing facts, product specifications, or other business facts.

A persona cannot override built-in Inbox safety behavior, handoff behavior, availability, sign-in settings, or other Inbox settings.

Do not write persona instructions such as "never hand off" or "always recommend a product." Shopify explicitly warns that persona instructions cannot force behavior that conflicts with settings/safety.

## Source location decision

### Product catalog/product pages

Put:

- factual product specifications;
- variants/colors/sizes;
- availability;
- current pricing;
- product-specific care/use information when appropriate.

### Store settings/policies

Put:

- return/refund rules;
- shipping/delivery rules;
- payment methods;
- account behavior;
- store-level terms.

### Published pages/guides

Put:

- sizing guides;
- product education;
- care guides;
- detailed comparison content;
- support process explanations.

### Shopify Knowledge Base

Put concise, durable FAQs when no better authoritative source exists or when AI shopping agents need a direct answer to a recurring question.

### Persona

Put:

- concise vs detailed preference;
- tone and warmth;
- pressure avoidance;
- how to acknowledge frustration;
- how to state uncertainty;
- question-asking style.

### Inbox settings

Put:

- assignment mode;
- staff availability;
- sign-in requirements;
- greeting;
- other chat behavior settings.

## Knowledge Base

Shopify Knowledge Base can surface automatically generated facts from store configuration and manually created/overridden FAQs. These facts can be used by AI shopping agents, including relevant Shopify experiences.

Current workflow supports:

- reviewing generated FAQs/facts;
- viewing top unanswered questions;
- adding custom FAQs;
- overriding an automatically generated answer when necessary;
- testing a question and seeing which resources match.

Shopify recommends brief FAQ answers. At build time, its Help Center suggests roughly 1-2 sentence answers for new FAQs.

### Source repair rule

If an automatically generated FAQ is wrong because the underlying return policy or shipping setting is wrong, fix the source rather than permanently papering over the problem with an override where possible.

### Hair Solutions Co priority knowledge domains

Audit these without inventing answers:

- base/material terminology and differences;
- available sizes/dimensions;
- color/density/curl/wave fields actually sold;
- stock/custom status;
- care and cleaning instructions;
- attachment/adhesive compatibility only where officially supported;
- styling/heat guidance only where verified;
- order processing/shipping;
- returns/refunds/exchanges/replacements;
- product selection process;
- support/contact process;
- common order-status questions.

For every gap, point to the correct source owner rather than drafting an unsupported fact.
