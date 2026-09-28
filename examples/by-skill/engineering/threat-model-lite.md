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

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
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
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

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
