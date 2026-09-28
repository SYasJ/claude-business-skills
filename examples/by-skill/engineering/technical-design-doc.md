# Technical Design Doc

`technical-design-doc`

## What this is for

Write a technical design that states the problem, the constraints, the chosen approach, and the rejected alternative.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a technical design doc by 30 September 2026. An engineer proposes a new service but has not said what happens when the dependency is down.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An engineer proposes a new service but has not said what happens when the dependency is down.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Technical design doc**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A design doc with the failure behavior, one rejected alternative, and a rollback path.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Problem**  
What must change for the user or operator, and why now.

**2. Context**  
The current system only as far as the decision needs. Do not invent architecture that is not in the repo or the user's description.

**3. Decision**  
The approach, the tradeoff, and one rejected alternative. A design with no alternative is a preference.

**4. Interfaces**  
Data, APIs, and failure behavior. Include the unhappy path.

**5. Risks**  
Migration, security, and operability. Security risks get a defensive control, not an exploit note.

**Deliberately not done**
- A design that invents the current system.
- No rejected alternative.
- Security described as 'we will add it later' with no owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
