---
name: hs-daily-briefing
description: Start the day with a prioritized Hair Solutions sales briefing — today's appointments, follow-ups due, HubSpot open deals, Shopify revenue vs. target, pending orders, and top three priorities. Use for "morning briefing", "daily brief", "what's on my plate today", or "start my day".
---

# HS Daily Briefing

Merged from: `daily-briefing` (Anthropic base) + `hubspot-business-ops` (HS)

## Trigger

User wants a daily oriented overview to start their work session at Hair Solutions Co.

## Inputs

- Today's date (auto-detected)
- Optional: list of today's appointments or meetings if the calendar is not connected
- Optional: revenue target for the current period

## Briefing Sections

### 1. Today's Appointments

List consultations, treatments, or calls scheduled today. For each: client name, time, service, and any open prep items.

### 2. Follow-Ups Due

Pull from HubSpot: contacts with tasks due today, deals with stale last-activity (>5 days), and any email threads awaiting a reply.

### 3. Pipeline Snapshot

Open deals by stage. Flag any deal with a close date in the past or no activity in 7+ days.

### 4. Revenue Check

Shopify revenue (yesterday and month-to-date) vs. monthly target. Flag if MTD is tracking below pace.

### 5. Pending Orders and Support

Unfulfilled Shopify orders older than 24 hours. Open customer support threads in HubSpot.

### 6. Top Three Priorities

Derive from the above: the three highest-leverage actions for today.

## Output

A scannable brief with each section as a short bulleted list. Fits a single screen. Ends with the three priorities.

## Guardrails

- Do not take any action in HubSpot or Shopify while generating the brief — read-only.
- If live data is unavailable, ask the user to paste the relevant context.
