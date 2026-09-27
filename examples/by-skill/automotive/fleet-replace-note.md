# Fleet Replacement Note

`fleet-replace-note`

## What this is for

Compare fleet units the user listed on age, cost, and downtime, without a forced replacement.

## Scenario

Harbor Goods can replace two vans this year. Three are old. Van 4 is on a safety hold for brakes. No residual values are in the file.

## Example data

```text
budget count: 2
van 2: 11 years, downtime 6 days this quarter
van 4: 9 years, safety hold, brakes, downtime 14 days
van 7: 12 years, downtime not recorded
residual values: none in the file
approver: Diane Cho
```

## Example outcome

**Replacement note**
First: van 4. It is on a safety hold. Budget optics do not delay that.
Second: van 2, because downtime is in the file: 6 days.
Van 7: unranked on downtime. The cell is empty. It is the one that stays if only two can be ordered.
No residual is in this note. None was supplied.
Approver: Diane. This is not a purchase order.
