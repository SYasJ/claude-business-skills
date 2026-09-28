# Documentation As Code

`documentation-as-code`

## What this is for

Write or repair technical docs so a new teammate can complete a task without a hallway conversation.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a documentation update by 30 September 2026. A README says 'run the script' and the script path does not exist.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A README says 'run the script' and the script path does not exist.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Documentation update**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Either uses the real path the user confirmed or marks the step unknown, and removes the stale command.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Audience and task**  
What the reader is trying to do. A doc with no task becomes a junk drawer.

**2. Truth**  
Steps match the repo or the user's confirmation. Do not invent flags, paths, or environment variables.

**3. Prerequisites**  
What must exist first, including access, without asking for secrets to be pasted into the doc.

**4. Failure**  
The common failure and the next check.

**5. Ownership**  
Who updates the doc when the system changes.

**Deliberately not done**
- Invented commands.
- Secrets in the example env file.
- A README that does not say how to run the project.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
