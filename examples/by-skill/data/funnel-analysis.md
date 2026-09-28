# Funnel Analysis

`funnel-analysis`

## What this is for

Analyze a funnel with explicit step definitions and a focus on the biggest leak that the team can affect.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a funnel analysis by 30 September 2026. A funnel shows a huge drop between two events that can fire in either order.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A funnel shows a huge drop between two events that can fire in either order.

extract date: 14 Sep 2026
owner: the sender
second source: not attached
nulls: not counted yet
```

## Example outcome

**Funnel analysis**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Calls the funnel unordered, pauses the product blame, and asks for a sequenced definition.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| extract date | 14 Sep 2026 | Needs confirmation |
| owner | the sender | Carried into the draft |
| second source | not attached | Carried into the draft |
| nulls | not counted yet | Needs confirmation |

**How this draft was built**

**1. Write the step definitions. If two steps can fire out of order, say the funnel is messy**

**2. Compute conversion only from counts they gave. Show the arithmetic**

**3. Find the largest loss of people, not the largest percentage on a tiny step, and say which one you are using**

**4. Note tracking gaps before blaming the product**

**5. Separate a new-user funnel from a returning-user funnel if they differ in the data**

**Deliberately not done**
- Blaming the product when tracking is broken.
- A funnel with undefined steps.
- Invented counts.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
