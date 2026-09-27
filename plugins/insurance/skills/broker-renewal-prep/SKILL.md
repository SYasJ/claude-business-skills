---
name: broker-renewal-prep
description: "Prepare an insurance renewal packet from the expiring facts and the changes the insured reported. Use when the user mentions insurance renewal, renewal submission, broker renewal, market submission, or asks for a renewal prep. Insurance operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: insurance
---

# Renewal Preparation

Prepare an insurance renewal packet from the expiring facts and the changes the insured reported.

## When to use this skill

Use this skill when the user:

- insurance renewal
- renewal submission
- broker renewal
- market submission

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

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

- Expiring terms they have
- Changes in operations
- Losses they reported
- The deadline

## Workflow


### 1. Step 1

List changes the insured actually reported.
### 2. Step 2

Include losses they documented. Do not omit a known loss.
### 3. Step 3

Mark unknown values as unknown.
### 4. Step 4

Note the questions underwriters asked last time if the user has them.
### 5. Step 5

Do not invent a premium.
### 6. Step 6

This packet does not bind coverage.

## Output

Deliver a **renewal prep**.

- Purpose of this renewal prep, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs a renewal prep by 30 September 2026. A renewal draft leaves off a recent claim to keep the story clean.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A renewal draft leaves off a recent claim to keep the story clean.

folder: the claim file they have
coverage opinion: not given
missing doc: named
handler: licensed owner
```

### Example outcome

**Renewal prep**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026

**Decision**
Includes the claim and labels any premium figure as not yet quoted.

**From the file**
- folder: the claim file they have
- coverage opinion: not given
- missing doc: named
- handler: licensed owner

Nothing in this draft was added from outside that file.
Next: Priya Shah by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An omitted known loss
- An invented premium
- A claim that coverage is bound

## Related skills

- `claim-file-checklist`
- `risk-assessment`
