# Dependency Upgrade

`dependency-upgrade`

## What this is for

Plan a dependency upgrade around risk, changelog, and rollback, not around a version number badge.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an upgrade plan by 30 September 2026. A bot opened a major upgrade and nobody has read the changelog.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A bot opened a major upgrade and nobody has read the changelog.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Upgrade plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Blocks the merge until breaking changes are read and a rollback is named.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
