---
name: policy-exception-log
description: "Record a policy exception so the company can see who accepted the risk and when it expires. Use when the user mentions policy exception, risk acceptance, exception log, waiver of policy, or asks for a policy exception record. Legal operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: legal
---

# Policy Exception Log

Record a policy exception so the company can see who accepted the risk and when it expires.

## When to use this skill

Use this skill when the user:

- policy exception
- risk acceptance
- exception log
- waiver of policy

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

This is not legal advice and does not create an attorney-client relationship. Do not invent statutes, case names, or filing deadlines. Drafts are for qualified counsel in the relevant jurisdiction.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The policy
- The exception requested
- The business reason
- The proposed expiry

## Workflow


### 1. State the rule and the break

What the policy requires and what the team wants to do instead.
### 2. Reason

The business reason in specific terms. 'We are busy' is not enough unless they truly have no other reason, in which case say that.
### 3. Risk

What bad outcome the policy was meant to prevent, in plain language.
### 4. Compensating step

What they will do meanwhile, and how someone will check.
### 5. Expiry and owner

An exception without an end date is a silent policy change. Name the acceptor.
### 6. No retroactive cover

Do not backdate an exception to hide something that already happened. Record the real dates.

## Output

Deliver a **policy exception record**.

- Purpose of this policy exception record, in two sentences.
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

Elena Voss, operations lead at Northline Studio in Calgary, needs a policy exception record by 30 September 2026. A team wants to skip a vendor security review for a tool they already bought.

### Example data

```text
From: Elena Voss, operations lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to skip a vendor security review for a tool they already bought.

name: Lumen Ledger, word mark, no logo
goods: bookkeeping software for independent shops
already checked: lumenledger.com open on 12 Sep 2026
register search: not in the file
```

### Example outcome

**Policy exception record**
To: Elena Voss, operations lead, Northline Studio
Date: 14 September 2026

**Decision**
An exception record with the skipped step, a short compensating review, a real expiry, and no backdating.

**From the file**
- name: Lumen Ledger, word mark, no logo
- goods: bookkeeping software for independent shops
- already checked: lumenledger.com open on 12 Sep 2026
- register search: not in the file

Nothing in this draft was added from outside that file.
Next: Elena Voss by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A permanent exception with no owner.
- Backdating.
- Logging an exception for conduct the user describes as deceptive.

## Related skills

- `security-exception`
- `policy-writer`
- `vendor-security-review`
