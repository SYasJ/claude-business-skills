# Policy Writer

`policy-writer`

## What this is for

Draft a policy people can follow, with an owner, an exception path, and a review date.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a policy draft by 30 September 2026. A draft cites several laws from memory to sound serious.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A draft cites several laws from memory to sound serious.

event: the one in the ask, not a one-word label
owner: blank
control: not named
score: not invented
```

## Example outcome

**Policy draft**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the invented citations, names an owner, and stays short enough to follow.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| event | the one in the ask, not a one-word label | Needs confirmation |
| owner | blank | Carried into the draft |
| control | not named | Carried into the draft |
| score | not invented | Needs confirmation |

**How this draft was built**

**1. State the purpose and who it applies to**

**2. Write requirements as behaviors**

**3. Point to the procedure for how. The policy should not be a novel**

**4. Add an exception path and an owner**

**5. Set a review date**

**Deliberately not done**
- A policy with no owner.
- Invented legal citations.
- Requirements nobody can perform.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
