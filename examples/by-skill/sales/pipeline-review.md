# Pipeline Review

`pipeline-review`

## What this is for

Review a pipeline so stages mean evidence, and stuck deals get a next action or an exit.

## Scenario

Samir Qureshi, account executive at Fieldnote in Edmonton, needs a pipeline review by 30 September 2026. A pipeline has 30 opportunities and 18 have no dated next step.

## Example data

```text
From: Samir Qureshi, account executive
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A pipeline has 30 opportunities and 18 have no dated next step.

account: Harbor Goods
last meeting: 9 Sep 2026, no dated next step
proof: one email
discount asked: 15 percent, not approved
```

## Example outcome

**Pipeline review**
To: Samir Qureshi, account executive, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Rewinds or removes undated deals and names one coaching point about buyer-owned next steps.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| account | Harbor Goods | Needs confirmation |
| last meeting | 9 Sep 2026, no dated next step | Carried into the draft |
| proof | one email | Carried into the draft |
| discount asked | 15 percent, not approved | Needs confirmation |

**How this draft was built**

**1. Check definitions**  
A stage without an evidence requirement is a label. Say so.

**2. Age**  
Deals older than the user's threshold need a reason to stay. No reason, recommend exit.

**3. Next step quality**  
A next step has a date and a buyer action. 'Follow up' is not a next step.

**4. Concentration**  
Note if the number depends on one deal. Do not hide concentration to make the team look diversified.

**5. Hygiene actions**  
Advance, rewind, or remove. Rewinding is healthy.

**Deliberately not done**
- Leaving zombie deals because removing them hurts the chart.
- Next steps with no buyer action.
- Changing stage definitions mid-meeting to save a forecast.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Samir Qureshi by 30 September 2026. This is a draft, not a sign-off.
