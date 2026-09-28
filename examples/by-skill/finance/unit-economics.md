# Unit Economics

`unit-economics`

## What this is for

Calculate contribution economics for one real unit the business sells, and show which assumption dominates.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs an unit economics sheet by 30 September 2026. A subscription team wants to know if a new annual plan clears contribution after onboarding labor.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A subscription team wants to know if a new annual plan clears contribution after onboarding labor.

The unit: customer, order, location, or contract: customer: in the file; order: not in the file; location: open; contract: in the file
Price and direct costs the user can support: CAD 49
Acquisition cost definition: CAD 18 direct. Overhead not in this line
Retention or repeat evidence, if any: one PDF, 2 pages, dated 14 September 2026
```

## Example outcome

**Unit economics sheet**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Defines the customer-year, keeps overhead out, and shows payback only to the extent retention evidence exists.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The unit: customer, order, location, or contract | customer: in the file; order: not in the file; location: open; contract: in the file | Needs confirmation |
| Price and direct costs the user can support | CAD 49 | Carried into the draft |
| Acquisition cost definition | CAD 18 direct. Overhead not in this line | Carried into the draft |
| Retention or repeat evidence, if any | one PDF, 2 pages, dated 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Define the unit**  
Say exactly what one unit is. Mixing orders and customers in one margin is how teams fool themselves.

**2. Build contribution**  
Price minus costs that vary with the unit. Keep fixed overhead out of the unit and show it separately.

**3. Treat acquisition honestly**  
Include the costs the user says are required to win the unit. Do not ignore discounts and onboarding if they are real.

**4. Show payback only if retention is known**  
If retention is a guess, label payback as illustrative and do not lead with it.

**5. Sensitivity**  
Name the one assumption that swings the answer. Recommend improving that input, not decorating the model.

**Deliberately not done**
- A lifetime value built on an invented retention curve.
- Forgetting discounts, refunds, or implementation cost.
- Comparing the result to a generic SaaS benchmark from memory.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
