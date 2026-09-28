# Roadmap Narrative

`roadmap-narrative`

## What this is for

Write a roadmap narrative that explains outcomes and sequencing, with dates only where they are real.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a roadmap narrative by 30 September 2026. Sales wants every prospect request placed on next quarter's roadmap.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales wants every prospect request placed on next quarter's roadmap.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

## Example outcome

**Roadmap narrative**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Keeps uncommitted requests in later or off-roadmap, with the reason.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| interviews | 12, March to June 2026 | Needs confirmation |
| decision | ship, hold, or cut | Carried into the draft |
| metric | not defined | Carried into the draft |
| kill line | not written | Needs confirmation |

**How this draft was built**

**1. Outcomes over features**  
Lead with the customer or business outcome. Features are evidence of the bet, not the headline.

**2. Now, next, later**  
Use this shape unless the user has a better one. Later is not a promise.

**3. Dates**  
Only committed dates get dates. Everything else is a sequence without a fake quarter.

**4. Why this order**  
The dependency or learning that forces the sequence.

**5. Not on the roadmap**  
Items people will ask about, and the reason they wait.

**Deliberately not done**
- A feature laundry list with fake dates.
- A roadmap that hides the delays.
- Different truths for different audiences.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
