# Production Variance

`production-variance`

## What this is for

Compare produced volumes to the nomination using the meters the user provides.

## Scenario

Devon has Tuesday's numbers for pad 14-22. The nomination was 4.2 mmcf. The meter, which he flagged as clean, read 3.6. He wants the variance without a reservoir story.

## Example data

```text
day: 16 Sep 2026
pad: 14-22
nomination: 4.2 mmcf
meter: 3.6 mmcf
meter note: clean, no fault flag
threshold for a call: 0.3 mmcf
who explains: Devon Hale
```

## Example outcome

**Variance — pad 14-22, 16 September**
Nomination 4.2. Meter 3.6. Gap 0.6. Over his 0.3 threshold.
Meter note is clean, so this note does not blame the meter and does not invent a reservoir cause.
No adjustment to make 3.6 look like 4.2.
Next: Devon writes the explanation. This note only records the gap.
