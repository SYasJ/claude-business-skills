# Cohort Analysis

`cohort-analysis`

## What this is for

Build a cohort view that follows a defined group over time without mixing incompatible cohorts.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a cohort analysis by 30 September 2026. Last week's cohort looks like it retained worse, but the week is not over.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Last week's cohort looks like it retained worse, but the week is not over.

The cohort definition: orders_daily, recorded 14 September 2026. No supporting file attached
The event that starts the clock: orders_daily, recorded 14 September 2026. No supporting file attached
The success event: orders_daily, recorded 14 September 2026. No supporting file attached
The time grain: five working days, due 30 September 2026
```

## Example outcome

**Cohort analysis**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Marks the week incomplete and refuses a churn conclusion from it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The cohort definition | orders_daily, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The event that starts the clock | orders_daily, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The success event | orders_daily, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The time grain | five working days, due 30 September 2026 | Needs confirmation |

**How this draft was built**

**1. Define membership and the start event before drawing a curve**

**2. Keep cohorts comparable. Do not mix a pricing change cohort into an older one without a label**

**3. Use only their data. If a week is incomplete, mark it incomplete rather than as a drop**

**4. Show the denominator. A retention rate without a cohort size is not interpretable**

**5. Call out mix shift if they supplied the evidence**

**Deliberately not done**
- An incomplete week drawn as churn.
- No denominator.
- Mixing incompatible cohorts silently.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
