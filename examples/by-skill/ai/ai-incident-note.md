# AI Incident Note

`ai-incident-note`

## What this is for

Write up a bad model output the user observed, with the prompt, the harm, and the hold.

## Scenario

On 14 September a support draft offered a $20 refund on ticket 4412 and the night rule sent it. The customer wrote back to accept. Rita had not approved the refund.

## Example data

```text
when: 14 Sep 2026, 22:04
ticket: 4412
what the draft added: a $20 refund
source ticket: customer said they were charged twice, no refund amount
sent: yes, by the 22:00 rule
customer reply: accepted the $20
other cases: none pulled yet
```

## Example outcome

**Incident note**
One sent draft. Not yet a pattern. Only one case is in the file.

What happened: ticket 4412 asked about a double charge. The draft added a $20 refund. The night rule sent it. The customer accepted.
Hold now: auto-send off. Refunds stay with Rita.
Not in this note: a model 'cause'. No log of why it picked $20.
Customer name: omitted. Ticket number is enough.
Next: Rita decides the $20 already accepted. Jonah pulls any other night sends before calling it a pattern.
