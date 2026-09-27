# Station Open Check

`station-open-check`

## What this is for

Check the station open items against the list the station uses.

## Scenario

The first wave is KA188 at 06:10. Fuel paperwork is still open. A draft says open the station because the clock says 05:40.

## Example data

```text
first wave: KA188 at 06:10
open: fuel paperwork
done: security walk, gate screens
signer required: Luis Ortega
draft: open anyway, it is 05:40
```

## Example outcome

**Open check**
Hold KA188. Fuel paperwork is open. The clock does not close it.
Done: security walk, gate screens.
Signer: Luis. He does not sign the fuel line blank.
A commercial wish to leave on time is not a reason to skip the check.
