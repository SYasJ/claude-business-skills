# Recall Owner Note

`recall-owner-note`

## What this is for

Draft the customer note for a recall using the notice the dealer has, not a homemade defect claim.

## Scenario

Notice 26-118 says park the vehicle and wait for the remedy. Bright Axle matched two VINs. A draft tells those owners they can keep driving until the part arrives.

## Example data

```text
notice: 26-118
remedy in the notice: park, wait for the part, dealer will call
VINs matched: 2, both in her sold file
failure rate: not in the notice
booking: Carla's desk, 403-555-0199
draft line: you can drive until the part arrives
```

## Example outcome

**Owner note**
Notice 26-118 says park the vehicle. This note repeats that. It does not say they can keep driving.

We matched two VINs in our file. This note goes to those two owners only.
The notice does not give a failure rate. None is added.
To book: call Carla's desk, 403-555-0199.
This note does not decide that a recall exists. It follows the notice they have.
