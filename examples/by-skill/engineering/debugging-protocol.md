# Debugging Protocol

`debugging-protocol`

## What this is for

Debug a defect by stating the symptom, the hypothesis, and the next observation, instead of changing five things at once.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a debugging note by 30 September 2026. A bug appears only for one customer, and the draft plan changes three services before reading that customer's error.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A bug appears only for one customer, and the draft plan changes three services before reading that customer's error.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Debugging note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
A note with one hypothesis, a read-only check, and a ban on disabling auth as a debugging shortcut.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
