# Plan Limit Note

`plan-limit-note`

## What this is for

Write the limit a plan enforces, and the message the user sees when they hit it.

## Scenario

Pro blocks an export at 5,000 rows. The message in the product still says 'You can export everything on Pro'. There is no overage price.

## Example data

```text
plan: Pro
limit: 5000 rows, then the export button stops
current message: You can export everything on Pro
overage price: none set
who changes the limit: Jonah
```

## Example outcome

**Limit**
Pro blocks at 5,000 rows. The button stops. It does not bill an overage. None is set.

Message: This export stops at 5,000 rows on Pro. It does not say unlimited.
Who changes the limit: Jonah. The pricing page has to say the same number.
