# User Story Map

`user-story-map`

## What this is for

Map the user's journey into slices of value so a release is a story, not a pile of tickets.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a story map by 30 September 2026. A team has 80 tickets and wants a release that builds the admin console before the user can finish the core job.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team has 80 tickets and wants a release that builds the admin console before the user can finish the core job.

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
```

## Example outcome

**Story map**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A map whose first slice completes the core job thinly, and parks the admin console.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| interviews | 12, March to June 2026 | Needs confirmation |
| decision | ship, hold, or cut | Carried into the draft |
| metric | not defined | Carried into the draft |
| kill line | not written | Needs confirmation |

**How this draft was built**

**1. Backbone**  
The steps the user takes, in order. Internal tasks do not lead the map.

**2. Stories under steps**  
Place each story under the step it serves. Orphan stories are a finding.

**3. Slice**  
Draw a first release that completes a thin journey. A release that finishes only the left half of the journey is not releasable.

**4. Later slices**  
What waits, and why.

**5. Risks**  
The step with the least evidence.

**Deliberately not done**
- A backlog dump called a map.
- A first release that cannot be used end to end.
- Stories with no user step.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
