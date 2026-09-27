---
name: prd-writer
description: "Write a product requirements document with a problem, scope, acceptance signals, and explicit non-goals. Use when the user mentions write a PRD, product requirements, feature spec, requirements document, or asks for a PRD. Product skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: product
---

# PRD Writer

Write a product requirements document with a problem, scope, acceptance signals, and explicit non-goals.

## When to use this skill

Use this skill when the user:

- write a PRD
- product requirements
- feature spec
- requirements document

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Product recommendations are hypotheses until evidence says otherwise. Label confidence. Do not ship dark patterns that hide cost or consent.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Problem and user
- Proposed scope
- Constraints
- Open questions

## Workflow


### 1. Problem and outcome

What will be true for the user if this ships. No outcome, no PRD.
### 2. Scope

The smallest slice that tests the outcome. Cut the rest into non-goals.
### 3. Flows

The main path and the important failure path. Do not specify every pixel unless the user asked for design detail.
### 4. Acceptance

Observable signals that the slice works. 'Feels better' is not acceptance.
### 5. Analytics and risks

What you will measure, and the risk you are accepting. Do not invent baseline numbers.
### 6. Open questions

Owner and date for each. A PRD that hides questions will slip in build.

## Output

Deliver a **PRD**.

- Purpose of this PRD, in two sentences.
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

Jonah Park, product manager at Fieldnote in Edmonton, needs a PRD by 30 September 2026. A PRD draft lists 15 features and no user outcome.

### Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A PRD draft lists 15 features and no user outcome.

Proposed scope: this decision only
Constraints: no extra headcount, and no result that is not in this file
Open questions: A PRD draft lists 15 features and no user outcome
```

### Example outcome

**Prd**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026

**Decision**
A rewritten PRD with one outcome, a small slice, testable acceptance, and the other features as non-goals.

**From the file**
- Proposed scope: this decision only
- Constraints: no extra headcount, and no result that is not in this file
- Open questions: A PRD draft lists 15 features and no user outcome

Nothing in this draft was added from outside that file.
Next: Jonah Park by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A PRD that is only a solution.
- Hidden non-goals.
- Acceptance criteria nobody can test.

## Related skills

- `user-story-map`
- `product-analytics-spec`
