# SLA Design

`sla-design`

## What this is for

Design a service level that matches a customer promise the team can measure and staff.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a service level design by 30 September 2026. Sales promises a one-hour response and the queue currently averages a day.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

Sales promises a one-hour response and the queue currently averages a day.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

## Example outcome

**Service level design**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Exposes the gap and proposes either a truthful promise or a staffed path, with no silent reclassification.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Start from the promise already made. If operations cannot meet it, the finding is the promise or the staffing, not a prettier SLA**

**2. Define the clock**  
when it starts and stops, and which tickets count.

**3. Set a target from their history or mark it as a proposal**

**4. Add an exception path for cases the SLA should not pretend to cover**

**5. Name the measure and the owner**

**Deliberately not done**
- An SLA nobody measures.
- Reclassifying misses.
- A target copied from a competitor.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
