# Observability Plan

`observability-plan`

## What this is for

Specify the logs, metrics, and traces a service needs to debug a user-facing failure.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an observability plan by 30 September 2026. A plan logs the full Authorization header to 'make debugging easier'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A plan logs the full Authorization header to 'make debugging easier'.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Observability plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Forbids that header, specifies a request id, and pages only on user-facing errors.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Question**  
The production question the signal must answer. Signals without a question are noise.

**2. Golden signals**  
Latency, errors, traffic, and saturation only where they match the service. Do not dump a template.

**3. Logs**  
Structured fields that help debug, excluding secrets, tokens, and full payment data.

**4. Traces**  
Where a trace would beat another log line, if they already use tracing. Do not mandate a vendor.

**5. Alerts**  
Page only on user pain or imminent user pain. A page on every warning trains people to ignore pages.

**Deliberately not done**
- Logging secrets or card numbers.
- Paging on every warning.
- A vendor mandate disguised as a plan.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
