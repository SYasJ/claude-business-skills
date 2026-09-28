# Security Exception

`security-exception`

## What this is for

Record a security exception with an owner, an expiry, and a compensating control.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a security exception record by 30 September 2026. A team wants to skip MFA forever because a vendor integration is inconvenient.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to skip MFA forever because a vendor integration is inconvenient.

The control: their one-page rule dated 2 Mar 2026. No exception log since
The reason: Access review Q3, recorded 14 September 2026. No supporting file attached
The compensating step: Access review Q3; Endpoint patch ring 2. Both unassigned as of 14 September 2026
The requested duration: Access review Q3, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Security exception record**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A time-boxed exception only if a compensating control exists, otherwise a refusal of the permanent waiver.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The control | their one-page rule dated 2 Mar 2026. No exception log since | Needs confirmation |
| The reason | Access review Q3, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The compensating step | Access review Q3; Endpoint patch ring 2. Both unassigned as of 14 September 2026 | Carried into the draft |
| The requested duration | Access review Q3, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. State the control and the gap in one sentence**

**2. Require a business reason more specific than urgency, or record that the reason is weak**

**3. Name a compensating control that reduces the same harm**

**4. Set an owner and an expiry. No expiry, no exception**

**5. Note what will be true at review time**

**Deliberately not done**
- A permanent waiver.
- An exception used to hide an incident.
- No compensating control.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
