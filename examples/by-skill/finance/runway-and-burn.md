# Runway and Burn

`runway-and-burn`

## What this is for

Compute cash runway from a defined burn, and show how hiring or a slipped receipt changes the date.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a runway note by 30 September 2026. A CEO says runway is 14 months, but the figure excludes two signed offers starting next month.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A CEO says runway is 14 months, but the figure excludes two signed offers starting next month.

Cash on hand: CAD 200,000 counted 14 September 2026
Which expenses are in burn: Payroll 15 September. Stated in the ask, not documented anywhere else
Expected receipts the user wants included or excluded: Operating cash and one other, both unconfirmed as of 14 September 2026
Upcoming committed hires: Payroll 15 September and one other, both unconfirmed as of 14 September 2026
```

## Example outcome

**13-week cash view, first four weeks shown**
Northline Studio · 14 September 2026 · CAD

Decision: do not add a new recurring cost until Kite Freight's 130,000 is collected or moved out of the plan. The hire is a cash condition, not a yes.

| Week | Opening | In | Out | Closing | Against buffer 25,000 |
| --- | --- | --- | --- | --- | --- |
| 1 | 200,000 | 0 | 60,000 payroll | 140,000 | above |
| 2 | 140,000 | 0 | 8,400 approved bills | 131,600 | above |
| 3 | 131,600 | 0 | 76,000 payroll and rent | 55,600 | above |
| 4 | 55,600 | 130,000 if the lag holds | 0 | 185,600 | above |

First tight week: none in the first four weeks.
Assumption: the 130,000 is collected in week 4 because that is the 20-day lag in the file. It is not booked revenue.
Not in this draft: a second scenario where the receipt slips past week 6. Build that before any offer letter.
Next action: Mara Chen confirms the collection date by 30 September 2026.
