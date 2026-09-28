# Landed Cost Review

`landed-cost`

## What this is for

Build a landed-cost view from cost elements the user can support, so a buy decision sees the full cash cost.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a landed cost note by 30 September 2026. A cheaper invoice price is recommended, and nobody added international freight.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A cheaper invoice price is recommended, and nobody added international freight.

Invoice cost: CAD 44 direct. Overhead not in this line
Freight, duty, and fees they know: CAD 180, from their sheet, not a guess
Volume: 70 in the last period. No prior period attached, so no trend
The alternative source: note from Diane Cho, 14 September 2026. No outside report
```

## Example outcome

**Landed cost note**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Holds the recommendation until freight is included or explicitly unknown.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Invoice cost | CAD 44 direct. Overhead not in this line | Needs confirmation |
| Freight, duty, and fees they know | CAD 180, from their sheet, not a guess | Carried into the draft |
| Volume | 70 in the last period. No prior period attached, so no trend | Carried into the draft |
| The alternative source | note from Diane Cho, 14 September 2026. No outside report | Needs confirmation |

**How this draft was built**

**1. List only cost elements they can support. Mark unknowns**

**2. Show cost per unit at the volume they named**

**3. Compare with the alternative on the same elements**

**4. Note cash timing if duties or freight are paid earlier**

**5. Do not invent a duty rate**

**Deliberately not done**
- An invented duty rate.
- A unit cost that ignores freight.
- A comparison that omits the alternative's freight.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
