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

The change description: requested 14 September 2026. Not yet approved
Auth and data paths: Access review Q3 and one other, both unconfirmed as of 14 September 2026
How secrets are handled: Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since
Threats they are worried about: Endpoint patch ring 2. Partly documented: the what is written down, the who is not
```

## Example outcome

**Secure code review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Requires the log removed, the token rotated, and no token reprinted in the comment.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The change description | requested 14 September 2026. Not yet approved | Needs confirmation |
| Auth and data paths | Access review Q3 and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| How secrets are handled | Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Threats they are worried about | Endpoint patch ring 2. Partly documented: the what is written down, the who is not | Needs confirmation |

**How this draft was built**

**1. Check authentication and authorization on the new path. Missing checks are a blocking finding**

**2. Look for secrets, tokens, or keys in the diff. Tell them to remove and rotate. Do not copy the secret into the review**

**3. Check input handling at trust boundaries in general terms**  
validate, encode, and parameterize. Do not provide payloads.

**4. Review logging to ensure secrets and personal data are not written**

**5. Ask for a regression test of the denied path**

**Deliberately not done**
- Payloads or proof-of-concept exploits.
- Repeating a live secret.
- Approving a missing authorization check.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
