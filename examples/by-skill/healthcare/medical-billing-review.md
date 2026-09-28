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

The services they say were provided: the one named in the ask. Version and owner not recorded
The codes they are considering: Tuesday clinic, recorded 14 September 2026. No supporting file attached
Payer edits they supplied: Tuesday clinic, last reviewed 14 September 2026. No owner named since
The documentation present: one PDF, 2 pages, dated 14 September 2026
```

## Example outcome

**Billing review checklist**
Cedar Clinic · 14 September 2026 · Due 30 September 2026

**Decision**
Keeps the supported code and sends the complexity question to a coder with the note gap visible.

**Checklist**

- [x] **The services they say were provided** — the one named in the ask. Version and owner not recorded  
      Evidenced in the file
- [x] **The codes they are considering** — Tuesday clinic, recorded 14 September 2026. No supporting file attached  
      Evidenced in the file
- [x] **Payer edits they supplied** — Tuesday clinic, last reviewed 14 September 2026. No owner named since  
      Evidenced in the file
- [ ] **The documentation present** — one PDF, 2 pages, dated 14 September 2026  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. Match codes only to services they say were documented
2. List missing documentation. Do not suggest adding a service that did not happen
3. Use payer edits they pasted. Do not invent a payer rule
4. Flag questions for a certified coder. This skill is not a coder's final assignment
5. Separate a patient estimate from a coverage promise

**Deliberately not done**
- Upcoding.
- Invented services.
- A coverage promise.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Dr. Helen Cho closes the open items before 30 September 2026.
