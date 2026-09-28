---
name: performance-review
description: "Draft a performance review from evidence, with no surprise criteria and no empty praise. Use when the user mentions performance review, write a review, annual review, review draft, or asks for a performance review draft. People and culture skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: people
---

# Performance Review

Draft a performance review from evidence, with no surprise criteria and no empty praise.

## When to use this skill

Use this skill when the user:

- performance review
- write a review
- annual review
- review draft

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Employment work must follow the organization's policies and local employment law. Do not invent legal requirements. Do not write content that discriminates or retaliates.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The goals that were actually set
- Evidence from the period
- The rating scale if one exists
- Development interest the employee stated

## Workflow


### 1. Use the original goals

Do not grade people on expectations never shared. If goals were missing, say the review is starting from a gap.
### 2. Evidence

Two or three specific examples for praise and for concern. No example, no strong claim.
### 3. Impact

What the work changed for customers or colleagues, not how hard the person seemed to work.
### 4. Development

One skill to grow, tied to upcoming work. A development list of ten items is a shrug.
### 5. Tone

Direct and respectful. No jokes, no medical speculation, no comparison to unnamed peers.
### 6. Manager owns it

The draft is for the manager to edit and deliver. You do not put words in the employee's mouth.

## Output

Deliver a **performance review draft**.

- Purpose of this performance review draft, in two sentences.
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

Chris Adeyemi, people lead at Northline Studio in Calgary, needs a performance review draft by 30 September 2026. A manager wants to rate someone low for 'attitude' but has not named a missed goal.

### Example data

```text
From: Chris Adeyemi, people lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A manager wants to rate someone low for 'attitude' but has not named a missed goal.

cadence: weekly, 30 minutes, Tuesday 10:00
status board: already updated daily
last meeting: 6 status questions, employee did not set the agenda
growth topic: none written down
```

### Example outcome

**Performance review draft**
To: Chris Adeyemi, people lead, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the attitude label, asks for examples against the original goals, and limits development to one skill.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| cadence | weekly, 30 minutes, Tuesday 10:00 | Needs confirmation |
| status board | already updated daily | Carried into the draft |
| last meeting | 6 status questions, employee did not set the agenda | Carried into the draft |
| growth topic | none written down | Needs confirmation |

**How this draft was built**

**1. Use the original goals**  
Do not grade people on expectations never shared. If goals were missing, say the review is starting from a gap.

**2. Evidence**  
Two or three specific examples for praise and for concern. No example, no strong claim.

**3. Impact**  
What the work changed for customers or colleagues, not how hard the person seemed to work.

**4. Development**  
One skill to grow, tied to upcoming work. A development list of ten items is a shrug.

**5. Tone**  
Direct and respectful. No jokes, no medical speculation, no comparison to unnamed peers.

**Deliberately not done**
- Surprise criteria.
- Praise with no example.
- A review that diagnoses a health or personality condition.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Chris Adeyemi by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Surprise criteria.
- Praise with no example.
- A review that diagnoses a health or personality condition.

## Related skills

- `pip-design`
- `manager-one-on-one`
- `thirty-sixty-ninety`
