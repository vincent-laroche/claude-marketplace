# Email Marketing

MailerLite-first email operations for Hair Solutions Co. The plugin covers briefs, production HTML,
native drag-and-drop modules, campaign drafts, audiences and consent, lifecycle automations, Shopify
ecommerce data, forms, deliverability, analytics, and controlled release.

The official MailerLite OAuth MCP is the primary live surface. Browser control is reserved for
dashboard-only work. Local scripts provide read-only account snapshots and deterministic HTML
validation. The legacy email-marketing-modules plugin remains the HubSpot Design Manager archive and
is not a dependency of this plugin.

Live mutations are always scoped by action: draft creation is distinct from test sends, scheduling,
automation activation, audience imports, DNS changes, deletion, and publication.

## Codex agents

The plugin ships eight validated custom agents. Install or refresh their personal Codex definitions
from the plugin root:

```bash
python3 scripts/install_codex_agents.py
python3 scripts/install_codex_agents.py --check
```

Start a new Codex chat after installation. Invoke an agent by its configured name, such as
`Email Lifecycle Architect` or `MailerLite Campaign Operator`. The documented `/agent` and
`/subagents` commands switch among agent threads that have already been spawned; they are not an
agent-definition catalog. There is no documented `/agents` plural command.
