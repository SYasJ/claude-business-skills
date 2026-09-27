# Demand Response Offer

`demand-response-offer`

## What this is for

Review a demand-response offer against the load the user can actually drop.

## Scenario

An offer pays for a 500 kW drop on weekday afternoons. The site log shows they can shed 200 kW by turning off two pumps. The offer includes a penalty if they miss the drop. The payment figure is $40 per kW-month.

## Example data

```text
offer drop: 500 kW
hours: weekdays 14:00-18:00
load they can drop: 200 kW, two pumps, log from August
penalty: in the offer, highlighted
payment: $40 per kW-month, in the offer
```

## Example outcome

**Offer note**
Do not sign for 500 kW. The log shows 200.
If they sign, the number has to be a drop they have shown. 200 is the figure in the file.
Penalty: it is in the offer. Do not leave it out of the conversation.
Payment in the offer: $40 per kW-month. This note does not improve it.
Hours match a window they can staff only if Devon says the pumps can stop at 14:00. He has not said that yet.
