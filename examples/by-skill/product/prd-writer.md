# PRD Writer

`prd-writer`

## What this is for

Write a product requirements document with a problem, scope, acceptance signals, and explicit non-goals.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a PRD by 30 September 2026. A PRD draft lists 15 features and no user outcome.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A PRD draft lists 15 features and no user outcome.

Problem and user: A PRD draft lists 15 features and no user outcome. Stated once, in the ask. Not written down anywhere else
Proposed scope: this decision only
Constraints: no extra headcount, and no result that is not in this file
Open questions: A PRD draft lists 15 features and no user outcome
```

## Example outcome

**Prd**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A rewritten PRD with one outcome, a small slice, testable acceptance, and the other features as non-goals.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Problem and user | A PRD draft lists 15 features and no user outcome. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| Proposed scope | this decision only | Carried into the draft |
| Constraints | no extra headcount, and no result that is not in this file | Carried into the draft |
| Open questions | A PRD draft lists 15 features and no user outcome | Needs confirmation |

**How this draft was built**

**1. Problem and outcome**  
What will be true for the user if this ships. No outcome, no PRD.

**2. Scope**  
The smallest slice that tests the outcome. Cut the rest into non-goals.

**3. Flows**  
The main path and the important failure path. Do not specify every pixel unless the user asked for design detail.

**4. Acceptance**  
Observable signals that the slice works. 'Feels better' is not acceptance.

**5. Analytics and risks**  
What you will measure, and the risk you are accepting. Do not invent baseline numbers.

**Deliberately not done**
- A PRD that is only a solution.
- Hidden non-goals.
- Acceptance criteria nobody can test.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
