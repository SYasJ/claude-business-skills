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

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Assortment review**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026

**Decision**
Separates the stockout from true slow sellers before any drop.

**From the file**
- store: Harbor Goods, Airdrie
- price: shelf price
- stock: the count
- review: not invented

Nothing in this draft was added from outside that file.
Next: Diane Cho by 30 September 2026. This is not a sign-off.
