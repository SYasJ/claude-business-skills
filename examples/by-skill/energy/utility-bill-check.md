# Utility Bill Check

`utility-bill-check`

## What this is for

Check a bill against the meter read and the rate the user has.

## Scenario

The September bill for site meter 4 shows 1,200 kWh. The read book shows 48,200 minus 47,150, which is 1,050. The rate sheet is 9.2 cents. Devon wants the check before anyone calls it fraud.

## Example data

```text
bill: Sep 2026, meter 4, 1200 kWh
read: 48200 end, 47150 start
rate sheet: 9.2 cents/kWh
prior bill: not in the folder
who calls: Devon Hale
```

## Example outcome

**Bill check**
Read difference: 47,150 to 48,200 is 1,050 kWh. Bill says 1,200. Gap 150 kWh.
At 9.2 cents that is a dollar gap, not a fraud finding. This note does not accuse anyone.
Lines not checked: riders and tax. The prior bill is not in the folder.
Next: Devon asks the utility about the 150 kWh. He does not short-pay from this note alone.
