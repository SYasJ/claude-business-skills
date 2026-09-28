# Milestone Plan

`milestone-plan`

## What this is for

Build a milestone plan from dependencies and evidence of done, not from evenly spaced dates.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a milestone plan by 30 September 2026. A plan shows design, build, and test as three equal months with no dependency on a vendor.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A plan shows design, build, and test as three equal months with no dependency on a vendor.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Milestone plan**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Places the vendor dependency, defines evidence of done, and labels uncommitted dates.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| milestone | the customer date | Needs confirmation |
| status | slipped | Carried into the draft |
| completed tasks | do not replace the slip | Carried into the draft |
| decision | needed | Needs confirmation |

**How this draft was built**

**1. Define done for each milestone as evidence, not as a meeting**

**2. Sequence from dependencies. Do not spray dates evenly unless the work is actually even**

**3. Put external dependencies on the plan with owners**

**4. Include a buffer only if the user accepts one, and label it**

**5. Mark any date that is a wish rather than a commitment**

**Deliberately not done**
- Evenly spaced dates with no dependencies.
- A milestone that is only a meeting.
- Wish dates labeled as commitments.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
