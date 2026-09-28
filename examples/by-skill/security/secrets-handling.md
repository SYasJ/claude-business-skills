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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Do not repeat the key, tells them to rotate it, and describes a store reference.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| policy | the one they have | Needs confirmation |
| report in the folder | none | Carried into the draft |
| control named | only if it is in the policy | Carried into the draft |
| owner | engineering lead | Needs confirmation |

**How this draft was built**

**1. Tell them to revoke or rotate the exposed secret. Do not ask them to paste the secret**

**2. Search guidance is about locations they own**  
repo, CI logs, tickets. Do not widen into unauthorized systems.

**3. Replace the secret with a reference to a secret store. Name the pattern, not a new secret value**

**4. Reduce who can read it**

**5. Set a rotation reminder appropriate to their policy**

**Deliberately not done**
- Asking them to paste a live secret.
- Hardcoding a replacement in the repo.
- Printing the secret back in a summary.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
