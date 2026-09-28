# Citation Hygiene

`citation-hygiene`

## What this is for

Check citations so every claim that needs a source has one the user can verify.

## Scenario

Dr. Nia Okonkwo, research lead at Riverbend College in Lethbridge, needs a citation check by 30 September 2026. A paragraph says 'studies show' and lists no study the user has.

## Example data

```text
From: Dr. Nia Okonkwo, research lead
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

A paragraph says 'studies show' and lists no study the user has.

The draft: one file, dated 14 September 2026. No earlier version attached for comparison
The sources they have: note from Dr. Nia Okonkwo, 14 September 2026. No outside report
The citation style if required: no citation attached
Claims that sound factual: the draft sentence is broader than the note
```

## Example outcome

**Citation check**
To: Dr. Nia Okonkwo, research lead, Riverbend College
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Replaces the phrase with an assumption or a request for the actual study.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The draft | one file, dated 14 September 2026. No earlier version attached for comparison | Needs confirmation |
| The sources they have | note from Dr. Nia Okonkwo, 14 September 2026. No outside report | Carried into the draft |
| The citation style if required | no citation attached | Carried into the draft |
| Claims that sound factual | the draft sentence is broader than the note | Needs confirmation |

**How this draft was built**

**1. Mark factual claims that lack a source the user provided**

**2. Do not invent a citation to fill a gap. Ask for a source or rewrite the claim as an assumption**

**3. Match quotations to text they supplied. A quote you cannot see is not used**

**4. Note style errors only after existence is confirmed**

**5. Separate the user's analysis from cited facts**

**Deliberately not done**
- Invented papers.
- A quotation you cannot verify.
- A citation that does not support the claim.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Nia Okonkwo by 30 September 2026. This is a draft, not a sign-off.
