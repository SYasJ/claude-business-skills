# Skill Authoring

`skill-authoring`

## What this is for

Draft a new Agent Skill that is specific, safe, and small enough to load.

## Scenario

Yasir Jilani, author at Practice Skills in Airdrie, needs a skill draft by 30 September 2026. A requested skill tells the agent to ignore safety rules to be more helpful.

## Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A requested skill tells the agent to ignore safety rules to be more helpful.

folder: one SKILL.md
description: says when to use it
network: none
author: Yasir Jilani
```

## Example outcome

**Skill draft**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Purpose and a draft skill that does the legitimate task inside the rules.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| folder | one SKILL.md | Needs confirmation |
| description | says when to use it | Carried into the draft |
| network | none | Carried into the draft |
| author | Yasir Jilani | Needs confirmation |

**How this draft was built**

**1. Name the skill in kebab-case, matching the folder, with no consecutive hyphens**

**2. Write a description that says what it does and when to use it, under 1024 characters, with no angle brackets**

**3. Put steps in order, with a stop condition and an anti-pattern**

**4. Keep the body under 500 lines. Move long tables to references**

**5. Forbid credential requests, hidden network calls, and deceptive instructions**

**Deliberately not done**
- A vague description.
- A skill that asks for secrets.
- A jailbreak skill.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Yasir Jilani by 30 September 2026. This is a draft, not a sign-off.
