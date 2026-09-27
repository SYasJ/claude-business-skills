# Headline Check

`headline-check`

## What this is for

Check a headline against the story's sourced facts.

## Scenario

The copy desk wrote 'Plant cuts safety staff before 10-day shutdown'. The story only has the 22 September start and the ten-day length from the statement.

## Example data

```text
headline: Plant cuts safety staff before 10-day shutdown
sourced: turnaround starts 22 Sep 2026, ten days, company statement 15 Sep
not sourced: safety staff, cuts, blame
deadline: 19 Sep 16:00
```

## Example outcome

**Headline check**
No. 'Cuts safety staff' is not in the story.

Options that match:
1. Company says plant turnaround starts 22 September
2. Statement: ten-day turnaround from Monday

Use 1. It is the date in the document.
Do not add a cause to make the line sharper.
