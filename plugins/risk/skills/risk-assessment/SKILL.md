---
name: risk-assessment
description: "Assess a few real risks with a scenario, a control, and an owner, using the organization's own scale. Use when the user mentions risk assessment, assess this risk, risk workshop, enterprise risk item, or asks for a risk assessment. Risk and compliance skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: risk
---

# Risk Assessment

Assess a few real risks with a scenario, a control, and an owner, using the organization's own scale.

## When to use this skill

Use this skill when the user:

- risk assessment
- assess this risk
- risk workshop
- enterprise risk item

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

- The objective at risk
- Scenarios they can describe
- Existing controls
- Their scale

## Workflow


### 1. Step 1

Write scenarios as events, not as one-word categories.
### 2. Step 2

Use their likelihood and impact scale. If none exists, propose a simple one and label it.
### 3. Step 3

Name the current control and whether they have evidence it operates.
### 4. Step 4

Rate residual risk only after the control is described.
### 5. Step 5

Recommend mitigate, accept, or transfer as a question for the owner. Insurance transfer is not confirmed unless they say a policy exists.
### 6. Step 6

Do not claim a certification because a risk was written down.

## Output

Deliver a **risk assessment**.

- Purpose of this risk assessment, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs a risk assessment by 30 September 2026. A workshop list says 'cyber' and 'talent' with no scenario.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A workshop list says 'cyber' and 'talent' with no scenario.

event: the one in the ask, not a one-word label
owner: blank
control: not named
score: not invented
```

### Example outcome

**Risk assessment**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026

**Decision**
Rewrites those into specific events or drops them until a scenario exists.

**From the file**
- event: the one in the ask, not a one-word label
- owner: blank
- control: not named
- score: not invented

Nothing in this draft was added from outside that file.
Next: Priya Shah by 30 September 2026. This is not a sign-off.

## Anti-patterns

- One-word risks
- A certification claim
- Ratings with no scale

## Related skills

- `risk-register`
- `control-design`
