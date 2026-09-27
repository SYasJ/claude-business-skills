# Delivery Exception

`delivery-exception`

## What this is for

Handle a failed delivery with a new promise you can keep and a reason the customer can understand.

## Scenario

Luis Ortega, dispatch lead at Kite Freight in Calgary, needs a delivery exception by 30 September 2026. A text says the parcel was delivered though the driver marked an access failure.

## Example data

```text
From: Luis Ortega, dispatch lead
Organization: Kite Freight, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A text says the parcel was delivered though the driver marked an access failure.

lane: the one in the ask
tally: their count
limit: the one they stated
concealment: not advised
```

## Example outcome

**Delivery exception**
To: Luis Ortega, dispatch lead, Kite Freight
Date: 14 September 2026

**Decision**
Corrects the status and offers a real redelivery window.

**From the file**
- lane: the one in the ask
- tally: their count
- limit: the one they stated
- concealment: not advised

Nothing in this draft was added from outside that file.
Next: Luis Ortega by 30 September 2026. This is not a sign-off.
