---
name: figma-agent-core
description: Operate Figma files safely and precisely through MCP. Use for Figma Design, FigJam, or Slides inspection and mutation; file creation; component, variable, asset, or layout work; and any task that needs the correct Figma execution surface and reliable visual verification.
---

# Figma Agent Core

Use this as the mandatory foundation for a Figma task. Load one specialist skill only after routing the job.

## Route the work

1. Identify the artifact (`design`, `figjam`, or `slides`), target file and node, intended outcome, and whether the action reads, mutates, creates, publishes, or changes sharing.
2. Verify the connected Figma account and the required tool before promising access. Inspect the target with metadata, a screenshot, design context, or FigJam context before a mutation.
3. Select the smallest sufficient execution surface:
   - MCP for an agent-mediated file task.
   - Plugin API for rich write access in one user-present file.
   - REST for unattended cross-file reads or endpoints that explicitly support writes.
   - Widget only for a persistent on-canvas multiplayer object.
4. Route to `$figma-library-engineering`, `$figma-design-delivery`, `$figma-shopify-bridge`, `$figma-integration-engineering`, or `$figma-research-motion`.

## Perform file work safely

- Treat `use_figma` as a file-context execution environment. Inspect first, mutate in small coherent batches, return affected node IDs and meaningful geometry, then verify through metadata and a fresh screenshot.
- Load every font before changing text. Narrow node types before using node-specific properties. Use async lookup and document APIs where available.
- Never use a screenshot as proof that a layout is editable. Validate Layers structure, auto layout, component instances, variables, and bindings when those properties matter.
- Keep Design, FigJam, and Slides rules separate. Do not call `createPage()` in FigJam or Slides. Use FigJam context to discover node IDs; use slide-grid APIs and read-only scripts to validate Slides.
- Before a new file, resolve the available plan and editor type. Create only the requested Design, FigJam, or Slides file, then report its URL and file key.
- For design-to-code, call design context on the exact target node before writing implementation. Do not substitute a screenshot for its measurements, assets, or structure.

## Safety and completion

- Treat planning, audit, critique, and handoff requests as read-only unless the user explicitly asks for an implementation or Figma edit.
- Do not publish libraries or Sites, alter file sharing, delete or bulk-move nodes, or overwrite production components without explicit approval.
- Distinguish a reference capture from native editable Figma work. Label captures with source, date, and `Reference` status.
- Report the file/node affected, what changed, direct validation evidence, and publication/sharing state. See [tool contract](references/tool-contract.md).
