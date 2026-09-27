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
Fieldnote · 14 September 2026

Decision: Removes the address, defines the click in context, and names the decision it serves.

| Item | Figure in the file | Call |
| --- | --- | --- |
| Harbor & Co | plan 150, actual 105 | use |
| Lumen Ledger | score 78 | do not treat as a benchmark |
| Missing export | not in the file | stop, do not invent it |

Next action: Jonah Park attaches the missing export or the cell stays blank. Due 30 September 2026.
