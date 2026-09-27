---
name: estimation-review
description: "Review an engineering estimate by exposing assumptions, slices, and the unknown, not by demanding false precision. Use when the user mentions engineering estimate, story points argument, how long will this take, estimation review, or asks for a estimate review. Engineering skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: engineering
---

# Estimation Review

Review an engineering estimate by exposing assumptions, slices, and the unknown, not by demanding false precision.

## When to use this skill

Use this skill when the user:

- engineering estimate
- story points argument
- how long will this take
- estimation review

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Prefer the repository's existing patterns. Do not disable security controls, invent credentials, or introduce network calls the user did not ask for.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The work as scoped
- Similar work they have done
- Unknowns
- Who is doing it

## Workflow


### 1. Scope

Restate the slice. An estimate of an unbounded idea is not an estimate. Cut scope first.
### 2. Assumptions

List the assumptions. The estimate is valid only while they hold.
### 3. Reference

Compare with a past piece of work they name. Do not invent a velocity number.
### 4. Unknowns

The spike that would shrink the range. Recommend a range, not a fake single day.
### 5. Capacity

Calendar time is not effort time. Include review and release if they matter.
### 6. Update

When the estimate should be replaced, after the spike or the first slice.

## Output

Deliver a **estimate review**.

- Purpose of this estimate review, in two sentences.
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

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an estimate review by 30 September 2026. A stakeholder wants a date for a rewrite with no scope and no prior art.

### Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A stakeholder wants a date for a rewrite with no scope and no prior art.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

### Example outcome

**Estimate review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Refuses the date, proposes a scoped spike, and offers a range only after that spike.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A single-day estimate for an unbounded project.
- Invented velocity.
- Hiding unknowns to look confident.

## Related skills

- `sprint-plan`
- `refactor-plan`
