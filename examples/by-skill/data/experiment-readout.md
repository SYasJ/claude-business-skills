# Experiment Readout

`experiment-readout`

## What this is for

Read out an experiment using the pre-written decision rule, the guardrail, and the sample they actually have.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs an experiment readout by 30 September 2026. The primary metric is flat, a secondary slice looks good, and the team wants to ship.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The primary metric is flat, a secondary slice looks good, and the team wants to ship.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Experiment readout**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026

**Decision**
Refuses the secondary-slice ship, notes the flat primary metric, and labels any follow-up as a new hypothesis.

**From the file**
- extract date: 14 Sep 2026
- owner: the sender
- second source: not attached
- nulls: not counted yet

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
