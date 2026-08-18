# Integration Guardrails

- Use service-owned OAuth/token models for multi-user or unattended systems; never embed or print secrets.
- Verify scopes, plan/seat access, endpoint write support, and rate limits against current official documentation where they affect a build.
- Register webhooks only after explicit approval, signed-event verification, idempotency, redacted logging, and a rollback path.
- Treat Figma publish, code mapping publish, asset transfer, Shopify mutation, and theme upload as separate external actions requiring their own authorization.
