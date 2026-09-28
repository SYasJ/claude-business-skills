# Analysis Plan

`analysis-plan`

## What this is for

Plan an analysis so the question, the data, and the decision rule are fixed before the slicing starts.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs an analysis plan by 30 September 2026. A team wants to know why conversion fell and plans to look at twelve dimensions with no primary comparison.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to know why conversion fell and plans to look at twelve dimensions with no primary comparison.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Analysis plan**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A plan with one primary comparison, the missing data called out, and a decision rule written first.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Restate the decision. An analysis with no decision is a tour**

**2. Write the comparison**  
against what period, segment, or control.

**3. List the data you have and the data you do not. Do not plan around a table nobody can access**

**4. Pre-commit the cut that would change the decision**

**5. Name biases in the sample the user described**

**Deliberately not done**
- Slicing until a flattering story appears.
- Assuming a dataset you cannot see.
- A notebook with no decision.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
