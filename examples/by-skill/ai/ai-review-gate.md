# AI Review Gate

`ai-review-gate`

## What this is for

Place a human review where a model output can move money, a customer message, or a record.

## Scenario

Fieldnote set refund drafts to send at 22:00 if no one clicks. Rita works 08:00 to 17:00. Jonah needs the gate written down.

## Example data

```text
output: customer email draft
can trigger: a refund mention and a send
reviewer role: support lead
hours staffed: 08:00-17:00 America/Edmonton, weekdays
current rule: auto-send at 22:00
queue last week: 14 night tickets
```

## Example outcome

**Review gate**
Night drafts wait.

| Output | Reviewer | If absent |
| --- | --- | --- |
| Reply draft | Rita Santos | Holds until next staffed morning |
| Refund or credit | Rita Santos | Not sent. Not a model decision |
| Internal summary | Jonah Park | May sit unread. Does not email the customer |

Remove the 22:00 auto-send. A gate no one staffs is not a gate.
Next: Jonah turns auto-send off before 18 September.
