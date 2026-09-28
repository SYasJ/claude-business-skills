# Liquidity Ladder

`liquidity-ladder`

## What this is for

Build a simple liquidity ladder from cash, committed inflows, and committed outflows.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a liquidity ladder by 30 September 2026. A ladder treats an undrawn line as money already in the account.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A ladder treats an undrawn line as money already in the account.

run: 14 Sep 2026
changed payee: email this morning, not verified
password: not collected
hold: that line
```

## Example outcome

**Liquidity ladder**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Separates the line from cash and flags the first short bucket.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| run | 14 Sep 2026 | Needs confirmation |
| changed payee | email this morning, not verified | Carried into the draft |
| password | not collected | Carried into the draft |
| hold | that line | Needs confirmation |

**How this draft was built**

**1. Group by the buckets they care about, such as this week and this month**

**2. Include only committed items unless an uncommitted item is clearly labeled**

**3. Show facilities separately from cash**

**4. Flag the first bucket that fails their minimum**

**5. Do not move money or request credentials**

**Deliberately not done**
- A facility shown as cash.
- Uncommitted inflow shown as certain.
- A credential request.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
