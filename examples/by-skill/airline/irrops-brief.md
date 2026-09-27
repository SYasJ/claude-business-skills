# Irregular Ops Brief

`irrops-brief`

## What this is for

Brief the station on a disrupted flight using the facts the controller has.

## Scenario

KA412 YYZ-YYC is late. The controller's note says a ground hold. A draft brief blames maintenance. Booked passengers are 142. No spare aircraft is assigned.

## Example data

```text
flight: KA412 YYZ-YYC
fact: ground hold, note timed 16 Sep 2026 14:05
passengers booked: 142
spare aircraft: none assigned
next update promised: 15:00
station: YYC, Luis Ortega
```

## Example outcome

**Station brief — KA412**
Ground hold. That is the reason in the note. Maintenance comes out of the draft.
Passengers booked: 142.
No spare is assigned. Do not tell the station one is coming.
Next update: 15:00. Luis owns the board until then.
