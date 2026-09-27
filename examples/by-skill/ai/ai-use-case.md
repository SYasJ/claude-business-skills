# AI Use Case

`ai-use-case`

## What this is for

Decide whether a task should use a model, who owns the failure, and what stays manual.

## Scenario

Fieldnote support wants a bot to issue refunds under $30 with no reviewer, because the night queue is slow. Jonah has one week of tickets and no accuracy test.

## Example data

```text
task: read a ticket and issue a refund under $30
wrong-answer cost: a refund the lead did not approve
reviewer today: Rita Santos, on shift 08:00-17:00 America/Edmonton
night volume: 14 tickets, 8-14 Sep 2026, none reviewed
data that would be sent: full ticket, including the card last-four on 6 of 14
test set: none
```

## Example outcome

**Use-case note**
Do not let the model issue refunds.

| Piece | Call |
| --- | --- |
| Draft a reply from the complaint text | Pilot, after the card last-four is stripped |
| Decide or send a refund | Stays with Rita |
| Night auto-send | No. 14 tickets is a queue fact, not a test |

Owner of a bad draft: Jonah. Reviewer before send: Rita.
Open: no labeled examples, so no accuracy claim.
Next: Rita confirms the day gate by 30 September 2026.
