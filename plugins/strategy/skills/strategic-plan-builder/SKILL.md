---
name: strategic-plan-builder
description: "Turn a vague ambition into a one-page strategy with a real choice, a few bets, and what you will not do. Use when the user mentions write a strategy, annual strategy, where should we focus, strategic plan, or asks for a one-page strategic plan. Strategy and leadership skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: strategy
---

# Strategic Plan Builder

Turn a vague ambition into a one-page strategy with a real choice, a few bets, and what you will not do.

## When to use this skill

Use this skill when the user:

- write a strategy
- annual strategy
- where should we focus
- strategic plan
- what not to do

## When not to use this skill

- A request for a financial model only
- A legal entity decision that needs counsel

## Professional boundary

Strategy work recommends a direction. It does not guarantee market outcomes.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Current position: customers, revenue motion, constraints
- The decision the plan must settle
- Time horizon, usually 12 months
- What is already committed and cannot move

## Workflow


### 1. Name the choice

State the strategic question in one sentence, such as which customer, motion, or market gets scarce attention this year.
### 2. Bound the horizon

Use the horizon the user gave. If they did not, use 12 months and say so. Do not write a five-year vision deck unless they asked for one.
### 3. Record the playing field

Summarize only facts the user supplied: who pays, why they pay, and what constraint is binding. Mark anything else as an assumption.
### 4. Make a few bets

Recommend no more than three bets. Each bet needs an owner, a cost, a leading indicator, and a kill criterion.
### 5. Write the nos

List at least three attractive options you are explicitly not doing, and the reason. A plan without nos is a wish list.
### 6. Set the review

Name the forum and cadence that will revisit the bets. Strategy that is never reviewed is a poster.

## Output

Deliver a **one-page strategic plan**.

- Purpose of this one-page strategic plan, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs an one-page strategic plan by 30 September 2026. A founder says the company should 'become the platform for mid-market clinics' but the team is still closing the first ten customers by hand.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A founder says the company should 'become the platform for mid-market clinics' but the team is still closing the first ten customers by hand.

Current position: customers, revenue motion, constraints: customers: in the file; revenue motion: not in the file; constraints: open
The decision the plan must settle: A founder says the company should 'become the platform for mid-market clinics' but the team is still closing the first ten customers by hand
Time horizon, usually 12 months: 13 weeks
```

### Example outcome

**One-page strategic plan**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026

**Decision**
Chooses a beachhead, names three bets, lists what will wait, and sets a 90-day review with kill criteria.

**From the file**
- Current position: customers, revenue motion, constraints: customers: in the file; revenue motion: not in the file; constraints: open
- The decision the plan must settle: A founder says the company should 'become the platform for mid-market clinics' but the team is still closing the first ten customers by hand
- Time horizon, usually 12 months: 13 weeks

Nothing in this draft was added from outside that file.
Next: Mara Chen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Listing every initiative the team already wanted and calling it a strategy.
- Confusing a vision statement with a choice.
- Inventing market size to make the plan look bigger.

## Related skills

- `scenario-planning`
- `portfolio-prioritization`
- `annual-planning-cycle`
