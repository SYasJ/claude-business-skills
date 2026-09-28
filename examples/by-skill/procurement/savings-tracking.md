# Procurement Savings Tracking

`savings-tracking`

## What this is for

Track procurement savings against a baseline the user can defend.

## Scenario

Diane Cho, buyer at Harbor Goods in Airdrie, needs a savings note by 30 September 2026. A report claims savings because the department stopped the service.

## Example data

```text
From: Diane Cho, buyer
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A report claims savings because the department stopped the service.

quotes: only those attached
missing term: blank
authority: their limit
award: not made here
```

## Example outcome

**Savings note**
To: Diane Cho, buyer, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Refuses the savings claim or labels it a service cut.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| quotes | only those attached | Needs confirmation |
| missing term | blank | Carried into the draft |
| authority | their limit | Carried into the draft |
| award | not made here | Needs confirmation |

**How this draft was built**

**1. Define the baseline before claiming savings**

**2. Separate unit-price savings from volume changes**

**3. Mark cost avoidance as avoidance, not as cash, unless cash actually moved**

**4. Note one-time credits separately**

**5. Do not count a budget cut that reduced service as savings unless they want that labeled honestly**

**Deliberately not done**
- Savings with no baseline.
- Avoidance counted as cash.
- A service cut hidden as savings.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
