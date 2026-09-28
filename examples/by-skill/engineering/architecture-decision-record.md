# Architecture Decision Record

`architecture-decision-record`

## What this is for

Record an architecture decision with context, the decision, and the consequences, in a page.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an architecture decision record by 30 September 2026. A team chose a queue technology in a meeting and nobody wrote why the simpler option lost.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team chose a queue technology in a meeting and nobody wrote why the simpler option lost.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Architecture decision record**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A one-page ADR with the rejected option, consequences, and status left as proposed until they accept it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Title and status**  
Proposed, accepted, or superseded. Do not mark accepted if the user has not accepted it.

**2. Context**  
The forces, from their system. No fictional scale numbers.

**3. Decision**  
One paragraph. What you will do.

**4. Alternatives**  
At least one rejected option and why.

**5. Consequences**  
What becomes easier, what becomes harder, and the security or operability effect.

**Deliberately not done**
- An ADR that is a tutorial.
- No alternative.
- Marking a draft as accepted.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
