# Data Retention Schedule

`retention-schedule-data`

## What this is for

Draft a retention note from the policy the user already has, not from a guessed law.

## Scenario

A draft schedule says delete support tickets after 90 days because a blog recommended it. Fieldnote's customer contract in the folder does not mention ticket retention.

## Example data

```text
dataset: support.tickets
columns called out: email, home address on 6 of 14 sample rows
clause in the folder: customer contract 2026, no retention sentence
blog rule in the draft: 90 days
delete approver in their policy: privacy lead, role vacant
backups: nightly, kept 35 days, per Noah's note
```

## Example outcome

**Retention note**
support.tickets: period unset. The contract in the folder has no clause. The 90-day blog line is removed.
Backups: 35 days, from Noah's note. A live-table delete would not clear those until they age out.
Personal columns in the sample: email, home address. That is a flag, not a delete order.
Approver: privacy lead. The role is vacant, so nobody can approve a delete from this note.
Next: counsel or the contract owner writes the period. This note does not invent one.
