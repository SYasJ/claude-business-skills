# Safety Stock Review

`safety-stock`

## What this is for

Review safety stock for a few items so cash is not trapped in a habit.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a safety stock review by 30 September 2026. Every item is set to 90 days because the spreadsheet default says so.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

Every item is set to 90 days because the spreadsheet default says so.

sku: 1044
supplier: Redline Parts
lead time: their number
alternate: none
```

## Example outcome

**Safety stock review**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Pilots a reduction on items with no risk story and leaves named risks alone.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| sku | 1044 | Needs confirmation |
| supplier | Redline Parts | Carried into the draft |
| lead time | their number | Carried into the draft |
| alternate | none | Needs confirmation |

**How this draft was built**

**1. Rank items by cash tied up and by stockout pain, using their data**

**2. Identify cover that exceeds their own rule**

**3. Ask what uncertainty the extra cover buys. If nobody knows, it is a candidate to reduce**

**4. Do not cut stock that covers a known supply risk they named**

**5. Recommend a pilot reduction with a stockout check**

**Deliberately not done**
- A blanket cut.
- Cutting stock that covers a known risk.
- No stockout check.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
