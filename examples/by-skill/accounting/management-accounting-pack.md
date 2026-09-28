# Management Accounting Pack

`management-accounting-pack`

## What this is for

Turn the ledger into a decision view: margins, cost centers, and a reconciliation back to the books.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a management accounting pack by 30 September 2026. Leaders want margin by service line, but half of delivery cost sits in a general pool.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Leaders want margin by service line, but half of delivery cost sits in a general pool.

Ledger for the period: month ending 14 September 2026
Dimensions they have: team, product, location: team: in the file; product: not in the file; location: open
Allocations they currently use: Sales tax payable and one other, both unconfirmed as of 14 September 2026
The decision the pack serves: Leaders want margin by service line, but half of delivery cost sits in a general pool
```

## Example outcome

**Management accounting pack**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows contribution before allocation, labels the pool as unallocated, and bridges to the ledger.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Ledger for the period | month ending 14 September 2026 | Needs confirmation |
| Dimensions they have: team, product, location | team: in the file; product: not in the file; location: open | Carried into the draft |
| Allocations they currently use | Sales tax payable and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| The decision the pack serves | Leaders want margin by service line, but half of delivery cost sits in a general pool | Needs confirmation |

**How this draft was built**

**1. Reconcile to the ledger**  
Every management view ties to the GL in a bridge. Untied 'adjusted' numbers are labeled non-GAAP or internal, in their words, and still bridge.

**2. Choose the cut**  
Product, location, or customer. One primary cut. A second cut only if they use it to decide.

**3. Allocations**  
Describe the driver they use. If there is no driver, show the cost as unallocated rather than inventing a spread.

**4. Contribution before overhead**  
Show a view before allocations so managers can see what they influence.

**5. Commentary**  
Three movements that matter, with facts. No invented market color.

**Deliberately not done**
- A management P&L that does not bridge to the books.
- Allocations with a made-up driver.
- Ten cuts and no decision.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
