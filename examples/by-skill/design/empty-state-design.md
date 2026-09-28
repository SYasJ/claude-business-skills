# Empty State Design

`empty-state-design`

## What this is for

Design an empty state that explains why it is empty and offers the next honest action.

## Scenario

Lena Ortiz, design lead at Fieldnote in Edmonton, needs an empty state spec by 30 September 2026. A dashboard shows sample revenue that looks like the customer's numbers.

## Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A dashboard shows sample revenue that looks like the customer's numbers.

screens: 8, dated 10 Sep 2026
job: the task in the ask
accessibility pass: not done
assets: theirs only
```

## Example outcome

**Empty state spec**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Labels or removes the sample and explains the true empty reason.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| screens | 8, dated 10 Sep 2026 | Needs confirmation |
| job | the task in the ask | Carried into the draft |
| accessibility pass | not done | Carried into the draft |
| assets | theirs only | Needs confirmation |

**How this draft was built**

**1. Say why the screen is empty**  
new user, filter, or no permission.

**2. Offer the next action only if it is really available**

**3. Do not fake sample data that looks like the user's own data**

**4. If a filter caused the empty state, show how to clear it**

**5. Keep the tone calm**

**Deliberately not done**
- Fake data that looks real.
- An action the role cannot do.
- An empty screen with no reason.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.
