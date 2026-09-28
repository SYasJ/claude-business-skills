# Planogram Brief

`planogram-brief`

## What this is for

Write a shelf placement brief that explains the logic behind the facing sequence and height allocation.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a planogram brief by 30 September 2026. A brief gives 8 facings to a slow-selling line because the vendor paid for placement but does not disclose that.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A brief gives 8 facings to a slow-selling line because the vendor paid for placement but does not disclose that.

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Planogram brief**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Uses their sales data and labels any placement that is not data-driven.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| store | Harbor Goods, Airdrie | Needs confirmation |
| price | shelf price | Carried into the draft |
| stock | the count | Carried into the draft |
| review | not invented | Needs confirmation |

**How this draft was built**

**1. State the shopper path through the category first**

**2. Place high-turn and high-margin items at eye level using their data**

**3. Do not assign facings based on vendor pressure if it is not also in the data**

**4. Note seasonal items separately from core planogram**

**5. Keep a facing floor of one for items the buyer wants to test**

**Deliberately not done**
- Vendor pressure disguised as a sales rule.
- Facings with no data basis.
- Missing seasonal note.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
