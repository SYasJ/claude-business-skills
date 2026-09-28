# Incoming Inspection

`incoming-inspection`

## What this is for

Plan incoming inspection for a material based on risk and the reaction to a failed lot.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs an incoming inspection plan by 30 September 2026. Failed material is left on the issue shelf so the line does not stop.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

Failed material is left on the issue shelf so the line does not stop.

The material risk: Line 2 is open. No score in the file
The characteristics: Line 2, recorded 14 September 2026. No supporting file attached
Sample practice they use: Gauge 7, recorded 14 September 2026. No supporting file attached
Fail reaction: Line 2; Lot 26-0914. Both unassigned as of 14 September 2026
```

## Example outcome

**Incoming inspection plan**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Moves failed material to hold and requires a named deviation before any use.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The material risk | Line 2 is open. No score in the file | Needs confirmation |
| The characteristics | Line 2, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Sample practice they use | Gauge 7, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Fail reaction | Line 2; Lot 26-0914. Both unassigned as of 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Tie inspection to risk. Critical characteristics are not sampled away because the dock is busy, if their rule says so**

**2. Write the accept and fail reaction**

**3. Identify the hold location so failed material cannot be issued**

**4. Feed repeats to supplier quality**

**5. Do not skip a hold to keep a line running unless the user names a deviation owner**

**Deliberately not done**
- A failed lot left in the issue location.
- Skipping a critical check for speed.
- No fail reaction.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
