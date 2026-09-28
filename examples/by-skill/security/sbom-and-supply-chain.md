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
How artifacts are built: Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since
Who can publish a release: Aisha Rahman, engineering lead
Known gaps: Access review Q3 is missing a source
```

## Example outcome

**Supply chain note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Makes inventory and a repeatable build the first actions, with no invented component list.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The inventory or SBOM they have | 20 on hand | Needs confirmation |
| How artifacts are built | Endpoint patch ring 2, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Who can publish a release | Aisha Rahman, engineering lead | Carried into the draft |
| Known gaps | Access review Q3 is missing a source | Needs confirmation |

**How this draft was built**

**1. Use only the inventory they provided. Do not claim you scanned the internet**

**2. Note missing owners, unpinned dependencies, and unpublished build steps**

**3. Recommend a repeatable build and a named publisher**

**4. Secrets in the build are a blocking finding. Do not print them**

**5. If they have no inventory, the first action is to generate one with their tools, not to invent components**

**Deliberately not done**
- A fake scan result.
- Invented components.
- Secrets printed in the note.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
