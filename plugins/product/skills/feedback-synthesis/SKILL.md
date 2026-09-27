---
name: feedback-synthesis
description: "Synthesize feedback from tickets, calls, or notes into themes with evidence, not a word cloud. Use when the user mentions synthesize feedback, voice of customer themes, ticket themes, interview synthesis, or asks for a feedback synthesis. Product skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: product
---

# Feedback Synthesis

Synthesize feedback from tickets, calls, or notes into themes with evidence, not a word cloud.

## When to use this skill

Use this skill when the user:

- synthesize feedback
- voice of customer themes
- ticket themes
- interview synthesis

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

- The raw notes or tickets
- The decision this informs
- How the sample was gathered
- What volume means in their context

## Workflow


### 1. Sample bias

Say who is missing from the pile. A pile of detractors is not the whole market.
### 2. Themes

Group by the job or failure, not by the feature name alone.
### 3. Evidence

Each theme has quotes or ticket counts from the supplied material. No theme without evidence.
### 4. Severity

Distinguish frequency from pain. A rare data-loss report can outrank a common color complaint.
### 5. Implication

What product should do next, and what should be a support macro instead.
### 6. Do not invent

If the notes do not support a favorite theme, say it is not in the evidence.

## Output

Deliver a **feedback synthesis**.

- Purpose of this feedback synthesis, in two sentences.
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

Jonah Park, product manager at Fieldnote in Edmonton, needs a feedback synthesis by 30 September 2026. A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures.

### Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

### Example outcome

**Feedback synthesis**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026

**Decision**
Leads with export failures, counts only supplied evidence, and parks the executive idea as unproven.

**From the file**
- interviews: 12, March to June 2026
- decision: ship, hold, or cut
- metric: not defined
- kill line: not written

Nothing in this draft was added from outside that file.
Next: Jonah Park by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A word cloud as the analysis.
- Ignoring sample bias.
- Themes with no quotes.

## Related skills

- `voice-of-customer`
- `discovery-interview`
