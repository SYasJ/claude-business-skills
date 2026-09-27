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
Harbor Goods · 14 September 2026

Blocks the change until their verified channel confirms it.

- [x] Required documents — in the file. one PDF, 2 pages, dated 14 September 2026
- [x] Risk tier — in the file. SKU 1044 cabin filter is open. No score in the file
- [x] System access needed — in the file. SKU 1044 cabin filter. Diane Cho noted it on 14 September 2026. No second file for this line.
- [ ] The first order — open. SKU 1044 cabin filter. Diane Cho noted it on 14 September 2026. No second file for this line.

Next action: Diane Cho closes the open items before 30 September 2026. Do not mark the pack done while a box is open.
