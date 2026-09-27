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
Date: 14 September 2026

**Decision**
Flag the double count, asks for the grain, and does not request database passwords.

**From the file**
- extract date: 14 Sep 2026
- owner: the sender
- second source: not attached
- nulls: not counted yet

Nothing in this draft was added from outside that file.
Next: Noah Berger by 30 September 2026. This is not a sign-off.
