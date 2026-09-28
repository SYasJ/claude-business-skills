---
name: design-handoff
description: "Hand a design to engineering with states, content, and open decisions explicit. Use when the user mentions design handoff, spec for engineering, developer handoff, design QA notes, or asks for a handoff note. Design skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: design
---

# Design Handoff

Hand a design to engineering with states, content, and open decisions explicit.

## When to use this skill

Use this skill when the user:

- design handoff
- spec for engineering
- developer handoff
- design QA notes

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Design critique improves the work. Do not copy a third party's branded assets. Accessibility is part of done, not a later pass to skip.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The screens
- States
- Content
- Known decisions still open

## Workflow


### 1. Step 1

List what is in scope for this handoff.
### 2. Step 2

Include empty, error, and loading states.
### 3. Step 3

Write the content, not lorem, unless a field is truly dynamic, and then say so.
### 4. Step 4

Mark open decisions so engineering does not guess.
### 5. Step 5

Note accessibility expectations for the flow.
### 6. Step 6

Do not treat a static mock as permission to skip the unauthorized state.

## Output

Deliver a **handoff note**.

- Purpose of this handoff note, in two sentences.
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

Lena Ortiz, design lead at Fieldnote in Edmonton, needs a handoff note by 30 September 2026. A handoff includes the success screen only for a payment flow.

### Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A handoff includes the success screen only for a payment flow.

screens: 8, dated 10 Sep 2026
job: the task in the ask
accessibility pass: not done
assets: theirs only
```

### Example outcome

**Handoff note**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Adds failure, empty, and the unauthorized state, and lists open decisions.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| screens | 8, dated 10 Sep 2026 | Needs confirmation |
| job | the task in the ask | Carried into the draft |
| accessibility pass | not done | Carried into the draft |
| assets | theirs only | Needs confirmation |

**How this draft was built**

**1. List what is in scope for this handoff**

**2. Include empty, error, and loading states**

**3. Write the content, not lorem, unless a field is truly dynamic, and then say so**

**4. Mark open decisions so engineering does not guess**

**5. Note accessibility expectations for the flow**

**Deliberately not done**
- Lorem on a commitment screen.
- Hidden open decisions.
- No error state.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Lorem on a commitment screen
- Hidden open decisions
- No error state

## Related skills

- `wireframe-spec`
- `accessibility-design`
