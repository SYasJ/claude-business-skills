# Incident Postmortem

`incident-postmortem`

## What this is for

Write a blameless postmortem that records the timeline, the impact, and the corrective actions that change a system.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a postmortem by 30 September 2026. A draft postmortem says the outage happened because 'Alex was careless'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft postmortem says the outage happened because 'Alex was careless'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Postmortem**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Replaces the blame line with the missing guardrail and one owned system fix.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
