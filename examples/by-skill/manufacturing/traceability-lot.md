# Lot Traceability

`traceability-lot`

## What this is for

Plan a lot trace from finished goods back to material, or the reverse, and record the breaks.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a trace exercise by 30 September 2026. A mock recall stops because a component lot was never recorded.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A mock recall stops because a component lot was never recorded.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Trace exercise**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Records the break, times the exercise, and assigns the recording gap.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Define the question**  
where did this lot go, or what went into it.

**2. Use their systems. Do not invent genealogy**

**3. Record every break where the link is missing**

**4. Time the exercise. A trace that takes days is a finding if their target is hours**

**5. Name the owner of each break**

**Deliberately not done**
- Invented genealogy.
- A trace that hides a break.
- Shipping a held lot.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
