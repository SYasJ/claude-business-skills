# Experiment Design

`experiment-design`

## What this is for

Design a product experiment with a hypothesis, a guardrail, and a decision rule written in advance.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs an experiment design by 30 September 2026. A team wants to ship the winner of a three-day test on a rare flow.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to ship the winner of a three-day test on a rare flow.

The hypothesis: A team wants to ship the winner of a three-day test on a rare flow. Stated once, in the ask. Not written down anywhere else
The change: requested 14 September 2026. Not yet approved
The primary metric and guardrail: plan 180, actual 90
The available sample: Activation checklist, recorded 14 September 2026. No supporting file attached
```

## Example outcome

**Experiment design**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Labels the work a probe, adds a guardrail, and refuses a conclusive ship decision.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The hypothesis | A team wants to ship the winner of a three-day test on a rare flow. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| The change | requested 14 September 2026. Not yet approved | Carried into the draft |
| The primary metric and guardrail | plan 180, actual 90 | Carried into the draft |
| The available sample | Activation checklist, recorded 14 September 2026. No supporting file attached | Needs confirmation |

**How this draft was built**

**1. Hypothesis**  
The user behavior you expect to change, and why.

**2. Change**  
One treatment. Name the control.

**3. Metrics**  
A primary metric and a guardrail that would make a 'win' unacceptable, such as errors or complaints.

**4. Decision rule**  
Ship, iterate, or stop, written before results.

**5. Sample**  
If the sample is too small, call the work a probe, not a conclusive test.

**Deliberately not done**
- Peeking and moving the metric.
- No guardrail.
- Calling a tiny sample conclusive.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
