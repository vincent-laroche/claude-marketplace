---
name: hs-email-sequence
description: Design and draft Hair Solutions Co. email sequences — welcome, abandoned cart, post-purchase, nurture, win-back, launch — with full copy, timing, branching, exit conditions, and beauty/e-commerce benchmarks. Also covers building emails as HubSpot Design Manager email_modules (account 50966981) — naming, light/dark variants, editability, validation, deployment. Use for any email flow or email module work. Not for one-off marketing copy (hs-content-creation) or CRM data/workflow changes.
---

# Hair Solutions Co. Email Sequence

> **Merged from:** `email-sequence` (Anthropic base) + `email-sequences`, `hubspot-email-modules` (Hair Solutions legacy)

Design and draft complete email sequences with full copy, timing, branching logic, and performance benchmarks — and build the resulting emails as Hair Solutions Co. HubSpot Design Manager modules.

## Trigger

User asks to create, design, build, or draft an email sequence, drip campaign, nurture flow, welcome series, abandoned cart flow, post-purchase flow, or onboarding series — or to work on HubSpot email modules.

## Inputs

Gather the following. If not provided, ask before proceeding:

1. **Sequence type** — welcome series, abandoned cart, post-purchase, lead nurture, re-engagement, win-back, product launch, event follow-up, upgrade/upsell, educational drip, onboarding.
2. **Goal** — what the sequence should achieve (activate new customers, convert leads, recover carts, drive reviews, reduce churn).
3. **Audience** — who receives it, what stage they're at, segmentation details (behaviour triggers, lifecycle stage, past purchases).
4. **Number of emails** (optional) — recommend a count from the templates below if unspecified.
5. **Timing/cadence** (optional).
6. **Brand voice** — Hair Solutions Co. voice: professional but approachable, empathetic, educational, trustworthy — no hype. Confirm before using a different register.
7. **Additional context** (optional) — offers, CTAs/landing pages, available content assets, product features, competitor differentiators.

## Process

### 1. Sequence Strategy

Before drafting any emails, define:

- **Narrative arc** — what story does the sequence tell end to end?
- **Journey mapping** — map each email to a stage (awareness, consideration, decision, activation, expansion).
- **Escalation logic** — how intensity, urgency, or value builds.
- **Success definition** — what action signals the sequence worked and the recipient should exit.

### 2. Individual Email Design

For each email produce:

**Subject line** — 2–3 options, varying approach (curiosity, benefit, urgency, personalization, question). Under 50 characters where possible.

**Preview text** — 40–90 characters complementing, not repeating, the subject.

**Email purpose** — one sentence on why it exists and what it moves the recipient toward.

**Body copy** — full draft, clear hierarchy (hook → body → CTA), short paragraphs (2–3 sentences), scannable, personalization tokens where relevant.

**Primary CTA** — button text and destination. One primary CTA per email.

**Timing** — days after trigger or previous email; note engagement-based adjustments.

**Segment/condition notes** — who receives it vs. who skips it.

### 3. Sequence Logic

- **Branching conditions** — e.g. "if opened email 2 but did not click, send 2b (softer re-ask) instead of 3".
- **Exit conditions** — remove on conversion; define what conversion means here.
- **Re-entry rules** — can someone re-enter, and when?
- **Suppression rules** — don't send if already in another active sequence, unsubscribed, or contacted support in the last 48 hours.

### 4. Performance Benchmarks

**Hair Solutions operative benchmarks (beauty / e-commerce):**

| Metric | Average | Good | Great |
| --- | --- | --- | --- |
| Open rate | 20% | 28% | 38%+ |
| Click rate | 2.5% | 4% | 7%+ |
| Abandoned cart recovery | 5% | 10% | 15%+ |
| Welcome series conversion | 3% | 7% | 12%+ |

Generic per-sequence-type reference:

| Metric | Onboarding | Lead Nurture | Re-engagement | Win-back |
| --- | --- | --- | --- | --- |
| Open rate | 50–70% | 20–30% | 15–25% | 15–20% |
| Click-through rate | 10–20% | 3–7% | 2–5% | 2–4% |
| Conversion rate | 15–30% | 2–5% | 3–8% | 1–3% |
| Unsubscribe rate | <0.5% | <0.5% | 1–2% | 1–3% |

The beauty/e-commerce table wins when the two disagree.

## Hair Solutions Flow Library (production templates)

Start from these before inventing a new structure.

### Welcome Series (5 emails)

**Email 1 — Immediate (0 min after signup)**
Subject: Welcome to [Brand] — here's your [lead magnet/discount] · Preview: Everything you need to get started
Deliver the promised incentive immediately · one-sentence brand story · what to expect from future emails · reply prompt: "What's your biggest [problem]?"

**Email 2 — Origin story (Day 2)**
Subject: Why we started [Brand] (the honest version) · Preview: It's not what you'd expect
Founder story focused on the problem you experienced · make the reader the hero · introduce one key differentiator · soft CTA to the most popular product/service.

**Email 3 — Education (Day 4)**
Subject: The [X] mistakes most [audience] make with [topic] · Preview: And how to avoid them
3–5 common mistakes with a brief solution for each · build authority without preaching · no hard sell.

**Email 4 — Social proof (Day 6)**
Subject: [Customer name]'s transformation · Preview: From [before] to [after]
Client transformation story · before/after specifics · how they achieved it · concrete results · CTA: see if this is right for you.

**Email 5 — Conversion (Day 8)**
Subject: Your [offer] expires in 48 hours · Preview: Don't leave this on the table
Recap the possible transformation · genuine deadline · objection removal in FAQ format · testimonial or guarantee · strong CTA.

### Abandoned Cart

**Email 1 (1 hour after abandonment)** — friendly reminder, not salesy · product image · "Was there a problem?" to lower friction · CTA: return to cart.

**Email 2 (24 hours)** — 2–3 relevant testimonials · address the top objection (price, results, fit) · "reply with questions" · CTA: complete your order.

**Email 3 (48 hours, optional discount)** — discount code · real deadline · reinforce benefit · CTA: use code at checkout.

### Post-Purchase

**Email 1 — Order confirmation (immediate)** — order details, receipt, shipping timeline, what's next, a thank-you that reads personal.

**Email 2 — Onboarding (Day 3 after delivery)** — how-to guide or usage tips, common mistakes, tutorials/knowledge base link, community invite.

**Email 3 — Check-in (Day 7)** — genuine check-in (not review-fishing), troubleshooting resource, feedback invite, soft cross-sell.

**Email 4 — Review request (Day 14)** — ask for an honest review, direct link, optional small incentive.

**Email 5 — Repurchase (Day 30–60 by product lifecycle)** — one-click reorder, new product suggestion, loyalty invite.

### Re-engagement / Win-back (inactive 90+ days)

1. "We miss you" — genuine, personal tone
2. "Has anything changed?" — update preferences
3. "Last chance to stay subscribed" — suppress if no open/click

## Additional Sequence Templates

- **Onboarding (5–7 emails / 14–21 days):** welcome and expectations → quick win → core feature → advanced feature → social proof → check-in → upgrade prompt
- **Lead nurture (4–6 / 3–4 weeks):** educational value → pain point → solution with proof → social proof → soft CTA → direct CTA
- **Re-engagement (3–4 / 10–14 days):** compelling reason to return → value reminder → incentive → last chance with deadline
- **Win-back (3–5 / 30 days):** what went wrong → what's new → offer → feedback request → final goodbye, door open
- **Product launch (4–6 / 2–3 weeks):** teaser → announcement → feature spotlight → social proof → limited offer → last chance
- **Event follow-up (3–4 / 7–10 days):** thank-you and takeaways → resource roundup → related offer → feedback survey
- **Upgrade/upsell (3–5 / 2–3 weeks):** milestone celebration → feature gap they're hitting → upgrade benefits with proof → incentive → plan comparison
- **Educational drip (5–8 / 4–6 weeks):** intro → foundational → intermediate → advanced → practical application → resources → graduation

## Subject Line Best Practices

- **Curiosity**: "The [thing] nobody tells you about [topic]"
- **Number**: "5 reasons your [thing] isn't working"
- **Personal**: "Quick question, [first name]"
- **Urgency**: "Closes at midnight"
- **Negative hook**: "What NOT to do with [product]"

**A/B test order:** subject line first, then send time, sender name, plain text vs HTML, CTA button colour/text.

## Building Emails in HubSpot (production stack)

Hair Solutions Co. marketing emails are built from custom HubSpot Design Manager modules. This section is live-account detail — follow it exactly.

### Canonical source

- Local repo: `/Users/vMac/03_agents/Projects/Email Marketing/Email Marketing Studio`
- Module source: `hubspot/design-manager/email_modules`
- Generated inventory: `lib/hubspotModuleInventory.generated.ts`
- HubSpot account: `50966981`
- Design Manager destination: `email_modules/`
- Primary checks: `npm run generate:hubspot-modules`, `npm run lint`, `npm run build`

Do not use old paths under `/Users/vMac/01_projects`, `/Users/vMac/04_marketing`, or legacy Email Studio folders without verifying current filesystem state.

### Required references

- `references/module-inventory.md` — active module folders, naming grammar, deleted/forbidden structures
- `references/deployment-playbook.md` — validation, upload/fetch, editability failures, draft repair warnings

### Non-negotiable rules

1. Inspect current local source before editing. Do not rely on remembered module names.
2. Active custom modules live only under `email_modules/core`, `email_modules/launch`, and `email_modules/newsletter` unless a genuinely new journey is being created.
3. No active module/folder/file should use `hsc_`, `hsc-`, `legacy`, `archive`, `not found`, fake `shop`, or unmanaged `warm` naming.
4. Every active module family needs exactly one Light and one Dark variant.
5. Every custom email module must be editable in the drag-and-drop editor: `global: false` in `meta.json`, every field `locked: false`, and fields exposing text/URLs/images/labels/choices/booleans rather than required raw HTML.
6. Do not make reusable headers journey-specific. Headers are CORE modules.
7. Do not create loose left-aligned rich-text modules. Every module needs a contained card/frame or deliberate table structure.
8. Do not use fake product/shop modules that only mimic Shopify. Use native HubSpot/Shopify integration sections for carts and products.
9. Do not send, schedule, publish marketing emails, mutate CRM records, or alter HubSpot workflows from this skill.
10. Design Manager deployment is a live write. Upload only the intended module folders/files; never use `--clean` unless explicitly replacing the whole destination.

### Design baseline

Email is not web. Use table-based structure, inline critical styles, a 600px wrapper, 568px internal cards where applicable, a 480px mobile breakpoint, and readable behaviour with images blocked.

Current email-module palette is **Core Palette v1** (seven colours), per `specs/PLATFORM_EMAIL.md` in `brand-design-system` — the authoritative source, verified 2026-07-03:

| Hex | Name | Role |
| --- | --- | --- |
| `#0F0F0F` | Ink Black | Highest-contrast ink, wordmark text, primary CTA fill on light |
| `#1B1B1B` | Body Black | Primary body text, footer authority, default dark panel |
| `#2A2929` | Soft Black | Secondary text, dark card surface, footer hierarchy |
| `#14213D` | Harbor Navy | Dark authority panels, structured support modules, selected state |
| `#E5E5E5` | Soft Silver | Email body background, light card surface, text on dark |
| `#D6D6D6` | Muted Silver | Borders, dividers, muted fields, secondary light fills |
| `#A63E1B` | Copper Clay | Small accent only — eyebrow, focus cue, proof marker, small rule. **Never the default CTA fill.** |

This replaces the pre-migration six-colour palette. If a module (local source or live Design Manager) still uses `#333533` (old "Deep Charcoal", now split into Body Black / Soft Black) or `#E06A2A` (old Copper Clay), that is exactly the residue the cleanup scans in step 6 should catch and migrate.

Approved logo masters live in `/Users/vMac/08_brand/Hair Solutions Co Logos`. Email-safe cropped exports are in HubSpot File Manager under `brand/hair-solutions-co-logos/email-exports/`. Light modules use ink logos; dark modules use soft-silver logos.

### Standard workflow

1. Read `references/module-inventory.md` and inspect the relevant module folder.
2. Check repo status; preserve unrelated local changes.
3. Make focused edits to `fields.json`, `meta.json`, and/or `module.html`.
4. Regenerate inventory: `npm run generate:hubspot-modules`
5. Validate: `npm run lint` and `npm run build`
6. Run targeted residue scans — old palette hexes, old logo URLs, `hsc_`, `hsc-`, `legacy`, `archive`, `not found`, `"global": true`, `"locked": true`.
7. Deploy only changed module folders/files, when explicitly approved.
8. Fetch the live HubSpot copy back to `/tmp` and verify live source — not just upload success.
9. Summarize changed files, deployed paths, checks, and residual risks. Separate Design Manager module updates from existing email draft instances.

### When existing emails stay broken

Changing module defaults does not always fix already-dropped module instances in existing HubSpot emails. Drafts may retain saved body values, a stale `module_id`, or module-id-only widget shapes. Inspect that draft separately. Repair drafts only with explicit approval, and never publish or send.

## Tool Integration

**HubSpot (live, account 50966981)** — sequences are HubSpot flows/automations; emails assemble from the Design Manager `email_modules` above. Reference lead scoring and lifecycle stage for segmentation and exit conditions. Per rule 9, this skill drafts and builds — it never sends, schedules, publishes, or alters workflows. Hand off to the owner for activation.

**Another platform (Klaviyo, Mailchimp, Customer.io)** — map the branching logic to that platform's visual flow builder, and note platform-specific features (smart send time, conditional splits, built-in A/B testing).

**No tools connected** — deliver copy-paste-ready content plus a setup checklist: create the automation, set the enrollment trigger, add each email with delays, configure branching and exits, set up tracking.

## Output

### Sequence Overview Table

| # | Subject Line | Purpose | Timing | Primary CTA | Condition |
| --- | --- | --- | --- | --- | --- |

### Full Email Drafts

Each email with subject line options, preview text, purpose, body copy, CTA, timing, and segment notes.

### Sequence Flow Diagram

```
[Trigger] --> Email 1 (Day 0)
                |
          Opened? --Yes--> Email 2 (Day 3)
                |              |
                No        Clicked CTA? --Yes--> [EXIT: Converted]
                |              |
                v              No
          Email 1b (Day 2)     |
                |              v
                +--------> Email 3 (Day 7)
                               |
                               v
                          Email 4 (Day 10)
                               |
                          [EXIT: Sequence complete]
```

### Branching Logic Notes

All conditions, exits, and suppressions as a reference list.

### A/B Test Suggestions

2–3 recommended tests: what to test, how to split, how to measure the winner.

### Metrics to Track

Primary conversion metric · per-email open/CTR/unsubscribe · sequence-level conversion rate, time to conversion, drop-off points · review cadence (weekly for the first month, then monthly).

## After the Sequence

Offer to: revise copy or tone for a specific email, add a branching path, create a variant for another segment, draft A/B subject-line variants, or build a companion sequence.
