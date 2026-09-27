# Cash forecast: can two hires start next month?

`cash-flow-forecast`

## What this is for

Build a 13-week direct cash forecast from collections and commitments, not from accrual revenue.

## Scenario

Mara Chen runs Northline Studio in Calgary. On 14 September 2026 she asks whether she can start two producers next month without missing payroll. She will not finish a week under 40,000 CAD. Harbor & Co owes 90,000 and usually pays 20 days late. That money is not in the bank.

## Example data

```text
opening cash: 180000 CAD, operating account, 14 Sep 2026
payroll: 70000 on the 1st and the 15th
rent: 12000 due in week 3
approved bills: 8400 due in week 2
receivable: Harbor & Co, 90000, usually 20 days late
buffer: 40000
proposed hires: 2 producers, 8500 each per month, start week 5
```

## Example outcome

Decision: do not send the two offers on this file. Week 3 closes at 19,600, under the buffer, before Harbor pays.

| Week | Opening | In | Out | Closing | Vs 40,000 |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 180,000 | 0 | 70,000 | 110,000 | above |
| 2 | 110,000 | 0 | 8,400 | 101,600 | above |
| 3 | 101,600 | 0 | 82,000 | 19,600 | below |
| 4 | 19,600 | 90,000 if the lag holds | 0 | 109,600 | above |
| 5 | 109,600 | 0 | 70,000 | 39,600 | below, hires not included |

The 90,000 is a collection, not booked revenue. The hires are not in the table. Adding them makes week 5 worse.

Optional check, using numbers you pass in:

```bash
python3 scripts/cashflow_check.py weeks.csv --opening 180000 --buffer 40000
```

The script adds and subtracts. It does not know the customer or a safe buffer.
