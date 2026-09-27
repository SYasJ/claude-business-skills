# Refactor Plan

`refactor-plan`

## What this is for

Plan a refactor that improves a named risk without pretending a rewrite is free.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a refactor plan by 30 September 2026. An engineer wants six weeks to rewrite a billing module before adding a small fee change.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An engineer wants six weeks to rewrite a billing module before adding a small fee change.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Refactor plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Adds characterization tests and a smaller slice that unblocks the fee change, and treats a full rewrite as a separate decision.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
