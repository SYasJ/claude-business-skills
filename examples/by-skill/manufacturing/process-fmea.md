# Process FMEA Facilitation

`process-fmea`

## What this is for

Facilitate a process FMEA on a few high-risk steps, with actions for the failures that lack detection.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a FMEA notes by 30 September 2026. A team wants to mark a safety failure as low severity so the FMEA looks acceptable.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to mark a safety failure as low severity so the FMEA looks acceptable.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Fmea notes**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Notes that keep the high severity and assign an action instead of editing the score.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Limit the session to the steps that can hurt the customer or safety**

**2. Write failure modes as what goes wrong, not as one-word fears**

**3. Record current prevention and detection**

**4. Use their scale or a labeled simple scale. Do not pretend a score is precise**

**5. Actions go to high-severity gaps with weak detection**

**Deliberately not done**
- Lowering severity to look green.
- A whole factory in one session.
- Scores with no action.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
