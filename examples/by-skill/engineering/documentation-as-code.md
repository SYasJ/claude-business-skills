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
Date: 14 September 2026

**Decision**
Either uses the real path the user confirmed or marks the step unknown, and removes the stale command.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
