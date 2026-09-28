# Purchase Order Control

`purchase-order-control`

## What this is for

Review purchase-order control so orders are approved, received, and matched without informal side deals.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a PO control review by 30 September 2026. A team lead emails a supplier directly to avoid the PO system.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A team lead emails a supplier directly to avoid the PO system.

Who can raise and approve: Diane Cho, supply lead
Receipt practice: Calgary-Edmonton lane. Partly documented: the what is written down, the who is not
Match exceptions: SKU 1044 cabin filter is open. Redline Parts was raised verbally and never logged
Known side arrangements: Redline Parts. Stated in the ask, not documented anywhere else
```

## Example outcome

**Po control review**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Treats the email order as a control break and names the missing approval.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Who can raise and approve | Diane Cho, supply lead | Needs confirmation |
| Receipt practice | Calgary-Edmonton lane. Partly documented: the what is written down, the who is not | Carried into the draft |
| Match exceptions | SKU 1044 cabin filter is open. Redline Parts was raised verbally and never logged | Carried into the draft |
| Known side arrangements | Redline Parts. Stated in the ask, not documented anywhere else | Needs confirmation |

**How this draft was built**

**1. Map raise, approve, receive, and pay. Note where one person does two steps**

**2. A side arrangement with no PO is a finding**

**3. Receipt should evidence that goods or services arrived**

**4. Match exceptions need an owner, not a permanent override**

**5. Do not help conceal a purchase from the required approver**

**Deliberately not done**
- Concealing a purchase.
- A permanent match override.
- One person ordering and approving.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
