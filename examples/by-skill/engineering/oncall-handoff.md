# On-Call Handoff

`oncall-handoff`

## What this is for

Write an on-call handoff that tells the next person what is on fire, what is quiet, and how to escalate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an on-call handoff by 30 September 2026. The outgoing engineer writes 'should be fine' after a migration that has not been verified.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The outgoing engineer writes 'should be fine' after a migration that has not been verified.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**On-call handoff**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Lists the unverified migration, the check to run, and the escalation owner.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Open items**  
What is paging or degraded, the current theory, and the next check. Theories are labeled.

**2. Recent changes**  
Deploys or migrations the next person should know about, from the user's list.

**3. Fragile spots**  
Known risks for this shift, with the runbook link if one exists. Do not invent a runbook.

**4. Escalation**  
Who to wake and for what. A handoff with no escalation path is incomplete.

**5. Noise**  
Alerts that are known noise, so the next person does not chase them blind. Do not tell them to ignore a security alert without an owner.

**Deliberately not done**
- A handoff that says 'all quiet' when an incident is open.
- Invented runbook links.
- Telling the next person to silence a security page with no owner.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
