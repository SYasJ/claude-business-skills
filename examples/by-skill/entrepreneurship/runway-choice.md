# Runway Choice

`runway-choice`

## What this is for

State the runway choice from cash, burn, and the hire they are considering.

## Scenario

Northline has $180,000 cash. Burn is $30,000 a month. A hire would add $8,000. A customer might pay $40,000. Mara wants to know if she can hire.

## Example data

```text
cash: 180000
monthly burn: 30000
hire: 8000 a month, not started
maybe receipt: 40000, not in the bank
date she cares about: 31 Mar 2027
```

## Example outcome

**Runway**
Current burn: 180,000 / 30,000 = 6 months. That is the file, not a promise.
With the hire: 38,000 a month, under 5 months. Do not start the hire on this note.
The $40,000 stays out. It is not cash.
No raise is assumed.
Choice: wait. Revisit if the $40,000 arrives.
