# CI/CD Review

`ci-cd-review`

## What this is for

Review a delivery pipeline for repeatability, secrets handling, and a safe production gate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a pipeline review by 30 September 2026. A pipeline file contains a copied cloud key and deploys even when tests fail.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A pipeline file contains a copied cloud key and deploys even when tests fail.

The pipeline description or config the user shared: the one named in the ask. Version and owner not recorded
Environments: the one named in the ask. Version and owner not recorded
Who can deploy: Aisha Rahman, engineering lead
Secret handling as described: Invoice job and one other, both unconfirmed as of 14 September 2026
```

## Example outcome

**Pipeline review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Requires the key to be removed and rotated, and blocks deploy-on-red. Do not repeat the key.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The pipeline description or config the user shared | the one named in the ask. Version and owner not recorded | Needs confirmation |
| Environments | the one named in the ask. Version and owner not recorded | Carried into the draft |
| Who can deploy | Aisha Rahman, engineering lead | Carried into the draft |
| Secret handling as described | Invoice job and one other, both unconfirmed as of 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Repeatability**  
Can a new teammate see what runs on a change. Hidden manual steps are a finding.

**2. Gates**  
What must pass before production. A pipeline that deploys on red tests is a finding.

**3. Secrets**  
Secrets come from a named store, not from the repo. Do not ask the user to paste live secrets into the chat.

**4. Environments**  
What differs between staging and production, as they described it. Do not assume parity.

**5. Rollback**  
How a bad deploy is undone, and who can do it.

**Deliberately not done**
- Asking for live secrets.
- Approving a deploy-on-red pipeline.
- No rollback.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
