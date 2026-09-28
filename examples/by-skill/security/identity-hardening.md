# Identity Hardening

`identity-hardening`

## What this is for

Plan identity hardening around administrators, joiners and leavers, and phishing-resistant sign-in where they can support it.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an identity hardening plan by 30 September 2026. Contractors keep admin access for months after the contract ends.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Contractors keep admin access for months after the contract ends.

The identity provider they use: Access review Q3, recorded 14 September 2026. No supporting file attached
Who has admin: Aisha Rahman, engineering lead
Joiner and leaver process: email to Aisha Rahman. No written steps after 1 Sep 2026
Exceptions they know about: Access review Q3 is open. Endpoint patch ring 2 was raised verbally and never logged
```

## Example outcome

**Identity hardening plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Ties leaver dates to access removal and refuses any request for live codes.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The identity provider they use | Access review Q3, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Who has admin | Aisha Rahman, engineering lead | Carried into the draft |
| Joiner and leaver process | email to Aisha Rahman. No written steps after 1 Sep 2026 | Carried into the draft |
| Exceptions they know about | Access review Q3 is open. Endpoint patch ring 2 was raised verbally and never logged | Needs confirmation |

**How this draft was built**

**1. Start with admins and remote access, not with a poster about passwords**

**2. Map joiner, mover, and leaver to access changes. A leaver delay is a finding**

**3. Recommend phishing-resistant factors if their provider supports them, as a question, not a product pitch**

**4. Shared accounts are replaced or given a named owner and a review date**

**5. Exceptions get an expiry**

**Deliberately not done**
- Asking for one-time codes.
- A plan that ignores leavers.
- Permanent exceptions.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
