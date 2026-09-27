---
name: information-architecture
description: "Recommend an information architecture from user tasks, not from the company's org chart. Use when the user mentions information architecture, site map, navigation, IA review, or asks for a IA recommendation. Design skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: design
---

# Information Architecture

Recommend an information architecture from user tasks, not from the company's org chart.

## When to use this skill

Use this skill when the user:

- information architecture
- site map
- navigation
- IA review

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

- Top tasks
- Current labels
- Evidence of confusion
- Constraints

## Workflow


### 1. Step 1

List tasks users come to finish.
### 2. Step 2

Group by those tasks, not by internal departments.
### 3. Step 3

Label in the user's words if you have them.
### 4. Step 4

Show what moves or gets cut.
### 5. Step 5

Note search versus navigation. Do not hide a bad structure behind a search box as the only plan.
### 6. Step 6

Test labels with a simple card sort or tree test plan if the stakes are high and they can run one.

## Output

Deliver a **IA recommendation**.

- Purpose of this IA recommendation, in two sentences.
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

Lena Ortiz, design lead at Fieldnote in Edmonton, needs an IA recommendation by 30 September 2026. The nav has a tab for each internal department and users cannot find billing.

### Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The nav has a tab for each internal department and users cannot find billing.

screens: 8, dated 10 Sep 2026
job: the task in the ask
accessibility pass: not done
assets: theirs only
```

### Example outcome

**Ia recommendation**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026

**Decision**
Groups billing under the task users named and demotes the org chart.

**From the file**
- screens: 8, dated 10 Sep 2026
- job: the task in the ask
- accessibility pass: not done
- assets: theirs only

Nothing in this draft was added from outside that file.
Next: Lena Ortiz by 30 September 2026. This is not a sign-off.

## Anti-patterns

- Navigation that mirrors the org chart
- A search box as the only fix
- Labels nobody outside the company uses

## Related skills

- `journey-map`
- `design-critique`
