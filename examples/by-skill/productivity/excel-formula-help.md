# Excel and Sheets Formula Help

`excel-formula-help`

## What this is for

Write or fix a spreadsheet formula that solves the calculation the user described, with a plain-English explanation.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a formula help by 30 September 2026. A user wants to look up a price from a table and cannot remember whether to use VLOOKUP or INDEX MATCH.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A user wants to look up a price from a table and cannot remember whether to use VLOOKUP or INDEX MATCH.

What the formula should return: Q4 objective 2, last reviewed 14 September 2026. No owner named since
The column and row structure they described: Friday review block, recorded 14 September 2026. No supporting file attached
An example of the input and expected output if they have one: Q4 objective 2. Partly documented: the what is written down, the who is not
```

## Example outcome

**Formula help**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Both formulas with the user's column letters, a plain explanation of when each breaks, and a test case.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What the formula should return | Q4 objective 2, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| The column and row structure they described | Friday review block, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| An example of the input and expected output if they have one | Q4 objective 2. Partly documented: the what is written down, the who is not | Carried into the draft |

**How this draft was built**

**1. Confirm the structure**  
which column holds the lookup value, which holds the result, and whether the match is exact or approximate.

**2. Write the formula with named ranges or column letters they described. Do not invent a structure they did not state**

**3. Explain each argument in one sentence. If the formula has a bracket inside a bracket, explain it from the inside out**

**4. Give a test case**  
this input should return this output.

**5. Warn if the formula will break when rows are added or deleted, and say what to change**

**Deliberately not done**
- Assuming a column layout they did not describe.
- Macros the user did not ask for.
- A formula without an explanation.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
