# Product Listing Review

`product-listing-review`

## What this is for

Review an online product listing for accurate claims, complete specs, and images that match what ships.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a product listing review by 30 September 2026. A listing says the item includes a charger but the SKU does not ship one.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A listing says the item includes a charger but the SKU does not ship one.

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Product listing review**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026

**Decision**
Removes the charger claim and flags the image showing one.

**From the file**
- store: Harbor Goods, Airdrie
- price: shelf price
- stock: the count
- review: not invented

Nothing in this draft was added from outside that file.
Next: Diane Cho by 30 September 2026. This is not a sign-off.
