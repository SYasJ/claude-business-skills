# Balance Reconciliation

`balance-reconciliation`

## What this is for

Reconcile two extracts the user provides and list the rows that do not match.

## Scenario

Noah has two extracts for 12 September. orders_daily sums to $18,400. The billing export sums to $17,160. Three order ids appear on only one side.

## Example data

```text
as of: 12 Sep 2026
key: order_id
amount column: total_cad
orders_daily: 42 rows, sum 18400
billing export: 40 rows, sum 17160
only in orders_daily: 4412, 4418, 4420
only in billing: none
difference: 1240
```

## Example outcome

**Tie-out — 12 September**
orders_daily $18,400. Billing $17,160. Gap $1,240. No plug.

| order_id | In orders_daily | In billing |
| --- | --- | --- |
| 4412 | yes | no |
| 4418 | yes | no |
| 4420 | yes | no |

The three ids are the unmatched set in these files. This note does not say why they are missing.
Do not refresh a revenue slide from orders_daily until Noah explains the three ids.
Next: Noah checks those ids by 16 September.
