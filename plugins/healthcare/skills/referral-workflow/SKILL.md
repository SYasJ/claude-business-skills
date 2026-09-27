---
name: referral-workflow
description: "Map a referral workflow so the sending and receiving sides know the packet, the owner, and the clock. Use when the user mentions referral workflow, referral leakage, specialist referral process, referral SOP, or asks for a referral workflow. Healthcare practice operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: healthcare
---

# Referral Workflow

Map a referral workflow so the sending and receiving sides know the packet, the owner, and the clock.

## When to use this skill

Use this skill when the user:

- referral workflow
- referral leakage
- specialist referral process
- referral SOP

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

This is not medical advice, diagnosis, or a treatment protocol. Do not recommend drugs, doses, or clinical interventions. Limit the work to practice operations, documentation quality, and communication drafts for a licensed clinician to approve.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The packet they require
- Who sends and receives
- Clocks they use
- What patients are told

## Workflow


### 1. Step 1

Define a complete packet from their list. Do not invent clinical requirements.
### 2. Step 2

Name the owner of each handoff.
### 3. Step 3

State what the patient is told and when.
### 4. Step 4

Track a stalled referral as an operations issue with an aging rule.
### 5. Step 5

Close the loop back to the sender when they say that is required.
### 6. Step 6

Escalate clinical questions to a clinician. Do not decide medical necessity.

## Output

Deliver a **referral workflow**.

- Purpose of this referral workflow, in two sentences.
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

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a referral workflow by 30 September 2026. Referrals leave the clinic and nobody knows which ones were received.

### Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

Referrals leave the clinic and nobody knows which ones were received.

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

### Example outcome

**Referral workflow**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026

**Decision**
A workflow with a packet, an owner, and an aging check, and no medical-necessity ruling.

**From the file**
- clinic: Cedar, Tuesday list
- diagnosis: not in this note
- roster: the one attached
- advice to a patient: not written

Nothing in this draft was added from outside that file.
Next: Dr. Helen Cho by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A referral with no owner
- Invented medical-necessity rulings
- Patients left without a status

## Related skills

- `patient-intake-sop`
- `prior-authorization-ops`
