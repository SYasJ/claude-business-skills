# Incident Response Coordination

`incident-response-coord`

## What this is for

Coordinate a security incident response with roles, containment, and communications that do not speculate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an incident coordination note by 30 September 2026. A chat is about to tell customers data was stolen before anyone has confirmed access.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A chat is about to tell customers data was stolen before anyone has confirmed access.

What is known: Phishing report 4412, last reviewed 14 September 2026. No owner named since
Systems affected: the one named in the ask. Version and owner not recorded
Who is in charge: Aisha Rahman, engineering lead
Legal or regulatory contacts they already have: Phishing report 4412 and one other, both unconfirmed as of 14 September 2026
```

## Example outcome

**Incident coordination note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Holds the claim, assigns a lead, and forbids log destruction.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What is known | Phishing report 4412, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| Systems affected | the one named in the ask. Version and owner not recorded | Carried into the draft |
| Who is in charge | Aisha Rahman, engineering lead | Carried into the draft |
| Legal or regulatory contacts they already have | Phishing report 4412 and one other, both unconfirmed as of 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Separate facts from theories. Write both, labeled**

**2. Assign roles**  
lead, communications, and a note taker. Everyone else stays available, not in the room.

**3. Containment actions must be authorized and reversible where possible. Do not include intrusion or retaliation steps**

**4. Preserve evidence. Do not tell anyone to wipe logs to hide the event**

**5. Communications**  
tell affected parties only what counsel or the incident lead has approved as known.

**Deliberately not done**
- Wiping logs.
- Speculative customer claims.
- Retaliation or hacking back.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
