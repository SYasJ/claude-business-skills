# Scope Change Control

`scope-change-control`

## What this is for

Write a scope change so the sponsor sees the trade before the team absorbs it silently.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a change request by 30 September 2026. A stakeholder adds a report and says it is tiny, with no estimate.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A stakeholder adds a report and says it is tiny, with no estimate.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Change request**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the silent add and offers a trade against the baseline.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| milestone | the customer date | Needs confirmation |
| status | slipped | Carried into the draft |
| completed tasks | do not replace the slip | Carried into the draft |
| decision | needed | Needs confirmation |

**How this draft was built**

**1. Restate the request and who asked**

**2. Show the impact on the binding constraint**

**3. Offer options**  
add time, add cost, or remove something else.

**4. Recommend one option. Silent absorption is not an option to hide**

**5. Name the decider. The delivery team does not accept scope by being polite**

**Deliberately not done**
- Absorbing scope with no record.
- A change with no impact.
- The team acting as the decider by default.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
