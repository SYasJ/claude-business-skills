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
Date: 14 September 2026

**Decision**
Parks the pour behind the inspection and names the constraint owner.

**From the file**
- site: Birch, Cochrane
- safety item: stays open
- quantity: their takeoff
- date: the look-ahead

Nothing in this draft was added from outside that file.
Next: Tom Reilly by 30 September 2026. This is not a sign-off.
