# toolkit-marketplace

Vincent Laroche's working toolkit — a Claude Code / Codex / Cursor plugin marketplace.

Repo: `vincent-laroche/claude-marketplace`. Marketplace name: `toolkit-marketplace` — the name
used in `plugin@name`, the install directory, and the cache path. Repo and marketplace name
deliberately differ, as they did originally.

**The name may not begin with `claude-` followed by a category noun.** Claude Code rejects
names that impersonate an official marketplace, re-checking on *every* load rather than only
at registration, so a bad name breaks every plugin at once. `claude-marketplace` and
`claude-plugins` both fail `claude plugin validate`; a suffix does not rescue them
(`claude-marketplace-hs` fails too) though a prefix does. `claude-skills`, `claude-agents` and
`claude-tools` pass — the block is on claiming to *be* the Claude marketplace, not on the word
`claude`. Names were `marketplace`/`atelier`, then briefly `claude-marketplace` (broken, ~1h),
now `toolkit-marketplace` as of 2026-08-18. Run `claude plugin validate .` before ever
changing it again.

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
  "toolkit-marketplace": { "source": { "source": "github", "repo": "vincent-laroche/claude-marketplace" } }
},
"enabledPlugins": {
  "storefront@toolkit-marketplace": true,
  "design-review@toolkit-marketplace": true
}
```

Plugins are deliberately **not** all enabled globally. Per-project `.claude/settings.json`
turns on the packs that project actually needs.

## Plugins

Counted from disk 2026-08-18. Agent counts are Claude `.md` agents; each currently has a
Codex `.toml` sibling. **~tok** is the skill frontmatter that loads into *every* context while
the plugin is enabled — the standing cost of having it on. **On** marks the three plugins that
install enabled; the rest ship `defaultEnabled: false` and are opt-in per project.

| Plugin | Skills | ~tok | On | Also ships |
| --- | ---: | ---: | :-: | --- |
| `media` | 44 | 3,747 | | — |
| `email-marketing` | 13 | 1,573 | | 8 agents, hooks, MailerLite MCP |
| `storefront` | 13 | 1,124 | ● | 9 agents, hooks, browser-QA + Desktop Commander MCP |
| `figma` | 12 | 1,228 | | 1 agent, 1 command, hooks, Figma MCP |
| `agent-ops` | 12 | 596 | ● | — |
| `marketing` | 11 | 1,313 | | — |
| `hs-sales` | 9 | 767 | | — |
| `integrations` | 7 | 795 | | — |
| `hs-marketing` | 6 | 826 | | — |
| `crm` | 5 | 550 | | — |
| `hs-operations` | 5 | 481 | | — |
| `design-review` | 4 | 448 | ● | — |
| **total** | **140** | **13,454** | | |

Enabling everything costs ~13.5k tokens of context before a single skill is used. The measured
justification for making most of it opt-in: across ~120 Claude Code startups, `pluginUsage` in
`~/.claude.json` recorded `storefront` invoked **64 times and every other plugin 0**. Carrying
12k tokens for capability that never fires is the wrong default.

`defaultEnabled: false` only sets the state at install time. It does not disable a plugin
someone has already enabled — that is a `settings.json` edit, and deliberately theirs to make.

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

## The cache is not the repository

`~/.claude/plugins/marketplaces/<name>/` is a clone Claude Code manages for you.
Authoring there is the failure mode this repository has actually suffered: the
`figma-import-html-to-sites` skill was committed only into that cache during the
`marketplace` → `claude-marketplace` rename and reached nobody. It was found by
accident weeks later, at which point the cache was 4 commits ahead and 6 behind
its own remote. A commit into a cache succeeds, looks ordinary, and is discarded
the next time the plugin system resets it.

| Path | Role |
|---|---|
| `~/03_agents/claude-marketplace` | Author here |
| `~/07_design/brand/brand-design-marketplace` | Author here — brand |
| `~/.claude/plugins/marketplaces/…` | Managed cache. Consume only. |

Two guards, both installed by the same script:

```bash
python3 scripts/marketplace_doctor.py                  # report, exit 1 on drift
python3 scripts/marketplace_doctor.py --no-fetch       # offline
python3 scripts/marketplace_doctor.py --install-guards # (re)install pre-commit guards
```

**The report** walks every installed cache and prints ahead/behind/dirty. Caches
whose remote is yours are judged — unpushed commits or a dirty tree exits 1.
Third-party caches are reported only; being 900 commits behind is staleness, not
data loss, because you never commit into them. Run it before any release.

**The guard** is a `pre-commit` hook written into the caches you own. It refuses
the commit and names the authoring checkout, which it resolves by matching
remotes. It works in any client — Claude Code, Codex, a plain terminal — because
it lives in git rather than in an agent's configuration.

Reinstalling a marketplace wipes its `.git/hooks`, so re-run `--install-guards`
after adding one. That is also the only step needed for a newly installed
marketplace you own: the doctor finds it automatically.

## Conventions

- Every skill is `plugins/<plugin>/skills/<name>/SKILL.md` with YAML frontmatter whose
  `name` matches its directory.
- **Quote any `description:` containing a colon-space.** Unquoted, YAML reads `Use for X: y`
  as a nested mapping and the whole frontmatter fails to parse — the skill then loads with
  every field silently dropped, so it is never matched. Three files shipped this way before
  `claude plugin validate --strict` caught them.
- Agent frontmatter carries a baseline beyond `name`/`description`/`tools`: `maxTurns`
  (30 read-only, 40 writers) bounds a runaway loop, and read-only agents add
  `disallowedTools: Write, Edit, NotebookEdit`. Judgment-heavy reviewers — `theme-reviewer`,
  `section-architect`, `deliverability-release-reviewer` — also set `effort: high`.
  **`model` is deliberately never set**: an agent inherits the session model, which is right
  unless there is strong reason otherwise, and a pinned tier silently caps quality later.
- **`tools:` is an allow-list, and `Bash` is in it for every "read-only" agent.** Fourteen
  agents describe themselves as read-only and can still write via `Bash` (`>`, `sed -i`,
  `cp`). `disallowedTools` does not close that — it blocks the `Write`/`Edit` tools, not the
  shell. Read "read-only" as convention plus prompt, not as an enforced boundary.
- Three marketplace manifests are kept byte-identical: `.claude-plugin/`,
  `.agents/plugins/`, `.cursor-plugin/`. A plugin registered in only one of them will not
  resolve for the other runtimes. (The `.agents/` mirror goes away with the Codex cut.)
  This drifts silently — `.agents/` was still carrying `"name": "atelier"` two renames later,
  because only the Claude and Cursor pair get diffed. Check all three.
- Removing or renaming a plugin needs a top-level `renames` entry (`"brand": null` for a
  removal, `"old": "new"` for a rename), or existing users hit `plugin-not-found` instead of
  migrating. Treat it as append-only history: never edit an old entry, add another and let
  Claude Code follow the chain. Requires Claude Code v2.1.193+.
- `design-review` consolidates four former stacks. The 2026-08-10 overlap cut took it 15 → 8;
  the 2026-08-18 design-system cut took it 8 → 4. What was removed and why is in
  `plugins/design-review/OVERLAP.md`, and every removed skill is recoverable from git history.
