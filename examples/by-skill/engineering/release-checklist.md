# Release Checklist

`release-checklist`

## What this is for

Run a release checklist that confirms scope, migrations, monitoring, and rollback before tagging.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a release checklist by 30 September 2026. A release includes a migration that the on-call has not seen, and the checklist says LGTM.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A release includes a migration that the on-call has not seen, and the checklist says LGTM.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Release checklist**
Fieldnote · 14 September 2026 · Due 30 September 2026

**Decision**
A hold until the migration owner is named and the rollback is written, with no secret values added.

**Checklist**

- [x] **The intended scope** — this decision only  
      Evidenced in the file
- [x] **Migrations** — Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.  
      Evidenced in the file
- [x] **Monitoring** — Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.  
      Evidenced in the file
- [ ] **Rollback** — Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.  
      Open — nothing in the file closes this

**The gates this list enforces, in order**

1. Scope
2. Migrations
3. Config and flags
4. Monitoring
5. Rollback

**Deliberately not done**
- Secret values in the checklist.
- A ship decision with no rollback.
- Scope nobody tested.

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: Aisha Rahman closes the open items before 30 September 2026.
