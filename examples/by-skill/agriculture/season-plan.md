# Season Plan

`season-plan`

## What this is for

Plan a season from fields, labor, and cash the farm can actually commit.

## Scenario

Ruth McKay, operator at Two Hills Farm in Olds, needs a season plan by 30 September 2026. A plan adds a crop the only operator cannot harvest in the same week as the existing one.

## Example data

```text
From: Ruth McKay, operator
Organization: Two Hills Farm, Olds
Date: 14 September 2026
Needed by: 30 September 2026

A plan adds a crop the only operator cannot harvest in the same week as the existing one.

week: 14 Sep 2026
cash: their figure
treatment: not prescribed here
sheet: theirs
```

## Example outcome

**Season plan**
To: Ruth McKay, operator, Two Hills Farm
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows the labor clash and asks which enterprise to cut.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| week | 14 Sep 2026 | Needs confirmation |
| cash | their figure | Carried into the draft |
| treatment | not prescribed here | Carried into the draft |
| sheet | theirs | Needs confirmation |

**How this draft was built**

**1. List enterprises they will run**

**2. Match labor and equipment to the calendar they supplied**

**3. Note cash needs at the expensive weeks**

**4. Respect withdrawal or rotation limits they stated. Do not provide instructions to synthesize pesticides or bypass a label**

**5. Identify the week that breaks if labor is short**

**Deliberately not done**
- Pesticide synthesis.
- A plan that ignores a stated label limit.
- No labor check.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Ruth McKay by 30 September 2026. This is a draft, not a sign-off.
