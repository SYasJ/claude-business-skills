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
Tests included or missing: Status page, recorded 14 September 2026. No supporting file attached
Risky areas: data, auth, migrations: data: in the file; auth: not in the file; migrations: open
Team conventions the user pointed to: two people on shift, one off
```

## Example outcome

**Code review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks on the missing denied-path test and does not suggest skipping the check.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The change and its stated intent | requested 14 September 2026. Not yet approved | Needs confirmation |
| Tests included or missing | Status page, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Risky areas: data, auth, migrations | data: in the file; auth: not in the file; migrations: open | Carried into the draft |
| Team conventions the user pointed to | two people on shift, one off | Needs confirmation |

**How this draft was built**

**1. Intent**  
Restate what the change is for. If the description is empty, ask for it before nitpicking style.

**2. Correctness**  
Walk the main path and the failure path. Point to the line and the concrete failure.

**3. Risk**  
Call out auth, data loss, migrations, and secrets. Do not request a bypass of a security control.

**4. Tests**  
Name the missing test that would have caught the bug you see. Do not demand tests for their own sake with no risk.

**5. Comments**  
Specific, kind, and ranked. Blocking issues are separate from nits.

**Deliberately not done**
- Style nits before understanding intent.
- Approving a migration with no rollback note.
- Asking the author to disable a security check to get the diff smaller.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
