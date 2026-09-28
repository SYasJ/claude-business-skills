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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Pauses the campaign idea until tracking is ruled in or out.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The metric and the unexpected movement | plan 180, actual 90 | Needs confirmation |
| Recent pipeline or tracking changes | requested 14 September 2026. Not yet approved | Carried into the draft |
| The decision waiting on the number | Conversion halves on the day a tracking change shipped, and marketing wants a new campaign | Carried into the draft |

**How this draft was built**

**1. Confirm the movement against the definition and the source**

**2. Check freshness, duplicates, and tracking changes before a business story**

**3. If a business event is known, test whether its timing matches. Do not invent a campaign or outage**

**4. Quantify who is affected using their slices, and stop if the slice is tiny**

**5. Say whether the number is safe to use today**

**Deliberately not done**
- A business story for a broken pipeline.
- Ignoring a tracking change.
- Acting on a tiny slice.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
