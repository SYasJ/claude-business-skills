# Accessibility Product Review

`accessibility-review`

## What this is for

Review a product flow for accessibility barriers and turn them into concrete fixes, not a vague pledge.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs an accessibility review by 30 September 2026. A checkout cannot be completed by keyboard, and the team wants a statement saying the product is accessible.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A checkout cannot be completed by keyboard, and the team wants a statement saying the product is accessible.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

## Example outcome

**Accessibility review**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the statement, names the keyboard barrier, and lists the fix and retest.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| interviews | 12, March to June 2026 | Needs confirmation |
| decision | ship, hold, or cut | Carried into the draft |
| metric | not defined | Carried into the draft |
| kill line | not written | Needs confirmation |

**How this draft was built**

**1. Scope the flow**  
One important path, not the whole product in one sitting.

**2. Barriers**  
Keyboard, labels, contrast, errors, and media alternatives, based on the material provided. Do not claim a conformance audit you did not perform.

**3. Impact**  
Who is blocked from the job, in practical terms.

**4. Fixes**  
Specific design or engineering changes, ordered by who is completely blocked.

**5. Tests**  
How the team can recheck the flow. Automated scans are a start, not a certificate.

**Deliberately not done**
- Claiming compliance from a glance.
- A pledge with no fixes.
- Ignoring a reported blocker because the visual design looks fine.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
