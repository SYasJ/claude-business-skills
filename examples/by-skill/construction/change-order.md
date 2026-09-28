# Change Order Brief

`change-order`

## What this is for

Brief a change order with the cause, the cost basis they have, and the time effect.

## Scenario

Tom Reilly, site lead at Birch Siteworks in Cochrane, needs a change-order brief by 30 September 2026. A superintendent wants a change order with a round number and no backup.

## Example data

```text
From: Tom Reilly, site lead
Organization: Birch Siteworks, Cochrane
Date: 14 September 2026
Needed by: 30 September 2026

A superintendent wants a change order with a round number and no backup.

site: Birch, Cochrane
safety item: stays open
quantity: their takeoff
date: the look-ahead
```

## Example outcome

**Change-order brief**
To: Tom Reilly, site lead, Birch Siteworks
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Blocks the round number until backup exists and records the direction to proceed.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| site | Birch, Cochrane | Needs confirmation |
| safety item | stays open | Carried into the draft |
| quantity | their takeoff | Carried into the draft |
| date | the look-ahead | Needs confirmation |

**How this draft was built**

**1. State the cause and who directed the work**

**2. Attach cost backup they have. Do not invent unit rates**

**3. Show time effect separately from cost**

**4. Identify contract clauses only if they pasted them**

**5. Mark entitlement as a question for the contract administrator**

**Deliberately not done**
- Invented rates.
- Hidden changes.
- An entitlement ruling from memory.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Tom Reilly by 30 September 2026. This is a draft, not a sign-off.
