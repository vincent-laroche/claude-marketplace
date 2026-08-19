# Shopify Flow design guide

## What Flow is

Shopify Flow uses triggers, conditions, and actions to automate store and app processes. It is available as a free app on Basic, Grow, Advanced, and Plus, with some feature differences by plan.

As verified 2026-08-19:

- Grow, Advanced, and Plus can use Send HTTP Request.
- Plus can use certain custom partner-app tasks.
- Usage/API limits vary with plan.

Re-check before implementation.

## Components

- Trigger: starts the workflow from a Shopify/app event, scheduled time, or supported external event.
- Condition: decides which branch/action runs based on trigger or related object data.
- Action: changes Shopify/app state, sends information, or calls an external service when supported.
- Connector: an action exposed by an integrated third-party service.

## Design standard

Name workflows by business behavior, not implementation detail:

`MKT | [state/event] | [result] | [channel/system]`

A workflow spec should include:

1. Trigger and trigger object
2. Entry conditions
3. Data fields referenced
4. Branches
5. Waits
6. Actions
7. Idempotency/duplicate protection
8. Exit behavior
9. Error/failure behavior
10. Side effects to customer/order data
11. Connected app dependencies
12. Test cases
13. Rollback/deactivation plan

## Customer joined segment trigger

Use for a state that is best represented as dynamic segment membership, for example VIP or win-back eligibility. Verify:

- whether existing qualifying customers will trigger as expected;
- what happens when a customer leaves/rejoins;
- whether segment recalculation timing affects the desired send;
- whether another workflow uses the same segment.

## Customer subscribed to email marketing trigger

Use only for supported subscription events. Shopify's Flow documentation notes that the trigger responds to subscription through supported Shopify form/theme actions. If consent is synchronized from another system, test whether the change produces the same trigger behavior before relying on it.

## Wait action

Wait pauses a path. Current Shopify documentation limits the number of Wait steps in a workflow; the skill build research found a maximum of 40. Re-check the live reference.

Every wait should answer: why is this duration commercially/customer-experience appropriate?

Avoid stacking many waits in one giant lifecycle workflow. Separate journeys can be easier to monitor and deactivate safely.

## Marketing email action

When Flow uses a Shopify Messaging marketing email action, keep consent/recipient rules and template requirements in mind. If the use case is already a native Messaging automation, prefer that simpler implementation unless Flow adds necessary logic.

## External systems

For Hair Solutions Co, HubSpot may also own sales/service/marketing lifecycle logic. Before connecting Shopify Flow to HubSpot or another system:

- decide which system owns the state;
- avoid bi-directional loops;
- define field mapping and source of truth;
- define retry/idempotency behavior;
- keep marketing-consent ownership explicit;
- test on non-production or constrained records when possible.

Do not make production CRM field changes without approval.
