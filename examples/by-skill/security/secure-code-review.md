# Secure Code Review

`secure-code-review`

## What this is for

Review a change for defensive security issues and request fixes, without writing an exploit.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a secure code review by 30 September 2026. A pull request logs a session token while debugging a login bug.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A pull request logs a session token while debugging a login bug.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Secure code review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Requires the log removed, the token rotated, and no token reprinted in the comment.

**From the file**
- policy: the one they have
- report in the folder: none
- control named: only if it is in the policy
- owner: engineering lead

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
