# Churn Save Plan

`churn-save-plan`

## What this is for

Plan a save offer from the cancel reasons in the export and the offer they can honor.

## Scenario

Forty cancels in August. Twenty-two said the export they need does not exist. Ten said price. Eight gave no reason. A draft offers 20 percent off to all forty. Jonah can approve a 10 percent credit, not 20.

## Example data

```text
cancels: 40, August 2026
missing export: 22
price: 10
no reason: 8
credit he can approve: 10 percent, one month
20 percent draft: not approved
```

## Example outcome

**Save plan**
Do not discount the 22. A cheaper plan does not create the missing export.
Price reason, 10 accounts: a 10 percent credit for one month is the offer he can honor. Not 20.
No reason, 8: no offer. Ask, or leave them.
No save rate is claimed. None was measured.
Approver for the credit: Jonah.
