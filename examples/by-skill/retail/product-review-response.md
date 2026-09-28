# Product Review Response

`product-review-response`

## What this is for

Draft a response to a customer product review that acknowledges the experience and does not argue.

## Scenario

Diane Cho, store lead at Harbor Goods in Airdrie, needs a review response by 30 September 2026. A one-star review says the zipper broke in a week. The response says "we're sorry you feel that way."

## Example data

```text
From: Diane Cho, store lead
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A one-star review says the zipper broke in a week. The response says "we're sorry you feel that way."

store: Harbor Goods, Airdrie
price: shelf price
stock: the count
review: not invented
```

## Example outcome

**Review response**
To: Diane Cho, store lead, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Acknowledges the zipper, says what the warranty covers, and invites a direct contact.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| store | Harbor Goods, Airdrie | Needs confirmation |
| price | shelf price | Carried into the draft |
| stock | the count | Carried into the draft |
| review | not invented | Needs confirmation |

**How this draft was built**

**1. Acknowledge what the reviewer said without paraphrasing it back sarcastically**

**2. Do not argue about whether the experience happened**

**3. If an issue is known and fixed, say so specifically**

**4. If resolution is possible, invite a private conversation and name the contact method**

**5. Keep it short. A long response looks defensive**

**Deliberately not done**
- Arguing with the reviewer.
- A copy-paste template.
- Promising a fix you cannot deliver.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
