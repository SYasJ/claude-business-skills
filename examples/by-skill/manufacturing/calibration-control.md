# Calibration Control

`calibration-control`

## What this is for

Review calibration control so instruments used for acceptance are in date, and out-of-date tools are not used.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a calibration control note by 30 September 2026. A caliper used for final accept is two months overdue and still on the bench.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A caliper used for final accept is two months overdue and still on the bench.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Calibration control note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Quarantines it and asks for a use review rather than inventing which lots moved.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.
