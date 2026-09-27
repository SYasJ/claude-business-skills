---
name: deal-desk-review
description: "Review a nonstandard deal for margin, precedent, and delivery risk before anyone signs. Use when the user mentions deal desk, nonstandard terms, discount approval, special deal review, or asks for a deal desk note. Sales skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: sales
---

# Deal Desk Review

Review a nonstandard deal for margin, precedent, and delivery risk before anyone signs.

## When to use this skill

Use this skill when the user:

- deal desk
- nonstandard terms
- discount approval
- special deal review

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Sell honestly. Do not invent customer proof, discounts, or competitor facts. Do not write deceptive, phishing, or high-pressure scripts.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The asked discount or term
- Margin math the user can show
- Delivery implications
- Precedent they worry about

## Workflow


### 1. Restate the ask

What is nonstandard, in one sentence.
### 2. Margin

Compute from their costs and price. If cost is missing, the review is incomplete. Do not invent a cost.
### 3. Delivery

Can the team deliver the promised start date and scope. A yes from sales is not a yes from delivery.
### 4. Precedent

Who else will ask for the same term if this is signed. Write that consequence.
### 5. Give-get

What the company gets for the concession.
### 6. Decision

Approve, approve with conditions, or decline. Name the approver role the user said has authority. Do not invent authority.

## Output

Deliver a **deal desk note**.

- Purpose of this deal desk note, in two sentences.
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

Samir Qureshi, account executive at Fieldnote in Edmonton, needs a deal desk note by 30 September 2026. Sales wants a custom integration included free to win a logo, and delivery has not estimated it.

### Example data

```text
From: Samir Qureshi, account executive
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales wants a custom integration included free to win a logo, and delivery has not estimated it.

account: Harbor Goods
last meeting: 9 Sep 2026, no dated next step
proof: one email
discount asked: 15 percent, not approved
```

### Example outcome

**Deal desk note**
To: Samir Qureshi, account executive, Fieldnote
Date: 14 September 2026

**Decision**
Conditions any approval on a delivery estimate and names the precedent risk of free custom work.

**From the file**
- account: Harbor Goods
- last meeting: 9 Sep 2026, no dated next step
- proof: one email
- discount asked: 15 percent, not approved

Nothing in this draft was added from outside that file.
Next: Samir Qureshi by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Approving a discount with no margin math.
- Ignoring delivery capacity.
- An approval that pretends not to set a precedent.

## Related skills

- `pricing-negotiation`
- `proposal-writer`
