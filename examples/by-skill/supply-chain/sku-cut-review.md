# SKU Cut Review

`sku-cut-review`

## What this is for

Propose SKUs to stop reordering from the movement and the stock the user shows.

## Scenario

Four SKUs sold zero units in 90 days. One is a winter blade Diane says they must keep for November. All four still have stock on the shelf.

## Example data

```text
window: 16 Jun to 14 Sep 2026
SKU 1044 filters: 0 sold, 18 on hand
SKU 2201 wiper: 0 sold, 6 on hand
SKU 2208 mat: 0 sold, 4 on hand
SKU 3310 winter blade: 0 sold, 20 on hand, must keep for November
approver: Diane
```

## Example outcome

**Stop-reorder**
| SKU | Sold | On hand | Call |
| --- | --- | --- | --- |
| 1044 | 0 | 18 | stop reorder |
| 2201 | 0 | 6 | stop reorder |
| 2208 | 0 | 4 | stop reorder |
| 3310 | 0 | 20 | keep, winter |

This is not a write-off and not a savings number. Stock stays on the shelf until she decides a clearance. Approver: Diane.
