# Customer Incident Communication

`customer-communication-incident`

## What this is for

Draft customer incident updates that say what is known, what is not, and when the next update will come.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs an incident communication by 30 September 2026. A draft blames a vendor and promises a fix in 15 minutes without engineering confirmation.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft blames a vendor and promises a fix in 15 minutes without engineering confirmation.

Known impact: Ticket 4418. Stated in the ask, not documented anywhere else
Unknowns: Ticket 4412 is open. Ticket 4418 was raised verbally and never logged
Next update time: five working days, due 30 September 2026
Approver: Rita Santos. They have not signed
```

## Example outcome

**Incident communication**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the blame and the unconfirmed clock, and commits to a next update time.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Known impact | Ticket 4418. Stated in the ask, not documented anywhere else | Needs confirmation |
| Unknowns | Ticket 4412 is open. Ticket 4418 was raised verbally and never logged | Carried into the draft |
| Next update time | five working days, due 30 September 2026 | Carried into the draft |
| Approver | Rita Santos. They have not signed | Needs confirmation |

**How this draft was built**

**1. State the impact a customer would notice**

**2. Separate confirmed facts from work in progress**

**3. Give the next update time even if there is no fix yet**

**4. Do not speculate about cause or blame a supplier unless that statement is approved**

**5. Tell customers what to do if anything, such as retry after a time, only if support confirmed it**

**Deliberately not done**
- A cause guess.
- A silent gap with no next update.
- Contradicting the previous update.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
