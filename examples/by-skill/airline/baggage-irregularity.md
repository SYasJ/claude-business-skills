# Baggage Irregularity

`baggage-irregularity`

## What this is for

Record a bag irregularity with the tag, the flight, and the status they know.

## Scenario

Tag 8812 did not arrive on KA412. Status in the system is delayed. A text already told the passenger the bag would be at the house by 8 p.m. Nobody has a delivery time.

## Example data

```text
tag: 8812
flight: KA412
status: delayed
passenger told: at the house by 20:00
delivery time on file: none
owner: station baggage desk
passport number: do not collect
```

## Example outcome

**Bag file — 8812**
Status: delayed, off KA412. Do not write lost.
The 20:00 house delivery was not known. Send a correction: we do not have a delivery time.
Owner: the baggage desk.
Do not put a passport number in this file.
