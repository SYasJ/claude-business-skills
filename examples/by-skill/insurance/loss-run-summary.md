# Loss Run Summary

`loss-run-summary`

## What this is for

Summarize a loss run the user provided, without forecasting a premium or hiding a large loss.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a loss-run summary by 30 September 2026. A summary averages away one severe open claim.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A summary averages away one severe open claim.

folder: the claim file they have
coverage opinion: not given
missing doc: named
handler: licensed owner
```

## Example outcome

**Loss-run summary**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows the severe claim separately and makes no price prediction.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| folder | the claim file they have | Needs confirmation |
| coverage opinion | not given | Carried into the draft |
| missing doc | named | Carried into the draft |
| handler | licensed owner | Needs confirmation |

**How this draft was built**

**1. State the period and the source**

**2. Summarize counts and amounts from the run**

**3. Call out large or open items**

**4. Do not drop a loss to improve the picture**

**5. Do not predict an insurer's price**

**Deliberately not done**
- A dropped loss.
- A premium prediction.
- An incomplete run treated as complete.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
