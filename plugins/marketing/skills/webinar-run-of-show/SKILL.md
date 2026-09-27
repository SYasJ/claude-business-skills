---
name: webinar-run-of-show
description: "Plan a webinar that teaches one job and makes one honest ask. Use when the user mentions webinar plan, run of show, online event, workshop agenda, or asks for a webinar run of show. Marketing skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: marketing
---

# Webinar Run of Show

Plan a webinar that teaches one job and makes one honest ask.

## When to use this skill

Use this skill when the user:

- webinar plan
- run of show
- online event
- workshop agenda

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

- The audience
- The one teaching goal
- Speakers
- The ask

## Workflow


### 1. Promise

The title matches the content. No bait title.
### 2. Run of show

Timed blocks, including questions. A 40-minute monologue is a finding.
### 3. Proof

Slides use only approved numbers. Mark missing numbers as gaps.
### 4. Ask

One next step at the end. Do not pretend the session is free of an ask if it is not.
### 5. Roles

Host, speaker, and the person watching questions. A demo backup if live product is involved.
### 6. Follow-up

The email after the session restates the teaching point, not only the pitch.

## Output

Deliver a **webinar run of show**.

- Purpose of this webinar run of show, in two sentences.
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

Lena Ortiz, marketing lead at Fieldnote in Edmonton, needs a webinar run of show by 30 September 2026. A webinar titled as a practical workshop is planned as a 45-minute product pitch.

### Example data

```text
From: Lena Ortiz, marketing lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A webinar titled as a practical workshop is planned as a 45-minute product pitch.

page: the live page
claim: broader than the note
proof: none attached
publish date wanted: 19 Sep 2026
```

### Example outcome

**Webinar run of show**
To: Lena Ortiz, marketing lead, Fieldnote
Date: 14 September 2026

**Decision**
Either retitles the session or replaces half the pitch with the promised practice.

**From the file**
- page: the live page
- claim: broader than the note
- proof: none attached
- publish date wanted: 19 Sep 2026

Nothing in this draft was added from outside that file.
Next: Lena Ortiz by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A bait-and-switch title.
- Unapproved metrics on slides.
- No time for questions in a session that promised them.

## Related skills

- `campaign-brief`
- `workshop-facilitation`
