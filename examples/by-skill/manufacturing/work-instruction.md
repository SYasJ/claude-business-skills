# Work Instruction

`work-instruction`

## What this is for

Write a work instruction a new operator can follow, including the stop and the quality check.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a work instruction by 30 September 2026. An instruction says 'tighten properly' and the torque is unknown.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

An instruction says 'tighten properly' and the torque is unknown.

The outcome: An instruction says 'tighten properly' and the torque is unknown. Stated once, in the ask. Not written down anywhere else
The steps as performed safely: Line 2; Lot 26-0914. Both unassigned as of 14 September 2026
The check: Line 2, recorded 14 September 2026. No supporting file attached
The stop conditions: Line 2, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Work instruction**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Marks torque as a required input from engineering rather than inventing a number.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The outcome | An instruction says 'tighten properly' and the torque is unknown. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| The steps as performed safely | Line 2; Lot 26-0914. Both unassigned as of 14 September 2026 | Carried into the draft |
| The check | Line 2, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The stop conditions | Line 2, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. Start with the outcome and the safety precondition they require**

**2. Number steps in the order the work is done**

**3. Include the quality check and what a fail looks like**

**4. Write the stop**  
when to call a lead.

**5. Use their terms for tools and parts. Do not rename equipment**

**Deliberately not done**
- An invented setting.
- No stop condition.
- A step order that does not match the work.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
