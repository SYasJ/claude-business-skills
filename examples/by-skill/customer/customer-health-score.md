# Customer Health Score

`customer-health-score`

## What this is for

Define a customer health score from signals that predict renewal risk, and show the formula.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs a health score definition by 30 September 2026. A health score marks accounts red and no one has a play for red.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A health score marks accounts red and no one has a play for red.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

## Example outcome

**Health score definition**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
A visible formula and a required human play for red, or a recommendation not to launch the score yet.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| ticket | 4412, 14 Sep 2026 | Needs confirmation |
| customer words | in the ticket | Carried into the draft |
| exception | not approved | Carried into the draft |
| card or password | not collected | Needs confirmation |

**How this draft was built**

**1. Start from the action a red score triggers. A score with no action is a toy**

**2. Choose signals they can collect without creepy surveillance**

**3. Show the formula. Hidden points are a finding**

**4. Weight only with evidence they have. If they have no history, call the score a hypothesis**

**5. Set a review so a red account gets a human, not only a color**

**Deliberately not done**
- A hidden formula.
- A score nobody acts on.
- Sensitive personal data as an input.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
