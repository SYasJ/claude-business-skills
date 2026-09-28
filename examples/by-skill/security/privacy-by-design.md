# Privacy by Design

`privacy-by-design`

## What this is for

Review a feature for data minimization, purpose, and user-facing honesty before it ships.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a privacy design note by 30 September 2026. A feature stores a full ID document to personalize a greeting.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A feature stores a full ID document to personalize a greeting.

The data the feature collects: Access review Q3, recorded 14 September 2026. No supporting file attached
The purpose: A feature stores a full ID document to personalize a greeting. Stated once, in the ask. Not written down anywhere else
Retention if known: Endpoint patch ring 2. Stated in the ask, not documented anywhere else
What the user is told: Phishing report 4412, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Privacy design note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Cuts the document, keeps the display name if needed, and flags the notice gap.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The data the feature collects | Access review Q3, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The purpose | A feature stores a full ID document to personalize a greeting. Stated once, in the ask. Not written down anywhere else | Carried into the draft |
| Retention if known | Endpoint patch ring 2. Stated in the ask, not documented anywhere else | Carried into the draft |
| What the user is told | Phishing report 4412, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. List each data element and the purpose it serves. No purpose, recommend cutting it**

**2. Prefer the least identifying option that still meets the purpose**

**3. Check that the notice or UI matches the collection. A mismatch is a finding**

**4. Retention is a question if unknown. Do not invent a period**

**5. Access, export, and deletion are product questions to flag, not legal conclusions**

**Deliberately not done**
- Collecting data for a future maybe.
- A UI that hides the collection.
- A fake legal clearance.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
