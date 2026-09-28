# Hospitality Shift Brief

`shift-brief-hospitality`

## What this is for

Write a hospitality shift brief covering VIPs they named, misses, and eighty-six items.

## Scenario

Sofia Alvarez, front office manager at Lantern Inn in Banff, needs a shift brief by 30 September 2026. A brief shares a guest's medical details with the whole dining team.

## Example data

```text
From: Sofia Alvarez, front office manager
Organization: Lantern Inn, Banff
Date: 14 September 2026
Needed by: 30 September 2026

A brief shares a guest's medical details with the whole dining team.

Covers or occupancy: Room block, 18 keys and one other, both unconfirmed as of 14 September 2026
Items they cannot sell: Friday dinner service, last reviewed 14 September 2026. No owner named since
Guest issues: Guest complaint 214, last reviewed 14 September 2026. No owner named since
Staffing gaps: Friday dinner service is missing a source
```

## Example outcome

**Shift brief**
To: Sofia Alvarez, front office manager, Lantern Inn
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the medical details and keeps the operational accommodation only if needed.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Covers or occupancy | Room block, 18 keys and one other, both unconfirmed as of 14 September 2026 | Needs confirmation |
| Items they cannot sell | Friday dinner service, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Guest issues | Guest complaint 214, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Staffing gaps | Friday dinner service is missing a source | Needs confirmation |

**How this draft was built**

**1. Lead with safety and eighty-six items**

**2. Note guest issues without gossip**

**3. State staffing gaps that change service**

**4. Assign the person who handles a known problem**

**5. Do not include a guest's sensitive personal data**

**Deliberately not done**
- Gossip.
- Sensitive personal data.
- A brief with no eighty-six list when items are down.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Sofia Alvarez by 30 September 2026. This is a draft, not a sign-off.
