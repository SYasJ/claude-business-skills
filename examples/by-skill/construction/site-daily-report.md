# Site Daily Report

`site-daily-report`

## What this is for

Write a site daily report from observed work, weather, and safety notes, with no invented quantities.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs a daily report by 30 September 2026. A draft says the slab was poured though the crew was rained out.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

A draft says the slab was poured though the crew was rained out.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Daily report**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Records the rain delay and leaves the pour unclaimed.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| site | Birch, Cochrane | Needs confirmation |
| safety item | stays open | Carried into the draft |
| quantity | their takeoff | Carried into the draft |
| date | the look-ahead | Needs confirmation |

**How this draft was built**

**1. Record only work they observed or documented**

**2. Quantities come from their count. Unknown stays unknown**

**3. Safety incidents and near misses they reported go in plainly**

**4. Delays get a cause they stated**

**5. Note visitors and inspections they named**

**Deliberately not done**
- Invented quantities.
- A hidden delay.
- A safety note removed to look clean.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
