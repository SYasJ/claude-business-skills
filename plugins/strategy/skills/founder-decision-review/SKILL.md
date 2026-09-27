---
name: founder-decision-review
description: "Help a founder pressure-test a lonely decision before they announce it. Use when the user mentions founder decision, am I about to make a mistake, pressure-test this call, solo founder choice, or asks for a founder decision review. Strategy and leadership skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: strategy
---

# Founder Decision Review

Help a founder pressure-test a lonely decision before they announce it.

## When to use this skill

Use this skill when the user:

- founder decision
- am I about to make a mistake
- pressure-test this call
- solo founder choice

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

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

- The decision and the deadline
- Alternatives still open
- What the founder is afraid of
- Whose advice they have already heard

## Workflow


### 1. Restate the decision

Reflect it back in one sentence so you are reviewing the real choice.
### 2. Separate fear from fact

List facts the founder supplied and the fear they named. Do not therapize. Do not flatter.
### 3. Stress the downside

What happens in 90 days if this is wrong, and is that downside reversible.
### 4. Look for a missing voice

Who is affected and has not been asked. Recommend asking them if there is time. Do not role-play their consent.
### 5. Offer a pre-mortem

Assume it failed and list the three most plausible reasons, using the founder's context.
### 6. Leave the decision with them

Recommend, but state that the call is theirs. Do not pretend to be a board.

## Output

Deliver a **founder decision review**.

- Purpose of this founder decision review, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs a founder decision review by 30 September 2026. A solo founder wants to fire their first salesperson before a board meeting in two days and is unsure.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A solo founder wants to fire their first salesperson before a board meeting in two days and is unsure.

decision: the one in the ask
options: two, named
evidence: the file only
unowned idea: parked
```

### Example outcome

**Founder decision review**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026

**Decision**
Restates the decision, separates facts from fear, names reversibility, and leaves the call with the founder.

**From the file**
- decision: the one in the ask
- options: two, named
- evidence: the file only
- unowned idea: parked

Nothing in this draft was added from outside that file.
Next: Mara Chen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Telling the founder what they want to hear.
- Expanding a hiring choice into a life-coaching session.
- Inventing investor or customer opinions.

## Related skills

- `decision-log`
- `founder-operating-review`
- `executive-one-pager`
