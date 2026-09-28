# Dashboard Spec

`dashboard-spec`

## What this is for

Specify a dashboard that answers a few decisions, with an owner and a refresh the team can trust.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a dashboard specification by 30 September 2026. A leader wants 30 tiles on one page and cannot name the Monday decision.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A leader wants 30 tiles on one page and cannot name the Monday decision.

The decisions the dashboard must support: A leader wants 30 tiles on one page and cannot name the Monday decision
The metrics and their definitions: plan 180, actual 95
Who will use it and how often: Noah Berger, data lead
Known data delays: customers. Stated in the ask, not documented anywhere else
```

## Example outcome

**Dashboard specification**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A spec of a few decision tiles, each with a source, a lag, and an owner.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The decisions the dashboard must support | A leader wants 30 tiles on one page and cannot name the Monday decision | Needs confirmation |
| The metrics and their definitions | plan 180, actual 95 | Carried into the draft |
| Who will use it and how often | Noah Berger, data lead | Carried into the draft |
| Known data delays | customers. Stated in the ask, not documented anywhere else | Needs confirmation |

**How this draft was built**

**1. Limit the dashboard to the decisions named. A gallery of charts is a finding**

**2. Every chart needs a question, a defined metric, and a source**

**3. State the refresh lag. A daily decision on a monthly feed is a mismatch**

**4. Specify filters that change a decision, not every possible slice**

**5. Name the owner who fixes a broken number**

**Deliberately not done**
- A chart with no question.
- Hidden refresh lag.
- No owner for a broken tile.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
