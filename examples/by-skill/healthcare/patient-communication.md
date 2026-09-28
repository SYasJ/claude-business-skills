# Patient Communication Draft

`patient-communication`

## What this is for

Draft a patient message in plain language that a clinician or clinic lead approves before sending.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a patient message by 30 September 2026. A draft tells a patient to double a medicine because the refill is late.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

A draft tells a patient to double a medicine because the refill is late.

The purpose: A draft tells a patient to double a medicine because the refill is late. Stated once, in the ask. Not written down anywhere else
Facts a clinician confirmed: Thursday clinic and one other, both unconfirmed as of 14 September 2026
The reading level they want: Tuesday clinic, recorded 14 September 2026. No supporting file attached
The approval owner: Dr. Helen Cho, clinic director
```

## Example outcome

**Patient message**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the dose change, explains the operational status, and waits for clinician approval.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The purpose | A draft tells a patient to double a medicine because the refill is late. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| Facts a clinician confirmed | Thursday clinic and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| The reading level they want | Tuesday clinic, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The approval owner | Dr. Helen Cho, clinic director | Needs confirmation |

**How this draft was built**

**1. State the purpose in the first line**

**2. Include only facts a clinician or the record confirmed. Do not add advice, doses, or a diagnosis**

**3. Tell the patient who to call if symptoms worry them, using their escalation line**

**4. Avoid blame and jargon**

**5. Mark the draft unsent until the named clinician or lead approves it**

**Deliberately not done**
- Doses or new diagnoses.
- An unapproved clinical instruction.
- Another patient's data.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
