# Dependency Upgrade

`dependency-upgrade`

## What this is for

Plan a dependency upgrade around risk, changelog, and rollback, not around a version number badge.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an upgrade plan by 30 September 2026. A bot opened a major upgrade and nobody has read the changelog.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A bot opened a major upgrade and nobody has read the changelog.

The dependency and versions: Checkout service is open. Invoice job was raised verbally and never logged
Why the upgrade is happening: A bot opened a major upgrade and nobody has read the changelog
Breaking changes the user found: requested 14 September 2026. Not yet approved
How the app is tested: Invoice job, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Upgrade plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the merge until breaking changes are read and a rollback is named.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The dependency and versions | Checkout service is open. Invoice job was raised verbally and never logged | Needs confirmation |
| Why the upgrade is happening | A bot opened a major upgrade and nobody has read the changelog | Carried into the draft |
| Breaking changes the user found | requested 14 September 2026. Not yet approved | Carried into the draft |
| How the app is tested | Invoice job, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Reason**  
Security fix, bug, or support window, as the user stated. Do not invent a CVE.

**2. Breaking changes**  
List the ones they found in notes or a changelog they pasted. If none were read, the plan starts by reading them.

**3. Blast radius**  
Which parts of the product use it.

**4. Test**  
The regression checks that matter for that blast radius.

**5. Rollback**  
How to return to the old version, and what data changes would make rollback hard.

**Deliberately not done**
- Inventing a CVE.
- Recommending curl piped to a shell.
- An upgrade with no rollback story.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
