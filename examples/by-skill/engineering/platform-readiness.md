# Platform Readiness

`platform-readiness`

## What this is for

Review whether a platform or internal tool is ready for other teams to depend on.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a platform readiness review by 30 September 2026. A platform team wants every service to migrate next month, and the quickstart is a stub.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A platform team wants every service to migrate next month, and the quickstart is a stub.

The users inside the company: Checkout service, recorded 14 September 2026. No supporting file attached
The promised interface: none written down beyond the ask
Support model: Invoice job, last reviewed 14 September 2026. No owner named since
Docs and SLOs they claim: the draft sentence is broader than the note
```

## Example outcome

**Platform readiness review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the mandate, names the quickstart gap, and recommends one adopting team.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The users inside the company | Checkout service, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The promised interface | none written down beyond the ask | Carried into the draft |
| Support model | Invoice job, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Docs and SLOs they claim | the draft sentence is broader than the note | Needs confirmation |

**How this draft was built**

**1. User**  
The internal team and the job they will do on the platform.

**2. Interface**  
The stable contract. If every consumer forks the internals, it is not ready.

**3. Operability**  
On-call, migration path, and a stated limit. Do not invent an SLO.

**4. Docs**  
A new team can complete the golden path from the docs the user has. Gaps are the finding.

**5. Support**  
Who answers in the first month, and what is not supported.

**Deliberately not done**
- A company-wide mandate with no docs.
- An invented uptime promise.
- No owner for questions.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
