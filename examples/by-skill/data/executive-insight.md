# Executive Insight Memo

`executive-insight`

## What this is for

Turn an analysis into a one-page insight a leader can use, with the number, the comparison, and the limit.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs an insight memo by 30 September 2026. An analyst has a retention drop and wants the memo to say a competitor caused it.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An analyst has a retention drop and wants the memo to say a competitor caused it.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Insight memo**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Reports the drop, refuses the competitor cause without evidence, and names the next question.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Lead with the finding and the comparison in one or two sentences**

**2. Show only numbers they provided. Round only if you say so**

**3. State what the finding does not prove**

**4. Recommend one decision or one question**

**5. Put method in a short note, not in the opening**

**Deliberately not done**
- A chart dump with no sentence.
- Causal language the design does not support.
- Invented context.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
