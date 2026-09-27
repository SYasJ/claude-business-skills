---
name: ip-ownership-checklist
description: "List who is supposed to own work product across employees, contractors, and vendors, based on documents the user has. Use when the user mentions IP ownership, who owns the code, contractor IP, work product assignment, or asks for a IP ownership checklist. Legal operations skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: legal
---

# IP Ownership Checklist

List who is supposed to own work product across employees, contractors, and vendors, based on documents the user has.

## When to use this skill

Use this skill when the user:

- IP ownership
- who owns the code
- contractor IP
- work product assignment

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

- Roles involved
- Agreements they have signed, as described
- The work product at issue
- Any open-source components they mentioned

## Workflow


### 1. Inventory the creators

Employees, contractors, agencies, and founders. Ownership follows documents, not assumptions about who paid.
### 2. Match agreements

For each creator type, note whether the user has an assignment or only a handshake. A missing document is the finding.
### 3. Scope of assignment

What the document says is assigned, including improvements and feedback, quoted briefly.
### 4. Third-party code

If they mentioned open source or a vendor toolkit, flag license review. Do not declare a license compatible from memory.
### 5. Gaps

Work done before an agreement, or by a friend, needs a cleanup question for counsel.
### 6. No filings

This skill does not file trademarks or patents and does not estimate registrability.

## Output

Deliver a **IP ownership checklist**.

- Purpose of this IP ownership checklist, in two sentences.
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

Elena Voss, operations lead at Northline Studio in Calgary, needs an IP ownership checklist by 30 September 2026. A contractor built the first version before any agreement existed, and the company is raising money.

### Example data

```text
From: Elena Voss, operations lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A contractor built the first version before any agreement existed, and the company is raising money.

name: Lumen Ledger, word mark, no logo
goods: bookkeeping software for independent shops
already checked: lumenledger.com open on 12 Sep 2026
register search: not in the file
```

### Example outcome

**Ip ownership checklist**
Northline Studio · 14 September 2026

Marks that work as an open ownership gap and lists the document counsel would need to review.

- [x] Roles involved — in the file. Harbor renewal. Elena Voss noted it on 14 September 2026. No second file for this line.
- [x] Agreements they have signed, as described — in the file. Harbor renewal. Elena Voss noted it on 14 September 2026. No second file for this line.
- [x] The work product at issue — in the file. Harbor renewal. Elena Voss noted it on 14 September 2026. No second file for this line.
- [ ] Any open-source components they mentioned — open. note from Elena Voss, 14 September 2026. No outside report

Next action: Elena Voss closes the open items before 30 September 2026. Do not mark the pack done while a box is open.

## Anti-patterns

- Assuming payment equals ownership.
- A fake patentability opinion.
- Ignoring pre-incorporation work.

## Related skills

- `open-source-license-review`
- `employment-agreement-review`
- `trademark-clearance-prep`
