# Product Analytics Spec

`product-analytics-spec`

## What this is for

Specify the events and properties a product change needs so the team can tell whether it worked.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs an analytics spec by 30 September 2026. A spec adds a property for a user's full home address to measure a button click.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A spec adds a property for a user's full home address to measure a button click.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

## Example outcome

**Analytics spec**
Fieldnote · 14 September 2026 · Due 30 September 2026

**Decision**
Removes the address, defines the click in context, and names the decision it serves.

| Item | Figure in the file | Call | Why |
| --- | --- | --- | --- |
| Harbor & Co | plan 150, actual 105 | Use | Both sides of the comparison are in the file |
| Lumen Ledger | score 78 | Report, do not benchmark | One score is a reading, not a baseline |
| Missing export | Not in the file | Stop | The cell stays blank until the export arrives |

**How these calls were made**

1. Decision first
2. Event definitions
3. Identity
4. Privacy
5. QA: How an engineer will know the event fired correctly before release

**Deliberately not done**
- Events with no decision behind them.
- Tracking secrets or card numbers.
- A spec that ignores the current naming convention.

**Open items**
- The missing export is the binding constraint. No figure was estimated to fill its place.
- Any row marked *Report, do not benchmark* needs a second period before it can carry a trend.

Next: Jonah Park attaches the missing export, or the cell stays blank. Due 30 September 2026.
