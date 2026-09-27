# Dock Exception

`dock-exception-note`

## What this is for

Record a dock exception with the count, the PO, and the photo or tally they have.

## Scenario

PO 5521 billed 40 filters. The dock tally is 32. The seal note says intact. No photo. Diane needs the exception before the 32 are marked as 40 in stock.

## Example data

```text
PO: 5521
billed: 40 of SKU 1044
tally: 32
seal: noted intact
photo: none
carrier: Kite Freight
date: 14 Sep 2026
```

## Example outcome

**Dock note — PO 5521**
Short 8. Available stock from this receipt: 32, not 40.
Seal was noted intact. That is not a theft finding. No photo is in the file.
Tell the buyer: Diane. Tell the carrier: after she sends this count, not before.
Do not raise available stock to match the PO while the 8 are open.
