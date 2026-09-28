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

interviews: 12, March to June 2026
decision: ship, hold, or cut
metric: not defined
kill line: not written
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
| interviews | 12, March to June 2026 | Needs confirmation |
| decision | ship, hold, or cut | Carried into the draft |
| metric | not defined | Carried into the draft |
| kill line | not written | Needs confirmation |

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
