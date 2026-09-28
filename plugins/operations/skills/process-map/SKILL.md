---
name: process-map
description: "Map a process as it is, including handoffs and waits, before anyone redesigns it. Use when the user mentions process map, current state map, handoff map, where does this process break, or asks for a process map. Operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: operations
---

# Process Map

Map a process as it is, including handoffs and waits, before anyone redesigns it.

## When to use this skill

Use this skill when the user:

- process map
- current state map
- handoff map
- where does this process break

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Operating procedures should be usable by the team that will run them. Do not add surveillance of employees beyond what the user explicitly asks to document as policy.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The start and end
- The people who touch it
- The waits they complain about
- The systems

## Workflow


### 1. Step 1

Map the current state, not the wished state. Label it current.
### 2. Step 2

Show handoffs and queues. The wait is often the process.
### 3. Step 3

Mark rework loops the user described.
### 4. Step 4

Do not add a control that does not exist and call it current.
### 5. Step 5

Identify one bottleneck with evidence from their description.
### 6. Step 6

Recommend a future change separately from the map.

## Output

Deliver a **process map**.

- Purpose of this process map, in two sentences.
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

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a process map by 30 September 2026. A team draws a five-box happy path and omits the two-day wait for approval.

### Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A team draws a five-box happy path and omits the two-day wait for approval.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

### Example outcome

**Process map**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Includes the approval wait and separates any future idea.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Map the current state, not the wished state. Label it current**

**2. Show handoffs and queues. The wait is often the process**

**3. Mark rework loops the user described**

**4. Do not add a control that does not exist and call it current**

**5. Identify one bottleneck with evidence from their description**

**Deliberately not done**
- A future-state map labeled current.
- Ignoring queues.
- A map with no handoffs.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- A future-state map labeled current
- Ignoring queues
- A map with no handoffs

## Related skills

- `sop-writer`
- `continuous-improvement`
