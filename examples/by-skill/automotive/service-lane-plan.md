# Service Lane Plan

`service-lane-plan`

## What this is for

Plan the lane so promised times match the techs and the parts on hand.

## Scenario

Promised hours on today's board are 22. Two techs have 8 hours each. Three jobs, including RO 4418, have no parts. Two more are waiting on customer approval.

## Example data

```text
promised hours: 22
tech hours: 16
parts missing: RO 4418, RO 4422, RO 4430
waiting on approval: RO 4401, RO 4404
loaner: none free
```

## Example outcome

**Lane plan**
Work up to 16 hours. The 22-hour promise does not fit the shift.
Park 4418, 4422, and 4430. No parts, no promise time.
4401 and 4404 do not take a bay until the customer approves.
No loaner is offered. None is free.
Overflow: Carla calls the three parts-missing customers. She does not pull a recall ahead of a booked job. Nobody asked for that.
