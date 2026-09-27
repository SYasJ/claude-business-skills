# Dependency Map

`dependency-map`

## What this is for

Map delivery dependencies so external waits have owners and dates, not just arrows.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a dependency map by 30 September 2026. A Gantt chart shows a vendor delivery with no named vendor owner.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A Gantt chart shows a vendor delivery with no named vendor owner.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Dependency map**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026

**Decision**
Marks the date unconfirmed and assigns an internal owner to chase it.

**From the file**
- milestone: the customer date
- status: slipped
- completed tasks: do not replace the slip
- decision: needed

Nothing in this draft was added from outside that file.
Next: Owen Blake by 30 September 2026. This is not a sign-off.
