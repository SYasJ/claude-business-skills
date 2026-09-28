# Logistics Exception

`logistics-exception`

## What this is for

Handle a logistics exception with the customer impact, the options, and a truthful status.

## Scenario

Diane Cho, supply lead at Harbor Goods in Airdrie, needs a logistics exception note by 30 September 2026. A carrier missed a pickup and the draft tells the customer the order is on time.

## Example data

```text
From: Diane Cho, supply lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A carrier missed a pickup and the draft tells the customer the order is on time.

The promise made: none written down beyond the ask
Options and costs they have: CAD 36 direct. Overhead not in this line
Who must be told: Diane Cho, supply lead
```

## Example outcome

**Logistics exception note**
To: Diane Cho, supply lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
States the miss, lists real options, and removes the on-time claim.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The promise made | none written down beyond the ask | Needs confirmation |
| Options and costs they have | CAD 36 direct. Overhead not in this line | Carried into the draft |
| Who must be told | Diane Cho, supply lead | Carried into the draft |

**How this draft was built**

**1. State the promise and the new fact**

**2. List options they can actually buy**  
wait, reroute, or partial ship.

**3. Show the customer impact in their words**

**4. Draft a status that does not promise a recovery time they do not have**

**5. Name the owner for the next update**

**Deliberately not done**
- A fake recovery time.
- No owner.
- Vague tracking language that hides the miss.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
