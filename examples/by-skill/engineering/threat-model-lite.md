# Lightweight Threat Model

`threat-model-lite`

## What this is for

Sketch a defensive threat model for a feature: assets, actors, abuses, and controls. No exploit steps.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a threat model note by 30 September 2026. A file-sharing feature has no answer for who can access a link.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A file-sharing feature has no answer for who can access a link.

The feature and its assets: Checkout service, recorded 14 September 2026. No supporting file attached
Actors: Aisha Rahman plus two others named in the thread. No distribution list attached
Existing controls: their one-page rule dated 2 Mar 2026. No exception log since
Data sensitivity they described: Checkout service. Partly documented: the what is written down, the who is not
```

## Example outcome

**Threat model note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Lists unauthorized access as a gap, recommends an access control and audit event, and includes no exploit procedure.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The feature and its assets | Checkout service, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Actors | Aisha Rahman plus two others named in the thread. No distribution list attached | Carried into the draft |
| Existing controls | their one-page rule dated 2 Mar 2026. No exception log since | Carried into the draft |
| Data sensitivity they described | Checkout service. Partly documented: the what is written down, the who is not | Needs confirmation |

**How this draft was built**

**1. Assets**  
What must be protected: credentials, personal data, money, or availability, as they described.

**2. Actors**  
Users, admins, and unauthenticated callers. Do not build a persona of a criminal how-to.

**3. Abuses**  
What could go wrong in plain language, such as unauthorized access or tampering. No payloads, bypasses, or step-by-step intrusion.

**4. Controls**  
Preventive and detective controls they can implement. Prefer known controls over novel tricks.

**5. Gaps**  
The abuse with no control. That is the work list.

**Deliberately not done**
- Exploit steps or payloads.
- A model with no assets.
- Claiming the feature is secure because the note exists.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
