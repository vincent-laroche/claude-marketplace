# atelier

Vincent Laroche's working toolkit — a Claude Code / Codex / Cursor plugin marketplace.

Repo: `vincent-laroche/marketplace`. Marketplace name: `atelier` (the name used in `plugin@name`;
it deliberately differs from the repo name, same as `hairsolutionsco` lives in
`hairsolutionsco-ai-toolkit`).

Replaces `hairsolutionsco-ai-toolkit`. That repo stays in place until this one is proven.

## Install

Register the marketplace, then enable only the plugins a project needs:

```jsonc
// ~/.claude/settings.json
"extraKnownMarketplaces": {
  "atelier": { "source": { "source": "github", "repo": "vincent-laroche/marketplace" } }
},
"enabledPlugins": {
  "storefront@atelier": true,
  "brand@atelier": true
}
```

Plugins are deliberately **not** all enabled globally. Per-project `.claude/settings.json`
turns on the packs that project actually needs.

## Plugins

| Plugin | Skills | Also ships |
| --- | ---: | --- |
| `storefront` | 13 | 3 agents, hook |
| `brand` | 4 | 1 agents |
| `marketing` | 11 | — |
| `email-marketing` | 13 | 8 paired agents, MailerLite MCP, hooks |
| `crm` | 5 | — |
| `hs-sales` | 9 | — |
| `hs-operations` | 5 | — |
| `hs-marketing` | 6 | — |
| `media` | 44 | — |
| `design-review` | 8 | — |
| `integrations` | 7 | — |
| `figma` | 11 | 1 agent, command, hooks |
| `agent-ops` | 11 | — |

## Provenance

`hs-*` plugins hold skills produced by merging Anthropic base skills with Hair Solutions Co.
legacy skills; each carries a `Merged from:` line naming its sources. The canonical record
lives in the Notion **Agents Dev Hub → Agent Skills** database — disk is authoritative for
content, Notion for curation.

`hs-marketing`'s 6 skills were approved and pulled from Notion on 2026-08-10. They remain
`Draft` status in the Notion database until flipped to `Active`.

## Conventions

- Every skill is `plugins/<plugin>/skills/<name>/SKILL.md` with YAML frontmatter whose
  `name` matches its directory.
- Three marketplace manifests are kept byte-identical: `.claude-plugin/`,
  `.agents/plugins/`, `.cursor-plugin/`. A plugin registered in only one of them will not
  resolve for the other runtimes.
- `design-review` consolidates four former stacks. The skill-level overlap cut was executed
  on 2026-08-10 (15 skills → 8); what was removed and why is in
  `plugins/design-review/OVERLAP.md`, and every removed skill is recoverable from git history.
