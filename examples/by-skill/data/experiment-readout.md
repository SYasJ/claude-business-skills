# Experiment Readout

`experiment-readout`

## What this is for

Read out an experiment using the pre-written decision rule, the guardrail, and the sample they actually have.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs an experiment readout by 30 September 2026. The primary metric is flat, a secondary slice looks good, and the team wants to ship.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

The primary metric is flat, a secondary slice looks good, and the team wants to ship.

The pre-registered metric and rule if they have one: plan 180, actual 90
The results they pasted: orders_daily, recorded 14 September 2026. No supporting file attached
Sample size: active_accounts, recorded 14 September 2026. No supporting file attached
Guardrail results: orders_daily, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Experiment readout**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the secondary-slice ship, notes the flat primary metric, and labels any follow-up as a new hypothesis.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The pre-registered metric and rule if they have one | plan 180, actual 90 | Needs confirmation |
| The results they pasted | orders_daily, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Sample size | active_accounts, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Guardrail results | orders_daily, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Start from the decision rule they wrote. If none exists, say the readout is exploratory**

**2. Report the primary metric and the guardrail before secondary slices**

**3. Do not crown a winner on a slice that was not the plan, unless you label it a hypothesis**

**4. State whether the sample can support the decision they want**

**5. Separate a failed experiment from a broken implementation**

**Deliberately not done**
- Moving the metric after seeing results.
- Ignoring a broken guardrail.
- Declaring a tiny sample conclusive.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
