# Database Change Review

`database-change-review`

## What this is for

Review a schema or data change for safety, rollback, and lock risk before it reaches production.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a database change review by 30 September 2026. A migration adds a NOT NULL column with a default on a table of unknown size and has no rollback.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A migration adds a NOT NULL column with a default on a table of unknown size and has no rollback.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Database change review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Marks risk unknown, requires a batched plan, and rejects credential pasting.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
