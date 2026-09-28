# Intercompany Reconciliation

`intercompany-reconcile`

## What this is for

Reconcile balances and transactions between entities so the group is not adding numbers that do not eliminate.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs an intercompany reconciliation by 30 September 2026. Two subsidiaries disagree by a material amount on a management fee, and the group close is tomorrow.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Two subsidiaries disagree by a material amount on a management fee, and the group close is tomorrow.

Entities involved: Undeposited funds. Stated in the ask, not documented anywhere else
Balances each side recorded: one file, dated 14 September 2026. No earlier version attached for comparison
In-transit items: Sales tax payable, last reviewed 14 September 2026. No owner named since
Who approves eliminations: Priya Shah, controller
```

## Example outcome

**Intercompany reconciliation**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Does not force a missing counterparty into existence.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Entities involved | Undeposited funds. Stated in the ask, not documented anywhere else | Needs confirmation |
| Balances each side recorded | one file, dated 14 September 2026. No earlier version attached for comparison | Carried into the draft |
| In-transit items | Sales tax payable, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Who approves eliminations | Priya Shah, controller | Needs confirmation |

**How this draft was built**

**1. Match both sides**  
Entity A receivable against entity B payable, same period. One-sided balances are the work.

**2. Classify differences**  
In-transit cash, FX, timing of invoices, or a booking error. Use the user's currency facts. Do not invent rates.

**3. Profit in inventory**  
If they sell goods between entities, flag unrealized profit as a question for their policy. Do not compute a tax position.

**4. Draft the elimination**  
Show the eliminating lines as a proposal that references both sides.

**5. Aging of differences**  
Old intercompany differences are a control failure, not a rounding issue.

**Deliberately not done**
- Eliminating a one-sided balance with no counterparty.
- Inventing an FX rate.
- Leaving multi-year differences as 'timing'.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
