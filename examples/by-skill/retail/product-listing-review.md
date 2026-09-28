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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the charger claim and flags the image showing one.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| store | Harbor Goods, Airdrie | Needs confirmation |
| price | shelf price | Carried into the draft |
| stock | the count | Carried into the draft |
| review | not invented | Needs confirmation |

**How this draft was built**

**1. Check every claim against the specs they supplied. Flag anything that cannot be confirmed**

**2. Identify missing dimensions, materials, or compatibility notes a buyer needs**

**3. Images must show what ships, at the quantity shown. Do not approve images of a bundle not included**

**4. No invented reviews, fake ratings, or implied endorsements**

**5. Follow category restrictions if the user named them**

**Deliberately not done**
- Invented specs.
- Images of items not in the package.
- Fake social proof.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
