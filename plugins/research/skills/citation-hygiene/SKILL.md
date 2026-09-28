---
name: citation-hygiene
description: "Check citations so every claim that needs a source has one the user can verify. Use when the user mentions citation check, references, bibliography hygiene, source this claim, or asks for a citation check. Research skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: research
---

# Citation Hygiene

Check citations so every claim that needs a source has one the user can verify.

## When to use this skill

Use this skill when the user:

- citation check
- references
- bibliography hygiene
- source this claim

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not fabricate citations, quotations, data, or participants. Separate evidence you were given from claims that still need a source.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The draft
- The sources they have
- The citation style if required
- Claims that sound factual

## Workflow


### 1. Step 1

Mark factual claims that lack a source the user provided.
### 2. Step 2

Do not invent a citation to fill a gap. Ask for a source or rewrite the claim as an assumption.
### 3. Step 3

Match quotations to text they supplied. A quote you cannot see is not used.
### 4. Step 4

Note style errors only after existence is confirmed.
### 5. Step 5

Separate the user's analysis from cited facts.
### 6. Step 6

Flag a citation that does not support the sentence it is attached to, if you can see both.

## Output

Deliver a **citation check**.

- Purpose of this citation check, in two sentences.
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

Dr. Nia Okonkwo, research lead at Riverbend College in Lethbridge, needs a citation check by 30 September 2026. A paragraph says 'studies show' and lists no study the user has.

### Example data

```text
From: Dr. Nia Okonkwo, research lead
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

A paragraph says 'studies show' and lists no study the user has.

The sources they have: note from Dr. Nia Okonkwo, 14 September 2026. No outside report
The citation style if required: no citation attached
Claims that sound factual: the draft sentence is broader than the note
```

### Example outcome

**Citation check**
To: Dr. Nia Okonkwo, research lead, Riverbend College
Date: 14 September 2026

**Decision**
Replaces the phrase with an assumption or a request for the actual study.

**From the file**
- The sources they have: note from Dr. Nia Okonkwo, 14 September 2026. No outside report
- The citation style if required: no citation attached
- Claims that sound factual: the draft sentence is broader than the note

Nothing in this draft was added from outside that file.
Next: Dr. Nia Okonkwo by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Invented papers
- A quotation you cannot verify
- A citation that does not support the claim

## Related skills

- `literature-review-plan`
- `research-memo`
