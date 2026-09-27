---
name: customer-health-score
description: "Define a customer health score from signals that predict renewal risk, and show the formula. Use when the user mentions health score, customer health, red account logic, success score, or asks for a health score definition. Customer experience skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: customer
---

# Customer Health Score

Define a customer health score from signals that predict renewal risk, and show the formula.

## When to use this skill

Use this skill when the user:

- health score
- customer health
- red account logic
- success score

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

- Signals they can collect
- What happened before past churn if known
- Who will act on red
- The formula they use today

## Workflow


### 1. Step 1

Start from the action a red score triggers. A score with no action is a toy.
### 2. Step 2

Choose signals they can collect without creepy surveillance.
### 3. Step 3

Show the formula. Hidden points are a finding.
### 4. Step 4

Weight only with evidence they have. If they have no history, call the score a hypothesis.
### 5. Step 5

Set a review so a red account gets a human, not only a color.
### 6. Step 6

Do not include sensitive personal data in the score.

## Output

Deliver a **health score definition**.

- Purpose of this health score definition, in two sentences.
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

Rita Santos, support lead at Fieldnote in Edmonton, needs a health score definition by 30 September 2026. A health score marks accounts red and no one has a play for red.

### Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A health score marks accounts red and no one has a play for red.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

### Example outcome

**Health score definition**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026

**Decision**
A visible formula and a required human play for red, or a recommendation not to launch the score yet.

**From the file**
- ticket: 4412, 14 Sep 2026
- customer words: in the ticket
- exception: not approved
- card or password: not collected

Nothing in this draft was added from outside that file.
Next: Rita Santos by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A hidden formula
- A score nobody acts on
- Sensitive personal data as an input

## Related skills

- `renewal-save`
- `cx-metric-tree`
