# RAID Log

`raid-log`

## What this is for

Maintain a RAID log that separates risks, assumptions, issues, and dependencies, each with an owner.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a RAID log by 30 September 2026. A dependency has already missed its date and is still labeled a risk.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A dependency has already missed its date and is still labeled a risk.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Raid log**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026

**Decision**
Reclassifies it as an issue, names the owner, and shows the delivery impact.

**From the file**
- milestone: the customer date
- status: slipped
- completed tasks: do not replace the slip
- decision: needed

Nothing in this draft was added from outside that file.
Next: Owen Blake by 30 September 2026. This is not a sign-off.
