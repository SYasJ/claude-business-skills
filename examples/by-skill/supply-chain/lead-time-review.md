# Lead Time Review

`lead-time-review`

## What this is for

Compare the lead time in the system to the receipts the user can show.

## Scenario

The system lead time for Redline Parts on SKU 1044 is 14 days. Diane has three receipts: 26, 28, and 27 days from PO to dock.

## Example data

```text
system lead time: 14 days
receipts: PO 12 Jul to dock 7 Aug (26 days); PO 2 Aug to dock 30 Aug (28); PO 18 Aug to dock 14 Sep (27)
excluded: one air freight in June, she said it is not the pattern
who edits the system: Diane Cho
```

## Example outcome

**Lead-time note**
Three ground receipts: 26, 28, 27 days. The system says 14. The gap repeats.
The June air freight stays out, as she asked.
Recommendation: Diane changes the system to 28 days, matching the slow receipt, not the average dressed up as exact.
Thin? No. Three receipts agree. Still her edit, not an automatic write.
Do not pad further without another receipt.
