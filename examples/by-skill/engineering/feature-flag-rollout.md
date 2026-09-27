# Feature Flag Rollout

`feature-flag-rollout`

## What this is for

Plan a feature-flag rollout with an audience, a kill switch, and a cleanup date.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a rollout plan by 30 September 2026. A team wants to enable a payments change for everyone and has no way to disable it without a deploy.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to enable a payments change for everyone and has no way to disable it without a deploy.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Rollout plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Starts with a small audience and names a disable path that does not require a heroic deploy.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
