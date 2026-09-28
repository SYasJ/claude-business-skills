# Renewal Preparation

`broker-renewal-prep`

## What this is for

Prepare an insurance renewal packet from the expiring facts and the changes the insured reported.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a renewal prep by 30 September 2026. A renewal draft leaves off a recent claim to keep the story clean.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A renewal draft leaves off a recent claim to keep the story clean.

Expiring terms they have: Coverage checklist, recorded 14 September 2026. No supporting file attached
Changes in operations: requested 14 September 2026. Not yet approved
Losses they reported: one file, dated 14 September 2026. No earlier version attached for comparison
The deadline: 30 September 2026
```

## Example outcome

**Renewal prep**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Includes the claim and labels any premium figure as not yet quoted.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Expiring terms they have | Coverage checklist, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| Changes in operations | requested 14 September 2026. Not yet approved | Carried into the draft |
| Losses they reported | one file, dated 14 September 2026. No earlier version attached for comparison | Carried into the draft |
| The deadline | 30 September 2026 | Needs confirmation |

**How this draft was built**

**1. List changes the insured actually reported**

**2. Include losses they documented. Do not omit a known loss**

**3. Mark unknown values as unknown**

**4. Note the questions underwriters asked last time if the user has them**

**5. Do not invent a premium**

**Deliberately not done**
- An omitted known loss.
- An invented premium.
- A claim that coverage is bound.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
