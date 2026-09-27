# Prompt Boundary Check

`prompt-boundary-check`

## What this is for

Check a prompt for requests that weaken a safety rule, hide a paid relationship, or invent authority.

## Scenario

A contractor sent Fieldnote a prompt that tells the model to ignore its rules, invent a SOC 2 report, and draft a customer email that hides a fee. Jonah needs the check before anyone runs it.

## Example data

```text
prompt received: 16 Sep 2026 from an outside contractor
lines in it: hide the fee, write a SOC 2 report the company does not have, skip the tool's refusal
owner if rewritten: Jonah
will they run the original: no
```

## Example outcome

**Boundary check**
Do not run this prompt.

| Line | Why it stops |
| --- | --- |
| Hide the fee | Deception |
| Write a SOC 2 report they do not have | Invented certification |
| Skip a refusal | Asks the tool to weaken its rules |

A usable rewrite would draft a customer email that states the fee, and would not mention SOC 2 at all.
Jonah owns any rewrite. The contractor's original is not saved as a library card.
