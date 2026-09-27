---
name: technical-design-doc
description: "Write a technical design that states the problem, the constraints, the chosen approach, and the rejected alternative. Use when the user mentions technical design, design doc, system design writeup, engineering design, or asks for a technical design doc. Engineering skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: engineering
---

# Technical Design Doc

Write a technical design that states the problem, the constraints, the chosen approach, and the rejected alternative.

## When to use this skill

Use this skill when the user:

- technical design
- design doc
- system design writeup
- engineering design

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Prefer the repository's existing patterns. Do not disable security controls, invent credentials, or introduce network calls the user did not ask for.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The problem and users
- Constraints: scale, security, deadline, existing systems
- The proposed approach
- Alternatives considered

## Workflow


### 1. Problem

What must change for the user or operator, and why now.
### 2. Context

The current system only as far as the decision needs. Do not invent architecture that is not in the repo or the user's description.
### 3. Decision

The approach, the tradeoff, and one rejected alternative. A design with no alternative is a preference.
### 4. Interfaces

Data, APIs, and failure behavior. Include the unhappy path.
### 5. Risks

Migration, security, and operability. Security risks get a defensive control, not an exploit note.
### 6. Rollout

How it ships and how it rolls back. No design is done without a rollback story.

## Output

Deliver a **technical design doc**.

- Purpose of this technical design doc, in two sentences.
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

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a technical design doc by 30 September 2026. An engineer proposes a new service but has not said what happens when the dependency is down.

### Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An engineer proposes a new service but has not said what happens when the dependency is down.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

### Example outcome

**Technical design doc**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
A design doc with the failure behavior, one rejected alternative, and a rollback path.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A design that invents the current system.
- No rejected alternative.
- Security described as 'we will add it later' with no owner.

## Related skills

- `architecture-decision-record`
- `threat-model-lite`
