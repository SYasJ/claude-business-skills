# Feedback Synthesis

`feedback-synthesis`

## What this is for

Synthesize feedback from tickets, calls, or notes into themes with evidence, not a word cloud.

## Scenario

Jonah Park, product manager at Fieldnote in Edmonton, needs a feedback synthesis by 30 September 2026. A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures.

## Example data

```text
From: Jonah Park, product manager
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures.

The raw notes or tickets: one file, dated 14 September 2026. No earlier version attached for comparison
The decision this informs: A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures
How the sample was gathered: Trial day-3 email, last reviewed 14 September 2026. No owner named since
What volume means in their context: 40 in the last period. No prior period attached, so no trend
```

## Example outcome

**Feedback synthesis**
To: Jonah Park, product manager, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Leads with export failures, counts only supplied evidence, and parks the executive idea as unproven.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The raw notes or tickets | one file, dated 14 September 2026. No earlier version attached for comparison | Needs confirmation |
| The decision this informs | A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures | Carried into the draft |
| How the sample was gathered | Trial day-3 email, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| What volume means in their context | 40 in the last period. No prior period attached, so no trend | Needs confirmation |

**How this draft was built**

**1. Sample bias**  
Say who is missing from the pile. A pile of detractors is not the whole market.

**2. Themes**  
Group by the job or failure, not by the feature name alone.

**3. Evidence**  
Each theme has quotes or ticket counts from the supplied material. No theme without evidence.

**4. Severity**  
Distinguish frequency from pain. A rare data-loss report can outrank a common color complaint.

**5. Implication**  
What product should do next, and what should be a support macro instead.

**Deliberately not done**
- A word cloud as the analysis.
- Ignoring sample bias.
- Themes with no quotes.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Jonah Park by 30 September 2026. This is a draft, not a sign-off.
