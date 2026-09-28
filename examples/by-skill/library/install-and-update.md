# Install and Update

`install-and-update`

## What this is for

Plan a local install or update of this library for a specific tool and domain.

## Scenario

Yasir Jilani, author at Practice Skills in Airdrie, needs an install plan by 30 September 2026. A user wants one command that downloads and executes an unknown installer.

## Example data

```text
From: Yasir Jilani, author
Organization: Practice Skills, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A user wants one command that downloads and executes an unknown installer.

The tool: the one named in the ask. Version and owner not recorded
The domain: plugins/finance/cash-flow-forecast, recorded 14 September 2026. No supporting file attached
Whether the install is user-level or project-level: plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not
Whether they want a dry run: plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not
```

## Example outcome

**Install plan**
To: Yasir Jilani, author, Practice Skills
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Uses the local Python installer, names the domain, and starts with a dry run.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The tool | the one named in the ask. Version and owner not recorded | Needs confirmation |
| The domain | plugins/finance/cash-flow-forecast, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Whether the install is user-level or project-level | plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not | Carried into the draft |
| Whether they want a dry run | plugins/finance/cash-flow-forecast. Partly documented: the what is written down, the who is not | Needs confirmation |

**How this draft was built**

**1. Recommend a domain install, not all skills, unless they explicitly want the full set and accept the description cost**

**2. Use the local installer. Do not recommend a remote pipe-to-shell command**

**3. Show the destination path for the tool they named**

**4. Prefer a dry run first**

**5. Updates replace files from this repository only. Do not tell them to mix in unreviewed third-party skills silently**

**Deliberately not done**
- curl piped to a shell.
- A required license key.
- Installing every skill by default.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Yasir Jilani by 30 September 2026. This is a draft, not a sign-off.
