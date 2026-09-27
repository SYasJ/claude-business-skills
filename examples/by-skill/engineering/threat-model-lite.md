# Lightweight Threat Model

`threat-model-lite`

## What this is for

Sketch a defensive threat model for a feature: assets, actors, abuses, and controls. No exploit steps.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a threat model note by 30 September 2026. A file-sharing feature has no answer for who can access a link.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A file-sharing feature has no answer for who can access a link.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Threat model note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Lists unauthorized access as a gap, recommends an access control and audit event, and includes no exploit procedure.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
