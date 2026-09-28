# Capacity Plan

`capacity-plan`

## What this is for

Plan capacity from demand and real throughput, and show the constraint before hiring or buying.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a capacity plan by 30 September 2026. A team wants three hires because the queue is long, and approvals sit for two days.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A team wants three hires because the queue is long, and approvals sit for two days.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

## Example outcome

**Capacity plan**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Tests the approval wait before treating hires as the answer.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Define the unit of work and the horizon**

**2. Use their throughput, not an industry benchmark**

**3. Name the constraint**  
people, a tool, a supplier, or a policy.

**4. Show the gap between demand and throughput in their units**

**5. Options**  
smooth demand, remove a wait, or add capacity. Adding capacity is not the default if a wait is the constraint.

**Deliberately not done**
- An invented benchmark.
- Hiring as the only option.
- A plan with no unit of work.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
