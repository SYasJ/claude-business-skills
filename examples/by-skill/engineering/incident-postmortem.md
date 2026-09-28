# Incident Postmortem

`incident-postmortem`

## What this is for

Write a blameless postmortem that records the timeline, the impact, and the corrective actions that change a system.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a postmortem by 30 September 2026. A draft postmortem says the outage happened because 'Alex was careless'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft postmortem says the outage happened because 'Alex was careless'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Postmortem**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Replaces the blame line with the missing guardrail and one owned system fix.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Facts**  
A timeline with times and sources. Unknowns stay unknown. Do not invent a root cause to close the doc.

**2. Impact**  
Who was affected and how, using the user's data. No inflated or minimized impact.

**3. Contributing factors**  
System and process, not a villain. Human error is a prompt to ask why the system allowed it.

**4. Detection**  
How it was found, and how it could be found sooner without a surveillance program on people.

**5. Actions**  
A few actions with owners that change code, config, or process. A lesson with no owner is a wish.

**Deliberately not done**
- A blame essay.
- An invented root cause.
- Twenty actions and no owners.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
