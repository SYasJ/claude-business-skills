# Meeting Operating System

`meeting-operating-system`

## What this is for

Redesign a meeting so it produces a decision or a documented exception, or cancel it.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a meeting system by 30 September 2026. A weekly meeting has 18 people and has not made a decision in a month.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A weekly meeting has 18 people and has not made a decision in a month.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

## Example outcome

**Meeting system**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Cuts attendees, requires a pre-read, and cancels the meeting if no decision remains.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Write the decision the meeting exists to make. If there is none, recommend cancellation or a written update**

**2. Cut attendees to deciders and the person with the facts**

**3. Require a one-page pre-read. No pre-read, no meeting**

**4. Exceptions only. Do not tour green metrics**

**5. End with owners and dates**

**Deliberately not done**
- A status meeting with no decision.
- Inviting everyone.
- No pre-read.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
