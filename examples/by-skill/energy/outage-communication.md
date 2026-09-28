# Outage Communication

`outage-communication`

## What this is for

Draft an outage message with the area, the known cause label, and the next update time.

## Scenario

Devon Hale, operations superintendent at Prairie Line Energy in Grande Prairie, needs an outage message by 30 September 2026. A message promises power in 30 minutes because that sounded reassuring.

## Example data

```text
From: Devon Hale, operations superintendent
Organization: Prairie Line Energy, Grande Prairie
Date: 14 September 2026
Needed by: 30 September 2026

A message promises power in 30 minutes because that sounded reassuring.

meter: the one they named
figure: their sheet
promised date from elsewhere: not in the file
owner: superintendent
```

## Example outcome

**Outage message**
To: Devon Hale, operations superintendent, Prairie Line Energy
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the 30-minute promise and commits to a next update.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| meter | the one they named | Needs confirmation |
| figure | their sheet | Carried into the draft |
| promised date from elsewhere | not in the file | Carried into the draft |
| owner | superintendent | Needs confirmation |

**How this draft was built**

**1. State who is affected in the terms they confirmed**

**2. Do not guess a cause**

**3. Give the next update time**

**4. Include safety instructions they already approved, such as staying away from downed lines. Do not invent technical bypass steps**

**5. Avoid promising a restoration minute they do not have**

**Deliberately not done**
- A guessed cause.
- A fake restoration minute.
- Bypass instructions for equipment.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Devon Hale by 30 September 2026. This is a draft, not a sign-off.
