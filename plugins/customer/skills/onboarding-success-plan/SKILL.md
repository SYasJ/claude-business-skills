---
name: onboarding-success-plan
description: "Plan customer onboarding to a first value moment, with owners on both sides. Use when the user mentions customer onboarding, implementation plan, time to value, success plan, or asks for a customer onboarding plan. Customer experience skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: customer
---

# Customer Onboarding Plan

Plan customer onboarding to a first value moment, with owners on both sides.

## When to use this skill

Use this skill when the user:

- customer onboarding
- implementation plan
- time to value
- success plan

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not blame the customer. Do not invent policy exceptions. Do not ask a customer for passwords or full payment card numbers.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The first value moment
- Steps to get there
- Customer owners
- Internal owners

## Workflow


### 1. Step 1

Define the first value moment in the customer's language.
### 2. Step 2

Sequence only the steps required to reach it. Park the rest.
### 3. Step 3

Assign a customer owner and an internal owner to each step.
### 4. Step 4

State the evidence that value happened.
### 5. Step 5

Name the stall that usually happens, if they know it, and the check-in that catches it.
### 6. Step 6

Do not promise a go-live date operations has not accepted.

## Output

Deliver a **customer onboarding plan**.

- Purpose of this customer onboarding plan, in two sentences.
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

Rita Santos, support lead at Fieldnote in Edmonton, needs a customer onboarding plan by 30 September 2026. A plan lists 30 setup tasks and never says what the customer can do at the end.

### Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A plan lists 30 setup tasks and never says what the customer can do at the end.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

### Example outcome

**Customer onboarding plan**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026

**Decision**
A plan aimed at one value moment, with owners and a stall check.

**From the file**
- ticket: 4412, 14 Sep 2026
- customer words: in the ticket
- exception: not approved
- card or password: not collected

Nothing in this draft was added from outside that file.
Next: Rita Santos by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An onboarding plan with no value moment
- Unowned steps
- A date operations did not accept

## Related skills

- `journey-map`
- `thirty-sixty-ninety`
