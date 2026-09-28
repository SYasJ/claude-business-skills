# Bank Reconciliation

`bank-reconciliation`

## What this is for

Reconcile book to bank and leave a list of items a human must clear, with no plugs.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, is closing August 2026. The operating account will not tie, and three deposits in transit are older than a month.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Period: August 2026 · Account: operating (CAD)

Bank statement ending balance, 31 Aug 2026 ....... 97,820.00
GL cash balance, 31 Aug 2026 .................... 94,350.00

Outstanding checks (per GL, not yet cleared):
  #2241  Office Depot     28 Aug 2026     3,250.00
  #2242  Redline Parts    29 Aug 2026     1,820.00

Deposits in transit (per GL, not on statement):
  DIT-01  deposited 21 Jul 2026  (41 days)   6,200.00
  DIT-02  deposited  4 Aug 2026  (27 days)   3,100.00
  DIT-03  deposited  9 Aug 2026  (22 days)   2,400.00

On statement, not in GL:  NSF fee 85.00 · service charge 65.00
Stale-item threshold (their policy): 30 days
Reviewer sign-off: not signed
```

## Example outcome

**Bank reconciliation — operating account, August 2026**
To: Priya Shah, controller, Northline Studio · Date: 14 September 2026

**Adjusted bank balance**

| Line | Amount (CAD) |
| --- | ---: |
| Statement balance, 31 Aug 2026 | 97,820.00 |
| Less: outstanding checks (#2241, #2242) | (5,070.00) |
| Add: deposits in transit (DIT-01/02/03) | 11,700.00 |
| **Adjusted bank balance** | **104,450.00** |

**Adjusted book balance**

| Line | Amount (CAD) |
| --- | ---: |
| GL balance, 31 Aug 2026 | 94,350.00 |
| Less: bank charges not yet booked (85.00 + 65.00) | (150.00) |
| **Adjusted book balance** | **94,200.00** |

**Unexplained difference: 10,250.00. This reconciliation does not close.**

The difference is shown, not plugged. No "other" line was created to force a zero.

**Items that need a decision**

| Item | Amount | Age | Why it is here |
| --- | ---: | ---: | --- |
| DIT-01 | 6,200.00 | 41 days | Past their 30-day threshold. Trace to the bank's deposit record. If the deposit never landed, reverse the GL entry and find the source funds. |
| DIT-02 | 3,100.00 | 27 days | Approaching the threshold. Confirm receipt with the bank this period. |
| DIT-03 | 2,400.00 | 22 days | Within tolerance. Carry, and watch next period. |

**Draft journal entry — for the controller to post, not posted here**

```
Dr  Bank service charges expense      150.00
      Cr  Cash — operating                      150.00
(NSF 85.00 + monthly service charge 65.00; confirm the NSF payee before posting)
```

**Deliberately not done**
- No plug labelled "other" to force the reconciliation to zero.
- No bank password or one-time code requested. Everything above came from the export Priya shared.
- No DIT written off silently; the 41-day item is raised as a decision, not carried forward again.

**Open items before sign-off**
- Investigate the 10,250.00 difference. The account does not close until it is explained or classified as a known error.
- Reviewer signature is missing. Close is not complete without it.
- Recs are stored in one person's inbox rather than the shared folder. Move them this period.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
