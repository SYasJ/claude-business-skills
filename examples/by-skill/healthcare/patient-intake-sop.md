# Patient Intake SOP

`patient-intake-sop`

## What this is for

Write an intake procedure that collects only what the visit needs and tells staff when to stop and ask a clinician.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs an intake procedure by 30 September 2026. An intake script asks the front desk to decide if chest pain can wait.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

An intake script asks the front desk to decide if chest pain can wait.

The visit types: Tuesday clinic, recorded 14 September 2026. No supporting file attached
Data they truly need: Tuesday clinic. Partly documented: the what is written down, the who is not
Their privacy rules: email and billing address. They said no health data
Escalation to a clinician: Tuesday clinic, first seen 14 September 2026. No root cause recorded yet
```

## Example outcome

**Intake procedure**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Stops and escalates urgent symptoms to a clinician instead of scoring them at the desk.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The visit types | Tuesday clinic, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Data they truly need | Tuesday clinic. Partly documented: the what is written down, the who is not | Carried into the draft |
| Their privacy rules | email and billing address. They said no health data | Carried into the draft |
| Escalation to a clinician | Tuesday clinic, first seen 14 September 2026. No root cause recorded yet | Needs confirmation |

**How this draft was built**

**1. List data elements required for registration and billing they described. Cut the rest**

**2. Write the script for missing information without pressuring a patient in distress**

**3. Tell staff which answers must go to a clinician rather than be interpreted at the desk**

**4. Include identity-check steps they already use. Do not invent a legal ID rule**

**5. Protect the conversation from the waiting room when the topic is sensitive**

**Deliberately not done**
- Desk staff giving treatment advice.
- Collecting data with no purpose.
- A public conversation about a sensitive issue.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
