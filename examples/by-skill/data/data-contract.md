# Data Contract

`data-contract`

## What this is for

Write the columns, grain, freshness, and owner a producer and a consumer can both use.

## Scenario

Product wants active_accounts on the dashboard by 06:00. Noah's job finished at 09:30 on eight of the last ten weekdays. They need a contract both sides can sign.

## Example data

```text
table: analytics.active_accounts
grain: one row per workspace per day
required columns: workspace_id, day, active_flag
nullable: none of those three
producer: Noah Berger
consumer: Jonah Park
job finish, last 10 weekdays: 09:12 to 09:41, two runs failed
consumer ask: 06:00 local
```

## Example outcome

**Contract — analytics.active_accounts**
Grain: one row per workspace per day.
Required: workspace_id, day, active_flag. None null.
Freshness in this contract: ready by 10:00 America/Edmonton, or the dashboard shows the prior day.
Not in this contract: 06:00. The job does not finish then.
Breaks the contract: a null workspace_id, a day with two rows, or a finish after 10:00.
Owners: Noah produces. Jonah accepts the 10:00 clock or funds a faster job.
Next: both initial this by 30 September 2026. Until then the dashboard must not say 'live at 6'.
