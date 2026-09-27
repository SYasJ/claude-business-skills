# Runbook Writer

`runbook-writer`

## What this is for

Write a runbook a tired on-call engineer can follow, with checks, stops, and escalation.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a runbook by 30 September 2026. A draft runbook starts by deleting a production table if an alert fires.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft runbook starts by deleting a production table if an alert fires.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Runbook**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Starts with read-only checks, removes the destructive first step, and escalates before any data deletion.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
