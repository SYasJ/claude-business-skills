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

How invoices arrive: plain, for people who already know the context. No house guide attached
Who can add a vendor: Priya Shah, controller
Approval limits: Undeposited funds. Partly documented: the what is written down, the who is not
Recent duplicate or fraud scares, if any: Sales tax payable. Partly documented: the what is written down, the who is not
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
| How invoices arrive | plain, for people who already know the context. No house guide attached | Needs confirmation |
| Who can add a vendor | Priya Shah, controller | Carried into the draft |
| Approval limits | Undeposited funds. Partly documented: the what is written down, the who is not | Carried into the draft |
| Recent duplicate or fraud scares, if any | Sales tax payable. Partly documented: the what is written down, the who is not | Needs confirmation |

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
