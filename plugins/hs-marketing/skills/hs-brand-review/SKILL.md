---
name: hs-brand-review
description: Strict, evidence-backed brand review for Hair Solutions Co. against the live Atelier Zero v7 authority — web pages, Shopify surfaces, HTML/HubSpot emails, social assets and series. Verifies canonical sources (never cached brand values), applies the 10-category compliance matrix, flags claims/consent/legal issues, and reports BLOCKER/MAJOR/MINOR findings with a COMPLIANT/CONDITIONAL/NON-COMPLIANT verdict. Audit-only by default; never publishes or edits production. Not for drafting new copy (hs-content-creation).
---

# Hair Solutions Co. Brand Review (Atelier Zero v7)

> **Merged from:** `brand-review` (Anthropic base) + `atelier-zero-brand-compliance`, `atelier-zero-design-system` (Hair Solutions legacy)

Review marketing content and customer-facing artifacts against the Hair Solutions Co. brand authority — Atelier Zero v7. Act as an independent brand guardian. Inspect the artifact that actually exists. Do not infer compliance from a brief, mock description, or clean build result.

## Trigger

User asks to review, check, or audit content against brand guidelines — a web page, Shopify surface, HTML or HubSpot email marketing template, social post, carousel, Story, Reel cover, thumbnail, or complete branded social series — before shipping, publishing, sending, scheduling, or approving customer-facing work, or whenever the user asks whether an artifact is on-brand.

## Default Boundary

- Audit only unless the user explicitly asks for fixes.
- Do not publish, deploy, send, schedule, approve consent, or mutate production.
- Do not generate missing brand imagery or substitute stock photography.
- Never downgrade a missing evidence requirement to a pass.

## Inputs

1. **Content to review** — accept content in any of these forms:
   - Pasted directly into the conversation
   - A file path or knowledge base reference (e.g. Notion page, shared doc)
   - A URL to a published page
   - Source (HTML/HubL/Liquid), rendered output, or a screenshot
   - Multiple pieces for batch review
2. **Brand guidelines source** — always the live Atelier Zero v7 authority (below). Do not ask the user to paste a style guide, do not review against memory, and never use cached brand values. Current filesystem evidence outranks copied guides, project-local tokens, screenshots, and memory.

## Open the Authority Gate

1. Read the adjacent `atelier-zero-design-system` skill (its operative rules are mirrored in the Quick Reference below — the live repository remains the authority).
2. Run its `scripts/check_sources.py`.
3. Read:
   - `/Users/vMac/08_brand/brand-design-system/PROJECT.md`
   - `/Users/vMac/08_brand/brand-design-system/AGENTS.md`
   - the relevant section of `brand-design-system.html`
   - `/Users/vMac/08_brand/atelier-zero-design-system-from-theme.md` for visual judgments
   - the canonical repository `SKILL.md`
   - the task-relevant tokens, component, composition, decision, voice, audience, and platform specifications
4. Inspect the destination project's instructions and the real artifact.

Stop if canonical verification fails. Report source drift as a blocker instead of auditing against uncertain rules.

**Authority resolution:**

- The masterfile defines Hair Solutions Co. intent, identity, audience, voice, safety, and governance.
- The measured theme source controls visual palette, geometry, signature motifs, interaction posture, and responsive reconstruction.
- Do not transfer its original technical-product copy, product names, coordinates, or licensing language.
- Production accessibility overrides low-contrast reference decoration: use Text Ink on Coral controls and readable Ink for essential metadata.
- Operate from the live system at `/Users/vMac/08_brand/brand-design-system`. Use `/Users/vMac/08_brand/logos` as the only approved logo directory.

**Portable sources to load (only what the task needs):**

- tokens and web reference: `tokens/` and `styles/atelier-zero.css`
- components and layouts: `specs/COMPONENT_CONTRACTS.md`, `COMPOSITION_RULES.md`, `DECISION_TREES.md`
- voice and audience: `specs/brand_voice.md`, `CUSTOMER_AVATARS.md`, `COMPETITORS.md`
- channel: `specs/PLATFORM_SHOPIFY.md`, `PLATFORM_EMAIL.md`, or `PLATFORM_SOCIAL.md`

## Classify the Target

- **Web:** URL, local HTML, screenshot, component, Shopify section/template, or page family.
- **Email:** rendered email, source HTML/HubL, HubSpot module/template, preview, or screenshot.
- **Social:** individual asset, carousel, Story set, Reel/TikTok cover, video frame sequence, caption set, thumbnail, or campaign series.
- **Mixed:** audit each channel independently, then add cross-channel consistency findings.

Load only the matching reference (shipped with the compliance skill):

- Web: `references/web-audit.md`
- Email: `references/email-audit.md`
- Social: `references/social-audit.md`

Always load `references/report-contract.md`.

Within a channel, classify the implementation subtype before applying checks. Mark genuinely irrelevant requirements `N/A` with a short reason — for example, Shopify schema and cart logic are `N/A` for a standalone static web page. Do not use `N/A` for evidence that should exist but was not inspected; that is `NOT VERIFIED`.

## Inspect Evidence

Use every supplied form of evidence:

- inspect source for literal colors, tokens, fonts, structure, semantics, alt text, motion, and hidden states
- inspect rendered output at the required dimensions
- inspect copy, claims, product facts, CTA posture, and consent dependencies
- inspect the full series or page sequence when adjacency and rhythm matter
- verify changing facts against the live owner when access is available
- record inaccessible requirements as `NOT VERIFIED`, not `PASS`

For screenshots without source, audit what is visible and explicitly list source-only checks that remain unverified. For source without rendering, audit implementation evidence and explicitly list visual checks that remain unverified.

## Apply the Compliance Matrix

Evaluate every applicable category:

1. authority and source provenance
2. logo and font provenance
3. palette, contrast, and Coral discipline
4. typography roles and hierarchy
5. spacing, container, grid, radii, surfaces, and elevation
6. components, states, focus, motion, and responsive behavior
7. imagery truth, consent, and artwork restrictions
8. voice, dignity, claims, and changing business facts
9. platform-specific structure and compliance
10. final rendering, accessibility, and operational readiness

Do not equate structural validity, successful builds, or platform acceptance with brand compliance.

Within the copy-facing categories, evaluate these dimensions:

**Voice and Tone**

- Does the content match the defined brand voice attributes?
- Is the tone appropriate for the content type and audience?
- Are there shifts in voice that feel inconsistent?
- Flag specific sentences or phrases that deviate, with an explanation of why.

**Terminology and Language**

- Are preferred brand terms used correctly?
- Are any "avoid" terms or phrases present?
- Is jargon level appropriate for the target audience?
- Are product names, feature names, and branded terms used correctly (capitalization, formatting)?

**Messaging Pillars**

- Does the content align with defined messaging pillars or value propositions?
- Are claims consistent with approved messaging?
- Is the content reinforcing or contradicting brand positioning?

**Style Guide Compliance**

- Grammar and punctuation per style guide (Oxford comma, title vs. sentence case)
- Formatting conventions (headers, lists, emphasis)
- Number formatting, date formatting
- Acronym usage (defined on first use?)

## Legal and Compliance Flags (Always Checked)

Regardless of channel, flag:

- **Unsubstantiated claims** — superlatives ("best", "fastest", "only") without evidence or qualification
- **Missing disclaimers** — financial claims, health claims, or guarantees that may need legal disclaimers
- **Comparative claims** — comparisons to competitors that could be challenged
- **Regulatory language** — content that may need compliance review
- **Testimonial issues** — quotes or endorsements without attribution or disclosure; for Hair Solutions Co., exact-use consent is required for customer media, testimonials, DMs, voice, and before/after assets
- **Copyright concerns** — content that appears to be closely paraphrased from other sources

## Atelier Zero v7 Quick Reference

Mirror of the design-system skill's operative rules. Re-verify against the live repository at audit time; never audit from this summary alone if `check_sources.py` fails.

### Palette and surfaces

- Paper `#EFE7D2` is the grain-bearing canvas. Paper Warm `#ECE4CF` is the alternate warm surface, Paper Dark `#DDD2B6` the secondary and commerce surface, and Bone `#F7F1DE` the raised card surface.
- Ink `#15140F` owns headings, controls and the dark-section surface. Ink Soft `#2A2620` is secondary dark and strong border; Ink Mute `#5A5448` is muted but readable text; Ink Faint `#8B8676` is decorative numerals and nonessential marks only.
- Coral `#ED6F5C` is the primary action and the only saturated UI color, staying under roughly 10% of a composition. Coral Soft `#F08E7C` is one emphasis on dark surfaces.
- Olive `#6E7448` is utility and success. Mustard `#E9B94A` is focus reinforcement and caution only, never decorative.
- Do not introduce gradients, glass effects, pure-white cards, arbitrary status colors, or undocumented aliases.

### Type

- Inter Tight: H1–H4, navigation, labels, buttons, and UI.
- Inter: body, leads, forms, and functional copy.
- Playfair Display italic: one short inline phrase inside H1 or H2 only.
- JetBrains Mono: 13px metadata, dates, SKUs, specs, and compact evidence.
- Scale: display/H1 up to 70px; H2 32px; H3 32px; H4 22px; body 18px; small 14px; micro/eyebrow 11px.
- End display headlines with one Coral terminal period.

### Geometry and composition

- Use the spacing ladder 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px.
- Use a 1300px maximum container, responsive 20–64px side padding, and a 24px gutter.
- Use 96px desktop and 72px mobile section rhythm.
- Radius roles: 4px forms/gallery plates, 8px stage/nested surfaces, 16px cards/major media/Ink panels, 999px actions and pills.
- Use the 37px inset frame and 11px micro-cap rails only on suitable desktop editorial surfaces at 1024px and above.
- Start with one hero. Left-align content leading to grids, lists, media, or tables. Center only a single statement, pull quote, focused CTA band, or simple hero.
- Never stack full-width dark sections.

### Components and interaction

- Primary: 56px Coral pill, Text Ink label, no border, shadow, lift, or scale.
- Secondary: transparent pill, Text Ink label, 1px Hairline border.
- Keep one primary action per decision area.
- Light cards use Raised, 16px radius, no border, and no shadow.
- Wash cards inside Ink Panel may rotate up to ±2° and use the one approved true shadow.
- Forms need persistent labels, 4px radius, at least 44px height, clear errors, and visible focus.
- Focus: 2px Coral on light, 2px Wash inside Ink Panel, both with 2px offset.
- Hover may change color/border, invert a nested arrow, or scale a clipped image up to 1.03. Never lift cards or buttons.
- Use 180ms color/border transitions and at most 420ms movement. Respect reduced motion.
- Preserve semantic headings, keyboard order, touch targets, alt text, stable media dimensions, and non-color state meaning.

### Signature devices

Use selectively: Coral folio and terminal period, route/status micro-caps, inset frame and rails, asymmetric hero, 2×2 capability cards, four-up method row, five-up editorial plates, two-up testimonials, Coral sequence numerals, one active Coral filter/progress mark, square registered plates, dotted-circle annotation, and dashed footer progress rule.

## Protect Assets, Truth, and Dignity

- Use only logos from `/Users/vMac/08_brand/logos`; verify filenames and hashes against `manifests/logos.json`.
- Use only the four font binaries in `manifests/fonts.json`.
- Use approved photography or owner-approved commissioned artwork. Never generate brand imagery or use stock photography.
- Preserve identity, skin, hair, hairline, base construction, density, color, texture, scale, and truthful results.
- Require exact-use consent for customer media, testimonials, DMs, voice, and before/after assets.
- Speak as "we" to "you" with calm, specific, adult language.
- Never use pity, shame, rescue, urgency, scarcity, hype, emoji, exclamation marks, medical framing, guarantees, or invented facts.
- Verify changing commerce and policy facts from their live owner.
- A compliant draft is not permission to publish, send, schedule, deploy, or modify production.

## Route by Channel

- **Web and Shopify:** preserve editor behavior, dynamic sources, SEO, accessibility, mobile behavior, and commerce logic. Do not use Shopify CLI or publish without approval.
- **Email:** follow the inbox-specific literal-hex, table, inline-style, safe-font, fallback, image-blocked, plain-text, and compliance rules.
- **Social:** keep one idea per asset; choose product, person, or message; protect safe zones, grid rhythm, compression legibility, consent, captions, and alt text.
- **Documents and prototypes:** translate the system without importing a generic template aesthetic; label non-production placeholders.

## Severity

- **BLOCKER:** unapproved logo/media, fabricated or unsupported claim, missing required consent, unreadable critical content, broken primary task, absent legal email content, canonical-source failure, or customer harm/trust risk.
- **MAJOR:** clear token/type/layout/component/platform violation that materially changes the brand, accessibility, comprehension, or conversion flow.
- **MINOR:** localized deviation with limited customer impact and a straightforward correction.
- **NOTE:** improvement or observation that is not a brand-rule violation.

## Verdict

- `COMPLIANT` — no blockers or majors, all release-critical evidence verified, only optional notes remain.
- `CONDITIONAL` — no blocker is proven, but one or more required checks are not verified or minor fixes remain.
- `NON-COMPLIANT` — any blocker or major violation exists.

Never issue `COMPLIANT` when source, rendering, consent, live facts, or required platform states are unavailable.

## Report

Follow `references/report-contract.md` exactly. Lead with the verdict, then evidence. Give each finding:

- severity and stable ID
- channel and location
- observed evidence
- governing source and rule
- customer/brand impact
- exact remediation
- verification needed after remediation

## After the Audit

When asked to fix after the audit:

- Preserve the report as the baseline, change only approved scope, and rerun every failed and release-critical check.
- Make the smallest compliant change only when the user asks for implementation.
- **Completion gate:** run the canonical verifier, inspect the real output at relevant sizes and states, confirm logo/font provenance, verify live claims, check accessibility/consent/truthful media, separate violations from unavailable evidence, and state every remaining production approval.

## Brand Voice Documentation Reference

Generic frameworks for documenting or extending brand voice. Where anything below conflicts with the Atelier Zero rules above (emoji, exclamation marks, urgency, guarantees), **Atelier Zero wins**.

### Brand Voice Documentation Framework

1. **Brand Personality** — define the brand as if it were a person.
2. **Voice Attributes** — 3–5 attributes, each defined with what it means in practice, what it does NOT mean, and an example.
3. **Audience Awareness** — who the brand speaks to, what they care about, their expertise, how they expect to be addressed.
4. **Core Messaging Pillars** — 3–5 themes, their hierarchy, and how each connects to audience needs.
5. **Tone Spectrum** — how voice adapts across contexts while staying recognizably the same brand.
6. **Style Rules** — specific grammar, formatting, and language rules.
7. **Terminology** — preferred and avoided terms.

### Voice Attribute Spectrums

| Spectrum | One End | Other End |
| --- | --- | --- |
| Formality | Formal, institutional | Casual, conversational |
| Authority | Expert, authoritative | Peer-level, collaborative |
| Emotion | Warm, empathetic | Direct, matter-of-fact |
| Complexity | Technical, precise | Simple, accessible |
| Energy | Bold, energetic | Calm, measured |
| Humor | Playful, witty | Serious, earnest |
| Innovation | Cutting-edge, forward-looking | Established, proven |

For each chosen attribute, document it in this format:

**[Attribute name]**

- **We are**: [what this means in practice]
- **We are not**: [common misinterpretation to avoid]
- **This sounds like**: [example sentence demonstrating the attribute]
- **This does NOT sound like**: [example sentence violating the attribute]

### Tone Adaptation Across Channels

| Channel | Tone Adaptation |
| --- | --- |
| Blog | Informative, conversational, educational |
| LinkedIn | Professional, thought-provoking, concise |
| Twitter/X | Punchy, direct, sometimes witty |
| Email marketing | Personal, helpful, action-oriented |
| Sales collateral | Confident, benefit-driven, specific |
| Support/Help docs | Clear, patient, step-by-step |
| Press release | Formal, factual, newsworthy |
| Error messages | Empathetic, helpful, blame-free |

### Tone by Situation

| Situation | Tone Adaptation |
| --- | --- |
| Product launch | Excited, confident, forward-looking |
| Incident or outage | Transparent, empathetic, accountable |
| Customer success story | Celebratory, specific, crediting the customer |
| Thought leadership | Authoritative, nuanced, evidence-based |
| Onboarding | Welcoming, encouraging, clear |
| Bad news (price increase, deprecation) | Honest, respectful, solution-oriented |
| Competitive comparison | Confident but fair, fact-based, not disparaging |

**Tone adaptation rule:** voice attributes remain fixed. Tone dials them up or down based on context. Neither attribute disappears; the balance shifts.

### Style Guide Enforcement

| Rule | Options | Example |
| --- | --- | --- |
| Oxford comma | Yes / No | "fast, reliable, and secure" vs. "fast, reliable and secure" |
| Sentence vs. title case | Sentence / Title | "How to get started" vs. "How to Get Started" |
| Contractions | Use / Avoid | "we're" vs. "we are" |
| Em dash spacing | No spaces / Spaces | "this—and more" vs. "this — and more" |
| Numbers | Spell out 1–9 / Always numerals | "five features" vs. "5 features" |
| Percent | % / percent | "50%" vs. "50 percent" |
| Date format | Month DD, YYYY | "January 15, 2025" |
| Time format | 12-hour / 24-hour | "3:00 PM" vs. "15:00" |
| Lists | Periods / No periods on fragments | "Set up your account." vs. "Set up your account" |

**Punctuation and emphasis** — exclamation marks and emoji: Atelier Zero rule is never, in any Hair Solutions Co. brand communication. Avoid ellipsis in professional contexts. Avoid ALL CAPS; use bold for emphasis.

### Terminology Management

| Use This | Not This | Notes |
| --- | --- | --- |
| sign up (verb) | signup (verb) | "signup" is the noun form |
| log in (verb) | login (verb) | "login" is the noun/adjective form |
| set up (verb) | setup (verb) | "setup" is the noun/adjective form |
| email | e-mail | No hyphen |
| website | web site | One word |

**Inclusive language** — gender-neutral (they/them for unknown individuals); avoid ableist language ("crazy", "blind spot", "lame"); person-first where appropriate; avoid culturally specific idioms; prefer "simple" or "straightforward" over "easy".

**Jargon management** — define which technical terms the audience knows, which must be replaced with plain language, and which acronyms need spelling out on first use.

**Competitor and category terms** — how to refer to your category, how to refer to competitors, terms competitors coined that you should avoid, and your preferred differentiation language.
