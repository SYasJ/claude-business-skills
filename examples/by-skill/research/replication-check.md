# Replication Check

`replication-check`

## What this is for

Check whether a result can be rerun from the files the user has.

## Scenario

Table 2 in Nia's draft cites analysis.R and interviews.csv. The R script is in the folder. The CSV is not. A README mentions a cutoff of 0.5 that is not in the script.

## Example data

```text
result: Table 2, 20 interviews, mean confidence 3.4
script in folder: analysis.R
file the script reads: interviews.csv
interviews.csv in folder: no
cutoff 0.5: in the README, not in the script
```

## Example outcome

**Replication note**
Table 2 is not rerunnable from this folder.
The script is here. interviews.csv is not. Stop there.
Do not type 0.5 into the script from the README and call it replicated.
What would make it rerunnable: the CSV the script names, unchanged, and a note if 0.5 was ever used.
This is not a new analysis.
