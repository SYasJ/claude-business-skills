# Search Log

`source-search-log`

## What this is for

Log the searches and the dates so a review can see what was looked for.

## Scenario

A methods draft says Nia searched PubMed, Scopus, and Web of Science on 2 September. Her notebook shows PubMed and Scopus only. Scopus returned zero hits. Web of Science is not in the notebook.

## Example data

```text
who: Dr. Nia Okonkwo
date in the draft: 2 Sep 2026
PubMed: query "small shop hiring interview", 42 hits, notebook page 3
Scopus: same query, 0 hits, notebook page 3
Web of Science: not in the notebook
filters: English, 2018-2026, written on page 3
```

## Example outcome

**Search log**
| Database | Date | Query | Hits |
| --- | --- | --- | --- |
| PubMed | 2 Sep 2026 | small shop hiring interview | 42 |
| Scopus | 2 Sep 2026 | small shop hiring interview | 0 |

Filters: English, 2018-2026.
Web of Science comes out of the methods draft. It was not opened.
Zero stays in the log. A log is not a review.
