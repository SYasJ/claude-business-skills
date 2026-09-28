# Nonconformance Report

`nonconformance-report`

## What this is for

Write a nonconformance report that contains the fact, the containment, and the owner.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a NCR by 30 September 2026. A report says 'bad parts' and the suspect lot is still being shipped.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A report says 'bad parts' and the suspect lot is still being shipped.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Ncr**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Stops the lot, describes the defect, and names the owner.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Describe the defect in observable terms**

**2. Record quantity and location only from their count**

**3. Containment first**  
stop the escape path they named.

**4. Do not dispose of evidence they said must be kept**

**5. Separate containment from root-cause work**

**Deliberately not done**
- A vague defect description.
- Disposing of required evidence.
- No containment.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
