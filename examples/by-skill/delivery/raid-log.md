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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Reclassifies it as an issue, names the owner, and shows the delivery impact.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| milestone | the customer date | Needs confirmation |
| status | slipped | Carried into the draft |
| completed tasks | do not replace the slip | Carried into the draft |
| decision | needed | Needs confirmation |

**How this draft was built**

**1. Classify each item**  
risk, assumption, issue, or dependency. An issue is already happening.

**2. Give each item one owner and a next date**

**3. Write the impact in delivery terms**

**4. Close items that are no longer true rather than letting the log rot**

**5. Escalate dependencies the team cannot move**

**Deliberately not done**
- A log with no owners.
- An issue disguised as a risk.
- A log nobody closes.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
