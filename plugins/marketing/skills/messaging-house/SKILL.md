---
name: messaging-house
description: "Build a messaging house so headline, pillars, and proof do not contradict each other. Use when the user mentions messaging house, message pillars, brand messages, what do we say, or asks for a messaging house. Marketing skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: marketing
---

# Messaging House

Build a messaging house so headline, pillars, and proof do not contradict each other.

## When to use this skill

Use this skill when the user:

- messaging house
- message pillars
- brand messages
- what do we say

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not invent testimonials, reviews, metrics, or claims the user cannot support. Do not draft spam, cloaking, fake scarcity, or impersonation.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The positioning
- Three proof points
- Objections sales hears
- Claims that must not be made

## Workflow


### 1. Headline

One sentence from the positioning. If positioning is missing, do that first.
### 2. Pillars

Three pillars a buyer can remember. Each pillar has a customer benefit, not an internal project name.
### 3. Proof under each pillar

Only supplied proof. Empty proof means the pillar is not ready for a homepage.
### 4. Objection line

One honest response to the top objection, with no fake logos.
### 5. Words to avoid

A short list of hype and unsupported comparisons.
### 6. Channel note

What changes for a sales call versus a homepage, without changing the meaning.

## Output

Deliver a **messaging house**.

- Purpose of this messaging house, in two sentences.
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

Lena Ortiz, marketing lead at Fieldnote in Edmonton, needs a messaging house by 30 September 2026. The homepage says 'effortless' and sales says implementation takes six weeks.

### Example data

```text
From: Lena Ortiz, marketing lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The homepage says 'effortless' and sales says implementation takes six weeks.

page: the live page
claim: broader than the note
proof: none attached
publish date wanted: 19 Sep 2026
```

### Example outcome

**Messaging house**
To: Lena Ortiz, marketing lead, Fieldnote
Date: 14 September 2026

**Decision**
Replaces 'effortless' with a truthful implementation claim and aligns both channels.

**From the file**
- page: the live page
- claim: broader than the note
- proof: none attached
- publish date wanted: 19 Sep 2026

Nothing in this draft was added from outside that file.
Next: Lena Ortiz by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Pillars with no proof.
- Different claims in sales and on the site.
- Internal jargon as a pillar.

## Related skills

- `positioning-statement`
- `marketing-claims-review`
