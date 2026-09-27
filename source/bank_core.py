"""Showcase scenarios that should not use the generated filler."""

from scenario_bank import put

put(
    "cash-flow-forecast",
    "Build a 13-week direct cash forecast from collections and commitments, not from accrual revenue.",
    "Mara Chen runs Northline Studio in Calgary. On 14 September 2026 she asks whether she can start two producers next month without missing payroll. She will not finish a week under 40,000 CAD. A customer owes 90,000 and usually pays 20 days late. That money is not in the bank.",
    """```text
opening cash: 180000 CAD, operating account, 14 Sep 2026, one entity
payroll: 70000 on the 1st and the 15th
rent: 12000 due in week 3
approved bills: 8400 due in week 2
receivable: Harbor & Co, 90000, usually 20 days late, not collected
buffer: do not finish a week under 40000
proposed hires: 2 producers, 8500 each per month, start week 5
credit line: exists, she does not treat it as cash
```""",
    """**13-week cash view — first five weeks**
Northline Studio · 14 September 2026 · CAD

Decision: do not send the two offers on this file. Week 3 closes under the 40,000 buffer before Harbor & Co pays. The hire is a cash condition, not a yes.

| Week | Opening | In | Out | Closing | Vs 40,000 |
| --- | --- | --- | --- | --- | --- |
| 1 | 180,000 | 0 | 70,000 payroll | 110,000 | above |
| 2 | 110,000 | 0 | 8,400 bills | 101,600 | above |
| 3 | 101,600 | 0 | 82,000 payroll and rent | 19,600 | below |
| 4 | 19,600 | 90,000 if the 20-day lag holds | 0 | 109,600 | above |
| 5 | 109,600 | 0 | 70,000 payroll, hires not included | 39,600 | below |

The 90,000 is a collection, not revenue. It is placed in week 4 only because that is her lag.
The two hires are not in the table. Adding 8,500 each would make week 5 worse.
Not a guarantee. She confirms the Harbor date before any offer goes out.
Next: Mara, by 18 September.""",
)
