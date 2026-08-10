---
name: social-media-design-science-audit
description: Audits Instagram, TikTok, Facebook, YouTube, paid social, short-form video, carousels, thumbnails, testimonial/proof assets, and social content systems with science-backed design, color, accessibility, safe-zone, platform-fit, attention, and brand-discipline criteria. Use when reviewing social media design, captions, hooks, overlays, carousels, reels, TikToks, ads, or Hair Solutions Co. social creative. Do not use for posting, scheduling, CRM actions, influencer outreach, or website/email-only audits.
---

# Social Media Design Science Audit

## Workflow

1. Identify the artifact: static post, carousel, Reel, TikTok, Story, Facebook creative, YouTube thumbnail, paid ad, caption, hook, script, testimonial, or platform spec.
2. Classify the audit mode:
   - **Design review**: image, screenshot, Figma/Canva export, thumbnail, or carousel.
   - **Video review**: Reel, TikTok, Story, YouTube Short, hook frame, overlay plan, or script.
   - **Copy review**: caption, headline, hashtags, CTA, or paid ad copy.
   - **System review**: content pillars, grid rhythm, campaign variants, or brand/platform spec.
3. Read references just in time:
   - `references/social-design-science.md` for attention, composition, hooks, accessibility, color, and UX science.
   - `references/platform-tools.md` for Instagram, TikTok, Facebook, YouTube, Meta/TikTok tools, analytics, and testing.
   - `references/hsc-social-platform-gap.md` when working with Hair Solutions Co. social design.
4. For exported image assets or briefs, run:

```bash
python3 scripts/audit_social_asset.py --format instagram-feed-portrait --image post.png --headline "How realistic should a hairline look?" --caption "..." --hashtags "hairreplacement,hairsystem" --cta "Read the guide" --alt-text "Close-up of a realistic hairline"
```

5. Evaluate the core lenses:
   - color science and contrast after platform compression;
   - UI/UX hierarchy, first-glance comprehension, and cognitive load;
   - safe zones and platform UI occlusion;
   - hook clarity and first-frame usefulness;
   - accessibility: captions, alt text, legibility, flashing risk, sound-off comprehension;
   - platform-native behavior: Instagram trust grid, Reels retention, TikTok directness, Facebook clarity, YouTube thumbnail clickability;
   - proof, testimonial, consent, and claims risk;
   - CTA-role fit by funnel stage;
   - brand discipline and repeatable content system fit;
   - measurement plan: saves, shares, retention, profile visits, clicks, CTR, qualified DMs, conversion.
6. Use `color-science-palette-audit` for palette-specific decisions and `website-ux-science-audit` for general hierarchy/composition logic when it transfers to social.
7. Separate measured checks from expert judgment and behavioral evidence. Do not claim performance without real analytics or test data.

## Output Standard

1. Start with a verdict: approve, approve with fixes, or do not approve.
2. Lead with ranked findings:
   - **P0 consent, claim, access, or brand-trust blocker**
   - **P1 platform fit, accessibility, safe-zone, or conversion risk**
   - **P2 hierarchy, hook, caption, CTA, or mobile legibility issue**
   - **P3 polish, rhythm, consistency, or test opportunity**
3. For each finding include: evidence type, affected area, issue, why it matters, exact fix, and verification method.
4. Include a platform-specific checklist: format, dimensions, safe zones, hook, overlay text, caption, CTA, alt/captions, export, and metric to watch.
5. Finish with the next safe action: revise asset, create A/B variant, run safe-zone check, add captions/alt text, verify consent, test in platform preview, or review analytics.

## Guardrails

1. Do not post, schedule, boost, or modify social content/accounts without explicit approval.
2. Do not treat a good-looking asset as platform-ready unless safe zones, legibility, captions/alt text, and claims are checked.
3. Do not recommend shame, fake urgency, miracle claims, medical claims, or unsupported before/after framing.
4. Do not use testimonials, client images, DMs, or before/after assets without verified consent for the exact channel/use.
5. Do not optimize only for thumb-stop if it damages trust, accuracy, or brand positioning.

## Error Handling

1. If only a caption or idea is provided, audit copy/platform fit and name missing visual proof.
2. If only an image is provided, audit dimensions/safe zones/visual hierarchy and name missing caption, alt text, CTA, and consent evidence.
3. If a video cannot be inspected, audit script/hook/overlay plan and request the export for timing, captions, safe zones, and sound-off review.
4. If platform specs or tooling claims matter for publishing, verify current official platform guidance before treating the detail as current.
5. If the request crosses into publishing, paid media launch, audience targeting, or customer data, stop for explicit approval.

## Resources

- `scripts/audit_social_asset.py`: deterministic platform-format and brief audit helper.
- `references/social-design-science.md`: attention, composition, accessibility, hook, and brand-discipline framework.
- `references/platform-tools.md`: current platform and tool guidance.
- `references/hsc-social-platform-gap.md`: findings from the attached Hair Solutions social platform spec.
