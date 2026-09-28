# Schedule Look-Ahead

`schedule-look-ahead`

## What this is for

Build a short look-ahead from constraints, not from a hopeful bar chart.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs a look-ahead by 30 September 2026. A look-ahead schedules a pour before the inspection the city requires.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

A look-ahead schedules a pour before the inspection the city requires.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Look-ahead**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Parks the pour behind the inspection and names the constraint owner.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| site | Birch, Cochrane | Needs confirmation |
| safety item | stays open | Carried into the draft |
| quantity | their takeoff | Carried into the draft |
| date | the look-ahead | Needs confirmation |

**How this draft was built**

**1. List activities the constraints actually allow**

**2. Mark activities blocked by a missing RFI, material, or inspection**

**3. Match crew to the allowed work**

**4. Do not show blocked work as committed**

**5. Identify the constraint to remove next**

**Deliberately not done**
- Blocked work shown as committed.
- No constraint column.
- A look-ahead that ignores yesterday.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
