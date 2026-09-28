# Product Metric Tree

`north-star-and-input-metrics`

## What this is for

Define a product outcome metric and the input metrics a team can move this month.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a product metric tree by 30 September 2026. A team wants to optimize signups, but activated users are the ones who finish a first export.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to optimize signups, but activated users are the ones who finish a first export.

Candidate metrics and definitions: plan 120, actual 80
What the team can change: two people on shift, one off
Known ways to game the metric: plan 120, actual 80
```

## Example outcome

**Product metric tree**
Fieldnote · 14 September 2026 · Due 30 September 2026

**Decision**
Uses the first successful export as the value moment and signups as a funnel input, with a failure counter-metric.

| Item | Figure in the file | Call | Why |
| --- | --- | --- | --- |
| Redline Parts | plan 120, actual 80 | Use | Both sides of the comparison are in the file |
| Lantern Inn | score 78 | Report, do not benchmark | One score is a reading, not a baseline |
| Missing export | Not in the file | Stop | The cell stays blank until the export arrives |

**How these calls were made**

1. Value moment
2. Definition
3. Inputs
4. Counter-metric
5. Gaming

**Deliberately not done**
- Signups as the value metric by default.
- No counter-metric.
- An invented baseline.

**Open items**
- The missing export is the binding constraint. No figure was estimated to fill its place.
- Any row marked *Report, do not benchmark* needs a second period before it can carry a trend.

Next: Jonah Park attaches the missing export, or the cell stays blank. Due 30 September 2026.
