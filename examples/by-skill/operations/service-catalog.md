# Service Catalog Entry

`service-catalog`

## What this is for

Write a service catalog entry that tells an internal customer what they can request, how long it takes, and what is not included.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a service catalog entry by 30 September 2026. An internal team is judged on a two-day turnaround it has never hit.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

An internal team is judged on a two-day turnaround it has never hit.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

## Example outcome

**Service catalog entry**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
An entry with a truthful lead time or an explicit unknown, plus exclusions.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Describe the service as an outcome, not as a department name**

**2. Say who may request it and how**

**3. Publish a lead time they have evidence they can meet. If they cannot, mark the time as unknown**

**4. List exclusions so hidden work does not arrive as emergencies**

**5. Name the owner and the escalation**

**Deliberately not done**
- A catalog with no exclusions.
- A lead time they cannot meet.
- A request path only insiders know.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
