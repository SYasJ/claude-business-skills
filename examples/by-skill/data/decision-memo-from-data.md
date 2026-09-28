# Decision Memo From Data

`decision-memo-from-data`

## What this is for

Write a decision memo that uses data the user supplied and labels every non-data judgment.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a decision memo by 30 September 2026. Leadership must cut one of two channels, and the data shows correlation, not incrementality.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Leadership must cut one of two channels, and the data shows correlation, not incrementality.

The decision: Leadership must cut one of two channels, and the data shows correlation, not incrementality
The options: keep orders_daily, or stop. No third option written
The constraints: no extra headcount, and no result that is not in this file
```

## Example outcome

**Decision memo**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Recommends a reversible cut or a test, and refuses a causal claim the data cannot support.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The decision | Leadership must cut one of two channels, and the data shows correlation, not incrementality | Needs confirmation |
| The options | keep orders_daily, or stop. No third option written | Carried into the draft |
| The constraints | no extra headcount, and no result that is not in this file | Carried into the draft |

**How this draft was built**

**1. State the decision in one sentence**

**2. List the data facts that bear on it, with comparisons**

**3. List judgments separately from facts**

**4. Compare options against the constraint they named, not against an invented benchmark**

**5. Recommend one option and the fact that would change it**

**Deliberately not done**
- A recommendation that ignores the constraint.
- Benchmarks from memory.
- Facts and judgments mixed.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
