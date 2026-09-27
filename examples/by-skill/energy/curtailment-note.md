# Curtailment Note

`curtailment-note`

## What this is for

Record a curtailment the user was instructed to make, with the volume and the time.

## Scenario

The grid instruction was to drop 2 MW from 14:00 to 16:00 on 16 September. The meter shows a 1.4 MW drop. Compensation is not in the instruction.

## Example data

```text
instruction: drop 2 MW, 14:00-16:00, 16 Sep 2026
meter after: 1.4 MW below the prior hour
compensation rate: not in the instruction
who acknowledges: Devon Hale
```

## Example outcome

**Curtailment note**
Told: 2 MW, 14:00 to 16:00, 16 September.
Meter: 1.4 MW below the prior hour. Both figures stay. The gap is not edited away.
No compensation rate is in the instruction, so none is written.
This is a record, not a dispute letter.
Acknowledged by: Devon.
