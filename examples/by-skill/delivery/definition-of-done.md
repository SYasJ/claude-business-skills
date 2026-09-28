# Definition of Done

`definition-of-done`

## What this is for

Write a definition of done that a team can apply to a backlog item without a debate each time.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a definition of done by 30 September 2026. The definition requires a help article, but nobody has written one in six months.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

The definition requires a help article, but nobody has written one in six months.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Definition of done**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Either restores the article check with an owner or removes it until the team means it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| milestone | the customer date | Needs confirmation |
| status | slipped | Carried into the draft |
| completed tasks | do not replace the slip | Carried into the draft |
| decision | needed | Needs confirmation |

**How this draft was built**

**1. List the checks that apply to this work type**  
tested, reviewed, documented, monitored, as they actually require.

**2. Separate acceptance criteria, which are specific to a story, from done, which is the team's bar**

**3. Cut checks the team does not perform. A fictional done definition will be ignored**

**4. Say who confirms each check**

**5. Note exceptions, such as a spike, so they are explicit**

**Deliberately not done**
- A done definition nobody follows.
- Mixing story acceptance into the team bar.
- A check with no owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
