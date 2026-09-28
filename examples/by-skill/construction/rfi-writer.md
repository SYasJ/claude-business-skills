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

The conflict: Birch site, Cochrane, recorded 14 September 2026. No supporting file attached
The drawing or spec location: two deals cited from memory. Neither has a written loss reason
The date needed: 30 September 2026
The proposed clarification if any: Birch site, Cochrane, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Rfi**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
An RFI with one located question, a need-by date, and no invented detail.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The conflict | Birch site, Cochrane, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The drawing or spec location | two deals cited from memory. Neither has a written loss reason | Carried into the draft |
| The date needed | 30 September 2026 | Carried into the draft |
| The proposed clarification if any | Birch site, Cochrane, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. Describe the conflict with locations they gave**

**2. Ask one question**

**3. State the date the answer is needed and why**

**4. A proposed clarification is labeled as a proposal, not as approval**

**5. Attach references they have. Do not invent a detail**

**Deliberately not done**
- Three questions in one RFI.
- An invented detail.
- Work proceeding on a silent guess.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
