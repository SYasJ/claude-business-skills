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

The work packages: Milestone 3 handover; RAID item 12. Both unassigned as of 14 September 2026
External teams or vendors: two people on shift, one off
Dates they have given: 30 September 2026
The consequence of a slip: Milestone 3 handover, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Dependency map**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Marks the date unconfirmed and assigns an internal owner to chase it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The work packages | Milestone 3 handover; RAID item 12. Both unassigned as of 14 September 2026 | Needs confirmation |
| External teams or vendors | two people on shift, one off | Carried into the draft |
| Dates they have given | 30 September 2026 | Carried into the draft |
| The consequence of a slip | Milestone 3 handover, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. List dependencies that can slip the outcome. Internal niceties stay off the map**

**2. Each dependency needs a giver, a receiver, a date, and evidence of done**

**3. Mark dates that were not confirmed**

**4. Show the consequence of the top slip**

**5. Escalate unowned dependencies. An arrow is not an owner**

**Deliberately not done**
- Unowned arrows.
- Unconfirmed dates drawn as promises.
- A map that includes every minor task.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
