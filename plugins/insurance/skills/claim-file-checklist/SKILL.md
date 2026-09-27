---
name: claim-file-checklist
description: "Organize a claim file so a handler can see facts, documents, and open questions. Use when the user mentions claim file, insurance claim checklist, FNOL file, claims documentation, or asks for a claim file checklist. Insurance operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: insurance
---

# Claim File Checklist

Organize a claim file so a handler can see facts, documents, and open questions.

## When to use this skill

Use this skill when the user:

- claim file
- insurance claim checklist
- FNOL file
- claims documentation

## When not to use this skill

- Claims fraud
- Inflating a loss

## Professional boundary

This is not coverage advice and not a claim determination. Do not tell anyone they are covered. Organize facts for a licensed professional.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The reported facts
- Documents on hand
- The policy form they have
- The handler

## Workflow


### 1. Step 1

Record facts separately from opinions.
### 2. Step 2

List missing documents.
### 3. Step 3

Do not decide coverage.
### 4. Step 4

Do not coach anyone to inflate a loss or omit a material fact.
### 5. Step 5

Note the next handler action and date.
### 6. Step 6

Minimize sensitive data in summaries.

## Output

Deliver a **claim file checklist**.

- Purpose of this claim file checklist, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs a claim file checklist by 30 September 2026. A customer asks how to describe the loss so the payout is higher than the damage.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A customer asks how to describe the loss so the payout is higher than the damage.

folder: the claim file they have
coverage opinion: not given
missing doc: named
handler: licensed owner
```

### Example outcome

**Claim file checklist**
Northline Studio · 14 September 2026

Refuses the inflation and lists the facts the handler still needs.

- [x] The reported facts — in the file. Redline Parts. Priya Shah noted it on 14 September 2026. No second file for this line.
- [x] Documents on hand — in the file. one PDF, 2 pages, dated 14 September 2026
- [x] The policy form they have — in the file. their one-page rule dated 2 Mar 2026. No exception log
- [ ] The handler — open. Redline Parts. Priya Shah noted it on 14 September 2026. No second file for this line.

Next action: Priya Shah closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- A coverage determination
- Inflated loss advice
- Omitted material facts

## Related skills

- `dispute-intake`
- `outside-counsel-brief`
