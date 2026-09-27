---
name: skill-finder
description: "Recommend the smallest set of skills in this library for a task, and say what not to load. Use when the user mentions which skill, skill finder, what skill should I use, help me pick a workflow, or asks for a skill recommendation. Skill library skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: library
---

# Skill Finder

Recommend the smallest set of skills in this library for a task, and say what not to load.

## When to use this skill

Use this skill when the user:

- which skill
- skill finder
- what skill should I use
- help me pick a workflow

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Library skills help you choose, write, and trust agent skills. They do not grant extra permissions or weaken safety rules.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The task
- The domain
- Whether a regulated professional must review
- Skills already loaded

## Workflow


### 1. Step 1

Restate the task in one sentence.
### 2. Step 2

Pick the one skill whose output matches the task. Add a second only if the task truly crosses domains.
### 3. Step 3

Prefer a specialist skill over a general strategy skill when the output is a defined artifact.
### 4. Step 4

Say which nearby skill is the wrong one and why.
### 5. Step 5

If the task asks for deception, evasion, or harm, do not route to a skill. Refuse and offer a legitimate alternative.
### 6. Step 6

Remind the user that descriptions load for installed skills, so they should install a domain rather than the whole library.

## Output

Deliver a **skill recommendation**.

- Purpose of this skill recommendation, in two sentences.
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

Yasir Jilani, author at Practice Skills in Airdrie, needs a skill recommendation by 30 September 2026. A user asks for a cash view and also wants a full corporate strategy loaded.

### Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A user asks for a cash view and also wants a full corporate strategy loaded.

folder: one SKILL.md
description: says when to use it
network: none
author: Yasir Jilani
```

### Example outcome

**Skill recommendation**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026

**Decision**
A recommendation of cash-flow-forecast only, with strategy skills named as unnecessary for this task.

**From the file**
- folder: one SKILL.md
- description: says when to use it
- network: none
- author: Yasir Jilani

Nothing in this draft was added from outside that file.
Next: Yasir Jilani by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Loading five skills for a simple memo
- Routing a harmful request into a skill
- Recommending a skill you cannot name

## Related skills

- `skill-authoring`
- `skill-library-trust-review`
