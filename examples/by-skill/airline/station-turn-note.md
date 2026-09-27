# Station Turn Note

`station-turn-note`

## What this is for

Record a turn delay with the minute it started and the cause the ramp lead wrote.

## Scenario

KA412's turn was scheduled at 40 minutes and took 55. The ramp note says the bag cart was late. A draft blames cabin cleaning so the ramp target holds.

## Example data

```text
flight: KA412
scheduled turn: 40 minutes
actual: 55
ramp note: late bag cart
draft cause: cabin cleaning
same aircraft next: KA188
who updates control: Luis Ortega
```

## Example outcome

**Turn note**
55 against 40. Fifteen minutes. Cause in the ramp note: late bag cart.
Cabin cleaning is not in the note. It does not replace the cart.
Next flight on the same aircraft: KA188. Control needs the 15 minutes, not a cleaned-up cause.
Updater: Luis.
