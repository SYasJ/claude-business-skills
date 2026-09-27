---
name: usability-test-plan
description: "Plan a usability test that watches someone attempt a task, instead of asking if they like the design. Use when the user mentions usability test, user test plan, prototype test, task-based test, or asks for a usability test plan. Product skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: product
---

# Usability Test Plan

Plan a usability test that watches someone attempt a task, instead of asking if they like the design.

## When to use this skill

Use this skill when the user:

- usability test
- user test plan
- prototype test
- task-based test

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

- The task that matters
- The prototype or product state
- Who should attempt it
- The questions the design must answer

## Workflow


### 1. Tasks

Write tasks as goals, not as click instructions. Do not give away the path.
### 2. Participants

People who have the problem. Five focused sessions beat a survey of opinions.
### 3. Script

Consent, think-aloud, tasks, and follow-ups. No 'do you like it' as the core.
### 4. Success

What completing the task looks like, observed, not self-reported.
### 5. Notes

Where they hesitate or fail. Quotes, not scores alone.
### 6. Limits

Say what a small test cannot prove, including market demand.

## Output

Deliver a **usability test plan**.

- Purpose of this usability test plan, in two sentences.
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

Jonah Park, product manager at Fieldnote in Edmonton, needs an usability test plan by 30 September 2026. A designer wants to ask ten coworkers whether they like a new color scheme and call it usability.

### Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A designer wants to ask ten coworkers whether they like a new color scheme and call it usability.

The prototype or product state: 8 screens, file dated 14 September 2026
Who should attempt it: Jonah Park, product manager
The questions the design must answer: A designer wants to ask ten coworkers whether they like a new color scheme and call it usability
```

### Example outcome

**Usability test plan**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026

**Decision**
Color preference is not the test.

**From the file**
- The prototype or product state: 8 screens, file dated 14 September 2026
- Who should attempt it: Jonah Park, product manager
- The questions the design must answer: A designer wants to ask ten coworkers whether they like a new color scheme and call it usability

Nothing in this draft was added from outside that file.
Next: Jonah Park by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A preference poll called a usability test.
- Tasks that reveal the answer.
- Treating five users as a market proof.

## Related skills

- `prototype-test-script`
- `usability-findings`
