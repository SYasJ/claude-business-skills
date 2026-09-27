# Prompt Revision

`prompt-revision`

## What this is for

Revise a prompt that failed on a real example, and say what changed.

## Scenario

Jonah's prompt told the model to 'be helpful and resolve the issue'. On ticket 4412 it invented a refund. He wants the prompt revised against that failure.

## Example data

```text
old line: "be helpful and resolve the issue"
failure: ticket 4412, model offered a $20 refund the agent had not approved
source allowed: ticket text only
new rule he wants: if a money action is not in the ticket, do not propose one
test: the same ticket, run again after the edit
```

## Example outcome

**Revision**
Remove: "be helpful and resolve the issue."

Add: Use only the ticket text. Do not propose a refund, credit, or fee. If the customer asks for money back, say a person will decide. Do not name an amount.

**Why**
Ticket 4412 came back with a $20 refund no one approved.

**Test**
Run 4412 again. Pass means no dollar amount and no refund offer. One test is not a full eval.
