# CI/CD Review

`ci-cd-review`

## What this is for

Review a delivery pipeline for repeatability, secrets handling, and a safe production gate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a pipeline review by 30 September 2026. A pipeline file contains a copied cloud key and deploys even when tests fail.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A pipeline file contains a copied cloud key and deploys even when tests fail.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Pipeline review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Requires the key to be removed and rotated, and blocks deploy-on-red. Do not repeat the key.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
