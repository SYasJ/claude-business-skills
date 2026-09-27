# Source Log

`source-log-news`

## What this is for

Log who said what, when, and whether it was on the record.

## Scenario

Jonah's notebook has a company statement and a sentence from a person who said they would not be named and would not be quoted.

## Example data

```text
source 1: Prairie Line statement, 15 Sep 2026, on the record as a document, turnaround 22 Sep, ten days
source 2: person at the gate, 15 Sep 16:40, said "do not quote me and do not name me"
callback: spokesperson, left message 15 Sep 17:10, no reply
document not in hand: any staffing list
```

## Example outcome

**Source log**
| Source | Status | Use |
| --- | --- | --- |
| 15 Sep statement | document | dates only |
| Gate conversation 16:40 | not for use | out |
| Spokesperson | no reply | do not write 'declined' |

The unnamed sentence does not go in the story.
No staffing list, so no staffing claim.
