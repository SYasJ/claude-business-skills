# Anomaly Investigation

`anomaly-investigation`

## What this is for

Investigate a metric anomaly by separating a data break from a real change before anyone acts.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs an anomaly note by 30 September 2026. Conversion halves on the day a tracking change shipped, and marketing wants a new campaign.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Conversion halves on the day a tracking change shipped, and marketing wants a new campaign.

The metric and the unexpected movement: plan 180, actual 90
Recent pipeline or tracking changes: requested 14 September 2026. Not yet approved
The decision waiting on the number: Conversion halves on the day a tracking change shipped, and marketing wants a new campaign
```

## Example outcome

**Anomaly note**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026

**Decision**
Pauses the campaign idea until tracking is ruled in or out.

**From the file**
- The metric and the unexpected movement: plan 180, actual 90
- Recent pipeline or tracking changes: requested 14 September 2026. Not yet approved
- The decision waiting on the number: Conversion halves on the day a tracking change shipped, and marketing wants a new campaign

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
