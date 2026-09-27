---
name: offer-letter-checklist
description: "Prepare an offer checklist so compensation, start date, and conditions are complete before anyone celebrates. Use when the user mentions offer letter, prepare an offer, offer checklist, verbal offer, or asks for a offer checklist. People and culture skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: people
---

# Offer Checklist

Prepare an offer checklist so compensation, start date, and conditions are complete before anyone celebrates.

## When to use this skill

Use this skill when the user:

- offer letter
- prepare an offer
- offer checklist
- verbal offer

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Employment work must follow the organization's policies and local employment law. Do not invent legal requirements. Do not write content that discriminates or retaliates.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Role and level
- Compensation parts the company intends
- Start date and contingencies
- Approver

## Workflow


### 1. List the parts

Base, variable, equity if any, and benefits status. Do not invent numbers or equity values.
### 2. Contingencies

Background, work authorization, or other checks only if the user says they are part of the process. Do not invent a check.
### 3. Manager alignment

The hiring manager and the approver agree on level and pay band. If they do not, stop the checklist and surface the conflict.
### 4. Candidate-facing clarity

What is guaranteed versus discretionary, in plain language.
### 5. Expiration

An offer date and a response date the user chooses. Do not create false urgency.
### 6. Counsel and HR own the letter

This skill checks completeness. It does not declare the letter legally sufficient.

## Output

Deliver a **offer checklist**.

- Purpose of this offer checklist, in two sentences.
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

Chris Adeyemi, people lead at Northline Studio in Calgary, needs an offer checklist by 30 September 2026. A manager told a candidate a number on a call, and finance has not approved the band.

### Example data

```text
From: Chris Adeyemi, people lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A manager told a candidate a number on a call, and finance has not approved the band.

Compensation parts the company intends: base CAD 60,000. Bonus line blank
Start date and contingencies: 30 September 2026
Approver: Chris Adeyemi. They have not signed
```

### Example outcome

**Offer checklist**
Northline Studio · 14 September 2026

Blocks the letter until the band is approved and lists the verbal number as not yet an offer.

- [x] Role and level — in the file. Jordan Hale. Chris Adeyemi noted it on 14 September 2026. No second file for this line.
- [x] Compensation parts the company intends — in the file. base CAD 60,000. Bonus line blank
- [x] Start date and contingencies — in the file. 30 September 2026
- [ ] Approver — open. Chris Adeyemi. They have not signed

Next action: Chris Adeyemi closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- A verbal offer that omits variable-pay conditions.
- Invented equity value.
- False exploding-offer pressure.

## Related skills

- `compensation-band`
- `employment-agreement-review`
- `onboarding-plan`
