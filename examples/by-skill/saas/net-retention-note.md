# Net Retention Note

`net-retention-note`

## What this is for

Compute net retention only from the starting and ending revenue they provide for the same accounts.

## Scenario

A board slide says NRR is 120 percent. The file has total MRR for two months and a list of new logos. It does not identify the same accounts at the start and the end.

## Example data

```text
slide: NRR 120 percent
file: August MRR 40500, September week MRR 42000
new logos: 6, revenue not split
same-account cohort: not in the file
expansion versus churn: not split
```

## Example outcome

**Retention note**
Do not use 120 percent. The file is not a same-account cohort.
New logos do not belong in that ratio, and their revenue is not even split out.
Ending and starting totals are a company MRR change, not NRR.
What would make the number possible: the same accounts, August revenue and current revenue, with new logos excluded.
Until that sheet exists, the cell stays blank.
