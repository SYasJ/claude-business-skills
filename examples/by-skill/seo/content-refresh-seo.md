# Search Refresh

`content-refresh-seo`

## What this is for

Decide whether an old URL should be updated, from the query and the stale claim.

## Scenario

The page /permits/sidewalk still ranks for a query Diane wants. It says the fee is $50. The 2026 fee sheet says $75. Someone suggested a new URL so the old one can stay.

## Example data

```text
url: /permits/sidewalk
query she still wants: sidewalk display permit Airdrie
stale sentence: fee is $50
new fact: town fee sheet, 1 Jan 2026, $75
new URL suggested: /permits/sidewalk-2026
```

## Example outcome

**Refresh note**
Keep /permits/sidewalk. The query is the same job.
Replace $50 with $75 and cite the fee sheet. Add: updated 20 September 2026.
Do not make /permits/sidewalk-2026. A new URL is a new job. This is not one.
Do not show the old fee to people and the new fee to crawlers. One page, one fee.
