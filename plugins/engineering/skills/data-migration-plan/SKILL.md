---
name: data-migration-plan
description: "Plan a data migration with reconciliation counts, a freeze or dual-write choice, and a stop condition. Use when the user mentions data migration, backfill plan, move this table, reconcile a migration, or asks for a data migration plan. Engineering skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: engineering
---

# Data Migration Plan

Plan a data migration with reconciliation counts, a freeze or dual-write choice, and a stop condition.

## When to use this skill

Use this skill when the user:

- data migration
- backfill plan
- move this table
- reconcile a migration

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Prefer the repository's existing patterns. Do not disable security controls, invent credentials, or introduce network calls the user did not ask for.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Source and target
- Volume if known
- Correctness rules
- Downtime tolerance

## Workflow


### 1. Rules

What makes a row correct in the target. Write the rule before writing the job.
### 2. Method

Dual-write, backfill, or freeze, chosen from their tolerance. Do not pick a method they cannot operate.
### 3. Reconciliation

Counts and checksums or samples they can actually run. A migration without reconciliation is a guess.
### 4. Stop

The mismatch that halts the job.
### 5. Privacy

Do not copy data into a less protected place for convenience. No exports of secrets into tickets.
### 6. Cutover

Who signs that the reconciliation passed.

## Output

Deliver a **data migration plan**.

- Purpose of this data migration plan, in two sentences.
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

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a data migration plan by 30 September 2026. A script copies customer records to a new store and the plan says 'check a few rows'.

### Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A script copies customer records to a new store and the plan says 'check a few rows'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

### Example outcome

**Data migration plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Is more than a glance.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A migration with no reconciliation.
- Copying sensitive data into a ticket.
- A method the team cannot operate.

## Related skills

- `migration-plan`
- `database-change-review`
