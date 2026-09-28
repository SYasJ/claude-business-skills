# Stakeholder PRD Review

`stakeholder-prd-review`

## What this is for

Review a PRD with stakeholders by separating decisions from opinions and parking out-of-scope demands.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a PRD review notes by 30 September 2026. Sales adds six prospect requests during a PRD review, and engineering thinks they are now committed.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales adds six prospect requests during a PRD review, and engineering thinks they are now committed.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

## Example outcome

**Prd review notes**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Notes that park the six requests, restate the surviving scope, and name the decider for any conflict.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| interviews | 12, March to June 2026 | Needs confirmation |
| decision | ship, hold, or cut | Carried into the draft |
| metric | not defined | Carried into the draft |
| kill line | not written | Needs confirmation |

**How this draft was built**

**1. Outcome check**  
Can every reviewer state the user outcome. If not, fix that before debating details.

**2. Classify comments**  
Decision, risk, or preference. Preferences do not silently change scope.

**3. Conflicts**  
Where two stakeholders demand incompatible scope, write the tradeoff and the decider.

**4. Parking lot**  
Out-of-scope requests go to the parking lot with a reason, not into the PRD out of politeness.

**5. Open questions**  
Owner and date. Unowned questions are the real launch risk.

**Deliberately not done**
- Adding every comment to the spec.
- Leaving the review with two different scopes in people's heads.
- Treating every preference as a requirement.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
