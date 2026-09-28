---
name: academic-integrity
description: "Plan an academic integrity conversation that is fair, specific, and not a trap. Use when the user mentions academic integrity, plagiarism conversation, cheating concern, integrity process, or asks for a integrity conversation plan. Education and training skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: education
---

# Academic Integrity Conversation

Plan an academic integrity conversation that is fair, specific, and not a trap.

## When to use this skill

Use this skill when the user:

- academic integrity
- plagiarism conversation
- cheating concern
- integrity process

## When not to use this skill

- Helping conceal misconduct
- Invented sanctions

## Professional boundary

Learning design supports the instructor. Do not complete graded work for a student or help anyone cheat. Do not invent accreditation requirements.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The concern and evidence
- The institution's process they supplied
- The student-facing next step
- Support available

## Workflow


### 1. Step 1

Stick to the evidence. Do not accuse beyond it.
### 2. Step 2

Follow the process they supplied. Do not invent a sanction.
### 3. Step 3

Tell the student the concern and how to respond, if their process allows that at this stage.
### 4. Step 4

Separate a citation skill gap from a deception concern when the evidence allows it.
### 5. Step 5

Do not help a student conceal misconduct, and do not help staff run a dishonest hearing.
### 6. Step 6

Point to support for writing skills when the issue is skill.

## Output

Deliver a **integrity conversation plan**.

- Purpose of this integrity conversation plan, in two sentences.
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

Mark Ellison, program chair at Riverbend College in Lethbridge, needs an integrity conversation plan by 30 September 2026. A teacher wants to fail a student immediately with no process because a paragraph looks similar.

### Example data

```text
From: Mark Ellison, program chair
Organization: Riverbend College, Lethbridge
Date: 14 September 2026
Needed by: 30 September 2026

A teacher wants to fail a student immediately with no process because a paragraph looks similar.

course: the one named
section: the one they teach
student submission: not written for them
due: 30 Sep 2026
```

### Example outcome

**Integrity conversation plan**
To: Mark Ellison, program chair, Riverbend College
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Follows their stated process, limits the claim to the evidence, and refuses a made-up sanction.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| course | the one named | Needs confirmation |
| section | the one they teach | Carried into the draft |
| student submission | not written for them | Carried into the draft |
| due | 30 Sep 2026 | Needs confirmation |

**How this draft was built**

**1. Stick to the evidence. Do not accuse beyond it**

**2. Follow the process they supplied. Do not invent a sanction**

**3. Tell the student the concern and how to respond, if their process allows that at this stage**

**4. Separate a citation skill gap from a deception concern when the evidence allows it**

**5. Do not help a student conceal misconduct, and do not help staff run a dishonest hearing**

**Deliberately not done**
- A sanction invented from memory.
- A trap conversation.
- Help concealing misconduct.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mark Ellison by 30 September 2026. This is a draft, not a sign-off.

## Anti-patterns

- A sanction invented from memory
- A trap conversation
- Help concealing misconduct

## Related skills

- `assessment-design`
- `feedback-on-work`
