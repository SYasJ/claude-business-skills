# SQL Review

`sql-review`

## What this is for

Review a query for correctness, grain, and safety, without running it against a database you were not given.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a SQL review by 30 September 2026. A revenue query joins invoices to line items and sums invoice totals.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A revenue query joins invoices to line items and sums invoice totals.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Sql review**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Flag the double count, asks for the grain, and does not request database passwords.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Restate the intended grain and metric**

**2. Check joins and filters against that intent. A fan-out that double-counts is a finding**

**3. Flag non-deterministic filters, missing time zones, and unbounded scans if visible in the text**

**4. If the query mutates or deletes data, require a WHERE and a stated backup. Do not suggest disabling safeguards**

**5. Do not invent table schemas. Mark assumptions**

**Deliberately not done**
- Approving a double-count join.
- Suggesting a credential share.
- An unbounded delete with no predicate.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
