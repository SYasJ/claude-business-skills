---
name: calibration-control
description: "Review calibration control so instruments used for acceptance are in date, and out-of-date tools are not used. Use when the user mentions calibration, gage control, instrument due, calibration overdue, or asks for a calibration control note. Manufacturing and quality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: manufacturing
---

# Calibration Control

Review calibration control so instruments used for acceptance are in date, and out-of-date tools are not used.

## When to use this skill

Use this skill when the user:

- calibration
- gage control
- instrument due
- calibration overdue

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

- The instrument list
- Due dates they have
- What the instrument accepts
- The quarantine practice

## Workflow


### 1. Step 1

Flag overdue instruments used for acceptance.
### 2. Step 2

Quarantine is the default they stated, or recommend it if they have none.
### 3. Step 3

Do not calculate a new calibration interval from memory.
### 4. Step 4

Record the last result they supplied.
### 5. Step 5

Assess impact only if they know the instrument was used while overdue. Do not invent affected lots.
### 6. Step 6

Name the owner of the recall or the review.

## Output

Deliver a **calibration control note**.

- Purpose of this calibration control note, in two sentences.
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

Gus Moretti, plant manager at Redline Parts in Nisku, needs a calibration control note by 30 September 2026. A caliper used for final accept is two months overdue and still on the bench.

### Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A caliper used for final accept is two months overdue and still on the bench.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

### Example outcome

**Calibration control note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026

**Decision**
Quarantines it and asks for a use review rather than inventing which lots moved.

**From the file**
- line: line 2
- lot: 26-0914
- hold: open
- count: the tally, not the order

Nothing in this draft was added from outside that file.
Next: Gus Moretti by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Using an overdue gage for acceptance
- An invented interval
- Invented affected lots

## Related skills

- `incoming-inspection`
- `nonconformance-report`
