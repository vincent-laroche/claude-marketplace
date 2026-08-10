---
name: atelier-zero-converter
description: Convert an existing page, template, component, Shopify section, email, social graphic, presentation, document, image, or other designed artifact into one standalone, browser-viewable Hair Solutions Co. Atelier Zero HTML file while preserving as much source structure, content, functionality, and responsive behavior as possible. Always output HTML and HTML only; non-HTML artifacts may be inspected as inputs but must never be the final deliverable. Use when asked to apply Atelier Zero, rebrand or reskin an existing artifact, translate a reference design into Hair Solutions Co. branding, replace another visual identity, migrate legacy Hair Solutions styling, or complete a partial Atelier Zero conversion.
---

# Atelier Zero Converter

Convert the artifact rather than redesigning it. Preserve what makes the source useful; replace what makes it belong to another visual identity.

## Enforce the HTML-only output contract

Produce exactly one primary deliverable: a complete `.html` file that the user can open and see in a browser.

This requirement is absolute:

- Write the conversion to disk as a real `.html` file. Do not return only advice, a design spec, source fragments, or a pasted code block.
- Make HTML the final format even when the input is Liquid, JSX, React, email, PDF, slide deck, document, image, social post, screenshot, or video reference.
- Do not deliver JSX, TSX, Liquid, MJML, JSON, CSS, JavaScript, PDF, PNG, SVG, Figma, Canva, DOCX, PPTX, or another native format instead of the HTML.
- Put all conversion CSS inside the HTML in `<style>` blocks. Put any required behavior inside the same HTML in `<script>` blocks using browser-native JavaScript.
- Do not generate required companion CSS or JavaScript files. Reference authorized existing image or font assets from the HTML, or embed them when portability requires it.
- Use a full document structure: `<!doctype html>`, `<html>`, `<head>`, responsive viewport metadata, `<body>`, and a descriptive `<title>`.
- If no output path is specified, create `atelier-zero-conversions/<descriptive-name>.html` inside the current safe project. Never overwrite the source artifact unless explicitly requested.
- If no writable location exists, stop and request one. Do not degrade to prose or a non-viewable mock.

The HTML is a faithful visual conversion and interactive preview. It is not a production Shopify, HubSpot, social-platform, document, or image-format mutation unless the user separately requests implementation.

Before completion, open the HTML in a browser, inspect it at the intended size and at a relevant responsive size, correct visible problems, and return a clickable absolute file link. A screenshot may be supplied as verification, but it is not the conversion deliverable.

## Establish authority

1. Read the target project's instruction and status files before editing.
2. Read [source-map.md](references/source-map.md) and load the current Atelier Zero sources it routes to. Never trust brand values remembered from this skill, another installed skill, an older Hair Solutions system, or the target artifact.
3. Read the platform spec for the input surface so the HTML representation preserves the correct dimensions, conventions, and content constraints.
4. Treat screenshots as visual evidence and editable source as implementation truth. If only a screenshot exists, state which behavior, responsive rules, and hidden states cannot be inferred.

Stop if the canonical brand repository is unavailable and the task requires exact brand output. Do not invent substitute colors, fonts, logos, tokens, or rules.

## Use faithful conversion by default

### Preserve

- Information architecture, section order, hierarchy, content intent, and recognizable composition.
- Visible behavior, links, forms, navigation, states, and interactions that can be represented safely in browser-native HTML.
- Responsive behavior, accessibility semantics, focus order, alt text, and reduced-motion support.
- Useful proportions, image crops, data presentation, and claims-safe copy.

### Replace completely

- Every non-Atelier color, color variable, theme scheme, and contrast pairing.
- Every non-approved typeface, weight role, fallback choice, and typographic treatment.
- Logos, marks, favicons, badges, and branded image assets from the source identity.
- CTA colors and shapes, radii, borders, shadows, gradients, textures, icon style, and decorative motifs that conflict with Atelier Zero.
- Legacy Hair Solutions systems, including old palette aliases and retired font treatments.
- Hype, pity, urgency, clinical framing, emoji, exclamation marks, title-case marketing headlines, and unverified claims.

### Adapt only when required

- Spacing, alignment, density, and component grouping: preserve the source rhythm when possible, but change it where current Atelier Zero or browser legibility requires it.
- Copy: preserve meaning and factual claims; change wording only enough to satisfy current voice and safety rules. Never invent a claim.
- Imagery: preserve subject and crop when suitable; change treatment or replace an asset only when it conflicts with current imagery rules or contains another brand identity.
- Backend-only behavior, personalization, platform bindings, and dynamic data: represent their visible states honestly in HTML without pretending the standalone file is connected to the live system.

Do not perform a superficial recolor. A conversion is incomplete while foreign fonts, colors, logo treatments, component shapes, effects, or voice residue remain.

## Inspect before creating the HTML

Inventory:

1. Input type and intended viewing dimensions.
2. Page/module/slide/post structure and responsive variants.
3. Visible colors, variables, theme schemes, and contrast pairs.
4. Font imports, family declarations, weights, sizes, line heights, tracking, and roles.
5. Logos, icons, imagery, illustration, and decorative treatments.
6. Buttons, inputs, cards, navigation, notices, badges, tables, and interactive states.
7. Spacing, grid, alignment, radii, borders, elevation, texture, and motion.
8. Copy casing, tone, claims, calls to action, legal text, and dynamic placeholders.
9. Behavior that must be recreated, simulated, or clearly labeled as unavailable in standalone HTML.

Classify each item as `preserve`, `replace`, `adapt`, or `blocked`. Resolve high-risk items before styling details.

Run the read-only scanner before and after conversion when source files are available:

```bash
python3 /Users/vMac/.claude/skills/atelier-zero-converter/scripts/audit_residue.py <target> --surface web
```

Use `--surface email` for email inputs and `--surface social` for text-based social design specs. Treat findings as inspection leads, not permission for bulk replacement.

## Build the standalone HTML

Read [surface-adapters.md](references/surface-adapters.md) and apply the relevant input adapter. Every adapter ends in the same output: one `.html` file.

- Define the currently approved Atelier Zero tokens once near the top of the embedded `<style>` block. Use variables everywhere else in the document.
- Use semantic HTML and responsive CSS. Use vanilla JavaScript only when the source has meaningful interactions that must remain visible or demonstrable.
- Recreate multiple slides, pages, carousel frames, or document pages as clearly separated HTML artboards inside the single document.
- Provide an unobtrusive HTML preview shell when needed for switching viewport, slide, state, or theme; keep it visually separate from the converted artifact.
- Keep remote or local asset references valid. Add meaningful alt text and explicit dimensions or aspect ratios.
- Label simulated dynamic values or unavailable platform behavior honestly. Never imply the preview is connected to Shopify, HubSpot, a CMS, or customer data.

## Verify the HTML conversion

1. Validate the deliverable contract:

   ```bash
   python3 /Users/vMac/.claude/skills/atelier-zero-converter/scripts/validate_html_output.py <converted-file.html>
   ```

2. Confirm the only primary deliverable has a `.html` extension and contains a complete document.
3. Confirm CSS and required JavaScript are contained in that HTML file.
4. Re-run the residue scanner against the HTML.
5. Search for source-brand font names, colors, logos, retired Hair Solutions values, arbitrary gradients, and undocumented shadows.
6. Open the HTML in a browser and inspect the rendered result, not just its source.
7. Compare it with the input at the same intended dimensions and at a relevant responsive size.
8. Test keyboard focus, links, controls, reduced motion, image alt text, and content without images.
9. Check contrast and current brand compliance against the live sources and relevant platform spec.
10. Confirm no live platform, production code, customer data, or published asset was changed.

The conversion passes only when the original remains recognizably useful, the foreign identity is gone, the HTML renders correctly, and the user can open the file directly.

## Report the result

Return the absolute clickable path to the `.html` file first. Then state briefly:

- What structure and behavior were preserved.
- What brand layers were replaced.
- What behavior is simulated rather than live.
- Which browser sizes and checks passed.
- Any blocked or unverified assets or states.

Never call prose, a plan, source fragments, a native-format file, or an unrendered HTML file a completed conversion.
