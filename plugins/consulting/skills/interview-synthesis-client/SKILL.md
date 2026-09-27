---
name: interview-synthesis-client
description: "Synthesize client interviews into themes with quotes the interviewee actually gave. Use when the user mentions interview synthesis, stakeholder interviews, client interviews, theme synthesis, or asks for a interview synthesis. Consulting skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: consulting
---

# Client Interview Synthesis

Synthesize client interviews into themes with quotes the interviewee actually gave.

## When to use this skill

Use this skill when the user:

- interview synthesis
- stakeholder interviews
- client interviews
- theme synthesis

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Client work stays confidential to the engagement. Do not fabricate findings to please a sponsor. Separate evidence from recommendation.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The notes
- The decision
- Who was not interviewed
- Confidentiality limits

## Workflow


### 1. Step 1

Theme only what the notes support.
### 2. Step 2

Use short quotes they captured. Do not improve a quote into a different meaning.
### 3. Step 3

Say who was not in the room.
### 4. Step 4

Respect confidentiality limits they stated.
### 5. Step 5

Recommend one implication.
### 6. Step 6

Do not attribute a view to a named person if the user said the readout must be anonymous.

## Output

Deliver a **interview synthesis**.

- Purpose of this interview synthesis, in two sentences.
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

Elena Voss, engagement manager at Clearlane Advisors in Calgary, needs an interview synthesis by 30 September 2026. A synthesis says the CFO demanded a cut, and the note was anonymous and less specific.

### Example data

```text
From: Elena Voss, engagement manager
Organization: Clearlane Advisors, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A synthesis says the CFO demanded a cut, and the note was anonymous and less specific.

decision: the one in the ask
evidence: notes only
out of scope: named
finding: not promised
```

### Example outcome

**Interview synthesis**
To: Elena Voss, engagement manager, Clearlane Advisors
Date: 14 September 2026

**Decision**
Keeps the anonymity rule and narrows the claim to the words in the note.

**From the file**
- decision: the one in the ask
- evidence: notes only
- out of scope: named
- finding: not promised

Nothing in this draft was added from outside that file.
Next: Elena Voss by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Improved quotes
- A missing-voice problem ignored
- Named comments in an anonymous readout

## Related skills

- `feedback-synthesis`
- `stakeholder-map`
