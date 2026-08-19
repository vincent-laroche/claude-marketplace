---
name: shopify-inbox-conversion
description: Configure, audit, train, and optimize Shopify Inbox for customer conversion and support, including the early-access Inbox agent, persona design, Shopify Knowledge Base, staff handoff, customer sign-in, quick replies, instant answers, AI-generated suggested replies, conversation operations, performance metrics, and safety QA. Use for Shopify Inbox setup, chat conversion strategy, AI agent configuration/training, knowledge-base readiness, support-to-sales chat workflows, staff versus AI routing, response quality, or customer-chat optimization for Hair Solutions Co.
---

# Shopify Inbox Conversion

Use this skill to make Shopify Inbox a trustworthy conversion and support layer for Hair Solutions Co. Optimize for accurate guidance, fast resolution, and appropriate handoff before raw automation rate.

## Current product state

As verified on 2026-08-19:

- Shopify Inbox supports staff-managed online-store chat.
- An early-access Inbox agent is available only to certain merchants.
- The Inbox agent can answer questions, recommend products, look up orders after sign-in, add products to cart, and reply in the customer's language.
- The agent uses store sources such as product catalog, policies, published storefront content, and Shopify Knowledge Base.
- For product-adjacent qualitative reviews/social proof, the agent can use cited web search as a secondary source, but store sources remain authoritative for product facts.
- Persona controls communication style, not factual store knowledge.
- Training refines persona/voice; it does not teach new store facts.
- Staff handoff remains necessary for low-confidence, complex, or sensitive interactions.

Read `references/current-inbox.md` for requirements and assignment behavior.

## Non-negotiable safety rules

Hair replacement is a trust-sensitive category. Apply these rules to persona design, knowledge, QA, and suggested responses:

1. Never diagnose hair loss, scalp conditions, or medical causes.
2. Never imply that a hair system grows biological hair or treats a medical condition.
3. Never invent product lifespan, wear duration, adhesive performance, maintenance interval, base durability, color/density match, styling capability, or suitability.
4. Never invent guarantees, refund rights, replacement rights, shipping promises, custom-order terms, or exceptions.
5. Never pressure a customer who expresses distress, embarrassment, insecurity, or medical concern.
6. Never use web reviews as authoritative product specifications or store policy.
7. When source information is missing, conflicting, or materially uncertain, hand off rather than guess.
8. Order information requires the platform's supported customer verification/sign-in flow.
9. Do not configure or activate the Inbox agent, change assignment mode, change privacy language, publish Knowledge Base facts, or change live chat settings without explicit approval.
10. Review AI-generated staff replies before sending; they are suggestions, not approved facts.

## Source-of-truth hierarchy

When answering a customer question, prefer sources in this order:

1. Current Shopify product catalog for factual product attributes, availability, and price.
2. Current store policies/settings for returns, shipping, payments, and customer-account behavior.
3. Published Hair Solutions Co pages, guides, and product-care content.
4. Shopify Knowledge Base custom/default FAQs.
5. Order/account data after required customer authentication.
6. Cited web search only for qualitative third-party reviews/social proof when the Inbox agent supports it.

If sources disagree, do not merge them into a confident answer. Flag the conflict and hand off.

Read `references/persona-and-knowledge.md` before changing persona or Knowledge Base.

## Choose the operating mode

- **Readiness audit**: requirements, customer accounts, content quality, policies, Knowledge Base, privacy disclosure, handoff coverage.
- **Persona design**: tone, wording, service style, boundaries.
- **Knowledge architecture**: identify missing facts and where each belongs.
- **Training**: practice scenarios and real-conversation feedback.
- **Routing/handoff**: assignment mode, availability, escalation conditions.
- **Staff efficiency**: quick replies, instant answers, AI suggested replies.
- **Conversion optimization**: product discovery, friction reduction, cart assistance, assisted-order analysis.
- **Quality review**: sample conversations, source failures, hallucination risks, customer feedback.

## Readiness audit workflow

Before recommending activation of the Inbox agent:

1. Confirm Shopify Inbox is installed and the online store is active.
2. Confirm the store is on an eligible plan.
3. Confirm the store uses new customer accounts if the early-access agent requires them. The current agent does not work with legacy customer accounts.
4. Confirm agent availability for the store; it is early access as of this build.
5. Audit product pages for factual completeness and consistency.
6. Audit return, shipping, privacy, payment, contact, and account information.
7. Audit published sizing, care, product education, and FAQ pages.
8. Audit Shopify Knowledge Base for generated and custom FAQs.
9. Test the Knowledge Base with representative customer questions and inspect matched sources.
10. Confirm sender email because it can be offered when staff handoff is unavailable.
11. Confirm staff availability hours and notification coverage.
12. Confirm customer sign-in/chat behavior.
13. Review the privacy policy for AI-assisted chat disclosure if the agent will be activated.
14. Build a safety/handoff matrix for Hair Solutions Co.
15. Run a pre-launch conversation test suite.
16. Present findings and require approval before activation or assignment-mode changes.

## Persona design

Use persona only for communication behavior. Never place factual product/policy rules only in the persona.

Recommended Hair Solutions Co persona characteristics:

- concise, calm, knowledgeable, and low-pressure;
- direct about uncertainty;
- asks one useful question at a time when product fit genuinely depends on it;
- explains differences without implying a medical diagnosis;
- does not overstate confidence in color, density, fit, durability, or appearance outcomes;
- prioritizes verified product facts and store policy;
- offers staff handoff when a decision is subjective, high-stakes, policy-sensitive, or unsupported by data;
- avoids shame, fear, or urgency tied to appearance/hair loss.

### Persona instruction pattern

Use short behavioral instructions, for example:

- Keep replies concise and practical.
- Use the customer's terminology when it is clear and non-medical.
- Ask only questions needed to narrow a product choice.
- Do not pressure customers to purchase.
- State when information is unavailable and offer staff help.
- For policy, order, product-specification, or care claims, rely on store sources rather than assumptions.

Do not put return windows, shipping rates, product specifications, business hours, or discount rules into persona text. Put those facts in the correct store source or Knowledge Base.

## Knowledge architecture

Read `references/persona-and-knowledge.md`.

For every recurring customer question, decide where the answer belongs:

- Product-specific fact -> product catalog/product page.
- Store-wide return/shipping/payment/account rule -> Shopify setting/policy.
- Detailed education/care/sizing explanation -> published page/guide where appropriate.
- Concise missing FAQ used by AI agents -> Shopify Knowledge Base.
- Style/tone preference -> Inbox persona.
- Routing/availability/sign-in -> Inbox settings.

Do not duplicate the same policy fact in multiple places unless necessary. Duplicates drift and create conflicting answers.

## Knowledge Base workflow

Shopify Knowledge Base can generate facts from store information and supports custom FAQs used as an AI-agent data source.

For each FAQ:

1. Confirm the question represents a real customer need.
2. Check whether an authoritative source already exists.
3. Fix the underlying source if the source itself is wrong.
4. Use a custom FAQ only to fill a real knowledge gap or add concise context.
5. Keep the answer short and factual. Shopify's current UI guidance recommends brief answers.
6. Avoid marketing claims that are not supported elsewhere.
7. Test the question and close paraphrases in Knowledge Base.
8. Review which source is matched.
9. Require approval before publishing new/overridden FAQ content.

## Training workflow

Read `references/training-and-qa.md`.

Training affects voice/persona, not store facts.

### Practice scenarios

Use before launch and after major persona changes:

1. Review generated scenarios.
2. Choose the better response or write an improved response.
3. Finish the training run.
4. Review the suggested persona update.
5. Compare against the active persona.
6. Reject changes that weaken safety, accuracy, or clarity.
7. Require approval before saving a material persona change.

### Real conversations

Use thumbs-up/down and edited alternatives to teach style preferences. Remember that editing/rating a past response does not correct the factual source. If a factual answer is wrong, update the product/policy/page/Knowledge Base source.

## Assignment-mode decision

The current Inbox agent offers modes equivalent to:

- All conversations
- Only when staff are unavailable
- Never

Recommended initial rollout for Hair Solutions Co: start with **Only when staff are unavailable** unless conversation testing demonstrates strong source coverage and safe handoff behavior. This minimizes customer risk while collecting real performance data.

Before choosing All conversations, confirm:

- product/policy content is complete;
- knowledge tests pass;
- privacy disclosure is ready;
- staff handoff works;
- sender email is monitored;
- high-risk topics are consistently escalated;
- customer satisfaction and error review are acceptable.

Changing assignment mode affects new conversations immediately. Require explicit approval.

## Handoff matrix

Read `references/conversation-operations.md`.

Always prefer staff handoff for:

- customer explicitly asks for a human;
- agent is not confident or sources conflict;
- refund/return exception or disputed policy;
- charge/payment dispute;
- order modification/cancellation outside supported self-service behavior;
- custom product promise or special accommodation;
- complaint involving customer harm, safety, or serious dissatisfaction;
- medical/scalp/hair-loss diagnosis or treatment question;
- legal/privacy request;
- claim that a product caused injury or a medical issue;
- any request requiring a promise not present in source material.

## Quick replies, instant answers, suggested replies, and agent

Do not confuse these tools.

### Quick replies

Reusable staff-authored snippets for common messages. Use them to speed staff responses while keeping staff in control.

Good uses:

- request for order number/sign-in;
- link to verified sizing/care guide;
- explain support hours;
- offer handoff/escalation;
- request the exact product/color/base information needed.

Avoid embedding policy details likely to change unless they are maintained deliberately.

### Instant answers

Customer-selectable FAQ-style chat options. The Track my order option has special built-in behavior and may remain available independently of the agent.

Use instant answers for high-volume, stable questions with one reliable answer.

### AI-generated suggested replies

These are staff composing aids, not the automatic Inbox agent. Current requirements include English store/admin and other eligibility conditions. Staff must review suggestions for accuracy before sending.

### Inbox agent

Automatically handles assigned conversations and can perform supported shopping/order tasks. It is not a replacement for authoritative source maintenance or staff escalation.

## Conversation conversion workflow

When evaluating a sales-oriented chat:

1. Identify the customer's stated goal.
2. Identify the minimum missing fit information.
3. Use verified catalog data to narrow options.
4. Explain the relevant tradeoff clearly.
5. Provide one or a small number of appropriate products, not an indiscriminate list.
6. Offer product links/add-to-cart when supported.
7. Use discounts only when a valid current discount exists and the use is approved/appropriate.
8. Do not turn uncertainty into a sales claim.
9. Handoff when fit depends on nuanced human judgment or unavailable data.

## Performance metrics

Current Inbox agent overview metrics include:

- Assisted sessions
- Assisted orders
- Satisfaction rate
- Average response time

Do not optimize assisted orders in isolation. Pair with:

- handoff rate and reasons;
- factual-error rate from audits;
- dissatisfaction themes;
- conversion by topic;
- repeat contacts for the same issue;
- policy/claim errors;
- staff workload reduction.

A lower handoff rate is not automatically better if it comes from overconfident AI answers.

## Review cadence

After rollout:

1. Review the first meaningful sample of conversations manually.
2. Classify factual errors versus style issues.
3. Fix factual errors at the source.
4. Use training/persona only for style and service behavior.
5. Add Knowledge Base FAQs only for repeated genuine gaps.
6. Track handoff topics and unanswered queries.
7. Re-test representative scenarios after material catalog/policy changes.

## Default output formats

### Inbox readiness audit

Return:

1. Requirement/status
2. Evidence/current state
3. Customer/revenue risk
4. Recommended fix
5. Source of truth to edit
6. Approval required
7. Test to verify

### Knowledge gap register

Return:

- Customer question
- Current source
- Problem/gap
- Correct destination: product / policy / page / Knowledge Base / persona / setting
- Proposed content requirement
- Risk if unanswered
- Approval required

### Conversation QA

For each reviewed conversation return:

- Intent/topic
- Outcome
- Correct facts?
- Source quality
- Tone/service quality
- Handoff correct?
- Conversion opportunity handled?
- Risk severity
- Source fix or training fix

## Reference loading guide

- `references/current-inbox.md` - requirements, assignment modes, data/privacy, agent capabilities and limits.
- `references/persona-and-knowledge.md` - persona versus facts, Knowledge Base architecture, source maintenance.
- `references/conversation-operations.md` - staff chat, handoff, quick responses, order/privacy handling, metrics.
- `references/training-and-qa.md` - training, test scenarios, Hair Solutions Co safety suite.
- `references/source-index.md` - official Shopify sources verified 2026-08-19.
