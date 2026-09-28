# Skill Library Trust Review

`skill-library-trust-review`

## What this is for

Review a skill or a skill repository for signs it is unsafe, deceptive, or pretending to be an official product.

## Scenario

Yasir Jilani, author at Practice Skills in Airdrie, needs a trust review by 30 September 2026. An installer asks the user to run a remote script and paste an API key to 'activate' free skills.

## Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

An installer asks the user to run a remote script and paste an API key to 'activate' free skills.

folder: one SKILL.md
description: says when to use it
network: none
author: Yasir Jilani
```

## Example outcome

**Trust review**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Names the remote script and the key request.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| folder | one SKILL.md | Needs confirmation |
| description | says when to use it | Carried into the draft |
| network | none | Carried into the draft |
| author | Yasir Jilani | Needs confirmation |

**How this draft was built**

**1. Prefer an installer that copies local files and does not pipe a remote script to a shell**

**2. Check scripts for network calls, obfuscation, and credential prompts**

**3. Descriptions should say what the skill does. Hidden instructions are a finding**

**4. Official-looking branding without a clear independent-author statement is a finding**

**5. A repository that promises guaranteed income, token claims, or wallet connections is out of scope for this library and should be treated as untrusted**

**Deliberately not done**
- A fake certification.
- Ignoring a curl-pipe installer.
- Treating a logo as proof of affiliation.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Yasir Jilani by 30 September 2026. This is a draft, not a sign-off.
