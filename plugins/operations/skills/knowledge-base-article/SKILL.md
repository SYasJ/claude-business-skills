---
name: knowledge-base-article
description: "Write a knowledge article that answers one question and tells the reader when to stop and escalate. Use when the user mentions knowledge base article, help center article, internal KB, how-to article, or asks for a knowledge article. Operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: operations
---

# Knowledge Base Article

Write a knowledge article that answers one question and tells the reader when to stop and escalate.

## When to use this skill

Use this skill when the user:

- knowledge base article
- help center article
- internal KB
- how-to article

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Operating procedures should be usable by the team that will run them. Do not add surveillance of employees beyond what the user explicitly asks to document as policy.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The question
- The correct steps
- The audience
- The escalation path

## Workflow


### 1. Step 1

Use the reader's question as the title.
### 2. Step 2

Number the steps. Include the expected result of the key step.
### 3. Step 3

Add the symptoms that mean this article is the wrong one.
### 4. Step 4

Tell them when to escalate, and to whom.
### 5. Step 5

Remove internal jargon or explain it.
### 6. Step 6

Do not include secrets, internal-only credentials, or a workaround that violates policy.

## Output

Deliver a **knowledge article**.

- Purpose of this knowledge article, in two sentences.
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

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a knowledge article by 30 September 2026. A help draft includes an admin password so customers can 'fix it themselves'.

### Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A help draft includes an admin password so customers can 'fix it themselves'.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

### Example outcome

**Knowledge article**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026

**Decision**
Removes the password, answers one question, and gives an escalation path.

**From the file**
- shift: two people
- SOP: one page, 2 Mar 2026
- exception: not logged
- queue: the items in the ask

Nothing in this draft was added from outside that file.
Next: Diane Cho by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An article that answers three questions badly
- A secret in a help article
- No escalation line

## Related skills

- `support-macro`
- `sop-writer`
