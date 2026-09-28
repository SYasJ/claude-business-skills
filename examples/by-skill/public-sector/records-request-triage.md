# Records Request Triage

`records-request-triage`

## What this is for

Triage a records request for scope, search, and exemptions their officer must decide.

## Scenario

Pat Nguyen, clerk at Town of Airdrie in Airdrie, needs a records request triage by 30 September 2026. A manager wants to delete drafts because a request might cover them.

## Example data

```text
From: Pat Nguyen, clerk
Organization: Town of Airdrie, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A manager wants to delete drafts because a request might cover them.

record: the agenda or request
vote: not implied if it has not happened
names: public record only
deadline: the posted one
```

## Example outcome

**Records request triage**
To: Pat Nguyen, clerk, Town of Airdrie
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Forbids deletion and lists locations for the officer to decide.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| record | the agenda or request | Needs confirmation |
| vote | not implied if it has not happened | Carried into the draft |
| names | public record only | Carried into the draft |
| deadline | the posted one | Needs confirmation |

**How this draft was built**

**1. Restate the scope. Ask one clarifying question if it is too broad to search**

**2. List likely locations. Do not search systems the user did not authorize**

**3. Flag exemptions as questions for the officer. Do not withhold records on a homemade theory**

**4. Note personal data that may need redaction by the officer**

**5. Do not destroy records because a request arrived**

**Deliberately not done**
- Destroying records after a request.
- A homemade exemption ruling.
- An invented legal deadline.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Pat Nguyen by 30 September 2026. This is a draft, not a sign-off.
