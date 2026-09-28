# Debugging Protocol

`debugging-protocol`

## What this is for

Debug a defect by stating the symptom, the hypothesis, and the next observation, instead of changing five things at once.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a debugging note by 30 September 2026. A bug appears only for one customer, and the draft plan changes three services before reading that customer's error.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A bug appears only for one customer, and the draft plan changes three services before reading that customer's error.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Debugging note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A note with one hypothesis, a read-only check, and a ban on disabling auth as a debugging shortcut.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Symptom**  
What the user or system does, and what was expected. Include the error text they provided. Do not invent logs.

**2. Boundary**  
Where it last worked. Version, user, or data slice.

**3. Hypothesis**  
One hypothesis that predicts a new observation.

**4. Observation**  
The safest check that would confirm or kill it. Read-only before write actions.

**5. Change**  
Only after the observation. One change at a time.

**Deliberately not done**
- Changing five things at once.
- Inventing log lines.
- Disabling auth to debug.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
