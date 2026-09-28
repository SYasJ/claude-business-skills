# API Design Review

`api-design-review`

## What this is for

Review an API for consistency, failure behavior, and compatibility, without turning the review into a style hobby.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an API review by 30 September 2026. A new billing endpoint has no idempotency key and retries would create a second charge.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A new billing endpoint has no idempotency key and retries would create a second charge.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Api review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks on the double-charge retry and refuses any suggestion to skip authentication.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Consumer job**  
What the caller is trying to do. Endpoints that do not serve a job are a finding.

**2. Contract**  
Names, types, and error shapes. Inconsistent errors are a finding if their standard exists.

**3. Failure**  
What the client should do on timeout, conflict, and unauthorized. Silence is a gap.

**4. Compatibility**  
What breaks existing callers. A breaking change needs a version or a migration note.

**5. Auth**  
Which identity is required. Do not suggest making an endpoint public to simplify a client.

**Deliberately not done**
- A public endpoint suggested for convenience.
- A breaking change with no migration.
- No error behavior.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
