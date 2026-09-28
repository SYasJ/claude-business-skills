---
name: survey-instrument
description: "Draft a survey that measures a defined construct without double-barreled or leading items. Use when the user mentions survey design, questionnaire, write a survey, instrument draft, or asks for a survey draft. Research skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: research
---

# Survey Instrument

Draft a survey that measures a defined construct without double-barreled or leading items.

## When to use this skill

Use this skill when the user:

- survey design
- questionnaire
- write a survey
- instrument draft

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not fabricate citations, quotations, data, or participants. Separate evidence you were given from claims that still need a source.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The decision
- The constructs
- The population
- Length they will tolerate

## Workflow


### 1. Step 1

Write the decision the survey must inform.
### 2. Step 2

One idea per item. Split double-barreled questions.
### 3. Step 3

Avoid leading wording and false precision.
### 4. Step 4

Use scales they can explain.
### 5. Pilot plan

who will try it before launch.
### 6. Step 6

Do not add demographic items you do not need. Minimize sensitive data.

## Output

Deliver a **survey draft**.

- Purpose of this survey draft, in two sentences.
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

Dr. Nia Okonkwo, research lead at Riverbend College in Lethbridge, needs a survey draft by 30 September 2026. An item asks whether the helpful and innovative service was satisfying.

### Example data

```text
From: Dr. Nia Okonkwo, research lead
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

An item asks whether the helpful and innovative service was satisfying.

site: one
sample: the count they gave
missing file: named in the ask
unopened citation: not used
```

### Example outcome

**Survey draft**
To: Dr. Nia Okonkwo, research lead, Riverbend College
Date: 14 September 2026

**Decision**
Splits the ideas, removes the leading praise, and cuts unused demographics.

**From the file**
- site: one
- sample: the count they gave
- missing file: named in the ask
- unopened citation: not used

Nothing in this draft was added from outside that file.
Next: Dr. Nia Okonkwo by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Double-barreled items
- Leading wording
- Sensitive items with no purpose

## Related skills

- `survey-analysis`
- `research-question`
