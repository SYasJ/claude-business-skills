# Escalation Playbook

`escalation-playbook`

## What this is for

Write an escalation path with levels, clocks, and the decision each level can make.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs an escalation playbook by 30 September 2026. Every angry email is marked severe, so the on-call ignores the queue.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Every angry email is marked severe, so the on-call ignores the queue.

Who is on each level: Rita Santos, support lead
Clocks they can staff: two people on shift
Customer communication owner: Rita Santos, support lead
```

## Example outcome

**Escalation playbook**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Defines severity by impact and reserves executive escalation for a written trigger.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Who is on each level | Rita Santos, support lead | Needs confirmation |
| Clocks they can staff | two people on shift | Carried into the draft |
| Customer communication owner | Rita Santos, support lead | Carried into the draft |

**How this draft was built**

**1. Define severity by impact, not by who shouted**

**2. Each level has a clock and a decision it can make**

**3. Name the customer communication owner so engineering is not surprised by a promise**

**4. Include how to de-escalate when impact falls**

**5. Record what must be true before waking an executive**

**Deliberately not done**
- Severity set by loudness.
- An executive ping with no path.
- Hidden security issues.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
