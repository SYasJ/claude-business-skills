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

The task a new person must complete: A README says 'run the script' and the script path does not exist. Stated once, in the ask. Not written down anywhere else
The current doc: Checkout service, recorded 14 September 2026. No supporting file attached
The commands or paths that are true: Checkout service, recorded 14 September 2026. No supporting file attached
The owner: Aisha Rahman, engineering lead
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
| The task a new person must complete | A README says 'run the script' and the script path does not exist. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| The current doc | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The commands or paths that are true | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The owner | Aisha Rahman, engineering lead | Needs confirmation |

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
