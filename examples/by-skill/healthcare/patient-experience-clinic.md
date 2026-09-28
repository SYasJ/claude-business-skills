# Clinic Experience Review

`patient-experience-clinic`

## What this is for

Review a clinic experience problem using waits, communication, and respect, without blaming the patient.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a clinic experience review by 30 September 2026. Patients wait 70 minutes and the draft response tells staff to smile more.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

Patients wait 70 minutes and the draft response tells staff to smile more.

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

## Example outcome

**Clinic experience review**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Treats the wait as a capacity problem and limits the script to truthful status updates.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| clinic | Cedar, Tuesday list | Needs confirmation |
| diagnosis | not in this note | Carried into the draft |
| roster | the one attached | Carried into the draft |
| advice to a patient | not written | Needs confirmation |

**How this draft was built**

**1. Describe the failed moment**  
wait, confusion, or disrespect.

**2. Use their wait data or mark it unknown**

**3. Separate a capacity problem from a courtesy problem**

**4. Recommend one change staff can make this month**

**5. Do not identify a patient in a broader share-out**

**Deliberately not done**
- Blaming the patient.
- Identifying a patient in a public note.
- A courtesy script for a capacity failure.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
