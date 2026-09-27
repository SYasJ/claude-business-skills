# Local Supplier Pick

`local-supplier-pick`

## What this is for

Pick between quotes the owner has, on price, lead time, and the terms on the page.

## Scenario

Diane has two quotes for oil. Redline is $4.10 a litre, 14 days, no return term on the page. A local yard is $4.40, 2 days, returns within 30 days. She will not use a third supplier who missed August.

## Example data

```text
quote A: Redline, $4.10/L, 14 days, return term not on the page
quote B: local yard, $4.40/L, 2 days, returns in 30 days
excluded: the August miss supplier
quality scores: none
```

## Example outcome

**Pick**
| Quote | Price | Lead | Returns |
| --- | --- | --- | --- |
| Redline | $4.10 | 14 days | not on the page |
| Local yard | $4.40 | 2 days | 30 days |

Recommend the local yard if she needs oil inside a week. The cheaper quote does not say she can send it back.
The August supplier stays out, as she asked.
No quality score. None was in the file.
