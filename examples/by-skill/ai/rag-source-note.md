# RAG Source Note

`rag-source-note`

## What this is for

Decide which documents may sit in a retrieval set and which are stale or out of bounds.

## Scenario

The support bot's folder has a 2023 refund policy and the 2026 policy, plus a draft price list marked 'do not share'. Jonah needs the set cut down.

## Example data

```text
files: refund-policy-2023.pdf, refund-policy-2026-03.pdf, price-draft-2026-08 marked do not share, shipping-faq undated
owner: Jonah Park
topics the bot must not answer: legal threats, medical, card numbers
review date wanted: 1 Oct 2026
```

## Example outcome

**Source pack**
In the set: refund-policy-2026-03.pdf only, for refund questions.
Out: the 2023 policy. Out: the August price draft.
Shipping FAQ: out until someone dates it.
Refuse rather than guess: legal threats, medical questions, anything with a card number.
Owner: Jonah. Review the set on 1 October 2026.
Do not add web pages to fill a gap.
