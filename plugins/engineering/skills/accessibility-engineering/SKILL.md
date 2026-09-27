---
name: accessibility-engineering
description: "Turn an accessibility barrier into an engineering fix with a test, without claiming a conformance certificate. Use when the user mentions accessibility bug, a11y fix, keyboard trap, screen reader bug, or asks for a accessibility engineering note. Engineering skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: engineering
---

# Accessibility Engineering

Turn an accessibility barrier into an engineering fix with a test, without claiming a conformance certificate.

## When to use this skill

Use this skill when the user:

- accessibility bug
- a11y fix
- keyboard trap
- screen reader bug

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

- The barrier
- The user impact
- The code or component involved
- The team's stated target

## Workflow


### 1. Reproduce

The exact barrier, such as a keyboard trap or a missing name. Do not claim you ran an assistive technology you did not run.
### 2. Fix

The specific code or component change. Prefer the platform's accessible primitive over a custom widget.
### 3. Test

A check the team can repeat, automated where it fits and manual where it does not.
### 4. Regression

Where this should live so it does not return.
### 5. Limits

What this fix does not prove. No blanket WCAG certificate.
### 6. Priority

Blockers to completing a task outrank cosmetic contrast issues, unless their policy says otherwise.

## Output

Deliver a **accessibility engineering note**.

- Purpose of this accessibility engineering note, in two sentences.
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

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an accessibility engineering note by 30 September 2026. A modal traps keyboard focus, and the proposed fix is a README badge that says 'accessible'.

### Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A modal traps keyboard focus, and the proposed fix is a README badge that says 'accessible'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

### Example outcome

**Accessibility engineering note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Specifies the focus fix and a keyboard test, and rejects the badge as proof.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A conformance certificate from a guess.
- A custom widget when a native control would do.
- Closing the bug with no regression check.

## Related skills

- `accessibility-review`
- `test-strategy`
