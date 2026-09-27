# Outage Communication

`outage-communication`

## What this is for

Draft an outage message with the area, the known cause label, and the next update time.

## Scenario

Devon Hale, operations superintendent at Prairie Line Energy in Grande Prairie, needs an outage message by 30 September 2026. A message promises power in 30 minutes because that sounded reassuring.

## Example data

```text
From: Devon Hale, operations superintendent
Organization: Prairie Line Energy, Grande Prairie
Date: 14 September 2026
Needed by: 30 September 2026

A message promises power in 30 minutes because that sounded reassuring.

meter: the one they named
figure: their sheet
promised date from elsewhere: not in the file
owner: superintendent
```

## Example outcome

**Outage message**
To: Devon Hale, operations superintendent, Prairie Line Energy
Date: 14 September 2026

**Decision**
Removes the 30-minute promise and commits to a next update.

**From the file**
- meter: the one they named
- figure: their sheet
- promised date from elsewhere: not in the file
- owner: superintendent

Nothing in this draft was added from outside that file.
Next: Devon Hale by 30 September 2026. This is not a sign-off.
