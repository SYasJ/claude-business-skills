---
name: supplier-quality
description: "Write a supplier quality note that states the defect, the containment, and the evidence requested. Use when the user mentions supplier quality, SCAR, supplier defect, vendor corrective action, or asks for a supplier quality note. Manufacturing and quality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: manufacturing
---

# Supplier Quality Note

Write a supplier quality note that states the defect, the containment, and the evidence requested.

## When to use this skill

Use this skill when the user:

- supplier quality
- SCAR
- supplier defect
- vendor corrective action

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Quality and safety procedures are drafts for the site's quality system. Do not bypass a hold, calibration, or safety step.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The defect evidence
- Lot information
- Containment
- What you are asking the supplier to do

## Workflow


### 1. Step 1

State the defect with evidence they have.
### 2. Step 2

Identify lots without inventing shipment history.
### 3. Step 3

Ask for containment and a cause, with a date.
### 4. Step 4

Do not accuse fraud. Ask for facts.
### 5. Step 5

Share only the data the supplier needs.
### 6. Step 6

Link repeats to the scorecard.

## Output

Deliver a **supplier quality note**.

- Purpose of this supplier quality note, in two sentences.
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

Gus Moretti, plant manager at Redline Parts in Nisku, needs a supplier quality note by 30 September 2026. A note calls the supplier negligent and does not describe the defect.

### Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A note calls the supplier negligent and does not describe the defect.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

### Example outcome

**Supplier quality note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Describes the defect, requests containment by a date, and removes the insult.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. State the defect with evidence they have**

**2. Identify lots without inventing shipment history**

**3. Ask for containment and a cause, with a date**

**4. Do not accuse fraud. Ask for facts**

**5. Share only the data the supplier needs**

**Deliberately not done**
- A fraud accusation with no evidence.
- Invented shipment history.
- A request with no date.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- A fraud accusation with no evidence
- Invented shipment history
- A request with no date

## Related skills

- `supplier-scorecard`
- `capa-plan`
