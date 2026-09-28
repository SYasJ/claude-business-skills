# Calibration Control

`calibration-control`

## What this is for

Review calibration control so instruments used for acceptance are in date, and out-of-date tools are not used.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a calibration control note by 30 September 2026. A caliper used for final accept is two months overdue and still on the bench.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A caliper used for final accept is two months overdue and still on the bench.

The instrument list: Line 2; Lot 26-0914; Gauge 7
Due dates they have: 30 September 2026
What the instrument accepts: Gauge 7, last reviewed 14 September 2026. No owner named since
The quarantine practice: Line 2, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Calibration control note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Quarantines it and asks for a use review rather than inventing which lots moved.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The instrument list | Line 2; Lot 26-0914; Gauge 7 | Needs confirmation |
| Due dates they have | 30 September 2026 | Carried into the draft |
| What the instrument accepts | Gauge 7, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| The quarantine practice | Line 2, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. Flag overdue instruments used for acceptance**

**2. Quarantine is the default they stated, or recommend it if they have none**

**3. Do not calculate a new calibration interval from memory**

**4. Record the last result they supplied**

**5. Assess impact only if they know the instrument was used while overdue. Do not invent affected lots**

**Deliberately not done**
- Using an overdue gage for acceptance.
- An invented interval.
- Invented affected lots.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
