# Foreign Exchange Exposure Review

`fx-exposure-review`

## What this is for

Identify where currency actually hits cash, and separate a hedge policy question from a bookkeeping curiosity.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a FX exposure review by 30 September 2026. A firm invoices in euros and pays staff in dollars and wants to know if last month's margin drop was FX.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A firm invoices in euros and pays staff in dollars and wants to know if last month's margin drop was FX.

Currencies of revenue, costs, and cash: CAD 44 direct. Overhead not in this line
Which exposures are contractual: unsigned draft, 8 pages, no signature date
The user's hedge policy, if any: their one-page rule dated 2 Mar 2026. No exception log
The decision they need to make: A firm invoices in euros and pays staff in dollars and wants to know if last month's margin drop was FX
```

## Example outcome

**Fx exposure review**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A map of contractual cash exposure, a translation-versus-transaction split, and policy questions rather than a trade order.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Currencies of revenue, costs, and cash | CAD 44 direct. Overhead not in this line | Needs confirmation |
| Which exposures are contractual | unsigned draft, 8 pages, no signature date | Carried into the draft |
| The user's hedge policy, if any | their one-page rule dated 2 Mar 2026. No exception log | Carried into the draft |
| The decision they need to make | A firm invoices in euros and pays staff in dollars and wants to know if last month's margin drop was FX | Needs confirmation |

**How this draft was built**

**1. Map cash exposures**  
Where currency hits a bank account, not only where a report is translated.

**2. Separate transaction from translation**  
Management action usually belongs on contracted cash flows. Say which one the user is looking at.

**3. Quantify only with their data**  
A rate move they specify, applied to exposures they listed. Do not invent a forecast rate and call it the market.

**4. Policy before trades**  
If they have no hedge policy, recommend writing the policy questions, not a trade ticket.

**5. Note operational natural hedges**  
Costs in the same currency as revenue may already offset. Do not propose a hedge that doubles the risk.

**Deliberately not done**
- Treating accounting translation as cash risk without checking.
- Inventing a hedge product and telling them to buy it.
- Asking for trading credentials.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
