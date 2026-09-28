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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A restore test into a non-production target, with a recorded time and a ban on production overwrite.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| policy | the one they have | Needs confirmation |
| report in the folder | none | Carried into the draft |
| control named | only if it is in the policy | Carried into the draft |
| owner | engineering lead | Needs confirmation |

**How this draft was built**

**1. Define the asset and the acceptable loss of data and time, in their words**

**2. A successful backup job is not evidence of a restorable backup. Plan an actual restore into a safe environment**

**3. The test environment must not overwrite production. Say that explicitly**

**4. Record what was restored, how long it took, and what failed**

**5. Name the owner who fixes a failed restore**

**Deliberately not done**
- Equating a green backup job with recoverability.
- A test that can overwrite production.
- Credentials in the plan.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
