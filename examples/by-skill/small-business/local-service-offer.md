# Local Service Offer

`local-service-offer`

## What this is for

Write a local offer from the price and the hours the owner can honor.

## Scenario

An ad draft says half-price oil changes all month. Diane priced $49 for Fridays only, and the lane can do six cars a day. The door is closed Sunday.

## Example data

```text
service: oil change
price she will honor: $49, Fridays in September 2026
capacity: 6 cars
door: closed Sunday
draft ad: half price, all month
half-price figure: she did not set one
```

## Example outcome

**Offer**
Friday oil changes, $49, six cars. September Fridays only.

Not the offer: half price, all month, Sunday.
Six is the cap. When six are booked, the ad stops for that Friday. No fake 'only two left' if the book is empty.
The door hours stand. Sunday is closed.
