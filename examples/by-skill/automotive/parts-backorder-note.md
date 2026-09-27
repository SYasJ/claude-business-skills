# Parts Backorder

`parts-backorder-note`

## What this is for

Tell the advisor what to say when a part is not in and a promise date is already on the RO.

## Scenario

RO 4418 was promised today. The brake pads are backordered. The supplier ETA field is blank. No loaner is free.

## Example data

```text
RO: 4418
part: front pads
promise already made: today, 16 Sep 2026
ETA: blank
loaner: none free
advisor: Carla Singh
```

## Example outcome

**What Carla can say**
The pads for RO 4418 are not in. I do not have a date. I am pulling today's promise.

Do not add a Friday ETA. The field is blank.
Do not offer a loaner. None is free.
Next: Carla makes the call. The RO promise date comes off today's board.
