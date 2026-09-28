# Spreadsheet Model Review

`spreadsheet-model-review`

## What this is for

Review a spreadsheet model for structure, formula errors, and hard-coded values that should be inputs.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, shares the FY2027 operating budget. Her analyst reports that changing the revenue assumption takes more than forty manual edits.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
File: FY2027 Operating Budget.xlsx (12 tabs)

Reported symptom: changing the revenue growth rate requires editing every month column.

Formulas pasted for review:
  P&L!B8   =4200*1.03          (repeated across C8:M8, 47 cells total)
  P&L!D22  =Sheet3!C4          (tab "Sheet3" was renamed to "COGS Detail")
  P&L!K34  =K32/K33            (K33 = headcount, can be 0 in a setup month)
  Assumptions tab: exists, unprotected, no named ranges
  Column A dates: rows 1-6 text "Jan-27", rows 7-12 serial 1/1/2027
```

## Example outcome

**Spreadsheet model review — FY2027 Operating Budget**
To: Priya Shah, controller, Northline Studio · Date: 14 September 2026

**Decision**
Two findings break the model today and must be fixed before anyone trusts Net Income. The rest are structural and can follow.

**Finding 1 — CRITICAL · Revenue hard-coded in 47 formula cells**

`P&L!B8` contains `=4200*1.03`, repeated across `C8:M8`. The growth rate lives inside the formula, so changing it means 47 edits and one of them will be missed.

Fix — move both numbers to inputs, then reference them:

```
Assumptions!B3  =4200     (revenue base, January)
Assumptions!B4  =1.03     (monthly growth rate)

P&L!B8  =Assumptions!$B$3 * (Assumptions!$B$4 ^ (COLUMN()-2))
```

One edit now updates all twelve months.

**Finding 2 — HIGH · COGS reference points at a tab that no longer exists**

`P&L!D22` is `=Sheet3!C4`. The tab was renamed to `COGS Detail`, so this returns `#REF!` and the error propagates silently into Net Income.

Fix: `='COGS Detail'!C4`, then define a named range so the next rename does not break it.

**Finding 3 — MEDIUM · Division with an unguarded zero denominator**

`P&L!K34` is `=K32/K33`, where K33 is headcount. A department in its setup month has zero headcount, which returns `#DIV/0!` and breaks the payroll summary.

Fix: `=IFERROR(K32/K33, 0)` — or `=IF(K33=0, 0, K32/K33)` if a zero should be visibly different from an error.

**Finding 4 — MEDIUM · Assumptions tab is unprotected**

Any user can overtype a formula or delete a range. Lock the formula cells and leave only the assumption inputs editable before this is shared more widely.

**Finding 5 — LOW · Mixed date types in column A**

Rows 1–6 hold the text `"Jan-27"`; rows 7–12 hold real date serials. Charts built on this column will sort wrongly. Standardise on serials with a `mmm-yy` display format.

**Order of work**

| # | Fix | Why first |
| --- | --- | --- |
| 1 | `#REF!` in COGS | It is wrong on screen today |
| 2 | Revenue inputs | Highest effort, highest payoff; everything else depends on it |
| 3 | `IFERROR` guard on K34 | Cheap, prevents a future break |
| 4 | Lock formula cells | Do before wider sharing |
| 5 | Date formats | Cosmetic until someone builds a chart |

**Deliberately not done**
- The model was not restructured beyond what was asked. One change at a time keeps it testable.
- No formula's intent was guessed. Where the purpose of a cell was unclear, it is listed for Priya to confirm rather than rewritten.
- No new tool was proposed. The spreadsheet is the right tool for this; it just needs its inputs separated.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
