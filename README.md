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
| `crm` | 5 | — |
| `hs-sales` | 9 | — |
| `hs-operations` | 5 | — |
| `hs-marketing` | 0 | — |
| `media` | 44 | — |
| `design-review` | 15 | — |
| `integrations` | 7 | — |
| `figma` | 5 | — |
| `agent-ops` | 11 | — |

## Provenance

`hs-*` plugins hold skills produced by merging Anthropic base skills with Hair Solutions Co.
legacy skills; each carries a `Merged from:` line naming its sources. The canonical record
lives in the Notion **Agents Dev Hub → Agent Skills** database — disk is authoritative for
content, Notion for curation.

`hs-marketing` is intentionally empty: its 6 skills are still `Draft` in Notion and have not
passed review.

## Conventions

- Every skill is `plugins/<plugin>/skills/<name>/SKILL.md` with YAML frontmatter whose
  `name` matches its directory.
- Three marketplace manifests are kept byte-identical: `.claude-plugin/`,
  `.agents/plugins/`, `.cursor-plugin/`. A plugin registered in only one of them will not
  resolve for the other runtimes.
- `design-review` consolidates four former stacks. Skill-level overlap is documented in
  `plugins/design-review/OVERLAP.md` and has **not** been cut.
