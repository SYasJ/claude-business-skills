# Code Review Standard

`code-review-standard`

## What this is for

Review a change for correctness, risk, and clarity, and write comments a teammate can act on.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a code review by 30 September 2026. A PR changes an authorization check and has no test for the denied path.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A PR changes an authorization check and has no test for the denied path.

The change and its stated intent: requested 14 September 2026. Not yet approved
Risky areas: data, auth, migrations: data: in the file; auth: not in the file; migrations: open
Team conventions the user pointed to: two people on shift, one off
```

## Example outcome

**Code review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Blocks on the missing denied-path test and does not suggest skipping the check.

**From the file**
- The change and its stated intent: requested 14 September 2026. Not yet approved
- Risky areas: data, auth, migrations: data: in the file; auth: not in the file; migrations: open
- Team conventions the user pointed to: two people on shift, one off

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
