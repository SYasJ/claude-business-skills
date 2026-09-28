# Clinical Documentation Quality

`clinical-documentation-quality`

## What this is for

Review documentation quality for completeness and clarity against their template, not for a diagnosis.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a documentation quality review by 30 September 2026. A manager asks to add a symptom the clinician did not record so a claim pays more.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

A manager asks to add a symptom the clinician did not record so a claim pays more.

Their template: their existing list, 6 lines. Two lines have no owner
The note or a description of gaps: Tuesday clinic is missing a source
Who signs: Dr. Helen Cho, clinic director
The handoff risk: Tuesday clinic is open. No score in the file
```

## Example outcome

**Documentation quality review**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Are truly missing.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Their template | their existing list, 6 lines. Two lines have no owner | Needs confirmation |
| The note or a description of gaps | Tuesday clinic is missing a source | Carried into the draft |
| Who signs | Dr. Helen Cho, clinic director | Carried into the draft |
| The handoff risk | Tuesday clinic is open. No score in the file | Needs confirmation |

**How this draft was built**

**1. Compare the note to their required elements. Missing elements are findings**

**2. Flag ambiguity that would confuse the next clinician, without supplying a diagnosis**

**3. Do not rewrite a note to add clinical facts that were not observed**

**4. Separate a billing-motivated addendum request from a clarity fix. Refuse invented history**

**5. Name who must correct the note under their policy**

**Deliberately not done**
- Invented history.
- A diagnosis added by the assistant.
- Coding pressure that changes the facts.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
