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

**Codex-native content is decided-out but not yet removed.** The call (2026-08-18) is that
Codex agents live in `agents-marketplace`. The commit that executed it — stripping 17 `.toml`
agents, 66 `openai.yaml` sidecars, the `.codex-plugin/` manifests and the `.agents/` mirror —
was discarded by a `git reset --hard` from a concurrent session and is **not** in this
history. It survives on the branch `backup-local-main-20260818`. Until it is re-applied, this
repo still ships the Codex layer described below, and the two intents keep colliding: see
"Concurrent sessions".

## Install

Register the marketplace, then enable only the plugins a project needs:

```jsonc
// ~/.claude/settings.json
"extraKnownMarketplaces": {
  "claude-marketplace": { "source": { "source": "github", "repo": "vincent-laroche/claude-marketplace" } }
},
"enabledPlugins": {
  "storefront@claude-marketplace": true,
  "design-review@claude-marketplace": true
}
```

Plugins are deliberately **not** all enabled globally. Per-project `.claude/settings.json`
turns on the packs that project actually needs.

## Plugins

Counted from disk 2026-08-18. Agent counts are Claude `.md` agents; each currently has a
Codex `.toml` sibling.

| Plugin | Skills | Also ships |
| --- | ---: | --- |
| `media` | 44 | — |
| `email-marketing` | 13 | 8 agents, hooks, MailerLite MCP |
| `storefront` | 13 | 9 agents, hooks, browser-QA + Desktop Commander MCP |
| `figma` | 12 | 1 agent, 1 command, hooks, Figma MCP |
| `agent-ops` | 12 | — |
| `marketing` | 11 | — |
| `hs-sales` | 9 | — |
| `integrations` | 7 | — |
| `hs-marketing` | 6 | — |
| `crm` | 5 | — |
| `hs-operations` | 5 | — |
| `design-review` | 4 | — |

## MCP servers

A plugin declares its own servers in `plugins/<plugin>/.mcp.json`, auto-discovered by Claude
Code when the plugin is enabled. `${CLAUDE_PLUGIN_ROOT}` expands to the plugin directory for
stdio servers. Three plugins declare one:

| Plugin | Server | Transport |
| --- | --- | --- |
| `email-marketing` | `mailerlite` | HTTP, `https://mcp.mailerlite.com/mcp` |
| `figma` | `figma` | HTTP, `https://mcp.figma.com/mcp` |
| `storefront` | `chrome-devtools`, `desktop-commander` | stdio, `npx` |

`email-marketing` additionally mirrors its block into `gemini-extension.json` and points at it
from `.cursor-plugin/plugin.json` (`"mcpServers": "./.mcp.json"`). Claude Code needs no
pointer — a bare `.mcp.json` at the plugin root is enough.

**Name collision to watch:** this marketplace's `figma` plugin and Anthropic's
`figma@claude-plugins-official` share both a plugin name and a server name, so both resolve to
the `mcp__plugin_figma_figma__*` prefix. Their skills do not overlap (ours is engineering —
REST, Plugin API, Shopify bridge, delivery; theirs is design authoring — `figma-use`,
`figma-design-to-code`), but running both enabled registers the same server twice. Pick one.

## Provenance

`hs-*` plugins hold skills produced by merging Anthropic base skills with Hair Solutions Co.
legacy skills; each carries a `Merged from:` line naming its sources. The canonical record
lives in the Notion **Agents Dev Hub → Agent Skills** database — disk is authoritative for
content, Notion for curation.

`hs-marketing`'s 6 skills were approved and pulled from Notion on 2026-08-10. They remain
`Draft` status in the Notion database until flipped to `Active`.

## Concurrent sessions

More than one agent session works this repo, and they have pushed opposing intents on the same
day — one stripping the Codex layer, another adding to it (`restore Desktop Commander
tooling`, `preserve browser QA MCP`, `add native-theme-settings-protector agent`). A
`git reset --hard origin/main` from one session silently dropped a pushed-nowhere commit.

- Do not `git reset --hard` a shared branch. Land work on a branch and push that.
- Before committing, check the index holds only your files: `git diff --cached --stat`.
- Re-fetch immediately before pushing; the tip moves.

## Conventions

- Every skill is `plugins/<plugin>/skills/<name>/SKILL.md` with YAML frontmatter whose
  `name` matches its directory.
- Three marketplace manifests are kept byte-identical: `.claude-plugin/`,
  `.agents/plugins/`, `.cursor-plugin/`. A plugin registered in only one of them will not
  resolve for the other runtimes. (The `.agents/` mirror goes away with the Codex cut.)
- `design-review` consolidates four former stacks. The 2026-08-10 overlap cut took it 15 → 8;
  the 2026-08-18 design-system cut took it 8 → 4. What was removed and why is in
  `plugins/design-review/OVERLAP.md`, and every removed skill is recoverable from git history.
