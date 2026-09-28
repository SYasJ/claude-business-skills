# Survey Analysis

`survey-analysis`

## What this is for

Analyze a survey without overclaiming a small or biased sample.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a survey analysis by 30 September 2026. An NPS of 80 from 11 self-selected responses is about to go on a board slide as proof of love.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An NPS of 80 from 11 self-selected responses is about to go on a board slide as proof of love.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Survey analysis**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the board claim, states the bias, and limits the use of the score.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Report the sample and the recruitment bias before the score**

**2. Do not treat a small sample as a population percentage without a caution**

**3. Separate closed scores from themes in open text they actually pasted**

**4. Do not invent themes**

**5. Tie one finding to a decision or say the survey cannot support one**

**Deliberately not done**
- A precise population claim from a tiny sample.
- Invented themes.
- Identifying a respondent.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
