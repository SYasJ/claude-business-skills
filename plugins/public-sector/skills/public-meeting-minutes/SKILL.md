---
name: public-meeting-minutes
description: "Draft minutes of a public meeting that record motions, votes, and conflicts. Use when the user mentions public minutes, council minutes, board minutes public, meeting record, or asks for a public minutes. Public sector skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: public-sector
---

# Public Meeting Minutes

Draft minutes of a public meeting that record motions, votes, and conflicts.

## When to use this skill

Use this skill when the user:

- public minutes
- council minutes
- board minutes public
- meeting record

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Public work should be accurate, even-handed, and suitable for the record. Do not draft deceptive communications, voter manipulation, or surveillance programs.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The agenda
- Motions and votes they recorded
- Conflicts declared
- The approver

## Workflow


### 1. Step 1

Record motions and votes as given.
### 2. Step 2

Note declared conflicts.
### 3. Step 3

Do not invent attendance or a vote.
### 4. Step 4

Summarize discussion without caricature.
### 5. Step 5

Mark the draft for the clerk or chair to approve.
### 6. Step 6

Keep the tone suitable for the public record.

## Output

Deliver a **public minutes**.

- Purpose of this public minutes, in two sentences.
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

Pat Nguyen, clerk at Town of Airdrie in Airdrie, needs a public minutes by 30 September 2026. Minutes say a motion passed unanimously though a dissent was recorded.

### Example data

```text
From: Pat Nguyen, clerk
Organization: Town of Airdrie, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

Minutes say a motion passed unanimously though a dissent was recorded.

record: the agenda or request
vote: not implied if it has not happened
names: public record only
deadline: the posted one
```

### Example outcome

**Public minutes**
To: Pat Nguyen, clerk, Town of Airdrie
Date: 14 September 2026

**Decision**
Minutes that include the dissent and wait for the clerk's approval.

**From the file**
- record: the agenda or request
- vote: not implied if it has not happened
- names: public record only
- deadline: the posted one

Nothing in this draft was added from outside that file.
Next: Pat Nguyen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An invented vote
- A missing declared conflict
- Color commentary

## Related skills

- `board-meeting-facilitator`
- `decision-log`
