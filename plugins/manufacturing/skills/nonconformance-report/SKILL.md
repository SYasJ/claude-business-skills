---
name: nonconformance-report
description: "Write a nonconformance report that contains the fact, the containment, and the owner. Use when the user mentions NCR, nonconformance, quality escape, defect report, or asks for a NCR. Manufacturing and quality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: manufacturing
---

# Nonconformance Report

Write a nonconformance report that contains the fact, the containment, and the owner.

## When to use this skill

Use this skill when the user:

- NCR
- nonconformance
- quality escape
- defect report

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

- What failed
- Where it was found
- Quantity if known
- Immediate containment

## Workflow


### 1. Step 1

Describe the defect in observable terms.
### 2. Step 2

Record quantity and location only from their count.
### 3. Containment first

stop the escape path they named.
### 4. Step 4

Do not dispose of evidence they said must be kept.
### 5. Step 5

Separate containment from root-cause work.
### 6. Step 6

Assign an owner and a date. A report with no owner will age in a drawer.

## Output

Deliver a **NCR**.

- Purpose of this NCR, in two sentences.
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

Gus Moretti, plant manager at Redline Parts in Nisku, needs a NCR by 30 September 2026. A report says 'bad parts' and the suspect lot is still being shipped.

### Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A report says 'bad parts' and the suspect lot is still being shipped.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

### Example outcome

**Ncr**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Stops the lot, describes the defect, and names the owner.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A vague defect description
- Disposing of required evidence
- No containment

## Related skills

- `capa-plan`
- `traceability-lot`
