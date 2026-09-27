# Work Instruction

`work-instruction`

## What this is for

Write a work instruction a new operator can follow, including the stop and the quality check.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a work instruction by 30 September 2026. An instruction says 'tighten properly' and the torque is unknown.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

An instruction says 'tighten properly' and the torque is unknown.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Work instruction**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Marks torque as a required input from engineering rather than inventing a number.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.
