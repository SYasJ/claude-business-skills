# Supplier Risk Note

`supplier-risk-note`

## What this is for

Note a supplier risk from the evidence the buyer has, without a mood score.

## Scenario

Harbor Goods buys SKU 1044 cabin filters only from Redline Parts. Lead time is 28 days. In August they were short 14 units. There is no second supplier in the file.

## Example data

```text
supplier: Redline Parts
sku: 1044 cabin filter
lead time in system: 28 days
August miss: 14 units, receipt 28 Aug 2026
alternate: none on file
buyer-caused forecast change: not in this file
cover Diane can place: a 2-week bridge buy if she finds a second quote
```

## Example outcome

**Risk note — SKU 1044**
Single source. 28-day lead time. August miss: 14 units. That is the evidence. No credit score is in the file, so none is written.

No alternate is on file. That is the risk, not a mood.
Cover this month: Diane gets one second quote, or she accepts the 28-day exposure. This note does not pick a vendor for her.
Do not add a forecast-blame line. None was in the file.
