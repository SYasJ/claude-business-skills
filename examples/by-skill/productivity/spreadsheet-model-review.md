# Spreadsheet Model Review

`spreadsheet-model-review`

## What this is for

Review a spreadsheet model for structure, formula errors, and hard-coded values that should be inputs.

---

## Scenario A — Budget model with hard-coded revenue

**Priya Shah, controller, Northline Studio, Calgary. Model: FY2027 operating budget.**

### What was shared

A 12-tab Excel file. The main P&L tab calculates net income. The analyst flagged that changing the revenue assumption takes 40+ manual edits.

### Structural findings

**Finding 1 — CRITICAL: Revenue hard-coded in 47 formula cells**

Row 8 (Jan revenue) contains `=4200*1.03` in every month column instead of referencing a single assumption cell. Changing the growth rate requires editing column B through M individually.

**Fix:** Create an `Assumptions` tab. Cell A3 = `Revenue base (Jan)`, cell B3 = `4200`. Cell A4 = `Monthly growth rate`, cell B4 = `1.03`. Then row 8 in P&L becomes `=$Assumptions.$B$3*($Assumptions.$B$4^(COLUMN()-2))` or equivalent. One edit, all months update.

---

**Finding 2 — HIGH: COGS formula references a moved sheet**

Cell D22 contains `=Sheet3!C4`. There is no `Sheet3` — the tab was renamed to `COGS Detail`. Excel returns `#REF!` which silently propagates to Net Income.

**Fix:** Update to `='COGS Detail'!C4` and add a named range so the formula survives future renames.

---

**Finding 3 — MEDIUM: Headcount costs use a division with a zero-denominator risk**

Cell K34: `=K32/K33`. If K33 (headcount) is ever zero (e.g., a new department in setup month), this returns `#DIV/0!` and breaks the payroll summary.

**Fix:** `=IFERROR(K32/K33, 0)` or `=IF(K33=0, 0, K32/K33)`.

---

**Finding 4 — MEDIUM: No input protection**

The `Assumptions` tab has no cell protection. Any user can overtype a formula or erase a named range. At minimum, lock formula cells and only leave assumption inputs editable.

---

**Finding 5 — LOW: Inconsistent date format in column A**

Rows 1–6 use `Jan-27` (text). Rows 7–12 use `1/1/2027` (date serial). Charts referencing this column may sort incorrectly.

**Fix:** Standardize to date serials and apply a custom format `mmm-yy`.

### What to do first

1. Fix the `#REF!` error in COGS (breaks net income today)
2. Create the Assumptions tab and rewire revenue (single highest-effort, single highest-value change)
3. Add IFERROR guards to the headcount division
4. Lock formula cells before sharing with the broader team

---

## Scenario B — Sales forecast with a lookup error

**Aisha Rahman, engineering lead, Fieldnote. Model: Q4 sales forecast.**

### Issue reported

VLOOKUP returns `N/A` for 3 of 12 sales reps.

### Diagnosis

```excel
=VLOOKUP(A2, RepTable, 3, FALSE)
```

`A2` contains `"Ahmed Al-Hassan "` (trailing space). The lookup table has `"Ahmed Al-Hassan"` (no space). `FALSE` (exact match) fails silently.

### Fix options

| Option | Formula | Notes |
|---|---|---|
| Trim at input | `=VLOOKUP(TRIM(A2), RepTable, 3, FALSE)` | Easiest; fixes all trailing spaces |
| INDEX/MATCH with TRIM | `=INDEX(RepTable_Col3, MATCH(TRIM(A2), TRIM(RepTable_Col1), 0))` | More robust; handles both sides |
| Clean the source | Remove spaces in column A before running report | Best long-term; one-time fix |

**Recommendation:** Apply TRIM to the source data this month. Add a data validation rule to the input column to prevent trailing spaces going forward.
