# Project Closeout

`project-closeout`

## What this is for

Close a project by confirming outcomes, handing over operations, and releasing the team.

## Scenario

Owen Blake, delivery lead at Harbor Goods in Airdrie, needs a closeout note by 30 September 2026. A project is declared done while operations does not know how to support the new workflow.

## Example data

```text
From: Owen Blake, delivery lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A project is declared done while operations does not know how to support the new workflow.

milestone: the customer date
status: slipped
completed tasks: do not replace the slip
decision: needed
```

## Example outcome

**Closeout note**
To: Owen Blake, delivery lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks full closure until the operational owner and open issues are named.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| milestone | the customer date | Needs confirmation |
| status | slipped | Carried into the draft |
| completed tasks | do not replace the slip | Carried into the draft |
| decision | needed | Needs confirmation |

**How this draft was built**

**1. Compare delivery to the charter outcome. Partial delivery is labeled partial**

**2. List open issues and who owns them after close**

**3. Hand over runbooks, access, and support paths. Do not share passwords in the closeout note**

**4. Release people and budget explicitly so the project does not linger**

**5. Record a few lessons that change a template**

**Deliberately not done**
- Closing with open issues and no owner.
- A success claim that ignores the charter.
- Passwords in the note.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Owen Blake by 30 September 2026. This is a draft, not a sign-off.
