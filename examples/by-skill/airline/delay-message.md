# Delay Message

`delay-message`

## What this is for

Write the passenger message from the delay facts the station can say.

## Scenario

Gate staff want a message for KA412. There is no new departure time. A draft says 18:40 and a free hotel. The station may offer water. It may not offer a hotel.

## Example data

```text
flight: KA412
new time: unknown
reason authorized: ground hold
care authorized: water at the gate
care not authorized: hotel, meal voucher
connections: not confirmed
```

## Example outcome

**Gate message**
KA412 is delayed for a ground hold. We do not have a new departure time.

Water is available at the gate. We cannot confirm a connection on this message.

**Not in the message**
18:40. A hotel. A meal voucher. A person to blame.
