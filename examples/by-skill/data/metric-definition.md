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
Fieldnote · 14 September 2026 · Due 30 September 2026

**Decision**
Picks one source, writes the formula, and flags the other report as a reconciliation item.

| Item | Figure in the file | Call | Why |
| --- | --- | --- | --- |
| Kite Freight | plan 180, actual 75 | Use | Both sides of the comparison are in the file |
| Bright Axle | score 62 | Report, do not benchmark | One score is a reading, not a baseline |
| Missing export | Not in the file | Stop | The cell stays blank until the export arrives |

**How these calls were made**

1. Write the decision the metric is for before naming the metric
2. Define numerator, denominator, time window, and exclusions in words a new analyst can apply
3. Name the source. If two reports disagree, the definition is not done until one source is chosen
4. Record the known ways the metric can be gamed and add a counter-metric
5. Set an owner and a change process. Silent definition changes are a finding

**Deliberately not done**
- A metric with no formula.
- Two teams using different sources without a note.
- An invented baseline.

**Open items**
- The missing export is the binding constraint. No figure was estimated to fill its place.
- Any row marked *Report, do not benchmark* needs a second period before it can carry a trend.

Next: Noah Berger attaches the missing export, or the cell stays blank. Due 30 September 2026.
