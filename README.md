# claude-marketplace

Vincent Laroche's working toolkit — a Claude Code / Codex / Cursor plugin marketplace.

Repo: `vincent-laroche/claude-marketplace`. Marketplace name: `claude-marketplace` — the name
used in `plugin@name`, the install directory, and the cache path. Repo and marketplace name
are deliberately kept identical; they were `marketplace` and `atelier` until 2026-08-18.

Replaces `hairsolutionsco-ai-toolkit`, which is now `vincent-laroche/agents-marketplace`.

## Scope — what does not live here

**The design system is not in this marketplace.** `vincent-laroche/brand-design-system` is the
sole authority for Atelier Zero tokens, foundations and specs. The `brand` plugin and
`design-review`'s extraction pipeline (`design-extract`, `design-system-package`, `token-map`,
`brand-identity`) were removed on 2026-08-18 for exactly this reason — they carried a second
copy of token values that would drift from the brand repo. Skills that need brand values read
them from that repo at runtime; they never restate them.

## Install

Register the marketplace, then enable only the plugins a project needs:

```jsonc
// ~/.claude/settings.json
"extraKnownMarketplaces": {
  "claude-marketplace": { "source": { "source": "github", "repo": "vincent-laroche/claude-marketplace" } }
},
"enabledPlugins": {
  "storefront@claude-marketplace": true,
  "brand@claude-marketplace": true
}
```

Plugins are deliberately **not** all enabled globally. Per-project `.claude/settings.json`
turns on the packs that project actually needs.

## Plugins

| Plugin | Skills | Also ships |
| --- | ---: | --- |
| `storefront` | 13 | 3 agents, hook |
| `marketing` | 11 | — |
| `email-marketing` | 13 | 8 paired agents, MailerLite MCP, hooks |
| `crm` | 5 | — |
| `hs-sales` | 9 | — |
| `hs-operations` | 5 | — |
| `hs-marketing` | 6 | — |
| `media` | 44 | — |
| `design-review` | 4 | — |
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
