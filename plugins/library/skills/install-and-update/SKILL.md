---
name: install-and-update
description: "Plan a local install or update of this library for a specific tool and domain. Use when the user mentions install skills, update skills, install a domain, where do skills go, or asks for a install plan. Skill library skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: library
---

# Install and Update

Plan a local install or update of this library for a specific tool and domain.

## When to use this skill

Use this skill when the user:

- install skills
- update skills
- install a domain
- where do skills go

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

- The tool
- The domain
- Whether the install is user-level or project-level
- Whether they want a dry run

## Workflow


### 1. Step 1

Recommend a domain install, not all skills, unless they explicitly want the full set and accept the description cost.
### 2. Step 2

Use the local installer. Do not recommend a remote pipe-to-shell command.
### 3. Step 3

Show the destination path for the tool they named.
### 4. Step 4

Prefer a dry run first.
### 5. Step 5

Updates replace files from this repository only. Do not tell them to mix in unreviewed third-party skills silently.
### 6. Step 6

No account, license key, or wallet is required.

## Output

Deliver a **install plan**.

- Purpose of this install plan, in two sentences.
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

Yasir Jilani, author at Practice Skills in Airdrie, needs an install plan by 30 September 2026. A user wants one command that downloads and executes an unknown installer.

### Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A user wants one command that downloads and executes an unknown installer.

folder: one SKILL.md
description: says when to use it
network: none
author: Yasir Jilani
```

### Example outcome

**Install plan**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026

**Decision**
Uses the local Python installer, names the domain, and starts with a dry run.

**From the file**
- folder: one SKILL.md
- description: says when to use it
- network: none
- author: Yasir Jilani

Nothing in this draft was added from outside that file.
Next: Yasir Jilani by 30 September 2026. This is not a sign-off.

## Anti-patterns

- curl piped to a shell
- A required license key
- Installing every skill by default

## Related skills

- `skill-finder`
- `skill-library-trust-review`
