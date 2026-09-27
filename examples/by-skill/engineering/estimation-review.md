# Estimation Review

`estimation-review`

## What this is for

Review an engineering estimate by exposing assumptions, slices, and the unknown, not by demanding false precision.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an estimate review by 30 September 2026. A stakeholder wants a date for a rewrite with no scope and no prior art.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A stakeholder wants a date for a rewrite with no scope and no prior art.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Estimate review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Refuses the date, proposes a scoped spike, and offers a range only after that spike.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
