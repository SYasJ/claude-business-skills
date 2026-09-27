# Flare Volume Note

`flare-volume-note`

## What this is for

Report flare volumes from the meter the user has, with the reason code they supplied.

## Scenario

The flare meter was down on 12 September. A draft report enters zero so the month still adds up. Devon has a reason code for a compressor trip on the 11th, when the meter worked.

## Example data

```text
period: 11 and 12 Sep 2026
11 Sep: meter 0.18 mmcf, reason code CT-compressor, his code
12 Sep: meter down, no reading
draft: 12 Sep entered as 0
signer: Devon Hale
```

## Example outcome

**Flare note**
11 September: 0.18 mmcf, reason CT-compressor, from his code. Use that.
12 September: blank. The meter was down. Zero is rejected. An estimate is not in this note.
This is not an emissions-factor calculation and not an assurance opinion.
Signer: Devon, after the 12th stays blank or a real reading replaces it.
