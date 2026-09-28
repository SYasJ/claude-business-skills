# Demand Plan Review

`demand-plan-review`

## What this is for

Review a demand plan for bias, assumptions, and the one driver that would change supply.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a demand plan review by 30 September 2026. The plan repeats last year's hockey stick and actuals have missed it three times.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

The plan repeats last year's hockey stick and actuals have missed it three times.

sku: 1044
supplier: Redline Parts
lead time: their number
alternate: none
```

## Example outcome

**Demand plan review**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Flag the bias and refuses to treat the hockey stick as the base.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| sku | 1044 | Needs confirmation |
| supplier | Redline Parts | Carried into the draft |
| lead time | their number | Carried into the draft |
| alternate | none | Needs confirmation |

**How this draft was built**

**1. Compare the plan to recent actuals they supplied**

**2. Separate a one-time event from a run-rate change**

**3. State the assumption that moves supply the most**

**4. Do not invent a market growth rate**

**5. Recommend a bias note if the plan is always high or low in their history**

**Deliberately not done**
- A plan with no actuals comparison.
- An invented growth rate.
- A hidden bias.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
