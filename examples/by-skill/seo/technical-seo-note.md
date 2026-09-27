# Technical SEO Note

`technical-seo-note`

## What this is for

Turn crawl findings the user exported into a fix list a developer can accept or reject.

## Scenario

A crawl of 40 Harbor Goods URLs on 18 September shows 12 service URLs with an empty title and every /blog URL marked noindex. Diane says the blog block was a March test.

## Example data

```text
export: 40 URLs, 18 Sep 2026
empty title: 12 URLs, all under /services/
noindex: 9 URLs, all under /blog/
out of scope this month: a redesign
deploy owner: her contractor, Sam, Fridays
```

## Example outcome

**Fix list**
1. Title template on /services/. 12 URLs, one template, not 12 projects.
2. Remove the March test noindex on /blog/. 9 URLs.

Not this month: a redesign.
No ranking lift is claimed. The export does not show ranks.
Owner: Sam, Friday deploy. Diane checks one service URL and one blog URL after.
