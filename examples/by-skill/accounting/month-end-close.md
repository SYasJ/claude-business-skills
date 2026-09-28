# Month-End Close

`month-end-close`

## What this is for

Run a practical month-end close that produces one set of numbers and a short list of judgments.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a month-end close pack by 30 September 2026. The controller wants a soft close by day six and cash is still unreconciled on day five.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The controller wants a soft close by day six and cash is still unreconciled on day five.

Period and entities: month ending 14 September 2026
Open reconciliations: Operating cash and one other, both unconfirmed as of 14 September 2026
Known judgments: Undeposited funds. Stated in the ask, not documented anywhere else
Sign-off owner: Priya Shah, controller
```

## Example outcome

**Month-end close pack**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses sign-off on unreconciled cash, lists open judgments, and separates any late entries.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Period and entities | month ending 14 September 2026 | Needs confirmation |
| Open reconciliations | Operating cash and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| Known judgments | Undeposited funds. Stated in the ask, not documented anywhere else | Carried into the draft |
| Sign-off owner | Priya Shah, controller | Needs confirmation |

**How this draft was built**

**1. Freeze the checklist**  
Use their close list. Add a missing reconciliation only if a balance sheet account has no owner.

**2. Clear suspense**  
Items in suspense need a destination or a labeled open item. Do not leave a plug and call the period closed.

**3. Record judgments**  
Accruals, cut-off, and estimates get a note with the fact pattern and the person who accepted it.

**4. Flux before sign-off**  
Explain material movements in plain language. A journal without a flux story is not reviewed.

**5. Lock and list**  
After sign-off, list post-close entries separately. Quiet edits are how trust dies.

**Deliberately not done**
- Closing with an unreconciled cash account.
- Post-close journals with no log.
- A narrative that invents reasons for a variance.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
