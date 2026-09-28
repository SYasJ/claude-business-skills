# Data Migration Plan

`data-migration-plan`

## What this is for

Plan a data migration with reconciliation counts, a freeze or dual-write choice, and a stop condition.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a data migration plan by 30 September 2026. A script copies customer records to a new store and the plan says 'check a few rows'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A script copies customer records to a new store and the plan says 'check a few rows'.

Source and target: note from Aisha Rahman, 14 September 2026. No outside report
Volume if known: 65 in the last period. No prior period attached, so no trend
Correctness rules: their one-page rule dated 2 Mar 2026. No exception log since
Downtime tolerance: five working days, due 30 September 2026
```

## Example outcome

**Data migration plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Is more than a glance.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Source and target | note from Aisha Rahman, 14 September 2026. No outside report | Needs confirmation |
| Volume if known | 65 in the last period. No prior period attached, so no trend | Carried into the draft |
| Correctness rules | their one-page rule dated 2 Mar 2026. No exception log since | Carried into the draft |
| Downtime tolerance | five working days, due 30 September 2026 | Needs confirmation |

**How this draft was built**

**1. Rules**  
What makes a row correct in the target. Write the rule before writing the job.

**2. Method**  
Dual-write, backfill, or freeze, chosen from their tolerance. Do not pick a method they cannot operate.

**3. Reconciliation**  
Counts and checksums or samples they can actually run. A migration without reconciliation is a guess.

**4. Stop**  
The mismatch that halts the job.

**5. Privacy**  
Do not copy data into a less protected place for convenience. No exports of secrets into tickets.

**Deliberately not done**
- A migration with no reconciliation.
- Copying sensitive data into a ticket.
- A method the team cannot operate.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
