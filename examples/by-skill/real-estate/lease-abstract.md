# Lease Abstract

`lease-abstract`

## What this is for

Abstract a lease the user provides into dates, money, and notice clauses, without a legal opinion.

## Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a lease abstract by 30 September 2026. An abstract assumes a five-year renewal the lease only mentions as a negotiation.

## Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

An abstract assumes a five-year renewal the lease only mentions as a negotiation.

address: the one in the ask
rent roll: their sheet
comp: not invented
legal review: not done here
```

## Example outcome

**Lease abstract**
To: Helen Cho, property manager, Cedar Street Properties
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Marks renewal as unwritten and lists the counsel question.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| address | the one in the ask | Needs confirmation |
| rent roll | their sheet | Carried into the draft |
| comp | not invented | Carried into the draft |
| legal review | not done here | Needs confirmation |

**How this draft was built**

**1. Quote dates, rent, and notice periods from the text**

**2. Flag missing pages or amendments**

**3. Do not assume a renewal right that is not written**

**4. Separate what the lease says from what the tenant hopes**

**5. List questions for counsel**

**Deliberately not done**
- Assumed renewal rights.
- A legal default opinion.
- An abstract of a missing page.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Helen Cho by 30 September 2026. This is a draft, not a sign-off.
