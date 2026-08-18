# HTML conversion adapters

Use the adapter matching the input. Every adapter must produce one standalone `.html` file as its only primary deliverable.

## Website, React, JSX, and static-page inputs

- Inspect the source framework and rendered page, then reproduce the visible artifact in semantic HTML, embedded CSS, and browser-native JavaScript.
- Preserve page structure, responsive hierarchy, content, links, controls, and meaningful interactions.
- Do not output React, JSX, TSX, component files, a stylesheet, or a JavaScript bundle.
- Define current Atelier Zero tokens once in the HTML's `<style>` block and use variables throughout the conversion.
- Make the standalone preview work when opened directly in a browser without a build step.

## Shopify and Liquid inputs

- Inspect Liquid, section schemas, product objects, dynamic sources, metafields, localization, and app blocks only to understand the intended visible states.
- Recreate those states as safe static or simulated HTML using representative source content. Label simulated cart, variant, account, personalization, or checkout behavior.
- Do not output Liquid or edit the live theme as part of this skill.
- Do not use publication actions or preview-theme surfaces as part of this skill. (`shopify theme dev` and `theme check` are permitted in the storefront repo generally — Vincent's ruling, 2026-08-17 — they are just not part of this conversion workflow, which outputs static HTML.)
- Preserve the composition and commerce hierarchy without claiming the HTML preview is production-connected.

## Email and HubSpot inputs

- Produce one complete, browser-viewable `.html` email using the current email platform spec.
- Keep the inbox-safe table structure, 600px wrapper, inline critical styles, approved literal colors, safe font fallbacks, mobile behavior, and image-blocked readability.
- Represent personalization with safe fallback content. Preserve required unsubscribe, sender, postal-address, and preference text visibly when present.
- Do not output MJML, HubL, module JSON, or a live HubSpot asset.
- Do not send, publish, activate, or mutate anything in HubSpot.

## Social graphics, carousels, stories, and video covers

- Create each post, carousel slide, story, reel cover, or video frame as an exact-size HTML artboard.
- Put every related artboard into the same HTML document with clear navigation or a vertical sequence.
- Preserve the requested platform, message, sequence, subject, crop, safe zones, and consent constraints.
- Use responsive preview framing without changing the artboard's actual target dimensions.
- Do not output PNG, video, Canva, Figma, or another design-tool file. The HTML artboards are the conversion.

## Presentation, PDF, and document inputs

- Recreate slides or pages as fixed-ratio HTML sections inside one document.
- Preserve order, hierarchy, text, charts, tables, links, notes that affect meaning, and reading flow.
- Provide keyboard or button navigation when it materially helps viewing.
- Do not output PPTX, PDF, DOCX, or separate page files.
- Render the complete HTML at desktop and a narrower viewport and correct overflow or unreadable scaling.

## Image and screenshot inputs

- Inspect the source at full resolution and recreate its layout as HTML/CSS.
- Reuse approved imagery through valid `<img>` references or embedded data where appropriate; rebuild text, branding, rules, shapes, and layout natively in HTML.
- Preserve dimensions, subject, crop, and factual content unless the user requests otherwise.
- Do not return an edited raster or image-only approximation as the conversion.
- If a photographic or illustrative pixel-level transformation cannot be expressed faithfully in HTML, keep the source image as a visual layer and explicitly identify that limitation.

## Text-only post inputs

- Turn the post into a viewable Atelier Zero HTML composition rather than returning revised text alone.
- Preserve the original message, facts, links, and call to action unless a narrow voice or claims-safety correction is required.
- Choose the current platform's default canvas and safe-zone rules when the user identifies a channel; otherwise use a responsive editorial card within the HTML preview.

## Multi-format inputs

- Place all converted formats in one HTML file only when they belong to the same conversion request.
- Use labeled sections or an unobtrusive preview switcher so each format can be seen at its intended proportions.
- Do not create one native file per source format.
