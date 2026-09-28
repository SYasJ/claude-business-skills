# Manufacturing Change Control

`change-control-manufacturing`

## What this is for

Review a manufacturing change for approval, risk, and the point it becomes effective.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a change-control note by 30 September 2026. A process tweak is already running and the change form is blank.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A process tweak is already running and the change form is blank.

The change: requested 14 September 2026. Not yet approved
The risk they see: Line 2 is open. No score in the file
Approvers: Gus Moretti. They have not signed
The effective lot or date: 30 September 2026
```

## Example outcome

**Change-control note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Stops the unofficial tweak until approval and an effective point exist.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The change | requested 14 September 2026. Not yet approved | Needs confirmation |
| The risk they see | Line 2 is open. No score in the file | Carried into the draft |
| Approvers | Gus Moretti. They have not signed | Carried into the draft |
| The effective lot or date | 30 September 2026 | Needs confirmation |

**How this draft was built**

**1. Describe the change and the reason**

**2. Identify what must be revalidated or reinspected, using their rules. Do not invent a regulatory filing**

**3. Name approvers. A change without the required approver is not effective**

**4. Set the effective lot or date so old and new do not mix unlabeled**

**5. Update the work instruction as part of done**

**Deliberately not done**
- An effective change with no approver.
- Mixed lots with no label.
- An invented filing.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
