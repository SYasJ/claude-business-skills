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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows the double-book harm and offers an access hold only within real room capacity.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| clinic | Cedar, Tuesday list | Needs confirmation |
| diagnosis | not in this note | Carried into the draft |
| roster | the one attached | Carried into the draft |
| advice to a patient | not written | Needs confirmation |

**How this draft was built**

**1. Separate visit types they already use. Do not invent clinical priorities**

**2. Fit the template to rooms and staffing they named**

**3. Hold a small portion for same-day access only if they asked for that operational goal**

**4. Show what happens on a provider absence**

**5. Do not promise a wait time the template cannot support**

**Deliberately not done**
- Clinical triage disguised as a template.
- A template that ignores rooms.
- A promised wait they cannot meet.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
