# Promotion Review

`promotion-review`

## What this is for

Review a promotion for margin, inventory, and honest terms.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a promotion review by 30 September 2026. A banner shows a crossed-out price the item never sold for.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A banner shows a crossed-out price the item never sold for.

The offer terms: CAD 79, dates not set, cap not set
Margin they can show: End-cap display 3, recorded 14 September 2026. No supporting file attached
Inventory: 70 on hand
Customer-facing rules: Kite Freight
```

## Example outcome

**Promotion review**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the crossed-out price and checks inventory before the banner runs.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The offer terms | CAD 79, dates not set, cap not set | Needs confirmation |
| Margin they can show | End-cap display 3, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Inventory | 70 on hand | Carried into the draft |
| Customer-facing rules | Kite Freight | Needs confirmation |

**How this draft was built**

**1. State the terms a shopper will see**

**2. Check margin from their cost. If cost is missing, say so**

**3. Confirm inventory can support the advertised depth**

**4. No fake was-prices or fake end times**

**5. Define the exception path for rain checks if they offer them**

**Deliberately not done**
- Fake was-prices.
- Advertising stock they do not have.
- Hidden exclusions.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
