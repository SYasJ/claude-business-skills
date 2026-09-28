# Prior Authorization Operations

`prior-authorization-ops`

## What this is for

Organize a prior-authorization packet and clock from the payer rules the user supplied.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs an authorization operations checklist by 30 September 2026. Staff want to change a note so the authorization is more likely to pass.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

Staff want to change a note so the authorization is more likely to pass.

The documents on hand: one PDF, 2 pages, dated 14 September 2026
The internal owner: Dr. Helen Cho, clinic director
The requested date: 30 September 2026
```

## Example outcome

**Authorization operations checklist**
Cedar Clinic · 14 September 2026 · Due 30 September 2026

**Decision**
A checklist of real gaps and a refusal to alter the record.

**Checklist**

- [x] **The payer requirements they have** — Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.  
      Evidenced in the file
- [x] **The documents on hand** — one PDF, 2 pages, dated 14 September 2026  
      Evidenced in the file
- [x] **The internal owner** — Dr. Helen Cho, clinic director  
      Evidenced in the file
- [ ] **The requested date** — 30 September 2026  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. Use only requirements the user supplied. Do not invent payer rules
2. List missing documents as gaps, not as reasons to fabricate a note
3. Assign an owner and a follow-up clock
4. Tell the patient the status in plain language without promising approval
5. Refuse any request to alter a clinical record to win an authorization

**Deliberately not done**
- Fabricated clinical notes.
- A promised approval.
- Invented payer rules.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Dr. Helen Cho closes the open items before 30 September 2026.
