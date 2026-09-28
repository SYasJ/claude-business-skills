# Returns Process

`returns-process`

## What this is for

Design a returns process with a reason code, a disposition, and a customer promise you can keep.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a returns process by 30 September 2026. The website promises instant refunds and the warehouse has not inspected the unit.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

The website promises instant refunds and the warehouse has not inspected the unit.

Reasons they see: Calgary-Edmonton lane. Stated in the ask, not documented anywhere else
Disposition options: keep SKU 1044 cabin filter, or stop. No third option written
Refund authority: SKU 1044 cabin filter and one other, both unconfirmed as of 14 September 2026
Customer promise: Kite Freight
```

## Example outcome

**Returns process**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Aligns the promise with inspection and keeps inventory records honest.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Reasons they see | Calgary-Edmonton lane. Stated in the ask, not documented anywhere else | Needs confirmation |
| Disposition options | keep SKU 1044 cabin filter, or stop. No third option written | Carried into the draft |
| Refund authority | SKU 1044 cabin filter and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| Customer promise | Kite Freight | Needs confirmation |

**How this draft was built**

**1. Capture a reason code that operations can act on**

**2. Route disposition**  
restock, repair, or scrap, based on their rules.

**3. State the customer promise and the clock they can meet**

**4. Separate a policy exception from the standard path**

**5. Track fraud concerns as a control question, not as an accusation in the customer message**

**Deliberately not done**
- A promise they cannot meet.
- Concealed returns.
- Accusing a customer in the template.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
