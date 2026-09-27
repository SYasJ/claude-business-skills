# Owner Cash Huddle

`owner-cash-huddle`

## What this is for

Set the week's cash picture from the till, the bills due, and the owner's buffer.

## Scenario

Diane counted $4,200 in the Harbor Goods till on Monday. Rent of $3,000 is due Thursday. A customer said they might pay $2,000. Her buffer is $1,500. A tax remittance of $800 is also due Friday.

## Example data

```text
counted: 4200 CAD, Mon 15 Sep 2026
rent: 3000, Thu 18 Sep
tax remittance: 800, Fri 19 Sep
maybe receipt: 2000, not in the bank
buffer: 1500
```

## Example outcome

**Week huddle**
Do not spend the $2,000. It is not in the till.

| Day | Cash if nothing else arrives | Bill |
| --- | --- | --- |
| Mon | 4,200 | — |
| Thu | 1,200 after rent | rent 3,000 |
| Fri | 400 after tax | tax 800 |

Thursday after rent is $1,200, under the $1,500 buffer, before Friday's tax. Friday's tax still gets paid. It is not the lever.
Decision: no owner draw and no new order this week unless the $2,000 actually arrives.
