# Evidence Table

`evidence-table`

## What this is for

Build an evidence table from sources the user supplied, with columns that match the question.

## Scenario

Dr. Nia Okonkwo, research lead at Riverbend College in Lethbridge, needs an evidence table by 30 September 2026. A table has effect sizes the user never found in the papers.

## Example data

```text
From: Dr. Nia Okonkwo, research lead
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

A table has effect sizes the user never found in the papers.

The question: A table has effect sizes the user never found in the papers
The sources they have: note from Dr. Nia Okonkwo, 14 September 2026. No outside report
The fields to extract: Interview set A, recorded 14 September 2026. No supporting file attached
Inclusion status: Interview set A. Stated in the ask, not documented anywhere else
```

## Example outcome

**Evidence table**
To: Dr. Nia Okonkwo, research lead, Riverbend College
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A table with those cells marked unknown and a warning against a numeric conclusion.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The question | A table has effect sizes the user never found in the papers | Needs confirmation |
| The sources they have | note from Dr. Nia Okonkwo, 14 September 2026. No outside report | Carried into the draft |
| The fields to extract | Interview set A, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Inclusion status | Interview set A. Stated in the ask, not documented anywhere else | Needs confirmation |

**How this draft was built**

**1. Columns follow the question**  
population, method, finding, limit.

**2. Extract only what the source they provided actually says**

**3. Mark a field unknown rather than filling it from memory**

**4. Keep excluded sources in a short log with the reason**

**5. Do not add a source you cannot identify**

**Deliberately not done**
- Cells filled from memory.
- Ghost sources.
- A conclusion the table does not support.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Nia Okonkwo by 30 September 2026. This is a draft, not a sign-off.
