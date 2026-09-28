# Offer Comparison

`offer-comparison`

## What this is for

Compare property offers on the terms the user cares about, without advising which legal form to sign.

## Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs an offer comparison by 30 September 2026. One offer is higher but waives an inspection the seller has not disclosed defects for.

## Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

One offer is higher but waives an inspection the seller has not disclosed defects for.

The offers: CAD 79, dates not set, cap not set
The seller or buyer priorities: Cedar Clinic
Deadlines they stated: 30 September 2026
Contingencies visible in the offers: CAD 79, dates not set, cap not set
```

## Example outcome

**Offer comparison**
To: Helen Cho, property manager, Cedar Street Properties
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows the inspection gap and leaves the signature to the principal and their professional.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The offers | CAD 79, dates not set, cap not set | Needs confirmation |
| The seller or buyer priorities | Cedar Clinic | Carried into the draft |
| Deadlines they stated | 30 September 2026 | Carried into the draft |
| Contingencies visible in the offers | CAD 79, dates not set, cap not set | Needs confirmation |

**How this draft was built**

**1. Build a matrix of price, timing, contingencies, and costs they can see**

**2. Rank only on priorities they named**

**3. Do not invent a buyer's financing strength**

**4. Flag a deadline that needs a professional response**

**5. Recommend questions, not a signature**

**Deliberately not done**
- Invented financing strength.
- A signature recommendation.
- Hidden contingencies.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Helen Cho by 30 September 2026. This is a draft, not a sign-off.
