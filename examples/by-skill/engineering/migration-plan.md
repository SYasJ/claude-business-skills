# Migration Plan

`migration-plan`

## What this is for

Plan a migration from one system or contract to another with a dual-run, a cutover, and a backout.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a migration plan by 30 September 2026. A team plans to switch billing systems over a weekend with no way to compare invoices.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team plans to switch billing systems over a weekend with no way to compare invoices.

Source and target: note from Aisha Rahman, 14 September 2026. No outside report
Data or traffic involved: 75 in the last period. No prior period attached, so no trend
Downtime tolerance: five working days, due 30 September 2026
Verification method: the method in the ask. No second design attached
```

## Example outcome

**Migration plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Adds a comparison phase and names the point of no return before any weekend cutover is approved.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Source and target | note from Aisha Rahman, 14 September 2026. No outside report | Needs confirmation |
| Data or traffic involved | 75 in the last period. No prior period attached, so no trend | Carried into the draft |
| Downtime tolerance | five working days, due 30 September 2026 | Carried into the draft |
| Verification method | the method in the ask. No second design attached | Needs confirmation |

**How this draft was built**

**1. Inventory**  
What moves, and what must not move, from their description.

**2. Dual run**  
How both sides can be compared before cutover. If comparison is impossible, say the risk is higher.

**3. Cutover**  
The steps, the owner, and the go/no-go check.

**4. Backout**  
The point of no return. Before it, how to return. After it, who accepts forward-only.

**5. Communication**  
Who is told, including support. No customer claim you cannot honor.

**Deliberately not done**
- A cutover with no backout and no accepted point of no return.
- Inventing record counts.
- A migration communicated as zero-risk.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
