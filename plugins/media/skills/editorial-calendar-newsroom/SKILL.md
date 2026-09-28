---
name: editorial-calendar-newsroom
description: "Plan a newsroom or content desk day around the stories that are ready and the slots that should stay empty. Use when the user mentions newsroom planning, desk plan, what do we run, editorial meeting, or asks for a planning note. Media and communications skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: media
---

# Newsroom Planning Note

Plan a newsroom or content desk day around the stories that are ready and the slots that should stay empty.

## When to use this skill

Use this skill when the user:

- newsroom planning
- desk plan
- what do we run
- editorial meeting

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not fabricate quotes, sources, or images. Label opinion. Do not draft impersonation or defamation.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Ready stories
- Open reporting
- Slots
- Legal or standards flags

## Workflow


### 1. Step 1

Run only stories with a sourced point.
### 2. Step 2

Leave a slot empty rather than fill it with an unsourced piece.
### 3. Step 3

Flag legal review where they said it is required.
### 4. Step 4

Separate opinion from news in the plan.
### 5. Step 5

Do not assign a story that requires deception to report.
### 6. Step 6

Name the editor for each slot.

## Output

Deliver a **planning note**.

- Purpose of this planning note, in two sentences.
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

Jonah Ellis, assignment editor at Foothills Desk in Calgary, needs a planning note by 30 September 2026. The plan assigns a trend piece with no sources because the slot is empty.

### Example data

```text
From: Jonah Ellis, assignment editor
Organization: Foothills Desk, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The plan assigns a trend piece with no sources because the slot is empty.

document: the statement in the folder
unnamed quote: not used
deadline: the board time
unknown: stays unknown
```

### Example outcome

**Planning note**
To: Jonah Ellis, assignment editor, Foothills Desk
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Kills or holds the piece and leaves the slot open.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| document | the statement in the folder | Needs confirmation |
| unnamed quote | not used | Carried into the draft |
| deadline | the board time | Carried into the draft |
| unknown | stays unknown | Needs confirmation |

**How this draft was built**

**1. Run only stories with a sourced point**

**2. Leave a slot empty rather than fill it with an unsourced piece**

**3. Flag legal review where they said it is required**

**4. Separate opinion from news in the plan**

**5. Do not assign a story that requires deception to report**

**Deliberately not done**
- Filling a slot with an unsourced piece.
- Opinion labeled as news.
- A deceptive reporting assignment.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Ellis by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Filling a slot with an unsourced piece
- Opinion labeled as news
- A deceptive reporting assignment

## Related skills

- `content-calendar`
- `editorial-brief`
