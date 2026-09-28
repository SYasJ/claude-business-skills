# Service Recovery

`service-recovery`

## What this is for

Plan recovery from a service failure with a truthful apology, a fix, and a remedy inside authority.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs a recovery plan by 30 September 2026. A draft says 'everything is resolved' while the queue is still failing.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft says 'everything is resolved' while the queue is still failing.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

## Example outcome

**Recovery plan**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
States the ongoing failure, omits the fake resolution, and offers only an authorized remedy.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| ticket | 4412, 14 Sep 2026 | Needs confirmation |
| customer words | in the ticket | Carried into the draft |
| exception | not approved | Carried into the draft |
| card or password | not collected | Needs confirmation |

**How this draft was built**

**1. State the failure plainly. Do not bury it in an apology paragraph**

**2. Say what you know and what you are still checking**

**3. Describe the fix and the time, if known. Do not invent a restoration time**

**4. Offer only an authorized remedy**

**5. Tell them how to ask a follow-up question**

**Deliberately not done**
- A fake restoration time.
- An unauthorized remedy.
- An apology that hides the failure.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
