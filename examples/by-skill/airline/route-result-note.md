# Route Result

`route-result-note`

## What this is for

Report a route day from the flights and the loads the user exported.

## Scenario

Luis exported 16 September for the YYC routes he watches. Four flights were planned. One cancelled. The three that flew had loads of 80, 91, and 70 percent. His target is 85. No yield is in the export.

## Example data

```text
day: 16 Sep 2026
planned: 4
cancelled: KA188
flew: loads 80, 91, 70
target load: 85
yield: not in the export
```

## Example outcome

**Route day**
Four planned. KA188 cancelled. Do not drop it to make the day look full.

| Flight | Load |
| --- | --- |
| three that flew | 80, 91, 70 |
| target | 85 |
| KA188 | cancelled |

Two of the three that flew are under 85. No yield is in this note.
Worst by his metric: the cancel, then the 70.
