# Dealer Launch Check

`dealer-launch-check`

## What this is for

Check whether a local launch day has the cars, the staff, and the offer the dealer can honor.

## Scenario

Saturday's ad says six cars to test-drive and a $299 payment. Two cars are on the ground. The payment was not calculated. Four staff are rostered.

## Example data

```text
date: Sat 20 Sep 2026
ad: 6 test-drive cars, $299 a month
on the ground: 2
in transit: 4, no arrival date
staff rostered: 4
payment worksheet: none
owner: Carla Singh
```

## Example outcome

**Launch check**
Cut the ad to two test-drive cars. The other four are not on the ground.
Remove $299. Nobody calculated it.
Staff: four are rostered. That part can stand.
Owner: Carla. She does not run the six-car line on Saturday.
