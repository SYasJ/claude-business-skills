---
name: stakeholder-prd-review
description: "Review a PRD with stakeholders by separating decisions from opinions and parking out-of-scope demands. Use when the user mentions PRD review, stakeholder review, spec review meeting, requirements review, or asks for a PRD review notes. Product skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: product
---

# Stakeholder PRD Review

Review a PRD with stakeholders by separating decisions from opinions and parking out-of-scope demands.

## When to use this skill

Use this skill when the user:

- PRD review
- stakeholder review
- spec review meeting
- requirements review

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Product recommendations are hypotheses until evidence says otherwise. Label confidence. Do not ship dark patterns that hide cost or consent.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The PRD
- The attendees and their concerns
- Decisions already made
- The open questions

## Workflow


### 1. Outcome check

Can every reviewer state the user outcome. If not, fix that before debating details.
### 2. Classify comments

Decision, risk, or preference. Preferences do not silently change scope.
### 3. Conflicts

Where two stakeholders demand incompatible scope, write the tradeoff and the decider.
### 4. Parking lot

Out-of-scope requests go to the parking lot with a reason, not into the PRD out of politeness.
### 5. Open questions

Owner and date. Unowned questions are the real launch risk.
### 6. Close

Restate the scope that survived the review so nobody leaves with a private version.

## Output

Deliver a **PRD review notes**.

- Purpose of this PRD review notes, in two sentences.
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

Jonah Park, product manager at Fieldnote in Edmonton, needs a PRD review notes by 30 September 2026. Sales adds six prospect requests during a PRD review, and engineering thinks they are now committed.

### Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales adds six prospect requests during a PRD review, and engineering thinks they are now committed.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

### Example outcome

**Prd review notes**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026

**Decision**
Notes that park the six requests, restate the surviving scope, and name the decider for any conflict.

**From the file**
- interviews: 12, March to June 2026
- decision: ship, hold, or cut
- metric: not defined
- kill line: not written

Nothing in this draft was added from outside that file.
Next: Jonah Park by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Adding every comment to the spec.
- Leaving the review with two different scopes in people's heads.
- Treating every preference as a requirement.

## Related skills

- `prd-writer`
- `roadmap-narrative`
