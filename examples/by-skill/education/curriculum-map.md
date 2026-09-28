# Curriculum Map

`curriculum-map`

## What this is for

Map a curriculum so outcomes, courses, and assessments line up without gaps or pointless overlap.

## Scenario

Mark Ellison, program chair at Riverbend College in Lethbridge, needs a curriculum map by 30 September 2026. A program claims a communication outcome and no course assesses it.

## Example data

```text
From: Mark Ellison, program chair
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

A program claims a communication outcome and no course assesses it.

course: the one named
section: the one they teach
student submission: not written for them
due: 30 Sep 2026
```

## Example outcome

**Curriculum map**
To: Mark Ellison, program chair, Riverbend College
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows the gap and recommends where an assessment should sit.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| course | the one named | Needs confirmation |
| section | the one they teach | Carried into the draft |
| student submission | not written for them | Carried into the draft |
| due | 30 Sep 2026 | Needs confirmation |

**How this draft was built**

**1. List program outcomes the user confirmed. Do not invent accreditation standards**

**2. Show where each outcome is taught and assessed. An outcome with no assessment is a gap**

**3. Mark redundant assessments that do not add evidence**

**4. Sequence prerequisites they actually require**

**5. Note workload spikes**

**Deliberately not done**
- Invented accreditation clauses.
- An outcome never assessed.
- A map that hides workload spikes.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mark Ellison by 30 September 2026. This is a draft, not a sign-off.
