# Vehicle Handover

`handover-checklist-auto`

## What this is for

Check a handover against the items the dealer says the customer must see.

## Scenario

A delivery is booked for 3 p.m. The handover list includes a recall check. It was not run. The draft checklist marks recall clear so the keys can go.

## Example data

```text
delivery: 16 Sep 2026 15:00
list: walkaround, recall check, second key, payment receipt
done: walkaround, second key
not done: recall check
payment receipt: in the file
salesperson: Jon
draft mark: recall clear
```

## Example outcome

**Handover**
Keys do not go at 3 p.m. The recall check was not run. Clear is a false mark. Remove it.
Done: walkaround, second key, payment receipt in the file.
Open: recall check.
Who hands the keys after the check: Jon. Not before.
