---
name: hs-call-summary
description: Process notes or a transcript from a Hair Solutions consultation or sales call — extract action items, draft a client follow-up email, log the activity in HubSpot, and update the deal stage. Use after discovery calls, treatment consultations, demos, or any client meeting.
---

# HS Call Summary

Merged from: `call-summary` (Anthropic base) + `hubspot-how-to` (HS)

## Trigger

User pastes rough notes or a transcript from a client call and wants a clean summary, follow-up email, and CRM update.

## Inputs

- Notes or transcript text (paste directly)
- Client name / HubSpot contact URL
- Call type: discovery, consultation, demo, check-in, objection handling

## Processing Sequence

1. **Extract key facts**: client stated goals, concerns raised, products or treatments discussed, pricing mentioned, timeline expectations.
2. **Identify action items**: what HS promised, what the client agreed to do, and any dependencies.
3. **Assess deal stage**: based on the conversation, recommend the correct HubSpot deal stage (e.g. Consultation Booked → Proposal Sent → Closed Won).
4. **Draft follow-up email**: Atelier Zero voice — warm, specific, no hype. Include: thank-you, summary of agreed next steps, booking link or product link if applicable.
5. **Log CRM note**: a concise internal summary (3–5 sentences) ready to paste into the HubSpot timeline.

## Output

- **Action items** (owner + deadline)
- **Deal stage recommendation** with reason
- **Client follow-up email** (ready to send, subject + body)
- **Internal HubSpot note** (paste-ready)

## Guardrails

- Do not send the follow-up or update HubSpot — present drafts for approval first.
- Do not invent details not in the notes. Mark unclear items as `[VERIFY]`.
- Follow Atelier Zero voice: no urgency language, no exclamation marks, no emoji.
