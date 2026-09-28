# Capex Business Case

`capex-business-case`

## What this is for

Write a capital-spend case that states the problem, the alternatives, and the cash consequences without fake precision.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a capex business case by 30 September 2026. Operations wants a packaging machine and has one quote and a claim that it will 'pay for itself'.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Operations wants a packaging machine and has one quote and a claim that it will 'pay for itself'.

cash: the counted figure in the ask, one entity
maybe receipt: not in the bank
buffer: the one they named
new spend: not in the base case
```

## Example outcome

**Capex business case**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A case with alternatives, cash timing, a benefit the team can later observe, and no invented hurdle rate.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| cash | the counted figure in the ask, one entity | Needs confirmation |
| maybe receipt | not in the bank | Carried into the draft |
| buffer | the one they named | Carried into the draft |
| new spend | not in the base case | Needs confirmation |

**How this draft was built**

**1. Define the problem**  
Downtime, capacity, safety, or compliance. A request that starts with the vendor's name is not ready.

**2. Compare alternatives**  
Buy, lease, outsource, or defer. Include do nothing and its operational cost if the user described one.

**3. Lay out cash**  
Deposit, install, training, and maintenance. Benefits are cash or a clearly non-cash obligation the user names, such as a safety requirement.

**4. Avoid theatrical IRR**  
If the user wants a return metric, compute it only from their cash items and show the sensitivity. Do not invent a hurdle rate.

**5. Name the benefit owner**  
Who will confirm, after installation, that the benefit showed up.

**Deliberately not done**
- A vendor quote pasted into a memo with no alternative.
- An IRR built on imagined savings.
- Ignoring training and downtime during install.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
