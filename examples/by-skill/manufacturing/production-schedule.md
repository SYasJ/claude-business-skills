# Production Schedule Review

`production-schedule`

## What this is for

Review a production schedule against capacity, materials, and the promise that will slip first.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a schedule review by 30 September 2026. The schedule loads 120 hours into an 80-hour cell and the status is on time.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

The schedule loads 120 hours into an 80-hour cell and the status is on time.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Schedule review**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Cuts or sequences to 80 hours and names the promise that moves.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.
