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
The alternative source: note from Diane Cho, 14 September 2026. No outside report
```

## Example outcome

**Landed cost note**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026

**Decision**
Holds the recommendation until freight is included or explicitly unknown.

**From the file**
- Invoice cost: CAD 44 direct. Overhead not in this line
- Freight, duty, and fees they know: CAD 180, from their sheet, not a guess
- The alternative source: note from Diane Cho, 14 September 2026. No outside report

Nothing in this draft was added from outside that file.
Next: Diane Cho by 30 September 2026. This is not a sign-off.
