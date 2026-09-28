# Disaster Recovery Brief

`disaster-recovery-brief`

## What this is for

Brief a disaster recovery choice for one system, including the recovery point they are actually buying.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a disaster recovery brief by 30 September 2026. A team claims a four-hour recovery and has never failed over the identity provider.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A team claims a four-hour recovery and has never failed over the identity provider.

The system: the one named in the ask. Version and owner not recorded
The recovery point and time they need: five working days, due 30 September 2026
What they have tested: A team claims a four-hour recovery and has never failed over the identity provider
Dependencies: SOP 118 receiving and one other, both unconfirmed as of 14 September 2026
```

## Example outcome

**Disaster recovery brief**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Downgrades the claim to untested and names the identity dependency.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The system | the one named in the ask. Version and owner not recorded | Needs confirmation |
| The recovery point and time they need | five working days, due 30 September 2026 | Carried into the draft |
| What they have tested | A team claims a four-hour recovery and has never failed over the identity provider | Carried into the draft |
| Dependencies | SOP 118 receiving and one other, both unconfirmed as of 14 September 2026 | Needs confirmation |

**How this draft was built**

**1. Define the business process the system serves**

**2. Record the recovery point and time they want, labeled as a want until a test proves it**

**3. List dependencies. A restored app with no identity provider is not recovered**

**4. Note the last test and its result. No test, no claim of readiness**

**5. Identify the gap between the want and the evidenced capability**

**Deliberately not done**
- Claiming a recovery time that was never tested.
- Ignoring a dependency.
- An invented price.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
