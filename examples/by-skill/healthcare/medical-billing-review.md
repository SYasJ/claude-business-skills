# Medical Billing Review

`medical-billing-review`

## What this is for

Review a billing packet for missing elements and coding questions, without upcoding or inventing services.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a billing review checklist by 30 September 2026. A biller wants a higher code because the visit 'felt complex' though the note does not support it.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

A biller wants a higher code because the visit 'felt complex' though the note does not support it.

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

## Example outcome

**Billing review checklist**
Cedar Clinic · 14 September 2026

Keeps the supported code and sends the complexity question to a coder with the note gap visible.

- [x] The services they say were provided — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [x] The codes they are considering — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [x] Payer edits they supplied — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [ ] The documentation present — open. one PDF, 2 pages, dated 14 September 2026

Next action: Dr. Helen Cho closes the open items before 30 September 2026. Do not mark the pack done while a box is open.
