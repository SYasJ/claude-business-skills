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
Fieldnote · 14 September 2026

A hold until the migration owner is named and the rollback is written, with no secret values added.

- [x] The intended scope — in the file. this decision only
- [x] Migrations — in the file. Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.
- [x] Monitoring — in the file. Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.
- [ ] Rollback — open. Checkout service. Aisha Rahman noted it on 14 September 2026. No second file for this line.

Next action: Aisha Rahman closes the open items before 30 September 2026. Do not mark the pack done while a box is open.
