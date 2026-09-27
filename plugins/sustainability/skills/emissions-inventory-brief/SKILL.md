---
name: emissions-inventory-brief
description: "Brief an emissions inventory from activity data they have, with factors labeled and gaps visible. Use when the user mentions emissions inventory, carbon footprint, GHG inventory, scope 1 2 3, or asks for a inventory brief. Sustainability skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: sustainability
---

# Emissions Inventory Brief

Brief an emissions inventory from activity data they have, with factors labeled and gaps visible.

## When to use this skill

Use this skill when the user:

- emissions inventory
- carbon footprint
- GHG inventory
- scope 1 2 3

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not invent emissions factors or certification status. Label estimates. This is not an assurance opinion.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Activity data
- Factors they are using
- Organizational boundary
- Known gaps

## Workflow


### 1. Step 1

Define the boundary they chose.
### 2. Step 2

List activity data they actually have.
### 3. Step 3

Apply only factors they supplied, and show the source. Do not invent a factor.
### 4. Step 4

Mark missing categories as gaps.
### 5. Step 5

Separate a number from an assurance opinion.
### 6. Step 6

Recommend the next data improvement, not a claim of net zero.

## Output

Deliver a **inventory brief**.

- Purpose of this inventory brief, in two sentences.
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

Devon Hale, reporting lead at Prairie Line Energy in Calgary, needs an inventory brief by 30 September 2026. A report states net zero because one office bought offsets, and no inventory exists.

### Example data

```text
From: Devon Hale, reporting lead
Organization: Prairie Line Energy, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A report states net zero because one office bought offsets, and no inventory exists.

period: the year they named
factor: only from their sheet
certification: not claimed
estimate: labeled
```

### Example outcome

**Inventory brief**
To: Devon Hale, reporting lead, Prairie Line Energy
Date: 14 September 2026

**Decision**
Refuses the claim and lists the missing activity data.

**From the file**
- period: the year they named
- factor: only from their sheet
- certification: not claimed
- estimate: labeled

Nothing in this draft was added from outside that file.
Next: Devon Hale by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An invented emissions factor
- A net-zero claim from a partial inventory
- Hidden gaps

## Related skills

- `marketing-claims-review`
- `metric-definition`
