# Payroll Accounting Review

`payroll-accounting-review`

## What this is for

Review the payroll journal path from the payroll register to the ledger, including accruals and remittances.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a payroll accounting review by 30 September 2026. The payroll register and the wage expense account have not matched for two months.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The payroll register and the wage expense account have not matched for two months.

Payroll register totals: CAD 70,000 on the 1st and the 15th
Ledger accounts used: 30 in the last period. No prior period attached, so no trend
Remittances due: Undeposited funds and one other, both unconfirmed as of 14 September 2026
Known off-cycle payments: Undeposited funds. Stated in the ask, not documented anywhere else
```

## Example outcome

**Payroll accounting review**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A tie-out of gross-to-journal, a mapping question on liabilities, and a control note on who reviews the register.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Payroll register totals | CAD 70,000 on the 1st and the 15th | Needs confirmation |
| Ledger accounts used | 30 in the last period. No prior period attached, so no trend | Carried into the draft |
| Remittances due | Undeposited funds and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| Known off-cycle payments | Undeposited funds. Stated in the ask, not documented anywhere else | Needs confirmation |

**How this draft was built**

**1. Tie the register to the journal**  
Gross pay, deductions, employer costs, and net pay. A difference is a finding, not a rounding story, unless they show the rounding.

**2. Liability accounts**  
Deductions and employer taxes should land in liabilities until remitted. Net pay sitting in an expense account is a mapping question.

**3. Accrual**  
Days worked but not paid at period end. Use their calendar. Do not invent a pay cycle.

**4. Off-cycle and manual payments**  
List them and ask whether they hit the same controls.

**5. Remittance calendar**  
What is due, without giving tax advice. The skill schedules their stated dues. It does not opine on tax law.

**Deliberately not done**
- Inventing tax rates.
- Ignoring off-cycle payments.
- Asking for payroll logins.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
