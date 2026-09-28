# Pull Request Description

`pr-description`

## What this is for

Write a pull request description that explains the why, the risk, and how to test.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a pull request description by 30 September 2026. A PR titled 'updates' changes a payment calculation and the description is empty.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A PR titled 'updates' changes a payment calculation and the description is empty.

What changed: requested 14 September 2026. Not yet approved
Why: A PR titled 'updates' changes a payment calculation and the description is empty
Risks and rollout: Checkout service is open. No score in the file
```

## Example outcome

**Pull request description**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
States the payment behavior, the missing test if none was run, and the rollback.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What changed | requested 14 September 2026. Not yet approved | Needs confirmation |
| Why | A PR titled 'updates' changes a payment calculation and the description is empty | Carried into the draft |
| Risks and rollout | Checkout service is open. No score in the file | Carried into the draft |

**How this draft was built**

**1. Why**  
The user or operator problem, not a restatement of the diff.

**2. What**  
The approach in a few lines. Point to the design if there is one.

**3. Test**  
The steps a reviewer can run, and the cases you did not test.

**4. Risk**  
Migrations, flags, and user-visible changes.

**5. Screens or samples**  
Only if the user supplied them. Do not invent output.

**Deliberately not done**
- A description that says 'fix bug'.
- Claiming tests you did not run.
- Hidden migration risk.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
