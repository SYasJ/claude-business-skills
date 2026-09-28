---
name: workforce-plan
description: "Connect a hiring plan to the work and the cash, and show which roles are load-bearing. Use when the user mentions workforce plan, hiring plan, headcount plan, capacity versus hiring, or asks for a workforce plan. People and culture skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: people
---

# Workforce Plan

Connect a hiring plan to the work and the cash, and show which roles are load-bearing.

## When to use this skill

Use this skill when the user:

- workforce plan
- hiring plan
- headcount plan
- capacity versus hiring

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

- The work to be done
- Current team and open roles
- Constraints from finance
- Skills that are scarce

## Workflow


### 1. Demand first

What work arrives next quarter, in their words. Hiring follows demand, not a headcount habit.
### 2. Capacity

Who can absorb work before a hire. A hire is a recommendation, not a reflex.
### 3. Sequence

Which role unblocks the others. Hiring five roles at once without a recruiter plan is a wish.
### 4. Cost

Use their pay assumptions. If pay is unknown, mark the cost as incomplete. Do not invent salaries.
### 5. Contract versus hire

Note where a short need does not justify a permanent role, as a question for HR and counsel, not a classification ruling.
### 6. Review point

When the plan is revisited if demand slips.

## Output

Deliver a **workforce plan**.

- Purpose of this workforce plan, in two sentences.
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

Chris Adeyemi, people lead at Northline Studio in Calgary, needs a workforce plan by 30 September 2026. A team asked for eight hires, and finance has capped the quarter at three.

### Example data

```text
From: Chris Adeyemi, people lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A team asked for eight hires, and finance has capped the quarter at three.

cadence: weekly, 30 minutes, Tuesday 10:00
status board: already updated daily
last meeting: 6 status questions, employee did not set the agenda
growth topic: none written down
```

### Example outcome

**Workforce plan**
To: Chris Adeyemi, people lead, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Unblock the work, with the other five parked and the cash cap respected.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| cadence | weekly, 30 minutes, Tuesday 10:00 | Needs confirmation |
| status board | already updated daily | Carried into the draft |
| last meeting | 6 status questions, employee did not set the agenda | Carried into the draft |
| growth topic | none written down | Needs confirmation |

**How this draft was built**

**1. Demand first**  
What work arrives next quarter, in their words. Hiring follows demand, not a headcount habit.

**2. Capacity**  
Who can absorb work before a hire. A hire is a recommendation, not a reflex.

**3. Sequence**  
Which role unblocks the others. Hiring five roles at once without a recruiter plan is a wish.

**4. Cost**  
Use their pay assumptions. If pay is unknown, mark the cost as incomplete. Do not invent salaries.

**5. Contract versus hire**  
Note where a short need does not justify a permanent role, as a question for HR and counsel, not a classification ruling.

**Deliberately not done**
- A headcount list with no link to work.
- Invented salaries.
- Hiring that ignores a cash constraint they already stated.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Chris Adeyemi by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- A headcount list with no link to work.
- Invented salaries.
- Hiring that ignores a cash constraint they already stated.

## Related skills

- `org-design-review`
- `runway-and-burn`
- `annual-planning-cycle`
