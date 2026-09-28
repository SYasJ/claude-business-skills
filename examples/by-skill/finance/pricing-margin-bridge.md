# Pricing and Margin Bridge

`pricing-margin-bridge`

## What this is for

Trace price, mix, and cost so a margin change has a cause and a commercial response.

## Scenario

Mara Chen, founder at Northline Studio in Calgary, needs a price-mix-cost bridge by 30 September 2026. Gross margin fell two points and sales says it was only product mix.

## Example data

```text
From: Mara Chen, founder
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

Gross margin fell two points and sales says it was only product mix.

Revenue and cost for two periods: month ending 14 September 2026
Price and volume detail if available: CAD 180
Known mix shifts: Harbor & Co receipt. Stated in the ask, not documented anywhere else
Discount or rebate practice: 55 in the last period. No prior period attached, so no trend
```

## Example outcome

**Price-mix-cost bridge**
To: Mara Chen, founder, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Shows what portion is mix, price, and cost on the available data, plus one commercial response.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Revenue and cost for two periods | month ending 14 September 2026 | Needs confirmation |
| Price and volume detail if available | CAD 180 | Carried into the draft |
| Known mix shifts | Harbor & Co receipt. Stated in the ask, not documented anywhere else | Carried into the draft |
| Discount or rebate practice | 55 in the last period. No prior period attached, so no trend | Needs confirmation |

**How this draft was built**

**1. Start with the margin change**  
State gross margin or contribution change in the user's currency and in points.

**2. Separate price, volume, and mix**  
Use the detail the user has. If mix cannot be seen, say the bridge is incomplete rather than forcing a fake split.

**3. Put discounts in price**  
A discount is a price decision. Do not hide it in cost.

**4. Isolate cost inflation**  
Input cost changes sit on their own step, with the user's evidence.

**5. Recommend one commercial move**  
A price test, a mix target, or a cost action. Not all three at full strength unless the user has capacity.

**Deliberately not done**
- A margin story with no bridge.
- Blaming mix when the data cannot show mix.
- Recommending a price increase with no customer consequence.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Mara Chen by 30 September 2026. This is a draft, not a sign-off.
