# Gas Nomination

`gas-nomination`

## What this is for

Check a nomination against the confirmed volume and the cycle time the user states.

## Scenario

The cycle closes at 11:00 America/Edmonton. Confirmed production for the pad is 3.6 mmcf. A draft nomination still says 4.2. It is 10:40.

## Example data

```text
cycle deadline: 11:00 America/Edmonton, 16 Sep 2026
now: 10:40
confirmed: 3.6 mmcf
draft nom: 4.2 mmcf
submitter: Devon Hale
threshold: 0.3
```

## Example outcome

**Nomination check**
Do not submit 4.2. Confirmed is 3.6. The gap is 0.6, over his threshold.
4.2 is a wish from yesterday's nom. It is not confirmed production.
There is time before 11:00 to submit 3.6. A nom after 11:00 is late. Do not call it on time.
Submitter: Devon.
