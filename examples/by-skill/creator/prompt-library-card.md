# Prompt Library Card

`prompt-library-card`

## What this is for

File a prompt card with the owner, the source, and the last test.

## Scenario

Fieldnote has three copies of the support prompt in three docs. Jonah wants one card so people stop pasting the old 'be helpful' line.

## Example data

```text
name: support-reply-draft
owner: Jonah Park
reviewer: Rita Santos
source allowed: ticket text
last failure: 4412, invented $20 refund, 14 Sep 2026
last edit: removed "be helpful and resolve"
status: test again on 4412 before anyone else uses it
```

## Example outcome

**Card — support-reply-draft**
Owner: Jonah Park. Reviewer: Rita Santos.
Use when: a support agent wants a draft from one ticket.
Source: that ticket only.
Must not: invent a refund, a credit, a policy, or a cause.
Last test: failed 14 September on ticket 4412.
Status: do not share the card until 4412 is rerun and has no dollar amount.
Old copies in the other two docs: delete the 'be helpful' line. This card is the one.
