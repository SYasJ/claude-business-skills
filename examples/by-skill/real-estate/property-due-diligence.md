# Property Due Diligence

`property-due-diligence`

## What this is for

Build a due-diligence checklist from the deal type and the documents the user can obtain.

## Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a due-diligence checklist by 30 September 2026. The checklist is marked complete though no survey was received.

## Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

The checklist is marked complete though no survey was received.

The deal type: Unit 4B lease, recorded 14 September 2026. No supporting file attached
Documents in hand: one PDF, 2 pages, dated 14 September 2026
Known red flags: Rent roll, 12 units. Stated in the ask, not documented anywhere else
The decision date: The checklist is marked complete though no survey was received
```

## Example outcome

**Due-diligence checklist**
Cedar Street Properties · 14 September 2026 · Due 30 September 2026

**Decision**
Keeps the survey open and refuses a clean conclusion.

**Checklist**

- [x] **The deal type** — Unit 4B lease, recorded 14 September 2026. No supporting file attached  
      Evidenced in the file
- [x] **Documents in hand** — one PDF, 2 pages, dated 14 September 2026  
      Evidenced in the file
- [x] **Known red flags** — Rent roll, 12 units. Stated in the ask, not documented anywhere else  
      Evidenced in the file
- [ ] **The decision date** — The checklist is marked complete though no survey was received  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. List documents they already require for this deal type
2. Mark missing items as gaps, not as clean
3. Separate physical, financial, and legal workstreams. Legal conclusions go to counsel
4. Do not invent inspection results
5. Recommend a walk-away question if a gap is material and the date is close

**Deliberately not done**
- A clean opinion with missing documents.
- Invented inspection results.
- Concealment advice.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Helen Cho closes the open items before 30 September 2026.
