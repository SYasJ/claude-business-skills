# Trial To Paid

`trial-to-paid`

## What this is for

Report trial-to-paid from the cohort dates in the export.

## Scenario

August trials: 100 started, 18 paid, trial length 14 days, all finished. September trials started 1 to 14 September and are still inside 14 days. A slide blends them.

## Example data

```text
trial length: 14 days
August: 100 started, 18 paid, cohort closed
September 1-14: 80 started, still inside the trial
paid definition: a paid workspace, not a card added and removed
channel split: not exported
```

## Example outcome

**Conversion**
August, closed: 18 of 100.
September 1-14: still open. Do not count them as lost or as converted.
Do not blend the months.
No channel split. None was exported.
Next cohort closes 28 September for the 14 September starts.
