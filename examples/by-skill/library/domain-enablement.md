# Domain Enablement

`domain-enablement`

## What this is for

Explain which domain plugin to enable for a team role, and which skills that role should try first.

## Scenario

Yasir Jilani, author at Practice Skills in Airdrie, needs an enablement note by 30 September 2026. A finance analyst is told to enable engineering, healthcare, and security plugins on day one.

## Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A finance analyst is told to enable engineering, healthcare, and security plugins on day one.

folder: one SKILL.md
description: says when to use it
network: none
author: Yasir Jilani
```

## Example outcome

**Enablement note**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Enables finance, names three starter skills, and leaves the other plugins off.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| folder | one SKILL.md | Needs confirmation |
| description | says when to use it | Carried into the draft |
| network | none | Carried into the draft |
| author | Yasir Jilani | Needs confirmation |

**How this draft was built**

**1. Map the role to one primary domain and at most one secondary domain**

**2. Name three starter skills, not the whole domain**

**3. Warn that regulated work still needs a qualified human**

**4. Tell them not to enable offensive, deceptive, or jailbreak workflows. This library does not ship those**

**5. Note the context cost of enabling many domains**

**Deliberately not done**
- Enabling every domain for every role.
- A remote install command.
- Starter skills unrelated to the role.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Yasir Jilani by 30 September 2026. This is a draft, not a sign-off.
