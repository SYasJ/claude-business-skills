# Observability Plan

`observability-plan`

## What this is for

Specify the logs, metrics, and traces a service needs to debug a user-facing failure.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an observability plan by 30 September 2026. A plan logs the full Authorization header to 'make debugging easier'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A plan logs the full Authorization header to 'make debugging easier'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Observability plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Forbids that header, specifies a request id, and pages only on user-facing errors.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
