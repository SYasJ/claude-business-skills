# Returns Desk Script

`returns-desk-script`

## What this is for

Script a returns conversation that follows policy and does not accuse the shopper.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a returns script by 30 September 2026. A script tells associates to shame the shopper into keeping the item.

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A script tells associates to shame the shopper into keeping the item.

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Returns script**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
States the policy calmly and escalates exceptions without shame.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| store | Harbor Goods, Airdrie | Needs confirmation |
| price | shelf price | Carried into the draft |
| stock | the count | Carried into the draft |
| review | not invented | Needs confirmation |

**How this draft was built**

**1. State the policy they supplied**

**2. Ask only for information the return requires**

**3. Do not accuse theft in the script. Route suspected fraud to their loss-prevention process**

**4. Offer the next step**  
refund, exchange, or decline, as policy allows.

**5. Escalate when the shopper's case does not fit the script**

**Deliberately not done**
- A theft accusation in the script.
- Invented policy.
- Unrelated personal data.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
