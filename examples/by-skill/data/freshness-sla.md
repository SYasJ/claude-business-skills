# Freshness SLA

`freshness-sla`

## What this is for

Set a freshness promise the job can meet, from the finish times the user has.

## Scenario

Jonah wants the dashboard to say data is ready at 06:00. Noah listed the last ten weekday finish times. Eight are after 09:00. Two failed.

## Example data

```text
job: fct_active_accounts
finish times: 09:12, 09:20, 09:41, failed, 09:18, 09:33, 09:15, failed, 09:28, 09:22
consumer need: 06:00 America/Edmonton
owner: Noah Berger
if late: dashboard should show the prior day, Jonah agrees
```

## Example outcome

**Freshness note**
Do not promise 06:00. Eight finished runs landed between 09:12 and 09:41. Two failed.

Promise that matches the file: ready by 10:00, or show the prior day.
Call if it misses 10:00: Noah first, Jonah if the prior day is also missing.
The average is not the promise. The slow run is.
Next: Jonah changes the dashboard label. Noah does not sign 06:00.
