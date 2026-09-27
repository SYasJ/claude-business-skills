# Data Lineage

`data-lineage`

## What this is for

Trace a metric to the source tables the user can name, and stop where the trail stops.

## Scenario

Jonah asked where active_accounts comes from. Noah can point at a dbt model name and then the trail stops. The slide says 'the warehouse'.

## Example data

```text
metric: active_accounts, defined as workspaces with a login on that day
known hop: model fct_active_accounts, owner Noah
source tables named: none
second writer: unknown
slide text: "comes from the warehouse"
```

## Example outcome

**Lineage note**
active_accounts is the count of workspaces with a login that day, per Jonah's definition.
Known hop: fct_active_accounts, owner Noah Berger.
Next hop: not in the file. Do not draw a source table from the column name.
The slide line 'the warehouse' is not a source.
Open: the table under the model, and whether any other job writes active_flag.
Next: Noah names that table before this metric is used in a board pack.
