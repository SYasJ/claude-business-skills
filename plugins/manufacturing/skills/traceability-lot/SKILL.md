---
name: traceability-lot
description: "Plan a lot trace from finished goods back to material, or the reverse, and record the breaks. Use when the user mentions traceability, lot trace, mock recall, batch genealogy, or asks for a trace exercise. Manufacturing and quality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: manufacturing
---

# Lot Traceability

Plan a lot trace from finished goods back to material, or the reverse, and record the breaks.

## When to use this skill

Use this skill when the user:

- traceability
- lot trace
- mock recall
- batch genealogy

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

- The lot to trace
- Systems involved
- Time target
- Known breaks

## Workflow


### 1. Define the question

where did this lot go, or what went into it.
### 2. Step 2

Use their systems. Do not invent genealogy.
### 3. Step 3

Record every break where the link is missing.
### 4. Step 4

Time the exercise. A trace that takes days is a finding if their target is hours.
### 5. Step 5

Name the owner of each break.
### 6. Step 6

Do not tell anyone to ship product they said is on hold.

## Output

Deliver a **trace exercise**.

- Purpose of this trace exercise, in two sentences.
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

Gus Moretti, plant manager at Redline Parts in Nisku, needs a trace exercise by 30 September 2026. A mock recall stops because a component lot was never recorded.

### Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A mock recall stops because a component lot was never recorded.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

### Example outcome

**Trace exercise**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Records the break, times the exercise, and assigns the recording gap.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Invented genealogy
- A trace that hides a break
- Shipping a held lot

## Related skills

- `nonconformance-report`
- `inventory-accounting`
