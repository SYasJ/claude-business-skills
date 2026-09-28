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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Corrects the status and offers a real redelivery window.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| lane | the one in the ask | Needs confirmation |
| tally | their count | Carried into the draft |
| limit | the one they stated | Carried into the draft |
| concealment | not advised | Needs confirmation |

**How this draft was built**

**1. Record the reason they know**

**2. Offer options they can perform**  
redelivery, pickup, or hold.

**3. Do not promise a window the route cannot make**

**4. Tell the customer the truth without blaming them for a company miss**

**5. Update the order status so the next driver sees it**

**Deliberately not done**
- A window the route cannot make.
- A blame-the-customer template.
- A status left stale.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Luis Ortega by 30 September 2026. This is a draft, not a sign-off.
