# Cohort Analysis

`cohort-analysis`

## What this is for

Build a cohort view that follows a defined group over time without mixing incompatible cohorts.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a cohort analysis by 30 September 2026. Last week's cohort looks like it retained worse, but the week is not over.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Last week's cohort looks like it retained worse, but the week is not over.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Cohort analysis**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026

**Decision**
Marks the week incomplete and refuses a churn conclusion from it.

**From the file**
- extract date: 14 Sep 2026
- owner: the sender
- second source: not attached
- nulls: not counted yet

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
