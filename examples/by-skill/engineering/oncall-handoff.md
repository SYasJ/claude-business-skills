# On-Call Handoff

`oncall-handoff`

## What this is for

Write an on-call handoff that tells the next person what is on fire, what is quiet, and how to escalate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an on-call handoff by 30 September 2026. The outgoing engineer writes 'should be fine' after a migration that has not been verified.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The outgoing engineer writes 'should be fine' after a migration that has not been verified.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**On-call handoff**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Lists the unverified migration, the check to run, and the escalation owner.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
