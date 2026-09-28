# Production Schedule Review

`production-schedule`

## What this is for

Review a production schedule against capacity, materials, and the promise that will slip first.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a schedule review by 30 September 2026. The schedule loads 120 hours into an 80-hour cell and the status is on time.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

The schedule loads 120 hours into an 80-hour cell and the status is on time.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Schedule review**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Cuts or sequences to 80 hours and names the promise that moves.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Show the constraint**  
labor, machine, or material, from their facts.

**2. Do not schedule over the constraint and call it a plan**

**3. Honor a frozen window they have. Changes inside it need a named approver**

**4. Identify the customer promise that slips first**

**5. Recommend a sequence rule they can repeat, not a daily argument**

**Deliberately not done**
- A schedule over known capacity.
- Silent changes inside a freeze.
- No view of the first slipped promise.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
