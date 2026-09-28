# Test Strategy

`test-strategy`

## What this is for

Choose a test strategy for a change that matches risk, instead of demanding every kind of test.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a test strategy note by 30 September 2026. A team argues about coverage percent while a refund path has no test.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team argues about coverage percent while a refund path has no test.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Test strategy note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Prioritizes the refund path and treats the coverage number as secondary.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Risk**  
Where a bug would hurt users, money, or data. Tests follow risk.

**2. Layer**  
Unit, integration, or end-to-end, chosen for the risk. Do not demand an end-to-end test for a pure function by reflex.

**3. Gaps**  
The specific case that is untested. Name it.

**4. Flakes**  
Do not add a known-flaky test as the only safety net. Say so.

**5. Non-goals**  
What you will not automate now, and why.

**Deliberately not done**
- Coverage percentage as the goal.
- A flaky end-to-end test as the only check.
- No test on a payments or auth change.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
