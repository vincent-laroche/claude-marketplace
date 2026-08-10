---
name: hs-create-asset
description: Generate tailored Hair Solutions sales assets — treatment guides, product comparison pages, before/after case studies, pricing one-pagers, and consultation landing pages. All assets must comply with Atelier Zero v7 brand rules. Use for "create a one-pager", "build a treatment guide", "write a case study", or "make a pricing page".
---

# HS Create Asset

Merged from: `create-an-asset` (Anthropic base) + `atelier-zero-design-system` (HS)

## Trigger

User needs a sales or marketing asset to share with a prospect, existing client, partner, or internal team.

## Asset Types

| Asset | Best for |
| --- | --- |
| Treatment guide | Explaining a service before booking |
| Product comparison page | Helping a client choose between options |
| Before/after case study | Social proof for a specific treatment |
| Pricing one-pager | Transparent pricing for consultations |
| Consultation landing page | Ad or email CTA destination |
| Partnership deck outline | B2B or influencer outreach |

## Production Sequence

1. **Define the audience and goal**: who receives this, what action should they take, and what objection does this overcome?
2. **Gather source material**: approved product/treatment facts, real client results (with consent), current pricing from the live storefront, Atelier Zero brand assets.
3. **Draft structure**: headline → key benefit → proof → CTA. One primary action per asset.
4. **Apply brand rules**: route to `hs-brand-review` for any customer-facing output before delivery. Key rules: Atelier Zero v7 palette, Inter Tight headings, Coral terminal period, no hype/urgency/emoji/exclamation.
5. **Output format**: for HTML deliverables use `atelier-zero-converter`. For copy-only assets, deliver as structured markdown.

## Guardrails

- Verify all claims against live product pages and current pricing before including them.
- Do not invent before/after results or client quotes. Use only consented, documented sources.
- Do not publish, post, or send any asset — deliver drafts for approval.
- Route all customer-facing assets through `hs-brand-review` before delivery.
