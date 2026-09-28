# Bank Reconciliation

`bank-reconciliation`

## What this is for

Reconcile book to bank and leave a list of items a human must clear, with no plugs.

---

## Scenario A — Unexplained difference and stale DITs

**Priya Shah, controller, Northline Studio, Calgary — August 2026 close**

### Input data

| | Amount (CAD) |
|---|---|
| Bank statement ending balance, 31 Aug 2026 | $97,820.00 |
| GL cash balance, 31 Aug 2026 | $94,350.00 |

Outstanding checks (per GL, not yet cleared bank):

| Check # | Payee | Date issued | Amount |
|---|---|---|---|
| 2241 | Office Depot | 28 Aug 2026 | $3,250.00 |
| 2242 | Redline Parts | 29 Aug 2026 | $1,820.00 |

Deposits in transit (per GL, not on statement):

| DIT ref | Deposited | Age | Amount |
|---|---|---|---|
| DIT-01 | 21 Jul 2026 | 41 days | $6,200.00 |
| DIT-02 | 4 Aug 2026 | 27 days | $3,100.00 |
| DIT-03 | 9 Aug 2026 | 22 days | $2,400.00 |

Bank charges on statement, not in GL: NSF fee $85.00, monthly service charge $65.00.

### Reconciliation

**Adjusted bank balance**

| | |
|---|---|
| Statement balance | $97,820.00 |
| Less: outstanding checks | ($5,070.00) |
| Add: deposits in transit | $11,700.00 |
| **Adjusted bank balance** | **$104,450.00** |

**Adjusted book balance**

| | |
|---|---|
| GL balance | $94,350.00 |
| Less: bank charges not yet booked | ($150.00) |
| **Adjusted book balance** | **$94,200.00** |

**Unexplained difference: $10,250.00 — reconciliation does not close.**

> This difference is not plugged. It requires investigation before sign-off.

### Items requiring a decision

**DIT-01 ($6,200.00, 41 days old):** A deposit in transit older than 30 days is unusual. Verify the deposit was made and trace to the bank's deposit records. If the deposit failed, reverse the GL entry and investigate the source funds.

**DIT-02 ($3,100.00, 27 days old):** Approaching threshold. Confirm deposit receipt with the bank.

**DIT-03 ($2,400.00, 22 days old):** Within tolerance; watch for next period.

### Journal entries proposed (draft — controller must approve and post)

```
Dr Cash — bank charges    $150.00
  Cr Bank service charges expense    $150.00
[NSF $85 + monthly fee $65; verify payee on NSF item before posting]
```

### Process findings

| Finding | Recommended fix |
|---|---|
| Unexplained $10,250 difference | Investigate before close sign-off |
| DIT-01 age 41 days | Confirm with bank; reverse if not deposited |
| Recs stored in one inbox, not shared folder | Move to shared drive this period |
| Reviewer signature missing | Required before close is complete |

---

## Scenario B — Clean reconciliation with one open item

**Quick close scenario: all DITs clear, one small charge.**

| | |
|---|---|
| Statement balance | $42,180.00 |
| Less: outstanding check #1891 (3 days old) | ($1,200.00) |
| Adjusted bank | $40,980.00 |
| GL balance | $40,900.00 |
| Add: bank interest not yet booked | $80.00 |
| Adjusted book | $40,980.00 |
| **Difference** | **$0.00 — reconciliation closes** |

Journal entry draft: Dr Cash $80 / Cr Interest income $80.

Reviewer can sign off once the interest entry is posted.
