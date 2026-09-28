# Assortment Review

`assortment-review`

## What this is for

Review an assortment for the customer job, the duplicate, and the item that does not earn its space.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs an assortment review by 30 September 2026. A slow-seller list includes an item that was empty for a month.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A slow-seller list includes an item that was empty for a month.

Items and sales they have: SKU 1044 cabin filter, last reviewed 14 September 2026. No owner named since
Space: End-cap display 3, recorded 14 September 2026. No supporting file attached
The customer job: the shopper solving one task in one trip. Not segmented further in the file
Known stockouts: End-cap display 3. Stated in the ask, not documented anywhere else
```

## Example outcome

**Assortment review**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Separates the stockout from true slow sellers before any drop.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Items and sales they have | SKU 1044 cabin filter, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| Space | End-cap display 3, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The customer job | the shopper solving one task in one trip. Not segmented further in the file | Carried into the draft |
| Known stockouts | End-cap display 3. Stated in the ask, not documented anywhere else | Needs confirmation |

**How this draft was built**

**1. Group items by the job the shopper is solving**

**2. Flag duplicates that do not change a choice**

**3. Note stockouts separately from slow sellers**

**4. Recommend a drop, a keep, or a test using their sales**

**5. Do not invent a trend to justify a pet product**

**Deliberately not done**
- An invented trend.
- Cutting a stocked-out item as if it were unwanted.
- No customer job.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
