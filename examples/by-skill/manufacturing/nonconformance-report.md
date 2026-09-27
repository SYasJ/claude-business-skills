# Nonconformance Report

`nonconformance-report`

## What this is for

Write a nonconformance report that contains the fact, the containment, and the owner.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a NCR by 30 September 2026. A report says 'bad parts' and the suspect lot is still being shipped.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A report says 'bad parts' and the suspect lot is still being shipped.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Ncr**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Stops the lot, describes the defect, and names the owner.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.
