# Public Meeting Minutes

`public-meeting-minutes`

## What this is for

Draft minutes of a public meeting that record motions, votes, and conflicts.

## Scenario

Pat Nguyen, clerk at Town of Airdrie in Airdrie, needs a public minutes by 30 September 2026. Minutes say a motion passed unanimously though a dissent was recorded.

## Example data

```text
From: Pat Nguyen, clerk
Organization: Town of Airdrie, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

Minutes say a motion passed unanimously though a dissent was recorded.

record: the agenda or request
vote: not implied if it has not happened
names: public record only
deadline: the posted one
```

## Example outcome

**Public minutes**
To: Pat Nguyen, clerk, Town of Airdrie
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Minutes that include the dissent and wait for the clerk's approval.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| record | the agenda or request | Needs confirmation |
| vote | not implied if it has not happened | Carried into the draft |
| names | public record only | Carried into the draft |
| deadline | the posted one | Needs confirmation |

**How this draft was built**

**1. Record motions and votes as given**

**2. Note declared conflicts**

**3. Do not invent attendance or a vote**

**4. Summarize discussion without caricature**

**5. Mark the draft for the clerk or chair to approve**

**Deliberately not done**
- An invented vote.
- A missing declared conflict.
- Color commentary.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Pat Nguyen by 30 September 2026. This is a draft, not a sign-off.
