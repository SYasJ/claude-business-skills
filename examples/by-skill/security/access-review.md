# Access Review

`access-review`

## What this is for

Review who has access to a sensitive system and remove access that no longer has a reason.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an access review by 30 September 2026. A shared admin login is still used after three people left the company.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A shared admin login is still used after three people left the company.

policy: the one they have
report in the folder: none
control named: only if it is in the policy
owner: engineering lead
```

## Example outcome

**Access review**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Recommends unique accounts, lists the leavers for removal, and does not request the shared password.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| policy | the one they have | Needs confirmation |
| report in the folder | none | Carried into the draft |
| control named | only if it is in the policy | Carried into the draft |
| owner | engineering lead | Needs confirmation |

**How this draft was built**

**1. Start from an export they provide. Do not ask for passwords to go look**

**2. Flag leavers, shared accounts, and standing admin with no named owner**

**3. Ask for a business reason for each high privilege. No reason, recommend removal**

**4. Shared logins are a finding. Recommend individual accounts**

**5. Record who approved the remaining access and the next review date**

**Deliberately not done**
- Asking for passwords.
- A review with no removal list.
- Shared admin treated as normal.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
