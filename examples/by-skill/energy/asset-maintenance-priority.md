# Maintenance Priority

`asset-maintenance-priority`

## What this is for

Prioritize maintenance work by safety and customer impact, using their defect list.

## Scenario

Devon Hale, operations superintendent at Prairie Line Energy in Grande Prairie, needs a maintenance priority by 30 September 2026. A cosmetic backlog is scheduled ahead of a known leak on a safety device.

## Example data

```text
From: Devon Hale, operations superintendent
Organization: Prairie Line Energy, Grande Prairie
Date: 14 September 2026
Needed by: 30 September 2026

A cosmetic backlog is scheduled ahead of a known leak on a safety device.

The defect list: Feeder 12; Site meter 4; September bill
Safety flags: September bill. Partly documented: the what is written down, the who is not
Customer impact: Redline Parts
Crew capacity: two people, no overtime figure
```

## Example outcome

**Maintenance priority**
To: Devon Hale, operations superintendent, Prairie Line Energy
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Puts the safety device first and parks cosmetics over capacity.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The defect list | Feeder 12; Site meter 4; September bill | Needs confirmation |
| Safety flags | September bill. Partly documented: the what is written down, the who is not | Carried into the draft |
| Customer impact | Redline Parts | Carried into the draft |
| Crew capacity | two people, no overtime figure | Needs confirmation |

**How this draft was built**

**1. Put safety defects they flagged first**

**2. Then customer-impacting defects**

**3. Capacity-cut the rest visibly**

**4. Do not defer a known safety defect to make a metric look better**

**5. Assign an owner and a date to the kept work**

**Deliberately not done**
- Deferring a known safety defect for a metric.
- No capacity cut.
- A crew sent with no location.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Devon Hale by 30 September 2026. This is a draft, not a sign-off.
