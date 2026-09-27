# Backup and Restore Test

`backup-and-restore-test`

## What this is for

Plan a restore test that proves a backup can be recovered, not merely that a backup job ran.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a restore test plan by 30 September 2026. The team says backups are fine because the nightly job is green, and nobody has restored one.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The team says backups are fine because the nightly job is green, and nobody has restored one.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Restore test plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
A restore test into a non-production target, with a recorded time and a ban on production overwrite.

**From the file**
- policy: the one they have
- report in the folder: none
- control named: only if it is in the policy
- owner: engineering lead

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
