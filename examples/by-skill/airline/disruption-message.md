# Disruption Message

`disruption-message`

## What this is for

Write the customer message for a cancellation with the rebooking fact they have.

## Scenario

KA188 is cancelled. No replacement seat is confirmed. A draft promises the 10:00 departure and a full refund. The station may say they are still searching for a seat.

## Example data

```text
flight: KA188
status: cancelled
rebooking confirmed: none
care authorized: say they are searching for a seat
refund amount: not in the file
reason authorized: none
```

## Example outcome

**Message**
KA188 is cancelled. We do not have a confirmed seat yet. We are still searching.

**Not in the message**
The 10:00. A full refund. A cause. None of those are in the file.
