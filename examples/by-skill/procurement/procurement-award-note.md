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

quotes: only those attached
missing term: blank
authority: their limit
award: not made here
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
| quotes | only those attached | Needs confirmation |
| missing term | blank | Carried into the draft |
| authority | their limit | Carried into the draft |
| award | not made here | Needs confirmation |

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
