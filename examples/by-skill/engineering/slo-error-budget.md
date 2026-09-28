# SLO and Error Budget

`slo-error-budget`

## What this is for

Draft an SLO from a user journey and explain how the error budget changes release behavior.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a SLO draft by 30 September 2026. A team copies a 99.99 SLO from a blog and has no latency metric.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team copies a 99.99 SLO from a blog and has no latency metric.

The user journey: the one named in the ask. Version and owner not recorded
Current performance if known: 30 in the last period. No prior period attached, so no trend
The pain that matters: Checkout service, recorded 14 September 2026. No supporting file attached
Release cadence: Status page and one other, both unconfirmed as of 14 September 2026
```

## Example outcome

**Variance note**
Fieldnote · period ending 14 September 2026

Decision: treat the gap as a miss against the file, not as a formatting issue. Do not call it timing unless the invoice date is in the file.

| Line | Plan | Actual | Gap |
| --- | --- | --- | --- |
| Main driver | 150 | 80 | 70 |
| One-off named in the file | — | not supplied | leave open |
| Full-period outlook | unchanged until the one-off is dated | | |

Refuses the copied target, names the missing metric, and proposes a journey-based indicator.
Next action: Aisha Rahman marks the gap as timing or as a real miss by 30 September 2026.
