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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Marks risk unknown, requires a batched plan, and rejects credential pasting.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Intent**  
What user or reporting problem the change serves.

**2. Safety**  
Locks, rewrites, and nullability. If size is unknown, say the risk is unknown rather than approving.

**3. Backfill**  
How existing rows become valid. A constraint added before a backfill is a finding.

**4. Rollback**  
How to get back, or an explicit statement that the change is forward-only and who accepts that.

**5. Observability**  
What to watch during the migration.

**Deliberately not done**
- Approving a lock-heavy migration with unknown table size.
- A constraint before the backfill.
- Pasting production credentials into the plan.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
