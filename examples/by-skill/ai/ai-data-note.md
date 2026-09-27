# AI Data Note

`ai-data-note`

## What this is for

Say what may be pasted into a model and what must stay in the source system.

## Scenario

Agents want to paste the whole ticket into a model. Six of fourteen sample tickets include a card last-four and a home address. Vendor terms are not in the folder.

## Example data

```text
fields in a ticket: complaint text, order id, card last-four, home address, agent notes
vendor terms in the folder: none
retention promised: not documented
who pastes today: any agent on shift
sample: 14 tickets, 8-14 Sep 2026
```

## Example outcome

**Data note**
Allowed in the paste: complaint text and order id.
Strip before paste: card last-four, home address.
Agent notes: stay in the help desk until Jonah says otherwise.
Vendor retention: open. No terms in the folder, so do not write 'they don't train on it'.
Who may paste: an agent on shift, after the strip.
Source of truth: the help desk, not the chat window.
