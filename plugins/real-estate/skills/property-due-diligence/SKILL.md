---
name: property-due-diligence
description: "Build a due-diligence checklist from the deal type and the documents the user can obtain. Use when the user mentions property due diligence, acquisition checklist, what should we review, property DD, or asks for a due-diligence checklist. Real estate skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: real-estate
---

# Property Due Diligence

Build a due-diligence checklist from the deal type and the documents the user can obtain.

## When to use this skill

Use this skill when the user:

- property due diligence
- acquisition checklist
- what should we review
- property DD

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

This is not brokerage, appraisal, or legal advice. Do not invent comparable sales, rents, or legal rights. A licensed local professional must confirm any transaction.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The deal type
- Documents in hand
- Known red flags
- The decision date

## Workflow


### 1. Step 1

List documents they already require for this deal type.
### 2. Step 2

Mark missing items as gaps, not as clean.
### 3. Step 3

Separate physical, financial, and legal workstreams. Legal conclusions go to counsel.
### 4. Step 4

Do not invent inspection results.
### 5. Step 5

Recommend a walk-away question if a gap is material and the date is close.
### 6. Step 6

No earnest-money trick and no concealed defect strategy.

## Output

Deliver a **due-diligence checklist**.

- Purpose of this due-diligence checklist, in two sentences.
- Facts the user supplied, listed separately from assumptions.
- The work itself, in the structure the workflow names.
- Open questions, risks, and the single next action with an owner.
- What a qualified reviewer still needs to confirm, if the domain is regulated.

## Quality bar

- Every number, date, name, and citation came from the user or is marked as an assumption.
- The artifact can be used without reading this skill again.
- Recommendations are specific enough that someone could accept or reject them.
- Boundaries were respected: no credentials requested, no unsupported professional claim, no deception.

## Example

### Scenario

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a due-diligence checklist by 30 September 2026. The checklist is marked complete though no survey was received.

### Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

The checklist is marked complete though no survey was received.

address: the one in the ask
rent roll: their sheet
comp: not invented
legal review: not done here
```

### Example outcome

**Due-diligence checklist**
Cedar Street Properties · 14 September 2026

Keeps the survey open and refuses a clean conclusion.

- [x] The deal type — in the file. Redline Parts. Helen Cho noted it on 14 September 2026. No second file for this line.
- [x] Documents in hand — in the file. one PDF, 2 pages, dated 14 September 2026
- [x] Known red flags — in the file. Redline Parts. Helen Cho noted it on 14 September 2026. No second file for this line.
- [ ] The decision date — open. The checklist is marked complete though no survey was received

Next action: Helen Cho closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- A clean opinion with missing documents
- Invented inspection results
- Concealment advice

## Related skills

- `ma-screening`
- `lease-abstract`
