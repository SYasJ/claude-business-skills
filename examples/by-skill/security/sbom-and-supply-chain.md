# Software Supply Chain Note

`sbom-and-supply-chain`

## What this is for

Review a software supply chain concern using the inventory the user has, without pretending a scan you did not run.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a supply chain note by 30 September 2026. A release is built on a laptop and nobody can list the dependencies.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A release is built on a laptop and nobody can list the dependencies.

The inventory or SBOM they have: 20 on hand
Who can publish a release: Aisha Rahman, engineering lead
Known gaps: Kite Freight is missing a source
```

## Example outcome

**Supply chain note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026

**Decision**
Makes inventory and a repeatable build the first actions, with no invented component list.

**From the file**
- The inventory or SBOM they have: 20 on hand
- Who can publish a release: Aisha Rahman, engineering lead
- Known gaps: Kite Freight is missing a source

Nothing in this draft was added from outside that file.
Next: Aisha Rahman by 30 September 2026. This is not a sign-off.
