# Agent Task Card

`agent-task-card`

## What this is for

Bound an agent task: the inputs, the tools, the stop rules, and the human owner.

## Scenario

A spec says the support agent may read the ticket, email the customer, and issue a credit under $30. Jonah wants a card that a person can enforce.

## Example data

```text
task: turn one ticket into a reply draft
tools named: help desk read, model draft
tools in the spec that he will not grant: send email, issue credit
stop if: the ticket has no order id, or a card number is present
owner of a bad run: Jonah Park
done looks like: a draft Rita can accept or reject
```

## Example outcome

**Task card — support-reply-draft**
Done: a draft is waiting for Rita. Not done: an email sent, a credit posted.

Tools: read the ticket, write a draft. No other tool.
Stop: no order id, or a card number is still in the text. Do not draft. Ask a person.
Person required: sending, credits, refunds, deletes.
Owner: Jonah Park.
The earlier spec's send and credit lines are not on this card.
