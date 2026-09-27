# Warehouse Model Review

`warehouse-model`

## What this is for

Review a warehouse model for grain mistakes and double-counted joins.

## Scenario

active_accounts jumped from 1,100 to 4,600 on 12 September after Noah joined the fact to payments. Payments has many rows per workspace. He has a 20-row sample.

## Example data

```text
claimed grain: one row per workspace per day
join added 12 Sep: payments on workspace_id
sample of 20 workspace-days: 17 have more than one payment row
metric before: 1,100 on 11 Sep
metric after: 4,600 on 12 Sep
modeler: Noah Berger
```

## Example outcome

**Model review**
Do not use the 12 September active_accounts figure.

The claimed grain is one row per workspace per day. The payments join is many rows per workspace.
In the 20-row sample, 17 keys fan out. That is the sample, not a rate for the whole table.
The jump from 1,100 to 4,600 fits a fan-out. It is not proof of 3,500 new workspaces.
Fix to ask Noah for: count of workspace-days with more than one row, and a join that does not multiply the flag.
This review does not rewrite the model.
