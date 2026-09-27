# Cash forecast assumptions

Use this note only when the cash-flow-forecast skill needs a place to park assumptions. Do not treat the samples below as a real company.

## What belongs here

- Opening cash by entity and currency, as supplied by the user.
- Collection lag the user calculated from their own receipts.
- Payroll, tax, rent, and debt dates the user confirmed.
- The minimum cash buffer they chose.
- The stress they asked for, such as collections slipping ten days.

## What does not belong here

- A bank login, token, or account password.
- A market interest rate you looked up from memory and presented as fact.
- A promise that a lender will extend a line.
- Accrual revenue relabeled as cash.

## Sample shape

| Week | Opening | Collections | Payroll | Other out | Closing | Note |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | user figure | user figure | user figure | user figure | calculated | assumption labeled |

If a cell is unknown, write unknown. Do not fill it to make the table look finished.
