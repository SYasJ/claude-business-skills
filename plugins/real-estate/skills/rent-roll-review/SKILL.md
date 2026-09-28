---
name: rent-roll-review
description: "Review a rent roll for inconsistencies, expirations, and concessions the user can see. Use when the user mentions rent roll, lease expiration review, commercial rent roll, occupancy review, or asks for a rent-roll review. Real estate skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: real-estate
---

# Rent Roll Review

Review a rent roll for inconsistencies, expirations, and concessions the user can see.

## When to use this skill

Use this skill when the user:

- rent roll
- lease expiration review
- commercial rent roll
- occupancy review

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

This is not brokerage, appraisal, or legal advice. Do not invent comparable sales, rents, or legal rights. A licensed local professional must confirm any transaction.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The rent roll
- What a row is supposed to mean
- Known concessions
- The questions of the reader

## Workflow


### 1. Step 1

Check that units, rent, and dates are internally consistent.
### 2. Step 2

Flag expirations inside their horizon.
### 3. Step 3

Separate contractual rent from concessions they disclosed.
### 4. Step 4

Do not invent market rent.
### 5. Step 5

Note vacant units and the story they gave.
### 6. Step 6

Send legal interpretation of odd clauses to counsel.

## Output

Deliver a **rent-roll review**.

- Purpose of this rent-roll review, in two sentences.
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

Helen Cho, property manager at Cedar Street Properties in Airdrie, needs a rent-roll review by 30 September 2026. A roll shows full occupancy while three units are marked 'free rent' with no end date.

### Example data

```text
From: Helen Cho, property manager
Organization: Cedar Street Properties, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A roll shows full occupancy while three units are marked 'free rent' with no end date.

address: the one in the ask
rent roll: their sheet
comp: not invented
legal review: not done here
```

### Example outcome

**Rent-roll review**
To: Helen Cho, property manager, Cedar Street Properties
Date: 14 September 2026

**Decision**
Separates free rent from paying occupancy and flags the missing end dates.

**From the file**
- address: the one in the ask
- rent roll: their sheet
- comp: not invented
- legal review: not done here

Nothing in this draft was added from outside that file.
Next: Helen Cho by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Invented market rent
- Concessions hidden in the headline rent
- A roll that does not add up

## Related skills

- `lease-abstract`
- `property-listing-brief`
