# Keyword Map

`keyword-map`

## What this is for

Map queries to pages the user already has, using only queries they exported or listed.

## Scenario

Diane listed eight queries for Harbor Goods. The site has a furnace page and an oil-change page. Two queries match neither.

## Example data

```text
pages: /services/furnace, /services/oil-change
queries she listed 18 Sep 2026:
furnace repair Airdrie -> furnace page
furnace tune-up Airdrie -> furnace page
emergency furnace Airdrie -> furnace page
oil change Airdrie -> oil-change page
synthetic oil change -> oil-change page
oil change price -> oil-change page
plumber Airdrie -> no page
roof repair -> no page
```

## Example outcome

**Query map**
| Query | Page |
| --- | --- |
| furnace repair Airdrie | /services/furnace |
| furnace tune-up Airdrie | /services/furnace |
| emergency furnace Airdrie | /services/furnace |
| oil change Airdrie | /services/oil-change |
| synthetic oil change | /services/oil-change |
| oil change price | /services/oil-change |

Gaps, not new doorway URLs: plumber Airdrie, roof repair. She does not do that work. Do not make pages for them.
Do not point furnace queries at the oil-change page.
