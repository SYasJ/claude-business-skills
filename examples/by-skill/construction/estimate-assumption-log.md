# Estimate Assumption Log

`estimate-assumption-log`

## What this is for

Log estimate assumptions so a bid can be explained without invented quantities.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs an assumption log by 30 September 2026. An estimate assumes night work is included but the invitation excludes it.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

An estimate assumes night work is included but the invitation excludes it.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Assumption log**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Records the conflict and refuses to hide the exclusion.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| site | Birch, Cochrane | Needs confirmation |
| safety item | stays open | Carried into the draft |
| quantity | their takeoff | Carried into the draft |
| date | the look-ahead | Needs confirmation |

**How this draft was built**

**1. State the documents the estimate is based on**

**2. List quantities as measured or as an allowance**

**3. Write exclusions plainly**

**4. Do not invent a productivity rate and call it fact. Label judgments**

**5. Note what a missing drawing would change**

**Deliberately not done**
- Hidden exclusions.
- Invented quantities.
- A log written to mislead.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
