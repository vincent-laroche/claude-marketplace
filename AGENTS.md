# AGENTS.md — toolkit-marketplace

Read `README.md` first — it is the durable source of truth for this repo's structure, plugin
list, MCP servers, and the cache/authoring rules that have already cost real time when
ignored. This file exists only because the wider `01_projects` convention expects an
`AGENTS.md` entry point; it does not restate README content, it points at it.

## The one thing to know before touching anything here

**Author in `~/03_agents/claude-marketplace`. Never in
`~/.claude/plugins/marketplaces/toolkit-marketplace/`** — that second path is a cache Claude
Code manages and can reset at any time. A commit made there looks ordinary and reaches nobody.
See README § "The cache is not the repository" for the incident that proved it.

## If you're here about MCP tools / connectors

This marketplace's own `.mcp.json` files cover three servers (`mailerlite`, `figma`,
`chrome-devtools` + `desktop-commander`). Everything else in Vincent's stack — Notion, Shopify,
Cloudflare, HubSpot, Google Workspace, GitHub, Stripe, Canva, and more — is a `claude.ai`
account-level OAuth connector, not marketplace config. Run `claude mcp list` for live status;
see README § "Connector stack" for how the tiers split and what was broken/fixed on 2026-08-18.
Do not go looking for a `.mcp.json` for Shopify or Notion in this repo — there isn't one.

## If you're here about brand values

They are not here either. `vincent-laroche/brand-design-system`
(`/Users/vMac/08_brand/brand-design-system`) is the sole authority. See README § "Scope — what
does not live here." The sibling `brand-design-marketplace` repo
(`~/07_design/brand/brand-design-marketplace`) packages the brand-compliance plugins that read
from it; this repo carries engineering and ops plugins that must never restate a token value.

## Everything else

Plugin structure, install instructions, agent-frontmatter conventions, the three-manifest
sync requirement, and the concurrent-session git hazards are all in `README.md`. Read it before
adding, renaming, or removing a plugin.
