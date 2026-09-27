# Payment Run Review

`payment-run-review`

## What this is for

Review a payment run for duplicates, approvals, and changes to payee details.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a payment run review by 30 September 2026. A payment run includes a new account number received by email this morning.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A payment run includes a new account number received by email this morning.

run: 14 Sep 2026
changed payee: email this morning, not verified
password: not collected
hold: that line
```

## Example outcome

**Payment run review**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026

**Decision**
Holds that item until the verified channel confirms it.

**From the file**
- run: 14 Sep 2026
- changed payee: email this morning, not verified
- password: not collected
- hold: that line

Nothing in this draft was added from outside that file.
Next: Priya Shah by 30 September 2026. This is not a sign-off.
