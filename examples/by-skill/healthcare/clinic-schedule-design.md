# Clinic Schedule Design

`clinic-schedule-design`

## What this is for

Design a clinic schedule around visit types and staffing, without pretending to triage medical urgency.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a clinic schedule by 30 September 2026. A manager wants to double-book every slot because the wait list is long.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

A manager wants to double-book every slot because the wait list is long.

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

## Example outcome

**Clinic schedule**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026

**Decision**
Shows the double-book harm and offers an access hold only within real room capacity.

**From the file**
- clinic: Cedar, Tuesday list
- diagnosis: not in this note
- roster: the one attached
- advice to a patient: not written

Nothing in this draft was added from outside that file.
Next: Dr. Helen Cho by 30 September 2026. This is not a sign-off.
