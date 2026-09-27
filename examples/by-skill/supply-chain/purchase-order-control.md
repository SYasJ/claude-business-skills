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

sku: 1044
supplier: Redline Parts
lead time: their number
alternate: none
```

## Example outcome

**Po control review**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026

**Decision**
Treats the email order as a control break and names the missing approval.

**From the file**
- sku: 1044
- supplier: Redline Parts
- lead time: their number
- alternate: none

Nothing in this draft was added from outside that file.
Next: Diane Cho by 30 September 2026. This is not a sign-off.
