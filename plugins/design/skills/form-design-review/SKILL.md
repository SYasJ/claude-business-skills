---
name: form-design-review
description: "Review a form for necessary fields, error recovery, and an honest submit. Use when the user mentions form review, form design, checkout form, signup form, or asks for a form review. Design skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: design
---

# Form Design Review

Review a form for necessary fields, error recovery, and an honest submit.

## When to use this skill

Use this skill when the user:

- form review
- form design
- checkout form
- signup form

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Design critique improves the work. Do not copy a third party's branded assets. Accessibility is part of done, not a later pass to skip.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The purpose of the form
- Fields
- Error states
- What submit commits the user to

## Workflow


### 1. Step 1

Cut fields that do not serve the purpose.
### 2. Step 2

Mark required fields and say why.
### 3. Step 3

Specify errors that tell the user how to fix the input.
### 4. State the commitment at submit

pay, publish, or send.
### 5. Step 5

Do not ask for secrets that do not belong, such as a password to 'confirm identity' by email reply.
### 6. Step 6

Mobile and keyboard paths are part of the review if they described those users.

## Output

Deliver a **form review**.

- Purpose of this form review, in two sentences.
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

Lena Ortiz, design lead at Fieldnote in Edmonton, needs a form review by 30 September 2026. A contact form requires a social security number.

### Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A contact form requires a social security number.

screens: 8, dated 10 Sep 2026
job: the task in the ask
accessibility pass: not done
assets: theirs only
```

### Example outcome

**Form review**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the number, states the real purpose, and specifies a useful error.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| screens | 8, dated 10 Sep 2026 | Needs confirmation |
| job | the task in the ask | Carried into the draft |
| accessibility pass | not done | Carried into the draft |
| assets | theirs only | Needs confirmation |

**How this draft was built**

**1. Cut fields that do not serve the purpose**

**2. Mark required fields and say why**

**3. Specify errors that tell the user how to fix the input**

**4. State the commitment at submit**  
pay, publish, or send.

**5. Do not ask for secrets that do not belong, such as a password to 'confirm identity' by email reply**

**Deliberately not done**
- Extra sensitive fields.
- A submit that hides a charge.
- Errors that only say invalid.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- Extra sensitive fields
- A submit that hides a charge
- Errors that only say invalid

## Related skills

- `privacy-by-design`
- `ux-writing`
