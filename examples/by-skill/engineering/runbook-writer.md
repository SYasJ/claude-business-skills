# Runbook Writer

`runbook-writer`

## What this is for

Write a runbook a tired on-call engineer can follow, with checks, stops, and escalation.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a runbook by 30 September 2026. A draft runbook starts by deleting a production table if an alert fires.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A draft runbook starts by deleting a production table if an alert fires.

The alert or symptom: Checkout service, recorded 14 September 2026. No supporting file attached
The checks that are safe: Checkout service, recorded 14 September 2026. No supporting file attached
The fix that is allowed: Checkout service, recorded 14 September 2026. No supporting file attached
Who to escalate to: Aisha Rahman, engineering lead
```

## Example outcome

**Runbook**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Starts with read-only checks, removes the destructive first step, and escalates before any data deletion.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The alert or symptom | Checkout service, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| The checks that are safe | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The fix that is allowed | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Who to escalate to | Aisha Rahman, engineering lead | Needs confirmation |

**How this draft was built**

**1. Symptom**  
What the human sees, in the alert's language.

**2. Impact**  
How to tell whether users are hurt, using signals they have.

**3. Checks**  
Safe, read-only checks first. Do not include destructive commands as the first step.

**4. Mitigation**  
The allowed mitigation, with the stop condition. No improvised production surgery.

**5. Escalation**  
When to stop and call the owner.

**Deliberately not done**
- Destructive commands with no stop condition.
- A runbook that requires hero knowledge.
- Secrets embedded in the steps.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
