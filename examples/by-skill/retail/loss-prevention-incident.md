# Loss Prevention Incident Log

`loss-prevention-incident`

## What this is for

Write a factual loss prevention incident log from the events the user described, without accusations beyond what evidence supports.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a LP incident log by 30 September 2026. A log says "the suspect stole the item" based on a single camera angle that does not show concealment.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A log says "the suspect stole the item" based on a single camera angle that does not show concealment.

What was observed: Returns desk log, last reviewed 14 September 2026. No owner named since
Timestamps and locations: five working days, due 30 September 2026
What evidence exists: one PDF, 2 pages, dated 14 September 2026
What action was taken: SKU 1044 cabin filter; End-cap display 3. Both unassigned as of 14 September 2026
```

## Example outcome

**Lp incident log**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Says "item not seen at checkout; camera angle does not confirm concealment; LP notified.".

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What was observed | Returns desk log, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| Timestamps and locations | five working days, due 30 September 2026 | Carried into the draft |
| What evidence exists | one PDF, 2 pages, dated 14 September 2026 | Carried into the draft |
| What action was taken | SKU 1044 cabin filter; End-cap display 3. Both unassigned as of 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Record only what was observed, on camera, or documented. Do not infer intent from observation alone**

**2. Timestamps and locations must come from the user. Do not guess**

**3. Evidence category**  
confirmed, on camera, alleged, or witness account. Label each.

**4. Actions taken**  
what happened and who authorized it. Do not recommend an arrest the policy does not support.

**5. No names of persons not yet confirmed as employees or involved parties**

**Deliberately not done**
- Inferring intent from observation.
- An arrest recommendation without policy support.
- Unnamed witnesses presented as confirmed.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
