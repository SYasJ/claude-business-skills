# Live Update

`live-blog-update`

## What this is for

Add one timestamped update from a new sourced fact, without mixing it into older items.

## Scenario

At 11:00 the live blog guessed the turnaround might start Sunday. At 14:10 a spokesperson confirmed Monday 22 September. Jonah needs the update line.

## Example data

```text
earlier item: 11:00, "may start Sunday", no source named
new fact: spokesperson, on the record, 14:10, starts Monday 22 Sep, ten days
still unconfirmed: staffing, cause, which units
clock zone: America/Edmonton
```

## Example outcome

**Update — 14:10**
A spokesperson said on the record that the turnaround starts Monday 22 September and is planned for ten days.

Still unconfirmed: staffing, cause, which units. Do not add them here.

Correction: the 11:00 item guessed Sunday and named no source. It stands as a bad item. Do not edit it into Monday. Point readers to this line.
