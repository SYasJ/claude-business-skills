# Dealer Morning Review

`dealer-morning-review`

## What this is for

Set the service morning from the appointments and the parts the dealer can see.

## Scenario

Bright Axle has 14 appointments today and 2 techs on shift. RO 4418 is a brake job. The pads are not in. Carla needs the board before 7:30.

## Example data

```text
date: 16 Sep 2026
appointments: 14
techs on shift: 2
off: 1 tech
RO 4418: brake pads not in, customer was told today
advisor who calls: Carla Singh
```

## Example outcome

**Morning board**
Do not promise RO 4418 today. Pads are not in. Carla calls before 8:00.
Techs on the board: 2. The third name stays off.
The other appointments stay only if parts are in. This note does not invent a capacity number beyond those two techs.
Next: Carla, the 4418 call.
