# Launch Readiness

`launch-readiness`

## What this is for

Run a launch-readiness review that checks support, measurement, rollback, and the promise.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a launch readiness review by 30 September 2026. Product wants to announce automation that still requires a manual file from support.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Product wants to announce automation that still requires a manual file from support.

What will be announced: Usage limit warning, last reviewed 14 September 2026. No owner named since
Support and docs status: Trial day-3 email, last reviewed 14 September 2026. No owner named since
Measurement: not defined beyond plan 120 and actual 85
Rollback path: Trial day-3 email, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Launch readiness review**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Tells the truth about the manual step.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| What will be announced | Usage limit warning, last reviewed 14 September 2026. No owner named since | Needs confirmation |
| Support and docs status | Trial day-3 email, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Measurement | not defined beyond plan 120 and actual 85 | Carried into the draft |
| Rollback path | Trial day-3 email, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Promise check**  
The announcement matches what the build does. Cut the rest.

**2. Support**  
Agents have an FAQ and a known issue list. No launch to a blind support team.

**3. Measurement**  
The event that tells you the launch worked is instrumented, or the gap is explicit.

**4. Rollback**  
Who can stop the launch, and how customers are told if you do.

**5. Legal and claims**  
Unapproved claims block the public line, not the internal note.

**Deliberately not done**
- A launch checklist that ignores support.
- Announcing unshipped scope.
- No one empowered to hold.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
