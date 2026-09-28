# Sunset Plan

`sunset-plan`

## What this is for

Plan the retirement of a feature or product so users are told the truth and given a path.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a sunset plan by 30 September 2026. Engineering wants to delete an API next week that three customers still call.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Engineering wants to delete an API next week that three customers still call.

What is being retired: Usage limit warning, last reviewed 14 September 2026. No owner named since
Who uses it, if known: Jonah Park, product manager
The replacement, if any: Activation checklist, recorded 14 September 2026. No supporting file attached
Contractual constraints the user mentioned: no extra headcount, and no result that is not in this file
```

## Example outcome

**Sunset plan**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the deletion until notice and a migration owner exist, and flags contract questions.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What is being retired | Usage limit warning, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| Who uses it, if known | Jonah Park, product manager | Carried into the draft |
| The replacement, if any | Activation checklist, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Contractual constraints the user mentioned | no extra headcount, and no result that is not in this file | Needs confirmation |

**How this draft was built**

**1. Why**  
The reason to retire, in plain language. Cost, risk, or focus. Do not invent usage data.

**2. Who is affected**  
Use their data. If you do not know who uses it, the first step is to find out before announcing.

**3. Path**  
The replacement or the workaround, including what it does not cover.

**4. Timeline**  
Notice, migration window, and removal date that the user can honor. No fake date.

**5. Support**  
Who answers migration questions. A sunset email with no owner creates a support incident.

**Deliberately not done**
- A surprise removal.
- Advising the company to ignore a contract.
- An announcement with no migration path and no owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
