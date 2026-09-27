# News Budget

`news-budget`

## What this is for

Rank stories the desk can staff today from the sources they have, not from the stories they wish they had.

## Scenario

Five items are on the board. Two have documents. Three reporters are on shift, and one is already out on a fire briefing. Four slots are open on the site.

## Example data

```text
candidates: plant turnaround (statement in hand), fare change (airline PDF in hand), school board rumor (no source), shop-fire follow (reporter out), council land vote (agenda PDF, no vote yet)
staff: 3 reporters, 1 already on the fire
slots: 4
```

## Example outcome

**Budget**
Staff two. Leave the other slots empty.

| Story | Source | Who |
| --- | --- | --- |
| Turnaround dates | statement | Jonah |
| Fare change | airline PDF | second reporter |

Not today: the school rumor, the land vote that has not happened, a second fire story. The reporter is already out and has not filed.
A full rundown is not the goal. An empty slot is better than an unsourced item.
