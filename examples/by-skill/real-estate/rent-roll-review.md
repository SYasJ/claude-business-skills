# Rent Roll Review

`rent-roll-review`

## What this is for

Review a rent roll for inconsistencies, expirations, and concessions the user can see.

## Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a rent-roll review by 30 September 2026. A roll shows full occupancy while three units are marked 'free rent' with no end date.

## Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A roll shows full occupancy while three units are marked 'free rent' with no end date.

address: the one in the ask
rent roll: their sheet
comp: not invented
legal review: not done here
```

## Example outcome

**Rent-roll review**
To: Helen Cho, property manager, Cedar Street Properties
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Separates free rent from paying occupancy and flags the missing end dates.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| address | the one in the ask | Needs confirmation |
| rent roll | their sheet | Carried into the draft |
| comp | not invented | Carried into the draft |
| legal review | not done here | Needs confirmation |

**How this draft was built**

**1. Check that units, rent, and dates are internally consistent**

**2. Flag expirations inside their horizon**

**3. Separate contractual rent from concessions they disclosed**

**4. Do not invent market rent**

**5. Note vacant units and the story they gave**

**Deliberately not done**
- Invented market rent.
- Concessions hidden in the headline rent.
- A roll that does not add up.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Helen Cho by 30 September 2026. This is a draft, not a sign-off.
