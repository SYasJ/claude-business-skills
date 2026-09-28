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

The change: requested 14 September 2026. Not yet approved
Table size and traffic if known: 65 in the last period. No prior period attached, so no trend
Rollback idea: A migration adds a NOT NULL column with a default on a table of unknown size and has no rollback. Stated once, in the ask. Not written down anywhere else
Data correctness risk: Checkout service is open. No score in the file
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
| The change | requested 14 September 2026. Not yet approved | Needs confirmation |
| Table size and traffic if known | 65 in the last period. No prior period attached, so no trend | Carried into the draft |
| Rollback idea | A migration adds a NOT NULL column with a default on a table of unknown size and has no rollback. Stated once, in the ask. Not written down anywhere else | Carried into the draft |
| Data correctness risk | Checkout service is open. No score in the file | Needs confirmation |

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
