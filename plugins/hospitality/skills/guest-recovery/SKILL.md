---
name: guest-recovery
description: "Plan guest recovery after a service miss, with a truthful apology and a remedy inside authority. Use when the user mentions guest recovery, hotel complaint, restaurant complaint, service miss hospitality, or asks for a guest recovery note. Hospitality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: hospitality
---

# Guest Recovery

Plan guest recovery after a service miss, with a truthful apology and a remedy inside authority.

## When to use this skill

Use this skill when the user:

- guest recovery
- hotel complaint
- restaurant complaint
- service miss hospitality

## When not to use this skill

- Paying to remove a review

## Professional boundary

Guest recovery should be sincere and within policy. Do not invent compensation authority the user has not granted.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The miss
- The guest's ask
- Authorized remedies
- The manager

## Workflow


### 1. Step 1

Acknowledge the specific miss.
### 2. Step 2

Do not invent a cause.
### 3. Step 3

Offer only an authorized remedy.
### 4. Step 4

Say what will change for the rest of the stay or meal if you know.
### 5. Step 5

Do not ask the guest to delete a review for compensation.
### 6. Step 6

Feed a repeated miss to the shift brief.

## Output

Deliver a **guest recovery note**.

- Purpose of this guest recovery note, in two sentences.
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

Sofia Alvarez, front office manager at Lantern Inn in Banff, needs a guest recovery note by 30 September 2026. A manager wants to offer a free stay if the guest removes a public review.

### Example data

```text
From: Sofia Alvarez, front office manager
Organization: Lantern Inn, Banff
Date: 14 September 2026
Needed by: 30 September 2026

A manager wants to offer a free stay if the guest removes a public review.

stay: the dates in the ask
offer: policy amount only
complaint: their words
manager: on duty
```

### Example outcome

**Guest recovery note**
To: Sofia Alvarez, front office manager, Lantern Inn
Date: 14 September 2026

**Decision**
Refuses the bargain and stays inside the authorized remedy.

**From the file**
- stay: the dates in the ask
- offer: policy amount only
- complaint: their words
- manager: on duty

Nothing in this draft was added from outside that file.
Next: Sofia Alvarez by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A review-deletion bargain
- An unauthorized comp
- A fake cause

## Related skills

- `service-recovery`
- `csat-recovery`
