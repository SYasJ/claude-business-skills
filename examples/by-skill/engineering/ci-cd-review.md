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

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
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
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

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
