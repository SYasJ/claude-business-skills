# Estimation Review

`estimation-review`

## What this is for

Review an engineering estimate by exposing assumptions, slices, and the unknown, not by demanding false precision.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an estimate review by 30 September 2026. A stakeholder wants a date for a rewrite with no scope and no prior art.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A stakeholder wants a date for a rewrite with no scope and no prior art.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Estimate review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the date, proposes a scoped spike, and offers a range only after that spike.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Scope**  
Restate the slice. An estimate of an unbounded idea is not an estimate. Cut scope first.

**2. Assumptions**  
List the assumptions. The estimate is valid only while they hold.

**3. Reference**  
Compare with a past piece of work they name. Do not invent a velocity number.

**4. Unknowns**  
The spike that would shrink the range. Recommend a range, not a fake single day.

**5. Capacity**  
Calendar time is not effort time. Include review and release if they matter.

**Deliberately not done**
- A single-day estimate for an unbounded project.
- Invented velocity.
- Hiding unknowns to look confident.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
