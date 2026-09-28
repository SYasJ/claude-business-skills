---
name: issue-management
description: "Record a compliance or control issue with severity, owner, and a dated remediation. Use when the user mentions issue management, control issue, remediation plan, audit issue, or asks for a issue record. Risk and compliance skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: risk
---

# Issue Management

Record a compliance or control issue with severity, owner, and a dated remediation.

## When to use this skill

Use this skill when the user:

- issue management
- control issue
- remediation plan
- audit issue

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

- The issue
- The failed control or obligation
- The harm
- The proposed fix

## Workflow


### 1. Step 1

Describe the issue as a fact, not as a softening adjective.
### 2. Step 2

Link it to the control or obligation.
### 3. Step 3

Rate severity with their scale or a labeled proposal.
### 4. Step 4

Write remediation with an owner and a date. A plan without either is a wish.
### 5. Step 5

Note compensating control until the fix lands.
### 6. Step 6

Verify closure with evidence, not with an email that says done.

## Output

Deliver a **issue record**.

- Purpose of this issue record, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs an issue record by 30 September 2026. An issue is marked closed because the owner said the spreadsheet was updated, with no sample.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

An issue is marked closed because the owner said the spreadsheet was updated, with no sample.

event: the one in the ask, not a one-word label
owner: blank
control: not named
score: not invented
```

### Example outcome

**Issue record**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
An open issue until a sample shows the control operating, with a dated owner.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| event | the one in the ask, not a one-word label | Needs confirmation |
| owner | blank | Carried into the draft |
| control | not named | Carried into the draft |
| score | not invented | Needs confirmation |

**How this draft was built**

**1. Describe the issue as a fact, not as a softening adjective**

**2. Link it to the control or obligation**

**3. Rate severity with their scale or a labeled proposal**

**4. Write remediation with an owner and a date. A plan without either is a wish**

**5. Note compensating control until the fix lands**

**Deliberately not done**
- Closure without evidence.
- No owner.
- A softened description that hides the gap.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Closure without evidence
- No owner
- A softened description that hides the gap

## Related skills

- `control-design`
- `audit-response`
