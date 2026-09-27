---
name: bank-reconciliation
description: "Reconcile book to bank and leave a list of items a human must clear, with no plugs. Use when the user mentions bank reconciliation, book to bank, unreconciled cash, bank rec, or asks for a bank reconciliation. Accounting skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: accounting
---

# Bank Reconciliation

Reconcile book to bank and leave a list of items a human must clear, with no plugs.

## When to use this skill

Use this skill when the user:

- bank reconciliation
- book to bank
- unreconciled cash
- bank rec

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

This is not an audit opinion, compilation, or tax advice. Do not invent accounting standards. Use the policy, framework, and chart of accounts the organization actually follows.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- Statement ending balance and date
- Book balance for the same account
- Outstanding checks and deposits
- Items the user cannot explain

## Workflow


### 1. Match the account and the date

A reconciliation of the wrong account or the wrong day is not a near miss. Stop and correct the frame.
### 2. Compute the difference

Statement balance to book balance, then list outstanding items the user supplied. Show the remaining unexplained amount in the open.
### 3. Classify leftovers

Timing, error, or unknown. Unknown is acceptable. A forced explanation is not.
### 4. Look for duplicates and old items

Outstanding items older than the user's threshold need a decision, not another month of carry-forward.
### 5. Propose entries only as drafts

The accountant posts. You do not declare the books updated.
### 6. No credentials

Do not ask for online banking passwords or one-time codes. Work from exports the user chooses to share.

## Output

Deliver a **bank reconciliation**.

- Purpose of this bank reconciliation, in two sentences.
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

Priya Shah, controller at Northline Studio in Calgary, needs a bank reconciliation by 30 September 2026. The operating account reconciliation has an unexplained difference and three deposits in transit older than a month.

### Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The operating account reconciliation has an unexplained difference and three deposits in transit older than a month.

period: August 2026
no preparer: undeposited funds, sales tax payable
cash recs: one inbox, not the shared folder
reviewer: not signed
```

### Example outcome

**Bank reconciliation**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026

**Decision**
Shows the unexplained amount, classifies the old deposits as needing a decision, and does not plug the difference.

**From the file**
- period: August 2026
- no preparer: undeposited funds, sales tax payable
- cash recs: one inbox, not the shared folder
- reviewer: not signed

Nothing in this draft was added from outside that file.
Next: Priya Shah by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A plug labeled 'other' to force a zero.
- Asking for a bank password.
- Carrying year-old outstanding items with no comment.

## Related skills

- `month-end-close`
- `treasury-policy-brief`
- `internal-controls-walkthrough`
