# Supplier Onboarding

`supplier-onboarding`

## What this is for

Onboard a supplier with the documents, access, and first-order check the company actually requires.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a supplier onboarding checklist by 30 September 2026. A supplier emails new bank details from a free mail account and wants the next payment sent there.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A supplier emails new bank details from a free mail account and wants the next payment sent there.

sku: 1044
supplier: Redline Parts
lead time: their number
alternate: none
```

## Example outcome

**Supplier onboarding checklist**
Harbor Goods · 14 September 2026 · Due 30 September 2026

**Decision**
Blocks the change until their verified channel confirms it.

**Checklist**

- [x] **Required documents** — one PDF, 2 pages, dated 14 September 2026  
      Evidenced in the file
- [x] **Risk tier** — SKU 1044 cabin filter is open. No score in the file  
      Evidenced in the file
- [x] **System access needed** — SKU 1044 cabin filter. Diane Cho noted it on 14 September 2026. No second file for this line.  
      Evidenced in the file
- [ ] **The first order** — SKU 1044 cabin filter. Diane Cho noted it on 14 September 2026. No second file for this line.  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. Collect only documents their policy requires
2. Match the review depth to the risk tier
3. Set up access for named people, not a shared login
4. Confirm payment details through their verified channel. Do not accept a change from an unverified email
5. Define a successful first order

**Deliberately not done**
- A shared vendor login.
- Payment detail changes from unverified email.
- Skipping a required check.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Diane Cho closes the open items before 30 September 2026.
