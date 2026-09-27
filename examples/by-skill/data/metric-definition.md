# Metric Definition

`metric-definition`

## What this is for

Define a metric so two teams would compute the same number from the same source.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a metric definition by 30 September 2026. Sales and finance report different revenue for the same month and both call it bookings.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales and finance report different revenue for the same month and both call it bookings.

The decision the metric serves: plan 180, actual 75
The source table or report they trust: note from Noah Berger, 14 September 2026. No outside report
The owner: Noah Berger, data lead
```

## Example outcome

**Metric definition**
Fieldnote · 14 September 2026

Decision: Picks one source, writes the formula, and flags the other report as a reconciliation item.

| Item | Figure in the file | Call |
| --- | --- | --- |
| Kite Freight | plan 180, actual 75 | use |
| Bright Axle | score 62 | do not treat as a benchmark |
| Missing export | not in the file | stop, do not invent it |

Next action: Noah Berger attaches the missing export or the cell stays blank. Due 30 September 2026.
