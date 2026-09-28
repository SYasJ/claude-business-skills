---
name: spreadsheet-model-review
description: "Review a spreadsheet model for structure, formula errors, and hard-coded values that should be inputs. Use when the user mentions spreadsheet review, excel review, check my model, formula audit, or asks for a spreadsheet review. Productivity skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: productivity
---

# Spreadsheet Model Review

Review a spreadsheet model for structure, formula errors, and hard-coded values that should be inputs.

## When to use this skill

Use this skill when the user:

- spreadsheet review
- excel review
- check my model
- formula audit
- spreadsheet audit

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Productivity systems serve the person's actual constraints. Do not recommend surveillance of colleagues or hidden monitoring.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The file or a paste of the key formulas
- The purpose of the model
- Outputs that matter
- Known errors or warnings

## Workflow


### 1. Step 1

Start from the outputs. Check that they trace back to assumptions, not to manually typed numbers buried in cells.
### 2. Step 2

Flag hard-coded values in formula cells. Those belong in an input section.
### 3. Step 3

Identify circular references and error values. Name the cell and the formula, not just the problem.
### 4. Step 4

Check cross-sheet references. A link to a renamed or moved sheet silently returns zero.
### 5. Step 5

Review error-handling. Divisions that can return a zero denominator need an IFERROR or an IF guard.
### 6. Step 6

Propose one structural change at a time. A model rebuilt all at once becomes untestable.

## Output

Deliver a **spreadsheet review**.

- Purpose of this spreadsheet review, in two sentences.
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

Mara Chen, founder at Northline Studio in Calgary, needs a spreadsheet review by 30 September 2026. A budget model has revenue hard-coded in 47 cells, so changing the assumption means 47 edits.

### Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A budget model has revenue hard-coded in 47 cells, so changing the assumption means 47 edits.

week: 14 Sep 2026
calendar: the meetings they listed
dissent: kept if it was said
monitoring: not recommended
```

### Example outcome

**Spreadsheet review**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026

**Decision**
Identifies the 47 cells, proposes a single input cell with references, and lists the other structural risks.

**From the file**
- week: 14 Sep 2026
- calendar: the meetings they listed
- dissent: kept if it was said
- monitoring: not recommended

Nothing in this draft was added from outside that file.
Next: Mara Chen by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Rewriting the model structure without being asked
- Guessing what a formula is supposed to do
- Proposing a new tool when the spreadsheet works

## Related skills

- `data-quality-check`
