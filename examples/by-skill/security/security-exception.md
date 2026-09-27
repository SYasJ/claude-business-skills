# Security Exception

`security-exception`

## What this is for

Record a security exception with an owner, an expiry, and a compensating control.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a security exception record by 30 September 2026. A team wants to skip MFA forever because a vendor integration is inconvenient.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to skip MFA forever because a vendor integration is inconvenient.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Security exception record**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
A time-boxed exception only if a compensating control exists, otherwise a refusal of the permanent waiver.

**From the file**
- policy: the one they have
- report in the folder: none
- control named: only if it is in the policy
- owner: engineering lead

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
