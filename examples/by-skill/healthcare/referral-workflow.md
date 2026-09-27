# Referral Workflow

`referral-workflow`

## What this is for

Map a referral workflow so the sending and receiving sides know the packet, the owner, and the clock.

## Scenario

Dr. Helen Cho, clinic director at Cedar Clinic in Red Deer, needs a referral workflow by 30 September 2026. Referrals leave the clinic and nobody knows which ones were received.

## Example data

```text
From: Dr. Helen Cho, clinic director
Organization: Cedar Clinic, Red Deer
Date: 14 September 2026
Needed by: 30 September 2026

Referrals leave the clinic and nobody knows which ones were received.

clinic: Cedar, Tuesday list
diagnosis: not in this note
roster: the one attached
advice to a patient: not written
```

## Example outcome

**Referral workflow**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026

**Decision**
A workflow with a packet, an owner, and an aging check, and no medical-necessity ruling.

**From the file**
- clinic: Cedar, Tuesday list
- diagnosis: not in this note
- roster: the one attached
- advice to a patient: not written

Nothing in this draft was added from outside that file.
Next: Dr. Helen Cho by 30 September 2026. This is not a sign-off.
