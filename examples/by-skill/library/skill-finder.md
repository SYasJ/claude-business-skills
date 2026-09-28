# Skill Finder

`skill-finder`

## What this is for

Recommend the smallest set of skills in this library for a task, and say what not to load.

## Scenario

Yasir Jilani, author at Practice Skills in Airdrie, needs a skill recommendation by 30 September 2026. A user asks for a cash view and also wants a full corporate strategy loaded.

## Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A user asks for a cash view and also wants a full corporate strategy loaded.

The task: A user asks for a cash view and also wants a full corporate strategy loaded. Stated once, in the ask. Not written down anywhere else
The domain: plugins/finance/cash-flow-forecast, recorded 14 September 2026. No supporting file attached
Whether a regulated professional must review: plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not
Skills already loaded: 50 in the last period. No prior period attached, so no trend
```

## Example outcome

**Skill recommendation**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A recommendation of cash-flow-forecast only, with strategy skills named as unnecessary for this task.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The task | A user asks for a cash view and also wants a full corporate strategy loaded. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| The domain | plugins/finance/cash-flow-forecast, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Whether a regulated professional must review | plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not | Carried into the draft |
| Skills already loaded | 50 in the last period. No prior period attached, so no trend | Needs confirmation |

**How this draft was built**

**1. Restate the task in one sentence**

**2. Pick the one skill whose output matches the task. Add a second only if the task truly crosses domains**

**3. Prefer a specialist skill over a general strategy skill when the output is a defined artifact**

**4. Say which nearby skill is the wrong one and why**

**5. If the task asks for deception, evasion, or harm, do not route to a skill. Refuse and offer a legitimate alternative**

**Deliberately not done**
- Loading five skills for a simple memo.
- Routing a harmful request into a skill.
- Recommending a skill you cannot name.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Yasir Jilani by 30 September 2026. This is a draft, not a sign-off.
