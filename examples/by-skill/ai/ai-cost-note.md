# AI Cost Note

`ai-cost-note`

## What this is for

Estimate the cost of a proposed AI workflow from the user's prices and volumes.

## Scenario

A vendor demo says the bot will save $40,000 a month. Jonah has a price of $0.01 per call and last month's ticket count. He has not measured minutes saved.

## Example data

```text
price: $0.01 CAD per call, quote dated 2 Sep 2026, not a signed order
volume: 3,200 tickets in August 2026
calls per ticket if they draft once: 1
human review: still required, minutes not measured
claimed savings: $40,000 a month, no worksheet
cap they can stomach: $100 a month
```

## Example outcome

**Cost note**
August calls at one draft each: 3,200 x $0.01 = $32. Under the $100 cap if they stay at one call and this quote.

The $40,000 savings is not in this note. Minutes saved were not measured.
Not in the price: retries, a second model, or a seat fee. None were on the quote.
High case: if they call the model three times per ticket, $96. Still under the cap, still not a savings claim.
Next: Jonah does not repeat the $40,000 figure.
