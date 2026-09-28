# Scrap and Rework Review

`scrap-and-rework`

## What this is for

Review scrap and rework so the largest cause gets an owner, and numbers tie to the floor.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a scrap review by 30 September 2026. Most scrap is coded 'other' and the team still wants a root cause.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

Most scrap is coded 'other' and the team still wants a root cause.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Scrap review**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Makes the dumping code the first problem and assigns an owner to fix the codes.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. Use their quantities. Do not invent a scrap rate**

**2. Separate scrap from rework. They need different actions**

**3. Rank causes. Attack the largest evidenced one**

**4. Check whether the reason codes are honest or a dumping code**

**5. Assign an owner**

**Deliberately not done**
- An invented yield.
- A dumping code ignored.
- No owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
