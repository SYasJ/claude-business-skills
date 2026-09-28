---
name: compliance-calendar
description: "Build a calendar of obligations the organization already knows it has, with owners and lead time. Use when the user mentions compliance calendar, obligations calendar, filing calendar, compliance dates, or asks for a compliance calendar. Risk and compliance skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: risk
---

# Compliance Calendar

Build a calendar of obligations the organization already knows it has, with owners and lead time.

## When to use this skill

Use this skill when the user:

- compliance calendar
- obligations calendar
- filing calendar
- compliance dates

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Risk work prioritizes uncertainty. It is not a certification. Do not claim SOC 2, ISO, HIPAA, or similar compliance unless the user has evidence of it.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Known obligations
- Owners
- External dates they have confirmed
- Last year's misses

## Workflow


### 1. Step 1

Record only obligations they confirmed. Do not invent a filing.
### 2. Step 2

Mark unconfirmed dates as unconfirmed.
### 3. Step 3

Put an internal due date earlier than the external one so review can happen.
### 4. Step 4

Assign an owner and a reviewer.
### 5. Step 5

Note evidence saved when the obligation is met.
### 6. Step 6

Send new-jurisdiction questions to counsel rather than answering them from memory.

## Output

Deliver a **compliance calendar**.

- Purpose of this compliance calendar, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs a compliance calendar by 30 September 2026. A team wants every possible global filing listed just in case.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A team wants every possible global filing listed just in case.

event: the one in the ask, not a one-word label
owner: blank
control: not named
score: not invented
```

### Example outcome

**Compliance calendar**
Northline Studio · 14 September 2026

A calendar of confirmed obligations, with unknowns flagged for counsel instead of invented.

- [x] Known obligations — in the file. Harbor & Co. Priya Shah noted it on 14 September 2026. No second file for this line.
- [x] Owners — in the file. Priya Shah, controller
- [x] External dates they have confirmed — in the file. 30 September 2026
- [ ] Last year's misses — open. Harbor & Co. Priya Shah noted it on 14 September 2026. No second file for this line.

Next action: Priya Shah closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- Invented deadlines
- A calendar with no owners
- Dates stored with portal passwords

## Related skills

- `tax-calendar`
- `regulatory-change-log`
