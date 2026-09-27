# AI Eval Plan

`ai-eval-plan`

## What this is for

Plan an evaluation from examples the user already has, with a pass rule they can apply.

## Scenario

A slide says the support draft model is 95 percent accurate. Jonah has 12 real tickets and no labels. He needs a plan, not the slide.

## Example data

```text
examples on hand: tickets 4401-4412, exported 14 Sep 2026
labels: none
pass rule the lead will accept: no invented refund, no date that is not in the ticket
labeler: Rita, 2 hours on 22 Sep
will not test yet: tone score, legal advice, other languages
```

## Example outcome

**Eval plan**
The 95 percent comes off the slide. Nothing has been labeled.

Pass on each ticket: every dollar amount and date in the draft appears in the ticket. If not, fail.
Who labels: Rita, 22 September, tickets 4401-4412.
This is a 12-ticket smoke test. It does not prove a rate for the whole queue.
Not in this plan: tone, legal questions, languages other than the English in these tickets.
Next: Jonah does not quote a percent until Rita's marks are in a sheet.
