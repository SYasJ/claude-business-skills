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

The packet they require: Tuesday clinic, recorded 14 September 2026. No supporting file attached
Who sends and receives: Dr. Helen Cho, clinic director
Clocks they use: Thursday clinic. Stated in the ask, not documented anywhere else
What patients are told: Referral desk, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Referral workflow**
To: Dr. Helen Cho, clinic director, Cedar Clinic
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A workflow with a packet, an owner, and an aging check, and no medical-necessity ruling.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The packet they require | Tuesday clinic, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Who sends and receives | Dr. Helen Cho, clinic director | Carried into the draft |
| Clocks they use | Thursday clinic. Stated in the ask, not documented anywhere else | Carried into the draft |
| What patients are told | Referral desk, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Define a complete packet from their list. Do not invent clinical requirements**

**2. Name the owner of each handoff**

**3. State what the patient is told and when**

**4. Track a stalled referral as an operations issue with an aging rule**

**5. Close the loop back to the sender when they say that is required**

**Deliberately not done**
- A referral with no owner.
- Invented medical-necessity rulings.
- Patients left without a status.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Dr. Helen Cho by 30 September 2026. This is a draft, not a sign-off.
