# Tech Debt Triage

`tech-debt-triage`

## What this is for

Triage tech debt by the risk and delay it causes, and cut the list to what the team will actually pay down.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a tech debt triage by 30 September 2026. A team has 60 debt tickets and wants them all in next sprint alongside a launch.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team has 60 debt tickets and wants them all in next sprint alongside a launch.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Tech debt triage**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Keeps the debt tied to launch risk, parks the rest, and makes the capacity trade explicit.

**From the file**
- branch: main, change not merged
- tests listed: none
- rollback: not written
- owner: the person who opened the change

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
