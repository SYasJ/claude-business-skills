---
name: writing-brief
description: "Brief a piece of writing so the drafter knows the reader, the point, and the length. Use when the user mentions writing brief, help me outline, draft structure, what should this say, or asks for a writing brief. Productivity skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: productivity
---

# Writing Brief

Brief a piece of writing so the drafter knows the reader, the point, and the length.

## When to use this skill

Use this skill when the user:

- writing brief
- help me outline
- draft structure
- what should this say

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Productivity systems serve the person's actual constraints. Do not recommend surveillance of colleagues or hidden monitoring.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The reader
- The point
- The length
- The action you want

## Workflow


### 1. Step 1

Name the reader and what they already know.
### 2. Step 2

Write the point in one sentence.
### 3. Step 3

Choose a structure that serves the point.
### 4. Step 4

Set a length.
### 5. Step 5

List facts that must be included and claims that must not.
### 6. Step 6

Do not start drafting until the point is stable, unless the user asked for a rough exploration.

## Output

Deliver a **writing brief**.

- Purpose of this writing brief, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs a writing brief by 30 September 2026. A brief says 'write something inspiring about the quarter' with no reader or ask.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A brief says 'write something inspiring about the quarter' with no reader or ask.

week: 14 Sep 2026
calendar: the meetings they listed
dissent: kept if it was said
monitoring: not recommended
```

### Example outcome

**Writing brief**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026

**Decision**
Names the reader, one point, and the action, or stops until those exist.

**From the file**
- week: 14 Sep 2026
- calendar: the meetings they listed
- dissent: kept if it was said
- monitoring: not recommended

Nothing in this draft was added from outside that file.
Next: Mara Chen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A draft with no point
- Unsupported claims required by the brief
- No reader

## Related skills

- `executive-one-pager`
- `creative-brief`
