# Farm Cash Week

`farm-cash-week`

## What this is for

Review a farm's coming weeks of cash against known receipts and bills.

## Scenario

Ruth McKay, operator at Two Hills Farm in Olds, needs a weekly farm cash note by 30 September 2026. A note treats an unsigned grain contract as cash already coming.

## Example data

```text
From: Ruth McKay, operator
Organization: Two Hills Farm, Olds
Date: 14 September 2026
Needed by: 30 September 2026

A note treats an unsigned grain contract as cash already coming.

week: 14 Sep 2026
cash: their figure
treatment: not prescribed here
sheet: theirs
```

## Example outcome

**Weekly farm cash note**
To: Ruth McKay, operator, Two Hills Farm
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Labels the contract hoped and shows the break week without it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| week | 14 Sep 2026 | Needs confirmation |
| cash | their figure | Carried into the draft |
| treatment | not prescribed here | Carried into the draft |
| sheet | theirs | Needs confirmation |

**How this draft was built**

**1. List receipts only if a buyer or program has confirmed them, or label them hoped**

**2. List bills by date**

**3. Show the week the buffer breaks**

**4. Separate a capital buy from operating bills**

**5. Do not advise a lender fraud or a concealed sale**

**Deliberately not done**
- Hoped receipts shown as certain.
- Concealed sales.
- A capital buy hidden in operations.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Ruth McKay by 30 September 2026. This is a draft, not a sign-off.
