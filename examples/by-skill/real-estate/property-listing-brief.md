# Property Listing Brief

`property-listing-brief`

## What this is for

Brief a property listing from facts the owner confirmed, with no invented features.

## Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a listing brief by 30 September 2026. A draft says the unit rents for a number the owner has not achieved.

## Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A draft says the unit rents for a number the owner has not achieved.

address: the one in the ask
rent roll: their sheet
comp: not invented
legal review: not done here
```

## Example outcome

**Listing brief**
To: Helen Cho, property manager, Cedar Street Properties
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the invented rent and lists defects the owner already disclosed.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| address | the one in the ask | Needs confirmation |
| rent roll | their sheet | Carried into the draft |
| comp | not invented | Carried into the draft |
| legal review | not done here | Needs confirmation |

**How this draft was built**

**1. Use only confirmed features**

**2. Disclose known material defects they told you about. Do not help hide them**

**3. Separate lifestyle copy from measurable facts**

**4. Do not invent school quality, income, or a legal use**

**5. Mark what a buyer must verify**

**Deliberately not done**
- Hidden defects.
- Invented income.
- A valuation disguised as a listing.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Helen Cho by 30 September 2026. This is a draft, not a sign-off.
