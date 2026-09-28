# Feature Flag Rollout

`feature-flag-rollout`

## What this is for

Plan a feature-flag rollout with an audience, a kill switch, and a cleanup date.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a rollout plan by 30 September 2026. A team wants to enable a payments change for everyone and has no way to disable it without a deploy.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to enable a payments change for everyone and has no way to disable it without a deploy.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Rollout plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Starts with a small audience and names a disable path that does not require a heroic deploy.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Audience**  
Who sees it first, and why. A 100 percent launch is a choice, not the default, when risk is unclear.

**2. Kill switch**  
Who can turn it off, and how long that takes. A flag with no kill path is a config liability.

**3. Watch**  
The user-facing signal that means stop. Use their metrics. Do not invent a dashboard.

**4. Stages**  
The next audience and the evidence required to expand.

**5. Cleanup**  
The date the flag is removed if the launch succeeds or fails. Permanent flags are debt.

**Deliberately not done**
- A flag nobody can turn off.
- No cleanup date.
- Expanding while the watch signal is red.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
