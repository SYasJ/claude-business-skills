# Accounts Payable Control

`accounts-payable-control`

## What this is for

Tighten payables so the company pays the right vendor, once, with evidence.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a payables control review by 30 September 2026. Two similar invoices from the same supplier were paid last quarter.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Two similar invoices from the same supplier were paid last quarter.

period: August 2026
no preparer: undeposited funds, sales tax payable
cash recs: one inbox, not the shared folder
reviewer: not signed
```

## Example outcome

**Payables control review**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Separates vendor setup from payment release and proposes a duplicate review list without accusing the supplier.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| period | August 2026 | Needs confirmation |
| no preparer | undeposited funds, sales tax payable | Carried into the draft |
| cash recs | one inbox, not the shared folder | Carried into the draft |
| reviewer | not signed | Needs confirmation |

**How this draft was built**

**1. Map the path**  
Invoice, receipt of goods or services, approval, payment. Note where one person can do two of those steps.

**2. Vendor master**  
New vendors need evidence the user already requires, plus a second look. Do not ask for or store bank passwords. Do not invent a vendor's bank details.

**3. Three-way match where it fits**  
Purchase, receipt, and invoice. Where a match does not fit, say what alternative evidence they use.

**4. Duplicate test**  
Same vendor, similar amount, close dates. Recommend a review list, not an automatic accusation.

**5. Payment run**  
Who reviews the run before release, and how exceptions are logged.

**Deliberately not done**
- One person adds vendors and releases payments with no second look.
- Calling every duplicate-looking item fraud.
- Requesting banking passwords.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
