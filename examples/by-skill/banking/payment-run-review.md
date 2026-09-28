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
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Holds that item until the verified channel confirms it.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| run | 14 Sep 2026 | Needs confirmation |
| changed payee | email this morning, not verified | Carried into the draft |
| password | not collected | Carried into the draft |
| hold | that line | Needs confirmation |

**How this draft was built**

**1. Check the run against approvals they require**

**2. Flag duplicate-looking items for review, not as accusations**

**3. Any payee detail change needs their verified channel**

**4. Do not ask for banking passwords or one-time codes**

**5. Exceptions need a named approver**

**Deliberately not done**
- A password request.
- A silent release of a failed item.
- An unverified bank-detail change.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
