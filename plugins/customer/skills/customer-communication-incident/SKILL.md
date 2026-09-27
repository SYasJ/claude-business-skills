---
name: customer-communication-incident
description: "Draft customer incident updates that say what is known, what is not, and when the next update will come. Use when the user mentions incident communication, status page update, outage email, customer incident update, or asks for a incident communication. Customer experience skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: customer
---

# Customer Incident Communication

Draft customer incident updates that say what is known, what is not, and when the next update will come.

## When to use this skill

Use this skill when the user:

- incident communication
- status page update
- outage email
- customer incident update

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Do not blame the customer. Do not invent policy exceptions. Do not ask a customer for passwords or full payment card numbers.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Known impact
- Unknowns
- Next update time
- Approver

## Workflow


### 1. Step 1

State the impact a customer would notice.
### 2. Step 2

Separate confirmed facts from work in progress.
### 3. Step 3

Give the next update time even if there is no fix yet.
### 4. Step 4

Do not speculate about cause or blame a supplier unless that statement is approved.
### 5. Step 5

Tell customers what to do if anything, such as retry after a time, only if support confirmed it.
### 6. Step 6

Keep a log of what was said so later updates do not contradict earlier ones.

## Output

Deliver a **incident communication**.

- Purpose of this incident communication, in two sentences.
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

Rita Santos, support lead at Fieldnote in Edmonton, needs an incident communication by 30 September 2026. A draft blames a vendor and promises a fix in 15 minutes without engineering confirmation.

### Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft blames a vendor and promises a fix in 15 minutes without engineering confirmation.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

### Example outcome

**Incident communication**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026

**Decision**
Removes the blame and the unconfirmed clock, and commits to a next update time.

**From the file**
- ticket: 4412, 14 Sep 2026
- customer words: in the ticket
- exception: not approved
- card or password: not collected

Nothing in this draft was added from outside that file.
Next: Rita Santos by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A cause guess
- A silent gap with no next update
- Contradicting the previous update

## Related skills

- `service-recovery`
- `war-room-brief`
