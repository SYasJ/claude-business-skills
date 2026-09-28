# Security Requirements

`security-requirements`

## What this is for

Write defensive security requirements for a feature so engineering can build controls without exploit instructions.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a security requirements by 30 September 2026. A new export feature has no statement about who may export customer data.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A new export feature has no statement about who may export customer data.

The feature and its data: Access review Q3, recorded 14 September 2026. No supporting file attached
Actors: Aisha Rahman plus two others named in the thread. No distribution list attached
Existing controls: their one-page rule dated 2 Mar 2026. No exception log since
Sensitivity the user described: Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Security requirements**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Requirements for authorization, audit, and a safe allow-and-deny test, with no attack procedure.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The feature and its data | Access review Q3, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Actors | Aisha Rahman plus two others named in the thread. No distribution list attached | Carried into the draft |
| Existing controls | their one-page rule dated 2 Mar 2026. No exception log since | Carried into the draft |
| Sensitivity the user described | Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. List assets and actors in plain language**

**2. Write requirements as observable controls**  
authenticate, authorize, log, limit, and protect data.

**3. Include failure behavior**  
deny by default, and what the user sees.

**4. Map each requirement to a test the team can run safely, such as an authorized versus unauthorized check**

**5. Do not include exploit steps, payloads, or bypass instructions**

**Deliberately not done**
- Exploit steps.
- A requirement list with no tests.
- Deferring auth with no owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
