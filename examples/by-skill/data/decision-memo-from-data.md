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
Date: 14 September 2026

**Decision**
Recommends a reversible cut or a test, and refuses a causal claim the data cannot support.

**From the file**
- The decision: Leadership must cut one of two channels, and the data shows correlation, not incrementality
- The options: keep orders_daily, or stop. No third option written
- The constraints: no extra headcount, and no result that is not in this file

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
