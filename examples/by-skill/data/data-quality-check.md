# Data Quality Check

`data-quality-check`

## What this is for

Check a dataset or pipeline for freshness, completeness, and a tie-out before anyone presents the number.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a data quality check by 30 September 2026. Monday's revenue dashboard is empty and the draft note says the business had zero revenue.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Monday's revenue dashboard is empty and the draft note says the business had zero revenue.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Data quality check**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026

**Decision**
Treats empty as late or broken until a tie-out says otherwise, and names the decision to pause.

**From the file**
- extract date: 14 Sep 2026
- owner: the sender
- second source: not attached
- nulls: not counted yet

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
