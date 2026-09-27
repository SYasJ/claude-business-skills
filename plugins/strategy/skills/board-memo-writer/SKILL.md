---
name: board-memo-writer
description: "Draft a board memo that leads with the decision, the ask, and the risk, not a recap of activity. Use when the user mentions board memo, board paper, write to the board, director update, or asks for a board decision memo. Strategy and leadership skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: strategy
---

# Board Memo Writer

Draft a board memo that leads with the decision, the ask, and the risk, not a recap of activity.

## When to use this skill

Use this skill when the user:

- board memo
- board paper
- write to the board
- director update
- board pre-read

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

- The decision or update type
- The ask, if any, including amount and timing
- Facts, misses, and risks the user can support
- What the board already knows

## Workflow


### 1. Lead with the ask

The first paragraph states the decision, the recommendation, and what happens if the board does nothing.
### 2. Separate news from noise

Include only changes since the last meeting that affect cash, risk, customers, or the strategy.
### 3. Show the downside

Name the main risk, the early warning sign, and the mitigation already in motion. Do not hide a miss in an appendix.
### 4. Give options when there is a decision

Two or three options, with cost, time, and what each gives up. Recommend one.
### 5. Keep it short

Aim for two pages. Move tables and backup to a short appendix the memo points to.
### 6. Mark drafts

Label the memo as a draft for the CEO or chair to approve. Do not invent resolutions or votes.

## Output

Deliver a **board decision memo**.

- Purpose of this board decision memo, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs a board decision memo by 30 September 2026. The CEO needs a pre-read asking the board to approve a hiring pause until a renewal lands.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The CEO needs a pre-read asking the board to approve a hiring pause until a renewal lands.

decision: the one in the ask
options: two, named
evidence: the file only
unowned idea: parked
```

### Example outcome

**Board decision memo**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026

**Decision**
A two-page memo with the ask, the cash implication, two alternatives, and the decision requested at the meeting.

**From the file**
- decision: the one in the ask
- options: two, named
- evidence: the file only
- unowned idea: parked

Nothing in this draft was added from outside that file.
Next: Mara Chen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Opening with a company history the board already knows.
- Burying a cash problem under product updates.
- Writing a resolution as if the board had already voted.

## Related skills

- `board-meeting-facilitator`
- `decision-log`
- `executive-one-pager`
