---
name: hs-competitive-intelligence
description: Research hair industry competitors and produce an interactive battlecard. Covers local salons, online hair product brands, DTC competitors, and treatment alternatives. Use for "competitive intel", "how do we compare to [competitor]", "battlecard for [brand]", or "what's new with [competitor]".
---

# HS Competitive Intelligence

Merged from: `competitive-intelligence` (Anthropic base)

## Trigger

User wants to understand how Hair Solutions Co. compares to a competitor, prepare a positioning argument for a client, or build a battlecard.

## Inputs

- Competitor name(s) or "all key competitors"
- Focus area: pricing, treatments, products, brand positioning, online presence, DTC/e-commerce, or all

## Research Sequence

1. **Identify competitor type**: local salon, national chain, DTC hair product brand, professional distributor, or treatment franchise.
2. **Web and social research**: website, Instagram, TikTok, Google reviews, pricing pages, hero treatments, product lines.
3. **Positioning analysis**: brand promise, target audience, tone, visual identity — how do they position against HS?
4. **Pricing comparison**: treatment price ranges, product price tiers, subscription or loyalty offers.
5. **Strengths and gaps**: where the competitor wins, where HS wins, and where neither covers well.
6. **Recent moves**: new products, campaigns, partnerships, or reviews in the last 90 days.

## Output

**Battlecard** (one per competitor):

- Competitor overview (1 sentence)
- Core positioning
- Price range vs. HS
- Where they beat HS / where HS beats them
- Key objection from a client considering both: HS answer
- Watch items (recent moves to monitor)

Optionally produce an HTML artifact with clickable competitor cards.

## Guardrails

- Use only publicly available information.
- Do not make unverified performance or safety claims about competitors.
- All competitive claims used in client-facing materials must be reviewed before use.
