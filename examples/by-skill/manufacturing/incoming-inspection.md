# Incoming Inspection

`incoming-inspection`

## What this is for

Plan incoming inspection for a material based on risk and the reaction to a failed lot.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs an incoming inspection plan by 30 September 2026. Failed material is left on the issue shelf so the line does not stop.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

Failed material is left on the issue shelf so the line does not stop.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Incoming inspection plan**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Moves failed material to hold and requires a named deviation before any use.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.
