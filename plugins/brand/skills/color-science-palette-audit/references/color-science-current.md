# Current Color Science Guidance

Use this reference when making claims about modern web color, palette compatibility, accessibility, or CSS color-token work.

## Standards Posture

- CSS Color Module Level 4 defines modern CSS color spaces and functions, including `lab()`, `lch()`, `oklab()`, `oklch()`, and wide-gamut `color()` workflows. Use these as the practical web-native model for perceptual palette reasoning.
- CSS Color Module Level 5 extends authoring workflows with features such as `color-mix()` and relative color syntax. These are useful for systematic tints, shades, and derived tokens, but production support must be checked for the target browser baseline before relying on them.
- WCAG 2.x contrast ratio remains the stable compliance floor for text contrast. Use 4.5:1 for normal text and 3:1 for large text or essential graphical UI boundaries.
- WCAG 3 and APCA-style contrast are promising for perceptual readability, polarity, and context, but WCAG 3 remains under development. Treat APCA as supplemental unless the user specifically asks for APCA analysis.

## Contrast

Measure every text/background candidate pair. Report:

- normal text pass/fail at 4.5:1;
- large text pass/fail at 3:1;
- low-contrast pairs that may still work for large surfaces, borders, or decorative fills;
- polarity concerns, especially muted text on tinted surfaces.

Avoid declaring a whole palette accessible; only pairings and usage contexts are accessible.

## Perceptual Distance

Use OKLab or OKLCH for palette distance because sRGB hex distance is visually misleading. As a practical heuristic:

- very small OKLab distance means likely duplicate or hard-to-distinguish colors;
- moderate distance is useful for adjacent UI roles such as surface, border, and muted fill;
- large distance is useful for text/surface contrast or primary accent separation;
- extreme jumps can feel harsh unless they map to a clear semantic role.

Distance does not prove harmony. It only describes separability.

## Temperature And Harmony

Use hue, chroma, and lightness together:

- warm palettes tend to cluster around red, orange, yellow, brown, cream, and clay families;
- cool palettes tend to cluster around blue, green, cyan, violet, and slate families;
- neutrals should have low chroma and stable lightness steps;
- accents should have clearly higher chroma or semantic purpose;
- too many mid-chroma hues with similar prominence creates brand noise.

For warm-neutral luxury/editorial brands, favor broad lightness contrast, restrained chroma, and one controlled accent family.

## Role Fit

Assign roles by measured properties before subjective naming:

- darkest low-chroma color: ink, heading, body text, icon, or high-emphasis border;
- lightest low-chroma color: page background, paper, card, or surface;
- low-contrast mid-light neutral: border, divider, disabled, muted fill;
- saturated warm hue: accent, CTA, highlight, warning-like emphasis only if semantics match;
- saturated cool hue: link, info, success, or utility state when it does not conflict with brand tone.

Do not assign a color to text until its intended background pair passes contrast.

## Accessibility

Minimum accessibility review:

- WCAG contrast ratios for text/background pairs;
- non-text UI boundary checks at 3:1 where boundaries convey state;
- avoid relying only on hue for state or status;
- check near-duplicate colors for color-blind and low-vision ambiguity;
- avoid very low chroma text on tinted surfaces when the contrast margin is narrow.

APCA can be used as an extra readability warning when available, especially for polarity and light/dark context, but it does not replace WCAG 2.x compliance.

## Brand Discipline

Judge whether the palette can become a small design system:

- every color should have a named role or be removed;
- reserve accent colors for repeatable intent, not decoration;
- normalize token names around usage, not appearance alone;
- avoid adding separate hex values for tiny visual differences;
- use derived tints/shades only when they can be regenerated from known base tokens;
- for hex-only brand documentation, keep public-facing values as uppercase hex even if analysis uses OKLCH internally.

## Useful Current Sources

- W3C CSS Color Module Level 4: https://www.w3.org/TR/css-color-4/
- W3C CSS Color Module Level 5: https://www.w3.org/TR/css-color-5/
- W3C WCAG 2.2 contrast criteria: https://www.w3.org/TR/WCAG22/#contrast-minimum
- W3C WCAG 3 draft: https://www.w3.org/TR/wcag-3.0/
- APCA documentation: https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell
- Color.js documentation: https://colorjs.io/docs/
