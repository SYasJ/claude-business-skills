# Ticket Quality Review

`ticket-quality-review`

## What this is for

Review support ticket quality for resolution, tone, and whether the article or product should change.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs a ticket quality review by 30 September 2026. Several tickets ask customers for their password to 'speed up' the fix.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Several tickets ask customers for their password to 'speed up' the fix.

The tickets or summaries: Ticket 4412, recorded 14 September 2026. No supporting file attached
The rubric they use: Ticket 4412, recorded 14 September 2026. No supporting file attached
Recurring issues: Ticket 4412, last reviewed 14 September 2026. No owner named since
What agents are allowed to do: Ticket 4420, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Ticket quality review**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Flag the password request as a stop-now finding and names the pattern.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The tickets or summaries | Ticket 4412, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The rubric they use | Ticket 4412, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Recurring issues | Ticket 4412, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| What agents are allowed to do | Ticket 4420, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Score against their rubric. If they have none, use resolution, accuracy, and next step, and label that as a proposal**

**2. Check that the reply answered the ask and did not invent a policy**

**3. Look for repeated issues that belong in a macro or a product fix**

**4. Note if agents are asking for secrets. That is a finding**

**5. Give coaching on the pattern, not a pile of nits**

**Deliberately not done**
- Coaching style before checking accuracy.
- Ignoring a secret request.
- A review with no pattern.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
