# Loyalty Program Design

`loyalty-program-design`

## What this is for

Draft a loyalty program structure that rewards the behavior the brand actually wants to drive.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a loyalty program brief by 30 September 2026. A program offers 10% back in points but the redemption minimum is higher than the average order, so few members ever cash out.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A program offers 10% back in points but the redemption minimum is higher than the average order, so few members ever cash out.

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Loyalty program brief**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Sets a redemption minimum below the average order and discloses the liability cap.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| store | Harbor Goods, Airdrie | Needs confirmation |
| price | shelf price | Carried into the draft |
| stock | the count | Carried into the draft |
| review | not invented | Needs confirmation |

**How this draft was built**

**1. Define the earn rule from the behavior they want, not from the points chart that sounds nice**

**2. State the redemption value in real dollars so they can check the margin math**

**3. A high earn rate with a blocked redemption is a fraud risk. Do not design that**

**4. Cap liability exposure if they name a max outstanding balance**

**5. Name what happens to points on a return**

**Deliberately not done**
- An earn rate that creates liability they cannot pay.
- Blocked redemption that misleads members.
- No return policy for points.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
