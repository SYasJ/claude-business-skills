# Dispatch Plan

`dispatch-plan`

## What this is for

Plan a dispatch from orders, hours, and equipment limits the user stated.

## Scenario

Luis Ortega, dispatch lead at Kite Freight in Calgary, needs a dispatch plan by 30 September 2026. A dispatcher is told to log a break that did not happen so the route stays legal on paper.

## Example data

```text
From: Luis Ortega, dispatch lead
Organization: Kite Freight, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A dispatcher is told to log a break that did not happen so the route stays legal on paper.

lane: the one in the ask
tally: their count
limit: the one they stated
concealment: not advised
```

## Example outcome

**Dispatch plan**
To: Luis Ortega, dispatch lead, Kite Freight
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the false log and shows which order must move instead.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| lane | the one in the ask | Needs confirmation |
| tally | their count | Carried into the draft |
| limit | the one they stated | Carried into the draft |
| concealment | not advised | Needs confirmation |

**How this draft was built**

**1. Assign work inside the hours and equipment limits they stated**

**2. Do not advise concealing hours or cargo**

**3. Show which order slips if a vehicle is down**

**4. Name the customer promise at risk**

**5. Include a check-in rule**

**Deliberately not done**
- Concealed hours.
- A plan over a stated limit.
- No view of the slipped order.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Luis Ortega by 30 September 2026. This is a draft, not a sign-off.
