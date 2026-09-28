# Account Opening Operations

`account-opening-ops`

## What this is for

Review an account-opening checklist for identity steps they require, without collecting secrets into the chat.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs an account-opening checklist by 30 September 2026. Staff want to skip an identity step because the customer is in a hurry.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Staff want to skip an identity step because the customer is in a hurry.

Their required steps: Payment run 14 Sep; Account opening file 221. Both unassigned as of 14 September 2026
What is complete: Liquidity ladder, last reviewed 14 September 2026. No owner named since
Exceptions: Payment run 14 Sep is open. Account opening file 221 was raised verbally and never logged
The reviewer: Priya Shah. No second reviewer named
```

## Example outcome

**Account-opening checklist**
Northline Studio · 14 September 2026 · Due 30 September 2026

**Decision**
Keeps the step and routes any exception to the compliance owner.

**Checklist**

- [x] **Their required steps** — Payment run 14 Sep; Account opening file 221. Both unassigned as of 14 September 2026  
      Evidenced in the file
- [x] **What is complete** — Liquidity ladder, last reviewed 14 September 2026. No owner named since  
      Evidenced in the file
- [x] **Exceptions** — Payment run 14 Sep is open. Account opening file 221 was raised verbally and never logged  
      Evidenced in the file
- [ ] **The reviewer** — Priya Shah. No second reviewer named  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. Use their checklist. Do not invent a regulator's rule
2. Note missing identity steps as gaps
3. Do not ask customers to send passwords or full card data by chat
4. Exceptions need their compliance owner
5. A possible sanctions match follows their screening process. Do not suggest altering a name

**Deliberately not done**
- Invented regulatory rules.
- Name changes to dodge screening.
- Secrets collected in chat.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Priya Shah closes the open items before 30 September 2026.
