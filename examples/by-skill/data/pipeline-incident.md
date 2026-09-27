# Pipeline Incident

`pipeline-incident`

## What this is for

Write a pipeline failure from the log lines the user has, with the hold and the rerun owner.

## Scenario

orders_daily failed this morning. Noah pasted one error line. The sales dashboard refreshed anyway and still shows yesterday's subtitle as today.

## Example data

```text
job: orders_daily
error line pasted: 15 Sep 2026 05:12 ERROR missing file s3://harbor/orders/2026-09-14.csv
table: analytics.orders_daily
last good load: 14 Sep 2026 05:40, covering 13 Sep
dashboard: refreshed 15 Sep 06:05, subtitle says 15 Sep
rerun owner: Noah Berger
credentials in the paste: none
```

## Example outcome

**Pipeline note**
orders_daily is stale. Last good load covers 13 September, loaded 14 September 05:40.
Error on file: missing 2026-09-14.csv at 05:12. No other cause is in the paste.
Hold: do not use the dashboard figure labeled 15 September. The refresh did not bring new orders.
Rerun: Noah, after the file is actually there. Do not rerun against a missing path and call it fixed.
Next: Jonah changes the subtitle to the last good day before the 09:00 sales meeting.
