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
Date: 14 September 2026

**Decision**
Places the vendor dependency, defines evidence of done, and labels uncommitted dates.

**From the file**
- milestone: the customer date
- status: slipped
- completed tasks: do not replace the slip
- decision: needed

Nothing in this draft was added from outside that file.
Next: Owen Blake by 30 September 2026. This is not a sign-off.
