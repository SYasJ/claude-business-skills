# Index Coverage

`index-coverage`

## What this is for

Read an index export and say which URLs are out and why the export says so.

## Scenario

Diane exported coverage on 18 September. 30 URLs are excluded. 9 are the blog, reason noindex. The other 21 are old tag URLs she says do not matter.

## Example data

```text
export date: 18 Sep 2026
excluded: 30
reason noindex: 9, all /blog/
reason crawled not indexed: 21, all /tag/
she cares about: the 9 blog URLs
she does not care about: /tag/
template owner: Sam
known test: blog noindex added in March
```

## Example outcome

**Index note**
The 9 blog URLs are out because of noindex. That matches the March test. Remove it.
The 21 tag URLs are in the export and out of scope. Do not spend the month on them.
This note does not say the blog will rank after the tag is removed. Indexing is not a rank.
Owner: Sam. Diane rechecks one blog URL after the Friday deploy.
