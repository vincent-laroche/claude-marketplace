---
name: hs-performance-report
description: "Build Hair Solutions Co. marketing performance reports — weekly, monthly, quarterly, campaign, or channel — with trend analysis, wins/misses, and prioritized recommendations. Pulls live data: GA4 Data API (traffic, e-commerce, funnels), Google Ads Scripts (spend, CPA, alerts), and GTM for event/tracking verification. Includes metric definitions, benchmarks, and cadence templates. Use for \"performance report\", \"campaign results\", \"GA4\", \"GTM\", \"ads automation\". Not for SEO audits (hs-seo-audit) or campaign planning (hs-campaign-plan)."
---

# Hair Solutions Co. Performance Report

> **Merged from:** `performance-report` (Anthropic base) + `google-analytics`, `google-tagmanager`, `google-ads-scripts` (Hair Solutions legacy)

Generate a marketing performance report with key metrics, trend analysis, insights, and optimization recommendations — pulling live Hair Solutions Co. data from GA4 and Google Ads, and verifying the tracking layer in GTM before trusting the numbers.

## Trigger

User runs `/performance-report` or asks for a marketing report, performance analysis, campaign results, metrics summary, GA4/analytics questions, GTM tracking work, or Google Ads automation.

## Inputs

1. **Report type** — determine which type of report the user needs:
   - **Campaign report** — performance of a specific campaign
   - **Channel report** — performance across a specific channel (email, social, paid, SEO, etc.)
   - **Content performance** — how content pieces are performing
   - **Overall marketing report** — cross-channel summary (weekly, monthly, quarterly)
   - **Custom** — user-defined scope
2. **Time period** — the reporting window (last week, last month, last quarter, custom date range)
3. **Data source** — the Hair Solutions Co. production stack:
   - **GA4** via the Data API (traffic, behavior, e-commerce — see below)
   - **Google Ads** via Ads Scripts reporting (spend, CPA, CTR — see below)
   - **Google Search Console** for organic metrics — use the CLI in `hs-seo-audit`
   - **HubSpot (account 50966981)** for email/CRM metrics — see `hs-email-sequence` for the email stack
   - If live pulls aren't available in the host environment, ask the user: "Please paste or share your performance data. I can work with spreadsheets, CSV data, dashboard screenshots described in text, or just the key numbers."
4. **Comparison period** (optional) — prior period or year-over-year for trend context
5. **Stakeholder audience** (optional) — who will read this report (executive summary style vs. detailed analyst view)

## Data Source: Google Analytics 4 (GA4)

Analyze website traffic, user behavior, and conversions using GA4's event-based measurement model.

### Authentication

```bash
export GA4_PROPERTY_ID="properties/123456789"
export GA4_KEY_FILE="path/to/service-account-key.json"
```

GA4 API uses Google OAuth 2.0 or Service Account authentication.

### Data API — Run Reports

**Basic Traffic Report**

```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest
)

client = BetaAnalyticsDataClient.from_service_account_file(GA4_KEY_FILE)

request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    dimensions=[
        Dimension(name="sessionDefaultChannelGroup"),
        Dimension(name="deviceCategory")
    ],
    metrics=[
        Metric(name="sessions"),
        Metric(name="engagedSessions"),
        Metric(name="totalRevenue"),
        Metric(name="conversions")
    ]
)

response = client.run_report(request)

for row in response.rows:
    print([dim.value for dim in row.dimension_values],
          [metric.value for metric in row.metric_values])
```

**E-commerce Performance Report**

```python
request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="7daysAgo", end_date="yesterday")],
    dimensions=[
        Dimension(name="itemName"),
        Dimension(name="itemCategory")
    ],
    metrics=[
        Metric(name="itemsPurchased"),
        Metric(name="itemRevenue"),
        Metric(name="itemsAddedToCart"),
        Metric(name="cartToViewRate")
    ],
    order_bys=[{"metric": {"metric_name": "itemRevenue"}, "desc": True}]
)
```

**Landing Page Performance**

```python
request = RunReportRequest(
    property=GA4_PROPERTY_ID,
    date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    dimensions=[Dimension(name="landingPage")],
    metrics=[
        Metric(name="sessions"),
        Metric(name="bounceRate"),
        Metric(name="averageSessionDuration"),
        Metric(name="conversions")
    ],
    limit=25
)
```

### Key GA4 Metrics Reference

| Metric Name | Description |
| --- | --- |
| `sessions` | Total sessions |
| `activeUsers` | Users who had at least 1 engaged session |
| `engagedSessions` | Sessions > 10s or with conversion / 2+ page views |
| `engagementRate` | Engaged sessions / total sessions |
| `bounceRate` | Non-engaged sessions / total sessions |
| `averageSessionDuration` | Avg seconds per session |
| `screenPageViews` | Total page views |
| `conversions` | Events marked as conversions |
| `totalRevenue` | E-commerce revenue |
| `purchaseRevenue` | Revenue from purchases |
| `transactions` | Number of purchases |
| `ecommercePurchases` | Purchase events |

### Key Dimensions Reference

| Dimension | Values |
| --- | --- |
| `sessionDefaultChannelGroup` | Organic Search, Paid Search, Direct, Social, Email, Referral |
| `deviceCategory` | desktop, mobile, tablet |
| `country` | Country name |
| `city` | City name |
| `landingPage` | URL path |
| `pagePath` | Current page URL path |
| `sessionSourceMedium` | `google / organic`, `facebook / cpc` |
| `firstUserMedium` | Acquisition medium for new users |

### Event Tracking

GA4 collects events automatically. Key automatic events:

| Event | Trigger |
| --- | --- |
| `page_view` | Every page load |
| `scroll` | User scrolls 90% of page |
| `click` | Outbound link clicks |
| `view_search_results` | Site search |
| `video_start` / `video_complete` | YouTube embeds |
| `purchase` | E-commerce purchase |
| `add_to_cart` | Add to cart |
| `begin_checkout` | Checkout initiated |

**Custom Events (via gtag.js)**

```javascript
// Book appointment click
gtag('event', 'book_appointment_click', {
  'appointment_type': 'keratin_treatment',
  'page_location': window.location.href
});

// Product video play
gtag('event', 'product_video_play', {
  'product_name': 'Hair Restoration Kit',
  'video_title': 'Product Demo'
});

// Newsletter signup
gtag('event', 'newsletter_signup', {
  'signup_location': 'footer'
});
```

### Conversion Configuration

Mark key events as conversions in GA4 Admin → Events → Toggle "Mark as conversion":

- `purchase` (automatic for e-commerce)
- `generate_lead`
- `book_appointment_click`
- `form_submit`

### Funnel Analysis (Exploration Reports)

Build the funnel in GA4 → Explore → Funnel Exploration:

```
Step 1: page_view (where: /products)
Step 2: add_to_cart
Step 3: begin_checkout
Step 4: purchase
```

### GA4 Debugging

Use the `?gtm_debug=x` URL parameter with GTM preview mode to verify events fire correctly. Or enable GA4 DebugView: Admin → DebugView (requires `debug_mode: true` in the gtag config).

## Data Source: Google Tag Manager (Tracking Layer)

Manage all tracking and marketing tags through GTM without requiring code deployments. **Verify the tracking layer before trusting any report** — bad measurement produces confident-looking nonsense.

### Install GTM on Shopify

Add to `theme.liquid`:

```liquid
{# In <head> — first line after opening tag #}
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>

{# In <body> — immediately after opening tag #}
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

### Data Layer

Push events from Liquid to the data layer:

```liquid
{# In theme.liquid <head> — before the GTM script #}
<script>
  window.dataLayer = window.dataLayer || [];

  {%- if template.name == 'product' -%}
  dataLayer.push({
    'event': 'view_item',
    'ecommerce': {
      'items': [{
        'item_id': '{{ product.id }}',
        'item_name': '{{ product.title | escape }}',
        'item_category': '{{ product.type | escape }}',
        'price': {{ product.price | divided_by: 100.0 }},
        'currency': '{{ shop.currency }}'
      }]
    }
  });
  {%- endif -%}

  {%- if template.name == 'index' -%}
  dataLayer.push({
    'pageType': 'homepage',
    'storeLanguage': '{{ shop.locale }}'
  });
  {%- endif -%}

  {%- if customer -%}
  dataLayer.push({
    'customerEmail': '{{ customer.email }}',
    'customerId': '{{ customer.id }}',
    'customerTags': '{{ customer.tags }}'
  });
  {%- endif -%}
</script>
```

### Standard Tag Configurations

**GA4 Configuration Tag**

- **Tag Type**: Google Analytics: GA4 Configuration
- **Measurement ID**: `G-XXXXXXXXXX`
- **Trigger**: All Pages
- **Fields to Set**: `send_page_view` → `true`

**GA4 Event Tag (Purchase)**

- **Tag Type**: Google Analytics: GA4 Event
- **Event Name**: `purchase`
- **Event Parameters**:
  - `transaction_id` → `{{DLV - transaction_id}}`
  - `value` → `{{DLV - order_total}}`
  - `currency` → `{{DLV - currency}}`
  - `items` → `{{DLV - items}}`
- **Trigger**: Custom Event = `purchase`

**Meta Pixel**

- **Tag Type**: Custom HTML
- **Trigger**: All Pages

```html
<script>
!function(f,b,e,v,n,t,s){...}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{{Meta Pixel ID}}');
fbq('track', 'PageView');
</script>
```

**Meta Purchase Event**

- **Tag Type**: Custom HTML
- **Trigger**: Custom Event = `purchase`

```html
<script>
fbq('track', 'Purchase', {
  value: {{DLV - order_total}},
  currency: '{{DLV - currency}}',
  content_ids: [{{DLV - product_ids}}],
  content_type: 'product'
});
</script>
```

### Variables Setup

**Data Layer Variables** — create these DLV variables:

- `DLV - transaction_id` → `transactionId`
- `DLV - order_total` → `orderTotal`
- `DLV - currency` → `currency`
- `DLV - items` → `items`
- `DLV - product_ids` → `productIds`

**JavaScript Variable**

```javascript
// Variable Type: Custom JavaScript
// Name: CJS - Current Page Type
function() {
  return document.body.getAttribute('data-page-type') || 'unknown';
}
```

### Trigger Types

| Trigger | Use Case |
| --- | --- |
| All Pages | GA4 config, Meta Pixel PageView |
| DOM Ready | Page-specific events needing DOM |
| Custom Event | Purchase, add_to_cart, etc. |
| Click - All Elements | CTA clicks |
| Click - Just Links | External link tracking |
| Form Submission | Newsletter, contact forms |
| Timer | Engagement time tracking |
| Scroll Depth | Content engagement |

### GTM Container Audit Checklist

- [ ] No duplicate tags firing (check "Tag Firing Summary" in preview)
- [ ] All triggers use specific conditions, not "All Pages" unless needed
- [ ] Variables named consistently (type prefix: DLV-, CJS-, CON-)
- [ ] Tags have descriptive names: `GA4 - Event - Purchase`
- [ ] Old/unused tags are paused, not deleted (for history)
- [ ] Preview mode tested before every publish
- [ ] Container has notes on major changes
- [ ] Folders used to organize tags by category

### Preview & Debug

1. Click "Preview" in GTM
2. Enter your store URL
3. The GTM debugger shows which tags fire on each page
4. Check "Tag Firing Summary" for any unexpected fires
5. Click specific tags to see the exact data pushed

### Publishing Workflow

1. Create all tags/triggers/variables in draft
2. Preview and test thoroughly
3. Fix any issues found in preview
4. Add a version note describing changes
5. Submit → Publish
6. Verify in GA4 DebugView / Meta Events Manager

### Common Issues

**Tag firing multiple times**

- Add "Once per page" firing frequency to single-fire tags
- Check for duplicate trigger configurations

**Purchase not tracking**

- Verify the data layer push fires on the /thank-you page
- Check variable names match between data layer and GTM variables
- Confirm the `purchase` event reaches GA4 via DebugView

**Slow page speed from GTM**

- Audit tags — remove old/unused ones
- Consolidate: replace multiple vendor pixels with server-side GTM
- Use async loading wherever possible

## Data Source: Google Ads Scripts (Paid Data + Automation)

Automate Google Ads management using JavaScript-based Scripts — run directly in the Google Ads interface with no setup required.

### Access

Google Ads → Tools & Settings → Bulk Actions → Scripts

Scripts run in your browser context and have full access to your Google Ads account.

### Script Structure

```javascript
function main() {
  // Your script logic here

  Logger.log("Script started: " + new Date().toISOString());

  // Always log results for debugging
  Logger.log("Script completed successfully");
}
```

### Budget Pacing Script

Pause campaigns that have spent their monthly budget:

```javascript
function main() {
  var MONTHLY_BUDGET = 2000; // $2,000/month
  var today = new Date();
  var daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
  var dayOfMonth = today.getDate();
  var expectedSpend = (MONTHLY_BUDGET / daysInMonth) * dayOfMonth;

  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .get();

  var totalSpend = 0;
  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    totalSpend += campaign.getStatsFor("THIS_MONTH").getCost();
  }

  Logger.log("Total spend this month: $" + totalSpend.toFixed(2));
  Logger.log("Expected spend at this point: $" + expectedSpend.toFixed(2));

  if (totalSpend > MONTHLY_BUDGET) {
    Logger.log("OVER BUDGET — pausing campaigns");
    // Add pause logic here
    sendAlert("Google Ads over monthly budget!", totalSpend);
  }
}

function sendAlert(subject, spend) {
  MailApp.sendEmail("info@hairsolutions.co", subject,
    "Total spend: $" + spend.toFixed(2) + "\nCheck your Google Ads account.");
}
```

### Performance Alert Script

Get emailed when campaigns underperform:

```javascript
function main() {
  var ALERT_EMAIL = "info@hairsolutions.co";
  var CPA_THRESHOLD = 30; // Alert if CPA > $30
  var CTR_THRESHOLD = 0.02; // Alert if CTR < 2%

  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .withCondition("Impressions > 100")
    .forDateRange("LAST_7_DAYS")
    .get();

  var alerts = [];

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor("LAST_7_DAYS");

    var ctr = stats.getCtr();
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = conversions > 0 ? cost / conversions : null;

    if (ctr < CTR_THRESHOLD) {
      alerts.push(campaign.getName() + ": Low CTR = " + (ctr * 100).toFixed(1) + "%");
    }

    if (cpa !== null && cpa > CPA_THRESHOLD) {
      alerts.push(campaign.getName() + ": High CPA = $" + cpa.toFixed(2));
    }
  }

  if (alerts.length > 0) {
    MailApp.sendEmail(ALERT_EMAIL,
      "Google Ads Performance Alert — " + new Date().toDateString(),
      "Performance issues detected:\n\n" + alerts.join("\n"));
    Logger.log("Alerts sent: " + alerts.length);
  }
}
```

### Keyword Bid Adjustment Script

Increase bids on high-converting keywords:

```javascript
function main() {
  var MIN_CONVERSIONS = 3;
  var TARGET_CPA = 20;
  var MAX_BID = 5.00;

  var keywords = AdsApp.keywords()
    .withCondition("Status = ENABLED")
    .withCondition("Conversions >= " + MIN_CONVERSIONS)
    .forDateRange("LAST_30_DAYS")
    .get();

  while (keywords.hasNext()) {
    var keyword = keywords.next();
    var stats = keyword.getStatsFor("LAST_30_DAYS");
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = cost / conversions;

    if (cpa < TARGET_CPA) {
      // Performing well — consider bid increase
      var currentBid = keyword.bidding().getCpc();
      var newBid = Math.min(currentBid * 1.1, MAX_BID); // 10% increase, cap at $5

      if (newBid > currentBid) {
        keyword.bidding().setCpc(newBid);
        Logger.log("Increased bid for: " + keyword.getText() +
                   " from $" + currentBid + " to $" + newBid);
      }
    }
  }
}
```

### Weekly Performance Report Script

```javascript
function main() {
  var EMAIL = "info@hairsolutions.co";
  var report = [];

  report.push("Google Ads Weekly Report — " + new Date().toDateString());
  report.push("Period: Last 7 Days\n");
  report.push("CAMPAIGN PERFORMANCE:");
  report.push("Campaign | Clicks | Impressions | CTR | Conversions | Cost | CPA");
  report.push("-".repeat(80));

  var campaigns = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .forDateRange("LAST_7_DAYS")
    .get();

  var totalCost = 0, totalConversions = 0, totalClicks = 0;

  while (campaigns.hasNext()) {
    var campaign = campaigns.next();
    var stats = campaign.getStatsFor("LAST_7_DAYS");

    var clicks = stats.getClicks();
    var impressions = stats.getImpressions();
    var ctr = impressions > 0 ? (clicks / impressions * 100).toFixed(1) + "%" : "0%";
    var conversions = stats.getConversions();
    var cost = stats.getCost();
    var cpa = conversions > 0 ? "$" + (cost / conversions).toFixed(2) : "N/A";

    totalCost += cost;
    totalConversions += conversions;
    totalClicks += clicks;

    report.push([
      campaign.getName().substring(0, 30),
      clicks, impressions, ctr, conversions.toFixed(0),
      "$" + cost.toFixed(2), cpa
    ].join(" | "));
  }

  report.push("\nTOTALS:");
  report.push("Total Spend: $" + totalCost.toFixed(2));
  report.push("Total Conversions: " + totalConversions.toFixed(0));
  report.push("Total Clicks: " + totalClicks);
  report.push("Overall CPA: $" + (totalConversions > 0 ? (totalCost / totalConversions).toFixed(2) : "N/A"));

  MailApp.sendEmail(EMAIL, "Google Ads Weekly Report", report.join("\n"));
  Logger.log("Report sent to " + EMAIL);
}
```

### Scheduling Scripts

In Google Ads → Scripts, set the schedule:

- **Hourly**: Budget monitoring, impression share alerts
- **Daily**: Performance alerts, bid adjustments
- **Weekly**: Performance reports, budget pacing checks
- **Monthly**: Account health audit

### Ads Scripts Best Practices

- Always preview changes with `campaign.pause()` replaced by `Logger.log("Would pause: " + campaign.getName())`
- Test on a small subset before running on all campaigns
- Add email alerts for exceptions (`MailApp.sendEmail()`)
- Use `AdsApp.currentAccount().getCustomerId()` to identify the account in multi-account scripts
- Store configuration at the top of the script (thresholds, emails) for easy adjustment
- Version control your scripts (copy before editing)

## Report Structure

### 1. Executive Summary

- 2–3 sentence overview of performance in the period
- Headline metric with trend direction (up/down/flat vs. prior period)
- One key win and one area of concern

### 2. Key Metrics Dashboard

Present core metrics in a summary table:

| Metric | This Period | Prior Period | Change | Target | Status |
| --- | --- | --- | --- | --- | --- |

Status indicators:

- On track (meeting or exceeding target)
- At risk (below target but within acceptable range)
- Off track (significantly below target)

**Metrics by Report Type**

**Campaign Report:**

- Impressions and reach
- Click-through rate (CTR)
- Conversion rate
- Cost per acquisition (CPA)
- Return on ad spend (ROAS) or ROI
- Total conversions/signups/leads

**Channel Report (Email):**

- Emails sent, delivered, bounced
- Open rate
- Click-through rate
- Unsubscribe rate
- Conversion rate

**Channel Report (Social):**

- Impressions and reach
- Engagement rate (likes, comments, shares)
- Follower growth
- Click-through rate
- Top-performing posts

**Channel Report (Paid):**

- Spend
- Impressions and clicks
- CTR
- CPC and CPM
- Conversions and CPA
- ROAS

**Channel Report (SEO/Organic):**

- Organic sessions
- Keyword rankings (movement)
- Pages indexed
- Backlinks acquired
- Top-performing pages

**Content Performance:**

- Pageviews and unique visitors
- Time on page
- Bounce rate
- Social shares
- Conversions attributed to content
- Top and bottom performers

**Overall Marketing Report:**

- Total leads generated
- Marketing qualified leads (MQLs)
- Pipeline contribution
- Customer acquisition cost (CAC)
- Channel-by-channel summary

### 3. Trend Analysis

- Performance trend over the period (week-over-week or month-over-month)
- Notable inflection points and what caused them
- Seasonal or cyclical patterns observed
- Comparison to benchmarks or targets

### 4. What Worked

- Top 3–5 wins with specific data
- Why these performed well (hypothesis)
- How to replicate or scale

### 5. What Needs Improvement

- Bottom 3–5 performers with specific data
- Hypotheses for underperformance
- Recommended fixes

### 6. Insights and Observations

- Patterns in the data that are not obvious from the metrics alone
- Audience behavior insights
- Content or creative themes that resonated
- External factors that may have influenced performance (seasonality, news, competitive moves)

### 7. Recommendations

For each recommendation:

- What to do
- Why (linked to a specific insight from the data)
- Expected impact (high, medium, low)
- Effort to implement (high, medium, low)
- Priority (immediate, next sprint, next quarter)

Prioritize recommendations in a 2x2 matrix format:

| | Low Effort | High Effort |
| --- | --- | --- |
| **High Impact** | Do first | Plan for next sprint |
| **Low Impact** | Do if time allows | Deprioritize |

### 8. Next Period Focus

- Top 3 priorities for the upcoming period
- Tests or experiments to run
- Targets for key metrics

## Metric Definitions and Benchmarks

### Email Marketing

| Metric | Definition | Benchmark Range | What It Tells You |
| --- | --- | --- | --- |
| Delivery rate | Emails delivered / emails sent | 95–99% | List health and sender reputation |
| Open rate | Unique opens / emails delivered | 15–30% | Subject line and sender effectiveness |
| Click-through rate (CTR) | Unique clicks / emails delivered | 2–5% | Content relevance and CTA effectiveness |
| Click-to-open rate (CTOR) | Unique clicks / unique opens | 10–20% | Email content quality (for those who opened) |
| Unsubscribe rate | Unsubscribes / emails delivered | <0.5% | Content-audience fit and frequency tolerance |
| Bounce rate | Bounces / emails sent | <2% | List quality and data hygiene |
| Conversion rate | Conversions / emails delivered | 1–5% | End-to-end email effectiveness |
| Revenue per email | Total revenue / emails sent | Varies | Direct revenue attribution |
| List growth rate | (New subscribers − unsubscribes) / total list | 2–5% monthly | Audience building health |

For Hair Solutions Co. beauty/e-commerce sequence benchmarks (open 20/28/38%+, click 2.5/4/7%+, cart recovery 5/10/15%+, welcome conversion 3/7/12%+), see `hs-email-sequence`.

### Social Media

| Metric | Definition | What It Tells You |
| --- | --- | --- |
| Impressions | Number of times content was displayed | Content distribution and reach |
| Reach | Number of unique users who saw content | Audience breadth |
| Engagement rate | (Likes + comments + shares) / reach | Content resonance |
| Click-through rate | Link clicks / impressions | Traffic driving effectiveness |
| Follower growth rate | Net new followers / total followers per period | Audience building |
| Share/Repost rate | Shares / reach | Content virality and advocacy |
| Video view rate | Views / impressions | Video content hook effectiveness |
| Video completion rate | Completed views / total views | Video content quality and length fit |
| Social share of voice | Your mentions / total category mentions | Brand visibility vs. competitors |

### Paid Advertising (Search and Social)

| Metric | Definition | What It Tells You |
| --- | --- | --- |
| Impressions | Times ad was shown | Budget utilization and targeting breadth |
| Click-through rate (CTR) | Clicks / impressions | Ad creative and targeting relevance |
| Cost per click (CPC) | Total spend / clicks | Cost efficiency of traffic generation |
| Cost per mille (CPM) | Cost per 1,000 impressions | Awareness cost efficiency |
| Conversion rate | Conversions / clicks | Landing page and offer effectiveness |
| Cost per acquisition (CPA) | Total spend / conversions | Full-funnel cost efficiency |
| Return on ad spend (ROAS) | Revenue / ad spend | Revenue generation efficiency |
| Quality Score (search) | Google's relevance rating (1–10) | Ad-keyword-landing page alignment |
| Frequency | Average times a user sees the ad | Ad fatigue risk |
| View-through conversions | Conversions from users who saw but did not click | Display/awareness campaign influence |

### SEO / Organic Search

| Metric | Definition | What It Tells You |
| --- | --- | --- |
| Organic sessions | Visits from organic search | SEO effectiveness and content reach |
| Keyword rankings | Position for target keywords | Search visibility |
| Organic CTR | Clicks / impressions in search results | Title and meta description effectiveness |
| Pages indexed | Number of pages in search index | Crawlability and site health |
| Domain authority | Third-party authority score | Overall site strength |
| Backlinks | Number of external sites linking to you | Content authority and off-page SEO |
| Page load speed | Time to interactive | User experience and ranking factor |
| Organic conversion rate | Organic conversions / organic sessions | Content quality and intent alignment |
| Top entry pages | Most-visited pages from organic search | Content driving the most organic traffic |

### Content Marketing

| Metric | Definition | What It Tells You |
| --- | --- | --- |
| Pageviews | Total views of content pages | Content reach and distribution |
| Unique visitors | Distinct users viewing content | Audience size |
| Average time on page | Time spent on content pages | Content engagement and depth |
| Bounce rate | Single-page sessions / total sessions | Content-audience fit and UX |
| Scroll depth | How far users scroll on a page | Content engagement through the piece |
| Social shares | Times content was shared on social | Content resonance and virality |
| Backlinks earned | External links to content | Content authority and SEO value |
| Lead generation | Leads attributed to content | Content conversion effectiveness |
| Content ROI | Revenue attributed / content production cost | Overall content investment return |

### Overall Marketing / Pipeline

| Metric | Definition | What It Tells You |
| --- | --- | --- |
| Marketing qualified leads (MQLs) | Leads meeting marketing qualification criteria | Top-of-funnel effectiveness |
| Sales qualified leads (SQLs) | MQLs accepted by sales | Lead quality |
| MQL to SQL conversion rate | SQLs / MQLs | Marketing-sales alignment and lead quality |
| Pipeline generated | Dollar value of opportunities created | Marketing impact on revenue |
| Pipeline velocity | How fast deals move through pipeline | Campaign urgency and quality |
| Customer acquisition cost (CAC) | Total marketing + sales cost / new customers | Efficiency of customer acquisition |
| CAC payback period | Months to recover CAC from revenue | Unit economics health |
| Marketing-sourced revenue | Revenue from marketing-originated deals | Direct marketing contribution |
| Marketing-influenced revenue | Revenue from deals where marketing touched | Broader marketing impact |

## Reporting Templates by Cadence

### Weekly Marketing Report

Quick-scan format for team standups:

- **Top 3 metrics** with week-over-week change
- **What worked** this week (1–2 bullet points with data)
- **What needs attention** (1–2 bullet points with data)
- **This week's priorities** (3–5 action items)

**Hair Solutions standing weekly scope (run Monday, from GA4):**

- Sessions and engagement rate vs. prior week
- Top landing pages by sessions
- Conversions by channel
- E-commerce revenue

### Monthly Marketing Report

Standard stakeholder report:

1. Executive summary (3–5 sentences)
2. Key metrics dashboard (table with MoM and target comparison)
3. Channel-by-channel performance summary
4. Campaign highlights and results
5. What worked and what did not (with hypotheses)
6. Recommendations and next month priorities
7. Budget spend vs. plan

**Hair Solutions standing monthly scope (from GA4):**

- Channel performance trend (4-week rolling)
- Top/bottom performing products
- Geo performance
- Device split
- New vs. returning user ratio

### Quarterly Business Review (QBR)

Strategic review for leadership:

1. Quarter performance vs. goals
2. Year-to-date trajectory
3. Channel ROI analysis
4. Campaign performance summary
5. Competitive and market observations
6. Strategic recommendations for next quarter
7. Budget request and allocation plan
8. Key experiments and learnings

## Dashboard Design Principles

- Lead with the metrics that map to business objectives (not vanity metrics)
- Show trends over time, not just point-in-time snapshots
- Include comparison context: prior period, target, benchmark
