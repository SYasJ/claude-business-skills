# Data Quality Check

`data-quality-check`

## What this is for

Check a dataset or pipeline for freshness, completeness, and a tie-out before anyone presents the number.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a data quality check by 30 September 2026. Monday's revenue dashboard is empty and the draft note says the business had zero revenue.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Monday's revenue dashboard is empty and the draft note says the business had zero revenue.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Data quality check**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Treats empty as late or broken until a tie-out says otherwise, and names the decision to pause.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Check grain and freshness first. A stale table cannot support today's decision**

**2. Tie a total to a source they trust. A mismatch is the finding, not a footnote**

**3. Look for duplicates, null keys, and sudden row-count jumps using the evidence they gave**

**4. Separate a pipeline break from a real business movement. Do not guess which without evidence**

**5. Write the user impact**  
which dashboard or decision is unsafe.

**Deliberately not done**
- Presenting a number that failed its tie-out.
- Inventing a row count.
- A quality check with no decision impact.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
