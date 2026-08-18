---
name: figma-research-motion
description: Turn approved visual research, web captures, recordings, flows, diagrams, FigJam boards, Slides, and motion into clear, validated Figma artifacts. Use for competitor or owned-page reference capture, UI video storyboards, interaction mapping, FigJam diagrams, Slides, and Figma motion inspection or edits.
---

# Figma Research and Motion

Load `$figma-agent-core` first. Keep research artifacts distinct from production components and implementation truth.

## Reference and video workflow

1. Confirm the source is authorized, its purpose, and the destination file/page. Isolate references from production library pages.
2. For web capture, label the imported frame with source, date, and `Reference`. Describe it as a best-effort reconstruction; validate editable layers and list simplified or rasterized material.
3. For a recording, analyze local frames and key states before touching Figma. Map visible state changes, trigger, annotation, confidence, and omitted transitions; then create a static editable storyboard after the manifest is ready.
4. Preserve source attribution and do not imply research is a production-ready design or that a screenshot proves hidden behavior.

## Use the right Figma surface

- Use FigJam for boards, diagrams, and collaboration. Inspect existing objects with FigJam context, organize with sections, and create connectors only after node positions are stable.
- Use a diagram generator only for supported diagram types. Validate Mermaid/input constraints and use a different representation for unsupported structures.
- Use Slides as a slide grid, not a Design document. Choose either a deck generator or an editable Slides workflow, never both for the same deck.
- For motion, inspect runtime support and existing styles before editing. Add only supported keyframes/styles, verify timeline duration/easing, and provide a reduced-motion fallback.

## Completion

Verify the final board, capture, storyboard, deck, or animation with a fresh screenshot and structural inspection. Report source, destination, editability limits, validation, confidence gaps, and publication state. See [research integrity](references/research-integrity.md).
