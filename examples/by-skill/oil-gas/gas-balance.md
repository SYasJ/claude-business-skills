# Gas Balance

`gas-balance`

## What this is for

Balance inlet, sales, fuel, and flare from the meters the user provides.

## Scenario

Devon's plant day: inlet 10.0, sales 8.1, fuel 0.4, flare meter down. His tolerance is 0.3. A colleague wants the gap parked in fuel so the day closes.

## Example data

```text
day: 15 Sep 2026
inlet: 10.0 mmcf
sales: 8.1
fuel: 0.4
flare: meter down, no reading
tolerance: 0.3
who explains a miss: Devon Hale
```

## Example outcome

**Balance — 15 September**
Outlets that can be added: sales 8.1 plus fuel 0.4 = 8.5. Inlet 10.0. Gap 1.5, and the flare meter is missing.
Do not put 1.5 into fuel. Do not enter flare as zero.
The day does not close. Tolerance is 0.3. This gap is over it even before flare is known.
Next: Devon. The note does not force a balance.
