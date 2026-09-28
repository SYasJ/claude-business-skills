# Supplier Quality Note

`supplier-quality`

## What this is for

Write a supplier quality note that states the defect, the containment, and the evidence requested.

## Scenario

Gus Moretti, plant manager at Redline Parts in Nisku, needs a supplier quality note by 30 September 2026. A note calls the supplier negligent and does not describe the defect.

## Example data

```text
From: Gus Moretti, plant manager
Organization: Redline Parts, Nisku
Date: 14 September 2026
Needed by: 30 September 2026

A note calls the supplier negligent and does not describe the defect.

line: line 2
lot: 26-0914
hold: open
count: the tally, not the order
```

## Example outcome

**Supplier quality note**
To: Gus Moretti, plant manager, Redline Parts
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Describes the defect, requests containment by a date, and removes the insult.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| line | line 2 | Needs confirmation |
| lot | 26-0914 | Carried into the draft |
| hold | open | Carried into the draft |
| count | the tally, not the order | Needs confirmation |

**How this draft was built**

**1. State the defect with evidence they have**

**2. Identify lots without inventing shipment history**

**3. Ask for containment and a cause, with a date**

**4. Do not accuse fraud. Ask for facts**

**5. Share only the data the supplier needs**

**Deliberately not done**
- A fraud accusation with no evidence.
- Invented shipment history.
- A request with no date.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Gus Moretti by 30 September 2026. This is a draft, not a sign-off.
