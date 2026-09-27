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
Date: 14 September 2026

**Decision**
Blocks on the double-charge retry and refuses any suggestion to skip authentication.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
