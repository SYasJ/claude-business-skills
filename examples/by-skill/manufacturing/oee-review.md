# OEE Review

`oee-review`

## What this is for

Review overall equipment effectiveness only as far as their data supports, and pick one loss to attack.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs an OEE review by 30 September 2026. A manager wants an OEE of 85 quoted to a customer, and downtime is not recorded.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A manager wants an OEE of 85 quoted to a customer, and downtime is not recorded.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Oee review**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the number and starts a downtime record before any customer claim.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Use only components they measured. Do not invent an OEE number**

**2. Define the time base they used**

**3. Pick the largest evidenced loss**

**4. Recommend one countermeasure with an owner**

**5. Do not turn OEE into a punishment metric in the write-up**

**Deliberately not done**
- An invented OEE.
- Three losses attacked at once.
- A blame report.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
