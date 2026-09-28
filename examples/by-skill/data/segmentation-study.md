# Segmentation Study

`segmentation-study`

## What this is for

Segment users or customers from supplied data into groups that change an action, not into decorative clusters.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a segmentation note by 30 September 2026. A model produced eight clusters and the team cannot say what they would do differently for any of them.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A model produced eight clusters and the team cannot say what they would do differently for any of them.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Segmentation note**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Collapses to a few actionable rules and parks the rest as unusable.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Start from the action**  
message, offer, or service model. Segments that do not change an action are cut.

**2. Use fields they have. Do not require a model they cannot run**

**3. Keep the number of segments small enough to operate**

**4. Describe each segment with a rule a teammate can apply, not only a cluster id**

**5. Note sample size. A segment of a handful of rows is a list, not a strategy**

**Deliberately not done**
- Clusters with no action.
- A segment too small to mean anything.
- Invented demographic attributes.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
