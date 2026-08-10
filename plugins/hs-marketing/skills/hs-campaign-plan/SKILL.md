---
name: hs-campaign-plan
description: Plan Hair Solutions Co. marketing campaigns end-to-end — objectives, audience, messaging, channel strategy, week-by-week content calendar, budget, and KPIs — plus the paid ads playbook (Google/Meta campaign structure, ad copy frameworks, retargeting sequences, beauty-industry benchmarks) and Instagram Graph API publishing/analytics. Use for "campaign plan", "launch plan", "paid ads", "ad copy", "retargeting", "Instagram posting". Not for one-off copy (hs-content-creation) or post-campaign reporting (hs-performance-report).
---

# Hair Solutions Co. Campaign Plan

> **Merged from:** `campaign-plan` (Anthropic base) + `paid-ads`, `instagram` (Hair Solutions legacy)

Generate a comprehensive marketing campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics — then execute the paid and Instagram legs with the Hair Solutions Co. production playbooks below.

## Trigger

User runs `/campaign-plan` or asks to plan, design, or build a marketing campaign, a paid ads campaign, ad copy, retargeting, or Instagram publishing.

## Inputs

Gather the following from the user. If not provided, ask before proceeding:

1. **Campaign goal** — the primary objective (e.g., drive signups, increase awareness, launch a product, generate leads, re-engage churned users)
2. **Target audience** — who the campaign is aimed at (demographics, roles, industries, pain points, buying stage)
3. **Timeline** — campaign duration and any fixed dates (launch date, event date, seasonal deadline)
4. **Budget range** — approximate budget or budget tier (optional; if not provided, generate a channel-agnostic plan and note where budget allocation would matter)
5. **Additional context** (optional):
   - Product or service being promoted
   - Key differentiators or value propositions
   - Previous campaign performance or learnings
   - Brand guidelines or constraints (for Hair Solutions Co., the Atelier Zero v7 authority — see `hs-brand-review`)
   - Geographic focus

## Campaign Brief Structure

Generate a campaign brief with the following sections:

### 1. Campaign Overview

- Campaign name suggestion
- One-sentence campaign summary
- Primary objective with a specific, measurable goal
- Secondary objectives (if applicable)

### 2. Target Audience

- Primary audience segment with description
- Secondary audience segment (if applicable)
- Audience pain points and motivations
- Where they spend time (channels, communities, publications)
- Buying stage alignment (awareness, consideration, decision)

### 3. Key Messages

- Core campaign message (one sentence)
- 3–4 supporting messages tailored to audience pain points
- Message variations by channel (if different tones are needed)
- Proof points or evidence to support each message

### 4. Channel Strategy

Recommend channels based on audience and goal. For each channel, include:

- Why this channel fits the audience and objective
- Content format recommendations
- Estimated effort level (low, medium, high)
- Budget allocation suggestion (if budget was provided)

Consider channels from:

- Owned: blog, email, website, social media profiles
- Earned: PR, influencer partnerships, guest posts, community engagement
- Paid: search ads, social ads, display, sponsored content, events

### 5. Content Calendar

Create a week-by-week (or day-by-day for short campaigns) content calendar:

- What content to produce each week
- Which channel each piece targets
- Key milestones and deadlines
- Dependencies between pieces (e.g., "landing page must be live before paid ads launch")

Format as a table:

| Week | Content Piece | Channel | Owner/Notes | Status |
| --- | --- | --- | --- | --- |

### 6. Content Pieces Needed

List every content asset required for the campaign:

- Asset name and type (blog post, email, social post, ad creative, landing page, etc.)
- Brief description of what it should contain
- Priority (must-have vs. nice-to-have)
- Suggested timeline for creation

### 7. Success Metrics

Define KPIs aligned to the campaign objective:

- Primary KPI with target number
- Secondary KPIs (3–5)
- How each metric will be tracked (GA4, Google Ads, Instagram insights — see `hs-performance-report` for the measurement stack)
- Reporting cadence recommendation

Reference historical performance benchmarks where available to inform targets; the beauty/hair paid benchmarks below are the Hair Solutions operative baseline.

### 8. Budget Allocation (if budget provided)

- Breakdown by channel or activity
- Production costs vs. distribution costs
- Contingency recommendation (typically 10–15%)

### 9. Risks and Mitigations

- 2–3 potential risks (timeline, audience mismatch, channel underperformance)
- Mitigation strategy for each

### 10. Next Steps

- Immediate action items to kick off the campaign
- Stakeholder approvals needed
- Key decision points

## Planning Reference

### Campaign Framework: Objective, Audience, Message, Channel, Measure

Every campaign should be built on this five-part framework:

**Objective** — define what success looks like before planning anything else.

- **Awareness**: increase brand or product visibility (measured by reach, impressions, share of voice)
- **Consideration**: drive engagement and education (measured by content engagement, email signups, webinar attendance)
- **Conversion**: generate leads or sales (measured by signups, demos, purchases, pipeline)
- **Retention**: re-engage existing customers (measured by churn reduction, upsell, NPS)
- **Advocacy**: turn customers into promoters (measured by referrals, reviews, UGC)

Good objectives are SMART: Specific, Measurable, Achievable, Relevant, Time-bound.

Example: "Generate 200 marketing qualified leads from mid-market SaaS companies in North America within 6 weeks of campaign launch."

**Audience** — define who you are trying to reach with enough specificity to guide messaging and channel decisions.

- **Demographics**: role/title, seniority, company size, industry
- **Psychographics**: motivations, pain points, goals, objections
- **Behavioral**: where they consume content, how they buy, what they have engaged with before
- **Buying stage**: are they unaware of the problem, researching solutions, or ready to buy?

Create a brief audience profile (not a full persona) for campaign planning:

> "[Role] at [company type] who is struggling with [pain point] and looking for [desired outcome]. They typically discover solutions through [channels] and care most about [priorities]."

**Message** — craft the core message and supporting points that will resonate with the audience.

- **Core message**: one sentence that captures what you want the audience to think, feel, or do
- **Supporting messages**: 3–4 points that provide evidence, address objections, or elaborate on benefits
- **Proof points**: data, case studies, testimonials, or third-party validation for each supporting message
- **Differentiation**: what makes your offering different from alternatives (including doing nothing)

Message hierarchy:

1. Why should I care? (addresses the pain point or opportunity)
2. What is the solution? (positions your offering)
3. Why you? (differentiates from alternatives)
4. What should I do? (call to action)

**Channel** — select channels based on where your audience is, not where you are most comfortable. See the Channel Selection Guide below.

**Measure** — define how you will know the campaign worked. See Success Metrics by Campaign Type below.

### Channel Selection Guide

**Owned Channels**

| Channel | Best For | Typical Metrics | Effort |
| --- | --- | --- | --- |
| Blog/Website | SEO, thought leadership, education | Traffic, time on page, conversions | Medium |
| Email | Nurture, retention, announcements | Open rate, CTR, conversions | Low-Medium |
| Social (organic) | Awareness, community, brand building | Engagement, reach, follower growth | Medium |
| Webinars | Education, lead gen, product demos | Registrations, attendance, pipeline | High |
| Podcast | Thought leadership, brand awareness | Downloads, subscriber growth | High |

**Earned Channels**

| Channel | Best For | Typical Metrics | Effort |
| --- | --- | --- | --- |
| PR/Media | Awareness, credibility, launches | Coverage, share of voice, referral traffic | High |
| Guest content | Audience expansion, SEO, credibility | Referral traffic, backlinks | Medium |
| Influencer/Partner | Audience expansion, trust | Reach, engagement, referral conversions | Medium-High |
| Community | Awareness, trust, feedback | Mentions, engagement, referral traffic | Medium |
| Reviews/Ratings | Credibility, SEO, consideration | Review volume, rating, conversion lift | Low-Medium |

**Paid Channels**

| Channel | Best For | Typical Metrics | Effort |
| --- | --- | --- | --- |
| Search ads (SEM) | High-intent lead capture | CPC, CTR, conversion rate, CPA | Medium |
| Social ads | Awareness, retargeting, lead gen | CPM, CPC, CTR, CPA, ROAS | Medium |
| Display/Programmatic | Awareness, retargeting | Impressions, CPM, view-through conversions | Low-Medium |
| Sponsored content | Thought leadership, lead gen | Engagement, leads, cost per lead | Medium |
| Events/Sponsorships | Relationship building, brand | Leads, meetings, pipeline influenced | High |

**Channel Selection Criteria** — when choosing channels, consider:

- Where does your target audience spend time?
- What is the buying stage you are targeting? (awareness channels vs. conversion channels)
- What is your budget? (paid channels require spend; owned/earned require time)
- What content assets do you already have or can you produce?
- What has worked in the past? (reference historical data if available)

### Content Calendar Creation

**Calendar Planning Process**

1. **Start with milestones**: campaign launch, event dates, product releases, seasonal moments
2. **Work backward**: what needs to be live and when? What is the production lead time?
3. **Map content to funnel stages**: ensure coverage across awareness, consideration, and conversion
4. **Batch by theme**: group related content pieces into weekly or bi-weekly themes
5. **Balance channels**: do not over-index on one channel; ensure the audience sees the campaign across touchpoints
6. **Build in flexibility**: leave 20% of calendar slots open for reactive or opportunistic content

**Content Cadence Guidelines**

- **Blog**: 1–4 posts per week depending on team size and goals
- **Email newsletter**: weekly or bi-weekly for most audiences
- **Social media**: 3–7 posts per week per platform (varies by platform; see the weekly rhythm in `hs-content-creation`)
- **Paid campaigns**: continuous during campaign window with creative refreshes every 2–4 weeks
- **Webinars**: monthly or quarterly depending on resources

**Production Timeline Benchmarks**

- Blog post: 3–5 business days (research, draft, review, publish)
- Email campaign: 2–3 business days (copy, design, test, send)
- Social media posts: 1–2 business days (draft, design, schedule)
- Landing page: 5–7 business days (copy, design, development, QA)
- Video content: 2–4 weeks (script, production, editing)
- Ebook/whitepaper: 2–4 weeks (outline, draft, design, review)

### Budget Allocation Approaches

**Percentage of Revenue Method**

- Industry benchmark: 5–15% of revenue for marketing, with B2B typically at 5–10% and B2C at 10–15%
- Startups and growth-stage companies often invest 15–25% of revenue in marketing
- Within the marketing budget, allocate across brand (long-term) and performance (short-term)

**Channel Allocation Framework** — a common starting framework (adjust based on goals and historical data):

| Category | Percentage of Budget | Examples |
| --- | --- | --- |
| Paid acquisition | 30–40% | Search ads, social ads, display |
| Content production | 20–30% | Blog, video, design, ebooks |
| Events and sponsorships | 10–20% | Conferences, webinars, meetups |
| Tools and technology | 10–15% | Analytics, automation, CRM |
| Testing and experimentation | 5–10% | New channels, A/B tests, pilots |

**Budget Optimization Principles**

- Start with your highest-confidence channel and allocate 60–70% of paid budget there
- Reserve 15–20% for testing new channels or tactics
- Shift budget monthly based on performance data (do not set and forget)
- Account for production costs, not just media spend
- Include a 10–15% contingency for unexpected opportunities or overruns

For the paid-media split by business stage, use the Hair Solutions Budget Allocation Framework in the Paid Advertising Playbook below.

### Success Metrics by Campaign Type

Map the primary KPI to the campaign objective (from the framework above):

- **Awareness**: reach, impressions, share of voice
- **Consideration**: content engagement, email signups, webinar attendance
- **Conversion**: signups, demos, purchases, pipeline
- **Retention**: churn reduction, upsell, NPS
- **Advocacy**: referrals, reviews, UGC

For paid campaigns, benchmark against the beauty/hair industry table below. For definitions and full metric tables, see `hs-performance-report`.

## Paid Advertising Playbook (Hair Solutions)

End-to-end paid ads framework covering campaign structure, copy, targeting, bidding, and optimization across all major platforms.

### Platform Selection Guide

| Goal | Best Platform |
| --- | --- |
| High-intent buyers (searching) | Google Search Ads |
| Visual brand discovery | Instagram, TikTok |
| B2B professional targeting | LinkedIn |
| Retargeting website visitors | Google Display, Meta |
| Video storytelling | YouTube, TikTok, Reels |
| Local service discovery | Google LSA (Local Service Ads) |

### Campaign Structure

**Account → Campaign → Ad Set → Ad**

```
Account: Hair Solutions Co.
├── Campaign: [Objective — Awareness / Traffic / Conversions]
│   └── Ad Set: [Audience + Budget + Placement]
│       └── Ad: [Creative + Copy]
```

**Google Ads Structure**

```
Campaign: Booking Conversions
├── Ad Group: Hair Treatments Toronto
│   ├── Keywords: [hair treatment toronto], [hair salon near me]
│   └── Ad: "Book Your Hair Transformation Today"
├── Ad Group: Hair Loss Solutions
│   ├── Keywords: [hair loss treatment], [hair restoration salon]
│   └── Ad: "Stop Hair Loss — Professional Treatment"
```

**Meta Campaign Structure**

```
Campaign: Lead Generation (Conversion objective)
├── Ad Set 1: Lookalike 1% (seed: past buyers)
│   └── Budget: $30/day
├── Ad Set 2: Interest targeting (hair care, beauty)
│   └── Budget: $20/day
└── Ad Set 3: Retargeting (website visitors 30 days)
    └── Budget: $15/day
```

### Ad Copy Frameworks

**PAS (Problem-Agitate-Solution)**

```
Headline: [State the specific problem]
Body: [Make the problem more vivid/painful]
CTA: [Present the solution + clear action]

Example:
"Bad Hair Days Ruining Your Confidence?"
"Dull, damaged hair makes you want to hide — not show up as your best self."
"Book a Transformation Treatment → First visit 20% off"
```

**BAB (Before-After-Bridge)**

```
Before: [Current frustrating state]
After: [Desired outcome state]
Bridge: [How your product/service gets them there]

Example:
"Before: Thin, lifeless hair you're embarrassed about"
"After: Full, shiny hair that turns heads"
"Bridge: Our Keratin Restoration Treatment — book today"
```

**Social Proof Formula**

```
"[N] clients in [city] have [achieved result] with [product/service]"
"⭐⭐⭐⭐⭐ '[Customer quote about transformation]' — [First name, Location]"
```

**Urgency + Scarcity**

```
"Only [N] spots left this month"
"[Offer] ends [date]"
"Book before [date] — pricing increases [date]"
```

Use urgency/scarcity only when genuine. Note: the Atelier Zero v7 brand voice (`hs-brand-review`) prohibits urgency, scarcity, and hype in brand communications — confirm with the owner before running urgency creative on brand surfaces.

### Google Ads

**Search Ad Best Practices**

- Include primary keyword in Headline 1
- Dynamic keyword insertion: `{KeyWord:Default Text}`
- Use all 15 headlines and 4 descriptions
- Pin critical headlines to positions 1 & 2
- Asset groups: sitelinks, callouts, structured snippets, call extension

**Keyword Match Types**

| Type | Format | When to Use |
| --- | --- | --- |
| Broad | `keyword` | Maximize reach, discovery phase |
| Phrase | `"keyword"` | Balanced intent + reach |
| Exact | `[keyword]` | Highest intent, efficiency |
| Negative | `-keyword` | Block irrelevant traffic |

**Bidding Strategy Selection**

| Objective | Bid Strategy |
| --- | --- |
| New campaign, limited data | Manual CPC or Max Clicks |
| Have conversion history (50+/mo) | Target CPA |
| E-commerce with revenue tracking | Target ROAS |
| Brand awareness | Target Impression Share |

**Quality Score Optimization**

- Keyword → Ad → Landing Page relevance triangle
- CTR is the #1 quality score signal
- Landing page load speed matters (under 3 seconds)
- Maintain 1 topic per ad group (SKAG approach for high-value terms)

### Meta Ads (Facebook/Instagram)

**Audience Targeting Layers**

```
Core Audiences (Interest/Behavior)
+ Custom Audiences (website visitors, email list, video viewers)
+ Lookalike Audiences (1–5% lookalike of best customers)
```

**Campaign Budget Optimization (CBO)**

- Set budget at campaign level
- Meta auto-distributes to best-performing ad sets
- Minimum: $10/ad set/day for meaningful data

**Creative Best Practices**

- **Hook**: First 3 seconds must stop the scroll
- **Aspect ratio**: 9:16 for Stories/Reels, 1:1 for feed
- **Captions**: Always on — 85% of videos watched silent
- **UGC style**: Outperforms polished ads 2–5x for cold audiences
- **Test**: 3–5 creatives per ad set minimum

**Facebook Pixel Events**

```javascript
// Purchase
fbq('track', 'Purchase', {value: 75.00, currency: 'CAD'});

// Lead
fbq('track', 'Lead');

// View Content (product page)
fbq('track', 'ViewContent', {content_ids: ['SKU-123'], content_type: 'product'});

// Add to Cart
fbq('track', 'AddToCart', {value: 35.00, currency: 'CAD'});
```

### Retargeting Sequences

**E-commerce Funnel**

```
Day 1–7: Viewed product → Show product + testimonial
Day 8–14: Added to cart → Show urgency + discount offer
Day 15–30: Purchased → Cross-sell complementary product
Day 31+: Exclude from purchase campaign
```

**Service Business Funnel**

```
Day 1–3: Visited booking page → "Still thinking about it? Here's what our clients say"
Day 4–7: Viewed services page → Specific service showcase + CTA
Day 8–14: General visitor → Brand story + social proof
Day 15–30: 3+ visits → Direct offer with incentive
```

### Budget Allocation Framework (by Business Stage)

| Business Stage | Search | Social | Display/Retargeting |
| --- | --- | --- | --- |
| New business | 60% | 30% | 10% |
| Growing | 40% | 40% | 20% |
| Scaling | 30% | 40% | 30% |

### Naming Convention

```
[Platform]-[Campaign Type]-[Audience]-[Offer]-[Date]

Examples:
META-CONV-LLA1-BookingOffer-2026Q1
GOOG-SEARCH-HairTreatments-BrandedKWs-2026Q1
META-RETARG-30DayVisitors-CarabanDiscount-2026Q1
```

### Key Performance Benchmarks (Beauty/Hair Industry)

| Metric | Good | Great |
| --- | --- | --- |
| Google Search CTR | >4% | >8% |
| Meta CTR (Feed) | >1.5% | >3% |
| Conversion Rate (Booking) | >3% | >7% |
| CPA (Appointment) | <$25 | <$12 |
| ROAS (Product) | >3x | >6x |

### Common Mistakes

- Pausing campaigns before the learning phase completes (50+ conversions needed)
- Too many ad sets competing for the same audience (audience overlap)
- No exclusion audiences (showing ads to existing customers)
- Changing bid strategy during the active learning phase
- Not separating prospecting and retargeting into different campaigns

## Instagram Execution (Graph API)

Manage a professional Instagram presence through the Meta Graph API. Requires a Business or Creator account connected to a Facebook Page.

### Prerequisites

1. Instagram Business or Creator account
2. Connected Facebook Page
3. Meta Developer App with Instagram Graph API permissions
4. `instagram_business_basic`, `instagram_content_publish`, `instagram_manage_comments` scopes

### Authentication

```bash
export IG_ACCESS_TOKEN="EAAxxxxx"
export IG_USER_ID="17841400000000000"
```

### Content Publishing

**Single Image Post**

```bash
# Step 1: Create media container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "image_url=https://your-cdn.com/hair-product.jpg" \
  -F "caption=Transform your hair care routine ✨ Shop link in bio." \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Publish (use returned creation_id)
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id=17889615814797252" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

**Reel**

```bash
# Step 1: Create reel container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "media_type=REELS" \
  -F "video_url=https://your-cdn.com/hair-tutorial.mp4" \
  -F "caption=60-second hair transformation 💆‍♀️ Save this for your next appointment!" \
  -F "share_to_feed=true" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Poll for ready status
curl "https://graph.facebook.com/v21.0/{creation_id}?fields=status_code&access_token=$IG_ACCESS_TOKEN"

# Step 3: Publish when status_code = FINISHED
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id={creation_id}" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

**Carousel Post**

```bash
# Step 1: Create child containers for each image
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "image_url=https://cdn.com/slide1.jpg" \
  -F "is_carousel_item=true" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 2: Create carousel container
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media" \
  -F "media_type=CAROUSEL" \
  -F "children=child_id_1,child_id_2,child_id_3" \
  -F "caption=Before & After: Our signature treatment 👑 Swipe to see the full transformation!" \
  -F "access_token=$IG_ACCESS_TOKEN"

# Step 3: Publish
curl -X POST "https://graph.facebook.com/v21.0/$IG_USER_ID/media_publish" \
  -F "creation_id={carousel_id}" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

### Analytics

**Account Insights**

```bash
curl "https://graph.facebook.com/v21.0/$IG_USER_ID/insights?metric=reach,impressions,profile_views,follower_count&period=day&since=2026-02-01&until=2026-02-27&access_token=$IG_ACCESS_TOKEN"
```

**Media Insights**

```bash
curl "https://graph.facebook.com/v21.0/{media_id}/insights?metric=reach,impressions,saved,video_views,shares&access_token=$IG_ACCESS_TOKEN"
```

**Audience Demographics**

```bash
curl "https://graph.facebook.com/v21.0/$IG_USER_ID/insights?metric=audience_city,audience_country,audience_gender_age&period=lifetime&access_token=$IG_ACCESS_TOKEN"
```

### Comment Management

**Get Comments**

```bash
curl "https://graph.facebook.com/v21.0/{media_id}/comments?fields=text,username,timestamp&access_token=$IG_ACCESS_TOKEN"
```

**Reply to Comment**

```bash
curl -X POST "https://graph.facebook.com/v21.0/{comment_id}/replies" \
  -F "message=Thank you! Book your appointment at the link in bio 💙" \
  -F "access_token=$IG_ACCESS_TOKEN"
```

**Hide Comment**

```bash
curl -X POST "https://graph.facebook.com/v21.0/{comment_id}?hidden=true&access_token=$IG_ACCESS_TOKEN"
```

### Best Posting Times for Beauty/Hair Industry

- Tuesday–Friday: 11am–1pm and 7pm–9pm (local time)
- Saturday: 10am–12pm
- Avoid: Monday mornings, late Sunday nights

### Content Strategy for Hair Solutions Co.

- **Feed posts**: Before/after transformations, product showcases, team spotlights
- **Reels**: Tutorials (30–60s), behind-the-scenes, trending audio hooks
- **Stories**: Daily engagement — polls, Q&As, flash promos, appointment reminders
- **Carousels**: Multi-step tutorials, product comparisons, tip lists (saves = reach boost)

### Rate Limits

- Content publishing: 50 posts per 24 hours
- API calls: 200/hour per token
