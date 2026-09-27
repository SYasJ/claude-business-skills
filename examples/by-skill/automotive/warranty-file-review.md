# Warranty File Review

`warranty-file-review`

## What this is for

Check a warranty file for the documents their checklist requires before it is submitted.

## Scenario

A warranty file for the failed pads has the RO and the odometer. The photo is missing. The cause line is blank. A clerk offered to write 'worn' so the claim can go tonight.

## Example data

```text
checklist: RO, odometer, photo of failed part, tech cause line
in the file: RO 4418, odometer 61240
missing: photo, tech cause
offered wording: worn
submitter: Carla, not the clerk
```

## Example outcome

**File review**
Hold. Photo missing. Cause line blank.
Do not type 'worn'. The tech did not write it. Do not touch the odometer.
Submitter is Carla, after the photo and the tech's own words are in the file.
This review does not grant goodwill and does not submit the claim.
