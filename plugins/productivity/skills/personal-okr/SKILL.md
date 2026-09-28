---
name: personal-okr
description: "Set a few personal objectives that fit the week you actually have. Use when the user mentions personal OKRs, personal goals, quarterly personal goals, life planning goals, or asks for a personal objectives. Productivity skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: productivity
---

# Personal OKRs

Set a few personal objectives that fit the week you actually have.

## When to use this skill

Use this skill when the user:

- personal OKRs
- personal goals
- quarterly personal goals
- life planning goals

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Productivity systems serve the person's actual constraints. Do not recommend surveillance of colleagues or hidden monitoring.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The outcomes that matter
- Time available
- Existing commitments
- How you will review

## Workflow


### 1. Step 1

Choose one to three objectives.
### 2. Step 2

Write key results you can observe.
### 3. Step 3

Check them against the calendar.
### 4. Step 4

Cut goals that require time you do not have.
### 5. Step 5

Set a review.
### 6. Step 6

Do not turn personal goals into a surveillance plan for family or coworkers.

## Output

Deliver a **personal objectives**.

- Purpose of this personal objectives, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs a personal objectives by 30 September 2026. A plan adds a daily two-hour course on top of a 50-hour job with no time removed.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A plan adds a daily two-hour course on top of a 50-hour job with no time removed.

week: 14 Sep 2026
calendar: the meetings they listed
dissent: kept if it was said
monitoring: not recommended
```

### Example outcome

**Personal objectives**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Fits the real week and names a review.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| week | 14 Sep 2026 | Needs confirmation |
| calendar | the meetings they listed | Carried into the draft |
| dissent | kept if it was said | Carried into the draft |
| monitoring | not recommended | Needs confirmation |

**How this draft was built**

**1. Choose one to three objectives**

**2. Write key results you can observe**

**3. Check them against the calendar**

**4. Cut goals that require time you do not have**

**5. Set a review**

**Deliberately not done**
- Goals that do not fit the calendar.
- Vanity goals with no review.
- Surveillance of other people.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Goals that do not fit the calendar
- Vanity goals with no review
- Surveillance of other people

## Related skills

- `okrs-and-scorecard`
- `weekly-review`
