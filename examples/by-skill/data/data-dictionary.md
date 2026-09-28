# Data Dictionary

`data-dictionary`

## What this is for

Write a data dictionary entry that tells an analyst what a field means, what it does not mean, and who owns it.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a data dictionary entry by 30 September 2026. A field called status has values 1, 2, and 9, and nobody agrees what 9 means.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A field called status has values 1, 2, and 9, and nobody agrees what 9 means.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Data dictionary entry**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Records the known values, marks 9 as unresolved, and names the owner who must decide.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Name the grain of the table before defining the field**

**2. Write the business meaning in plain language, plus a false friend it is often confused with**

**3. Document nulls, sentinels, and units. Do not guess a unit**

**4. State the source system if they know it**

**5. Name an owner. An unowned field will rot**

**Deliberately not done**
- A dictionary that copies the column name as the definition.
- Invented example customers.
- No owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
