# RFI Writer

`rfi-writer`

## What this is for

Write a request for information that states the conflict, the location, and the date the answer is needed.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs a RFI by 30 September 2026. An RFI asks the designer to 'see the attached and advise' with no question.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

An RFI asks the designer to 'see the attached and advise' with no question.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Rfi**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026

**Decision**
An RFI with one located question, a need-by date, and no invented detail.

**From the file**
- site: Birch, Cochrane
- safety item: stays open
- quantity: their takeoff
- date: the look-ahead

Nothing in this draft was added from outside that file.
Next: Tom Reilly by 30 September 2026. This is not a sign-off.
