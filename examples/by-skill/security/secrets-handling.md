# Secrets Handling

`secrets-handling`

## What this is for

Review how a secret is stored and rotated, and remove it from code, tickets, and chat.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a secrets handling review by 30 September 2026. A key was committed and the user pastes it into chat asking if it looks real.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A key was committed and the user pastes it into chat asking if it looks real.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Secrets handling review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Do not repeat the key, tells them to rotate it, and describes a store reference.

**From the file**
- policy: the one they have
- report in the folder: none
- control named: only if it is in the policy
- owner: engineering lead

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
