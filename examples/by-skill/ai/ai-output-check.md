# AI Output Check

`ai-output-check`

## What this is for

Check a model draft against the source text the user supplied.

## Scenario

Jonah has ticket 4418 and a model reply. The reply says the order shipped on 12 September and offers a $15 credit. The ticket does not say either.

## Example data

```text
ticket 4418: "charged twice on 12 Sep, order 4418. Please look."
draft: "Your order shipped on 12 September. I have applied a $15 credit."
claims that matter: ship date, credit
sender if approved: Rita
```

## Example outcome

**Output check**
Do not send.

| Draft claim | In the ticket? |
| --- | --- |
| Charged twice | Yes, customer said it |
| Order 4418 | Yes |
| Shipped 12 September | No |
| $15 credit | No |

Cut both added lines. A person may say they will look. They may not add a ship date or a credit from this check.
Next: Rita sends her own sentence, or a draft with those two lines gone.
