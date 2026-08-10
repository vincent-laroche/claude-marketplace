---
name: hs-seo-audit
description: Run SEO audits for Hair Solutions Co. web properties (hairsolutions.co, Shopify storefront) — keyword research, on-page checks, content gaps, technical/Core Web Vitals fixes, Shopify-specific checks, local SEO, and competitor comparison, using live Google Search Console data via the gsc_tool.py CLI. Use for "SEO audit", "keyword research", "rank higher", indexing or sitemap troubleshooting. Not for writing the content itself (hs-content-creation) or GA4 traffic reporting (hs-performance-report).
---

# Hair Solutions Co. SEO Audit

> **Merged from:** `seo-audit` (Anthropic base) + `seo-audit` (custom), `google-search-console` (Hair Solutions legacy)

Audit SEO health for Hair Solutions Co. web properties (Shopify store and service pages), research keyword opportunities, identify content gaps, and benchmark against competitors. Produces a prioritized action plan a marketer can execute immediately.

## Trigger

User asks for an SEO audit, keyword research, content gap analysis, technical SEO check, competitor SEO comparison, or Search Console / indexing / sitemap troubleshooting.

## Inputs

Gather the following. If not provided, ask before proceeding:

1. **URL or domain** — the site to audit, or a topic/keyword for keyword research mode. The Hair Solutions Co. Search Console property is `sc-domain:hairsolutions.co`.
2. **Audit type** — one of:
   - **Full site audit** — end-to-end review covering all sections below
   - **Keyword research** — identify opportunities for a topic or domain
   - **Content gap analysis** — topics competitors rank for that you don't
   - **Technical SEO check** — crawlability, speed, structured data, infrastructure
   - **Competitor SEO comparison** — head-to-head benchmarking

   If not specified, default to **full site audit**.
3. **Target keywords or topics** (optional)
4. **Competitors** (optional) — if not provided and the audit needs them, use web search to identify 2–3 likely competitors.

## Data Source: Google Search Console CLI (first-party data)

Hair Solutions Co. has a dedicated Python CLI for live Search Console data. Prefer it over estimates whenever the host environment supports it.

### Prerequisites

1. Python 3 with `google-api-python-client` and `google-auth` installed.
2. Authentication via Application Default Credentials with the Search Console scope. If auth fails:

   ```shell
   gcloud auth application-default login --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly"
   ```

### Available commands

`gsc_tool.py` lives in `plugins/seo-tools/commands/`.

**1. List properties** — confirm the exact `--site` string:

```shell
./plugins/seo-tools/commands/gsc_tool.py list-sites
```

**2. Performance** — clicks, impressions, CTR, average position:

```shell
./plugins/seo-tools/commands/gsc_tool.py performance --site "sc-domain:hairsolutions.co" --start "2024-01-01" --end "2024-01-31" --dimensions "query,page"
```

Available dimensions: `date`, `query`, `page`, `country`, `device`.

**3. URL inspection** — indexing status, canonicalization, mobile usability:

```shell
./plugins/seo-tools/commands/gsc_tool.py inspect --site "sc-domain:hairsolutions.co" --url "https://hairsolutions.co/products/example"
```

**4. Sitemaps** — submitted sitemaps and processing status:

```shell
./plugins/seo-tools/commands/gsc_tool.py sitemaps --site "sc-domain:hairsolutions.co"
```

### Interpreting GSC results

- **Coverage state** — "Indexed", "Crawled - currently not indexed", or "Discovered - currently not indexed". Use this to diagnose indexing pipeline issues.
- **Position** — 1-indexed; lower is better.
- "No data found" usually means an invalid date range (GSC data lags ~48 hours) or a property string that doesn't exactly match `list-sites` output.

### When to use GSC data

- **SEO audits** — top queries, top pages, general search performance
- **Troubleshooting** — why a page isn't getting traffic (URL inspection)
- **Post-launch** — verify newly published pages are indexed or in a sitemap
- **Property discovery** — confirm which GSC properties are accessible

Cross-reference keyword targets with GA4 organic traffic to validate which keywords drive visits and conversions (see `hs-performance-report`). For search volume and difficulty estimates, supplement with Keyword Planner, Ubersuggest, or Ahrefs; without those, use web search and **label estimates as estimates**.

## Process

### 1. Keyword Research

**Keyword tiers (portfolio structure):**

- **Tier 1 — Pillar** (10,000+/mo, high competition) — long-term authority. Pillar pages, comprehensive guides.
- **Tier 2 — Target** (500–10,000/mo, medium) — primary traffic drivers. Service/product pages, blog posts.
- **Tier 3 — Long-tail** (50–500/mo, low) — quick wins, specific buyer intent. FAQ pages, specific articles.

**Research process:**

1. Seed keywords from business description + competitor domains
2. Expand using Google Autocomplete + People Also Ask
3. Analyze using Keyword Planner, Ubersuggest, or Ahrefs
4. Group by search intent (informational, commercial, transactional)
5. Map keywords to specific pages (one primary keyword per page)
6. Identify gaps — topics competitors rank for but you don't

**For each opportunity, assess:** primary keywords, secondary keywords, search volume signals, keyword difficulty, long-tail opportunities, question-based keywords, and intent classification.

### 2. On-Page SEO Audit

For each key page (homepage, top landing pages, top products/collections, recent blog posts):

- [ ] Unique title tag (50–60 chars) with primary keyword
- [ ] Meta description (150–160 chars), compelling, keyword-rich, with a CTA
- [ ] H1 exists, contains primary keyword, appears exactly once
- [ ] H2/H3 used for logical hierarchy, secondary keywords where natural
- [ ] Primary keyword in first 100 words, used naturally, not over-stuffed
- [ ] Images have descriptive alt text (not "image123.jpg")
- [ ] Internal linking connects related pages; orphan pages identified; descriptive anchor text
- [ ] URL slugs descriptive and keyword-rich (no parameters, no excessive depth)

### 3. Content Quality & Gap Analysis

**Content quality floor:**

- [ ] Minimum 300 words per indexable page (service/product pages: 600+)
- [ ] No thin or duplicate content
- [ ] FAQs added to target People Also Ask
- [ ] Fresh content signals (blog updated regularly)

**Gap analysis:** competitor topic coverage, content freshness (12+ months stale), thin content, missing content types (guides, comparisons, glossaries, tools), funnel gaps, and topic-cluster opportunities (see the pillar strategy in `hs-content-creation`).

### 4. Technical SEO Checklist

- [ ] Loads under 3 seconds (LCP < 2.5s, FID < 100ms, CLS < 0.1)
- [ ] HTTPS with no mixed content
- [ ] XML sitemap exists and submitted (verify with `sitemaps`)
- [ ] robots.txt correctly configured (not blocking key pages)
- [ ] No duplicate content (canonical tags correct)
- [ ] Mobile-friendly (responsive, tap targets, font sizes, viewport)
- [ ] No broken links (404s, redirect chains)
- [ ] Structured data — FAQ, HowTo, Product, Article, Organization, Breadcrumb
- [ ] Hreflang if multilingual
- [ ] Indexation — pages that should be indexed but aren't (URL inspection)
- [ ] Page speed — slow pages and likely causes

### 5. Shopify-Specific Checks

- [ ] Product descriptions unique (not manufacturer copy)
- [ ] Collection pages have descriptive intro text
- [ ] Product images optimized (WebP, alt text)
- [ ] Shopify auto-generated canonical tags verified correct
- [ ] No duplicate pages from faceted navigation

### 6. Core Web Vitals Fixes

**LCP** — optimize above-fold images (compress, WebP, `loading="eager"`), preload hero with `<link rel="preload">`, use a CDN (Cloudinary for image delivery), reduce server response time.

**CLS** — set explicit width/height on all images and videos, reserve space for ads and embeds, avoid injecting content above existing content.

**FID** — minimize main-thread JavaScript, defer non-critical JS, break up long tasks.

### 7. Local SEO (service business side)

- Complete Google Business Profile with photos, hours, services
- NAP consistency (Name, Address, Phone) across all citations
- Encourage and respond to Google reviews
- Local landing pages per service area
- LocalBusiness schema markup
- Citations in relevant directories

### 8. Competitor SEO Comparison

For each top-3 competitor: domain authority, top organic keywords, backlink sources, content gaps, and page-structure differences on high-ranking pages.

Compare across: keyword overlap, keyword gaps, domain authority signals, content depth, backlink profile observations, SERP feature ownership, and technical advantages.

## On-Page Optimization Template

```markdown
Page: [URL]
Primary Keyword: [keyword] (monthly volume: X)
Secondary Keywords: [keyword1, keyword2]

CURRENT:
Title: [current title]
Meta: [current meta description]
H1: [current H1]
Word Count: [X]

OPTIMIZED:
Title: [keyword] | [Brand Name]  (under 60 chars)
Meta: [compelling description with keyword + CTA, 150–160 chars]
H1: [primary keyword naturally included]
Content Additions: [list what's missing]
```

## Output

### Executive Summary

3–5 sentences on overall SEO health: biggest strength, top 3 highest-impact priorities, and an overall assessment (strong foundation / needs work / critical issues).

### Keyword Opportunity Table

| Keyword | Est. Difficulty | Opportunity Score | Current Ranking | Intent | Recommended Content Type |
| --- | --- | --- | --- | --- | --- |

Opportunity score: high / medium / low, from demand × difficulty × relevance. Pull current rankings from the GSC `performance` command where available. Include 15–25 opportunities sorted by score.

### On-Page Issues Table

| Page | Issue | Severity | Recommended Fix |
| --- | --- | --- | --- |

Severity: **Critical** (hurting rankings or preventing indexation) · **High** · **Medium** · **Low**.

### Content Gap Recommendations

For each gap: topic/keyword, why it matters, recommended format, priority, and estimated effort (quick win 1–2h / moderate half-day / substantial multi-day).

### Technical SEO Checklist

| Check | Status | Details |
| --- | --- | --- |

Status: Pass, Fail, or Warning.

### Competitor Comparison Summary

| Dimension | Your Site | Competitor A | Competitor B | Winner |
| --- | --- | --- | --- | --- |

Include rows for keyword count, content depth, publishing frequency, backlink signals, technical score, SERP feature presence.

### Prioritized Action Plan

**Quick Wins (this week)** — under 2 hours, immediate impact: fix title tags, add meta descriptions, fix broken links, add alt text.

**Strategic Investments (this quarter)** — more effort, long-term growth: build a topic cluster, create a pillar page, launch link-building, overhaul site structure.

For each action: what to do, expected impact, effort estimate, dependencies.

## Reporting Metrics (monthly cadence)

Track in Search Console + GA4: total organic impressions and clicks, average position for top 20 keywords, CTR by page, pages gaining/losing impressions, Core Web Vitals scores.

## Follow-Up

After presenting the audit, offer to: draft content briefs for the top keyword opportunities, create optimized titles and meta descriptions, build a content calendar from the gap analysis, dive deeper into a section, or run the same analysis for another competitor or domain.
