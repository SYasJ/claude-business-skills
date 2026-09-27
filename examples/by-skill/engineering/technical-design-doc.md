# Technical Design Doc

`technical-design-doc`

## What this is for

Write a technical design that states the problem, the constraints, the chosen approach, and the rejected alternative.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a technical design doc by 30 September 2026. An engineer proposes a new service but has not said what happens when the dependency is down.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An engineer proposes a new service but has not said what happens when the dependency is down.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Technical design doc**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
A design doc with the failure behavior, one rejected alternative, and a rollback path.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
