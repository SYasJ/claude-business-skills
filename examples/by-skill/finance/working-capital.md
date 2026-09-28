# Working Capital Review

`working-capital`

## What this is for

Find cash trapped in receivables, inventory, or payables, and separate a process fix from a one-time release.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a working-capital review by 30 September 2026. Cash is tight even though the company is profitable, and receivables grew faster than sales.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Cash is tight even though the company is profitable, and receivables grew faster than sales.

Receivables, inventory, and payables balances: Harbor & Co owes CAD 60,000, usually 20 days late
Related revenue or cost, so days can be calculated: CAD 36 direct. Overhead not in this line
Known disputes or obsolete stock: Harbor & Co receipt. Stated in the ask, not documented anywhere else
Payment terms the user actually offers: CAD 180, dates not set, cap not set
```

## Example outcome

**Working-capital review**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Calculates days from the user's bases, flags concentration if known, and separates a one-time release from a process change.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Receivables, inventory, and payables balances | Harbor & Co owes CAD 60,000, usually 20 days late | Needs confirmation |
| Related revenue or cost, so days can be calculated | CAD 36 direct. Overhead not in this line | Carried into the draft |
| Known disputes or obsolete stock | Harbor & Co receipt. Stated in the ask, not documented anywhere else | Carried into the draft |
| Payment terms the user actually offers | CAD 180, dates not set, cap not set | Needs confirmation |

**How this draft was built**

**1. Compute days only if the bases exist**  
Do not invent DSO. Show the formula you used.

**2. Separate structural from overdue**  
Terms the company chose are not the same as customers paying late.

**3. Look at concentration**  
A few old invoices or SKUs often hold the cash. Ask for the aging if it was not provided, and do not pretend you saw it.

**4. Recommend a release that is real**  
Collections on disputed invoices are not a plan. Name what must be resolved first.

**5. Watch the rebound**  
A one-time collection is not a new run-rate. Say whether the improvement persists.

**Deliberately not done**
- A days metric with no formula.
- Counting disputed receivables as cash you will collect next week.
- A supplier stretch with no service risk.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
