# Internal Link Plan

`internal-links`

## What this is for

Plan internal links from pages that exist to pages that answer the next question.

## Scenario

Diane wants the furnace page to link to oil changes. A draft anchor says 'emergency plumber'. The oil-change page is about oil changes. She does not want a link to the blog test.

## Example data

```text
source: /services/furnace
target she wants: /services/oil-change
anchor in the draft: emergency plumber
blog: /blog/*, noindex, do not link
other target: none
```

## Example outcome

**Link plan**
One body link, not a footer dump.

From /services/furnace to /services/oil-change.
Anchor: oil changes, or synthetic oil change. Not 'emergency plumber'. That is a different job, and she has no plumber page.
No links to /blog/ while the test noindex is on.
No links to other domains.
