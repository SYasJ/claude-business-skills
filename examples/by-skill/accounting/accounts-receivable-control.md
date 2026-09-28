# Accounts Receivable Control

`accounts-receivable-control`

## What this is for

Review receivables so the aging means something and cash collection is a process, not a hope.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a receivables control review by 30 September 2026. The AR aging shows a large over-90 bucket, and cash sits unapplied in the same report.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The AR aging shows a large over-90 bucket, and cash sits unapplied in the same report.

period: August 2026
no preparer: undeposited funds, sales tax payable
cash recs: one inbox, not the shared folder
reviewer: not signed
```

## Example outcome

**Receivables control review**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Reconciles the aging, separates disputes from overdue, and lists unapplied cash before anyone writes a chase note.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| period | August 2026 | Needs confirmation |
| no preparer | undeposited funds, sales tax payable | Carried into the draft |
| cash recs | one inbox, not the shared folder | Carried into the draft |
| reviewer | not signed | Needs confirmation |

**How this draft was built**

**1. Tie the aging to the ledger**  
If the aging and the GL disagree, that is the first finding. Do not analyze a report that does not tie.

**2. Split the buckets**  
Current, overdue, disputed, and unapplied. A disputed invoice is not a collections script.

**3. Credit notes and cash application**  
Unapplied cash hides both problems and comfort. List it.

**4. Concentration**  
A few customers may dominate overdue. Name them only from the user's data.

**5. Write the action by bucket**  
Bill, call, resolve dispute, or reserve. Reserving is an accounting judgment for the policy owner, not a collection tactic.

**Deliberately not done**
- An aging that does not tie to the ledger.
- Treating disputes as lazy customers.
- Threatening language in a collections note.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
