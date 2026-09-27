---
name: medical-billing-review
description: "Review a billing packet for missing elements and coding questions, without upcoding or inventing services. Use when the user mentions medical billing review, claim checklist, coding question operations, clean claim, or asks for a billing review checklist. Healthcare practice operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: healthcare
---

# Medical Billing Review

Review a billing packet for missing elements and coding questions, without upcoding or inventing services.

## When to use this skill

Use this skill when the user:

- medical billing review
- claim checklist
- coding question operations
- clean claim

## When not to use this skill

- Upcoding
- False claims

## Professional boundary

This is not medical advice, diagnosis, or a treatment protocol. Do not recommend drugs, doses, or clinical interventions. Limit the work to practice operations, documentation quality, and communication drafts for a licensed clinician to approve.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The services they say were provided
- The codes they are considering
- Payer edits they supplied
- The documentation present

## Workflow


### 1. Step 1

Match codes only to services they say were documented.
### 2. Step 2

List missing documentation. Do not suggest adding a service that did not happen.
### 3. Step 3

Use payer edits they pasted. Do not invent a payer rule.
### 4. Step 4

Flag questions for a certified coder. This skill is not a coder's final assignment.
### 5. Step 5

Separate a patient estimate from a coverage promise.
### 6. Step 6

Refuse upcoding, unbundling schemes, and false claims.

## Output

Deliver a **billing review checklist**.

- Purpose of this billing review checklist, in two sentences.
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

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a billing review checklist by 30 September 2026. A biller wants a higher code because the visit 'felt complex' though the note does not support it.

### Example data

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

### Example outcome

**Billing review checklist**
Cedar Clinic · 14 September 2026

Keeps the supported code and sends the complexity question to a coder with the note gap visible.

- [x] The services they say were provided — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [x] The codes they are considering — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [x] Payer edits they supplied — in the file. Tuesday clinic. Dr. Helen Cho noted it on 14 September 2026. No second file for this line.
- [ ] The documentation present — open. one PDF, 2 pages, dated 14 September 2026

Next action: Dr. Helen Cho closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- Upcoding
- Invented services
- A coverage promise

## Related skills

- `clinical-documentation-quality`
- `prior-authorization-ops`
