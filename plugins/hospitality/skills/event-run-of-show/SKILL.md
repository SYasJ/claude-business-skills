---
name: event-run-of-show
description: "Write a run of show for a hosted event with owners, cues, and a guest-impact backup. Use when the user mentions run of show, banquet event order, event cues, hospitality event plan, or asks for a event run of show. Hospitality skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: hospitality
---

# Event Run of Show

Write a run of show for a hosted event with owners, cues, and a guest-impact backup.

## When to use this skill

Use this skill when the user:

- run of show
- banquet event order
- event cues
- hospitality event plan

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Guest recovery should be sincere and within policy. Do not invent compensation authority the user has not granted.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The guest promise
- Cues and times
- Owners
- The backup if a cue fails

## Workflow


### 1. Step 1

List cues in order with owners.
### 2. Step 2

State the guest promise that cannot slip.
### 3. Step 3

Add a backup for the fragile cue.
### 4. Step 4

Note dietary or access needs they confirmed, without extra personal detail.
### 5. Step 5

Do not promise a vendor who has not confirmed.
### 6. Step 6

Name the person who may change the plan during the event.

## Output

Deliver a **event run of show**.

- Purpose of this event run of show, in two sentences.
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

Sofia Alvarez, front office manager at Lantern Inn in Banff, needs an event run of show by 30 September 2026. A run of show promises a speaker who has not confirmed.

### Example data

```text
From: Sofia Alvarez, front office manager
Organization: Lantern Inn, Banff
Date: 14 September 2026
Needed by: 30 September 2026

A run of show promises a speaker who has not confirmed.

The guest promise: none written down beyond the ask
Cues and times: five working days, due 30 September 2026
Owners: Sofia Alvarez, front office manager
```

### Example outcome

**Event run of show**
To: Sofia Alvarez, front office manager, Lantern Inn
Date: 14 September 2026

**Decision**
Marks the speaker unconfirmed and names a backup cue.

**From the file**
- The guest promise: none written down beyond the ask
- Cues and times: five working days, due 30 September 2026
- Owners: Sofia Alvarez, front office manager

Nothing in this draft was added from outside that file.
Next: Sofia Alvarez by 30 September 2026. This is not a sign-off.

## Anti-patterns

- An unconfirmed vendor presented as certain
- No backup
- Extra personal details

## Related skills

- `webinar-run-of-show`
- `shift-brief-hospitality`
