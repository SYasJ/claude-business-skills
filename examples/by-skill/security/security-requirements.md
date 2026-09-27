# Security Requirements

`security-requirements`

## What this is for

Write defensive security requirements for a feature so engineering can build controls without exploit instructions.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a security requirements by 30 September 2026. A new export feature has no statement about who may export customer data.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A new export feature has no statement about who may export customer data.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Security requirements**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Requirements for authorization, audit, and a safe allow-and-deny test, with no attack procedure.

**From the file**
- policy: the one they have
- report in the folder: none
- control named: only if it is in the policy
- owner: engineering lead

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
