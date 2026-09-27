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

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

## Example outcome

**Patient message**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026

**Decision**
Removes the dose change, explains the operational status, and waits for clinician approval.

**From the file**
- clinic: Cedar, Tuesday list
- diagnosis: not in this note
- roster: the one attached
- advice to a patient: not written

Nothing in this draft was added from outside that file.
Next: Dr. Helen Cho by 30 September 2026. This is not a sign-off.
