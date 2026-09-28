# Deal Desk Review

`deal-desk-review`

## What this is for

Review a nonstandard deal for margin, precedent, and delivery risk before anyone signs.

## Scenario

Samir Qureshi, account executive at Fieldnote in Edmonton, needs a deal desk note by 30 September 2026. Sales wants a custom integration included free to win a logo, and delivery has not estimated it.

## Example data

```text
From: Samir Qureshi, account executive
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Sales wants a custom integration included free to win a logo, and delivery has not estimated it.

account: Harbor Goods
last meeting: 9 Sep 2026, no dated next step
proof: one email
discount asked: 15 percent, not approved
```

## Example outcome

**Deal desk note**
To: Samir Qureshi, account executive, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Conditions any approval on a delivery estimate and names the precedent risk of free custom work.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| account | Harbor Goods | Needs confirmation |
| last meeting | 9 Sep 2026, no dated next step | Carried into the draft |
| proof | one email | Carried into the draft |
| discount asked | 15 percent, not approved | Needs confirmation |

**How this draft was built**

**1. Restate the ask**  
What is nonstandard, in one sentence.

**2. Margin**  
Compute from their costs and price. If cost is missing, the review is incomplete. Do not invent a cost.

**3. Delivery**  
Can the team deliver the promised start date and scope. A yes from sales is not a yes from delivery.

**4. Precedent**  
Who else will ask for the same term if this is signed. Write that consequence.

**5. Give-get**  
What the company gets for the concession.

**Deliberately not done**
- Approving a discount with no margin math.
- Ignoring delivery capacity.
- An approval that pretends not to set a precedent.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Samir Qureshi by 30 September 2026. This is a draft, not a sign-off.
