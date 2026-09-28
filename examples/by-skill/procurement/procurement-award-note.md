# Award Note

`procurement-award-note`

## What this is for

Write an award note that shows scores, price, and the authority to award.

## Scenario

Diane Cho, buyer at Harbor Goods in Airdrie, needs an award note by 30 September 2026. A low-scoring friend of the buyer is moved to first after evaluation.

## Example data

```text
From: Diane Cho, buyer
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A low-scoring friend of the buyer is moved to first after evaluation.

The criteria: their existing list, 6 lines. Two lines have no owner
The scores and prices they have: CAD 120
Conflicts: Quote set, 3 vendors. Stated in the ask, not documented anywhere else
The approver: Diane Cho. They have not signed
```

## Example outcome

**Award note**
To: Diane Cho, buyer, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the move and records the original scores.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The criteria | their existing list, 6 lines. Two lines have no owner | Needs confirmation |
| The scores and prices they have | CAD 120 | Carried into the draft |
| Conflicts | Quote set, 3 vendors. Stated in the ask, not documented anywhere else | Carried into the draft |
| The approver | Diane Cho. They have not signed | Needs confirmation |

**How this draft was built**

**1. Show scores against the published criteria**

**2. Separate price from non-price scores**

**3. Record conflicts and recusals**

**4. Recommend an award only if the evaluation supports it**

**5. Do not change scores to fit a preferred vendor**

**Deliberately not done**
- Scores changed to fit a favorite.
- A missing conflict.
- An award with no approver.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
