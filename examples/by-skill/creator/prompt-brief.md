# Prompt Brief

`prompt-brief`

## What this is for

Brief a prompt the person will run, with the job, the source, and the stop rule.

## Scenario

Jonah at Fieldnote wants a prompt that turns a customer's own support note into a reply draft. He does not want the model to invent a refund. The source is one note the customer wrote.

## Example data

```text
job: draft a reply the agent can edit
source: the customer note in the ticket, nothing else
must not: invent a refund, a policy, or a cause
tone: short, no blame
reviewer: Rita, support lead, before send
ticket sample: "charged twice on 12 Sep, order 4412"
```

## Example outcome

**Prompt brief**
Job: draft a reply. A person sends it.

Source: only the text in the ticket. If the order is not in the ticket, the draft says it is not in the ticket.

Stop: do not offer a refund, a credit, or a cause. Rita decides those.
Tone: short. No blame.

Review: Rita reads it before it is sent. The draft is not the reply.
