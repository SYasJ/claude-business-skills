# Inventory Policy

`inventory-policy`

## What this is for

Set an inventory policy from service target, lead time, and demand variability they can show.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs an inventory policy note by 30 September 2026. A buyer wants six weeks of safety stock because it feels safe, with a two-week lead time.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A buyer wants six weeks of safety stock because it feels safe, with a two-week lead time.

Service target: 160
Lead time: 28 days
Cost of a miss they described: CAD 36 direct. Overhead not in this line
```

## Example outcome

**Inventory policy note**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Asks for the service target and variability before accepting six weeks.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Service target | 160 | Needs confirmation |
| Lead time | 28 days | Carried into the draft |
| Cost of a miss they described | CAD 36 direct. Overhead not in this line | Carried into the draft |

**How this draft was built**

**1. Define the item and the service target in their words**

**2. Use their lead time. A generic lead time is labeled a guess**

**3. If variability is unknown, say the safety stock is incomplete rather than inventing a formula result**

**4. Separate cycle stock from safety stock**

**5. Name who may override the target**

**Deliberately not done**
- An invented safety-stock percentage.
- A policy with no owner.
- Mixing cycle and safety stock.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
