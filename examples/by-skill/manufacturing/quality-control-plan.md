# Quality Control Plan

`quality-control-plan`

## What this is for

Draft a control plan for a process step: what is checked, how often, and what happens on a fail.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a control plan by 30 September 2026. A plan checks a safety dimension weekly because daily checks feel expensive.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A plan checks a safety dimension weekly because daily checks feel expensive.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Control plan**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Keeps the safety check at the frequency their rule requires and flags the cost as a separate decision.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Name the characteristic that matters to the customer or the safety rule they cited**

**2. Specify method and frequency they can staff**

**3. Write the reaction to a fail**  
stop, sort, or call. A fail with no reaction is a finding.

**4. Identify the owner of the check**

**5. Do not loosen a limit they said is safety-related**

**Deliberately not done**
- A check with no reaction.
- Loosening a safety limit.
- An unstaffed frequency.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
