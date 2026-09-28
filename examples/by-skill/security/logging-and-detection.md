# Logging and Detection

`logging-and-detection`

## What this is for

Specify defensive logs and alerts for a likely abuse, without writing an intrusion guide.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a detection note by 30 September 2026. A team wants an alert on data export but also asks to log every keystroke of a department.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants an alert on data export but also asks to log every keystroke of a department.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Detection note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the keystroke surveillance.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| policy | the one they have | Needs confirmation |
| report in the folder | none | Carried into the draft |
| control named | only if it is in the policy | Carried into the draft |
| owner | engineering lead | Needs confirmation |

**How this draft was built**

**1. Describe the abuse in outcome language, such as mass export or repeated denied access. No attack procedure**

**2. Specify the event fields needed to investigate, excluding secrets and excessive personal data**

**3. Write the alert in terms of a threshold they choose, and who is paged**

**4. Include a false-positive note so the alert is tunable**

**5. State the response's first safe step, usually verify and contain, and point to the incident skill**

**Deliberately not done**
- An intrusion how-to.
- Logging secrets.
- Employee surveillance beyond the stated event.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
