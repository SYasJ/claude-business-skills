# Punch List

`punch-list`

## What this is for

Turn a punch list into items with a location, an owner, and a done standard.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs a punch list by 30 September 2026. A punch list says 'finish lobby' with no owner.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

A punch list says 'finish lobby' with no owner.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Punch list**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A list of located items, with life-safety called out and an owner on each line.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| site | Birch, Cochrane | Needs confirmation |
| safety item | stays open | Carried into the draft |
| quantity | their takeoff | Carried into the draft |
| date | the look-ahead | Needs confirmation |

**How this draft was built**

**1. One item, one location, one owner**

**2. Describe the defect so someone can find it**

**3. Define done as observable, not as 'make good'**

**4. Separate life-safety items and say they are not cosmetic**

**5. Do not invent counts**

**Deliberately not done**
- A vague make-good list.
- Life-safety mixed with paint nits.
- Closure without evidence.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
