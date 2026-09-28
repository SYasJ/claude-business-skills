"""Hand-written scenarios. A skill listed here overrides the generated example."""

BANK = {}


def put(name, purpose, scenario, data, outcome):
    BANK[name] = {
        "purpose": purpose.strip(),
        "scenario": scenario.strip(),
        "data": data.strip(),
        "outcome": outcome.strip(),
    }


put(
    "bank-reconciliation",
    "Reconcile book to bank and leave a list of items a human must clear, with no plugs.",
    "Priya Shah, controller at Northline Studio in Calgary, is closing August 2026. The operating "
    "account will not tie, and three deposits in transit are older than a month.",
    """```text
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
```""",
    """**Bank reconciliation — operating account, August 2026**
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

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.""",
)


put(
    "cash-flow-forecast",
    "Build a 13-week direct cash forecast from collections and commitments, not from accrual revenue.",
    "Mara Chen runs Northline Studio in Calgary. On 14 September 2026 she asks whether she can start "
    "two producers next month without missing payroll. She will not finish a week under 40,000 CAD. "
    "Harbor & Co owes 90,000 and usually pays 20 days late. That money is not in the bank.",
    """```text
opening cash: 180000 CAD, operating account, 14 Sep 2026
payroll: 70000 on the 1st and the 15th
rent: 12000 due in week 3
approved bills: 8400 due in week 2
receivable: Harbor & Co, 90000, usually 20 days late
buffer: 40000
proposed hires: 2 producers, 8500 each per month, start week 5
```""",
    """**13-week cash forecast — first five weeks**
Northline Studio · 14 September 2026 · CAD

**Decision**
Do not send the two offers on this file. Week 3 closes at 19,600 — under the 40,000 buffer — and that is before Harbor & Co pays.

| Week | Opening | In | Out | Closing | Vs 40,000 |
| --- | ---: | ---: | ---: | ---: | --- |
| 1 | 180,000 | 0 | 70,000 payroll | 110,000 | above |
| 2 | 110,000 | 0 | 8,400 approved bills | 101,600 | above |
| 3 | 101,600 | 0 | 82,000 payroll + rent | 19,600 | **below** |
| 4 | 19,600 | 90,000 if the lag holds | 0 | 109,600 | above |
| 5 | 109,600 | 0 | 70,000 payroll | 39,600 | **below**, hires not included |

**What the table does and does not assume**
- The 90,000 from Harbor & Co is a *collection*, not booked revenue. It sits in week 4 only because that is the 20-day lag in the file. If Harbor slips a week, week 4 closes at 19,600 too.
- The two proposed hires are **not** in the table. Adding 17,000 a month from week 5 makes an already-below-buffer week worse.

**Deliberately not done**
- No revenue was recognised that has not been collected.
- No second scenario was invented. Build the "Harbor pays late" case before any offer letter goes out — that is the case that decides this.
- The buffer was not lowered to make the answer come out yes.

**Optional check, using numbers you pass in**

```bash
python3 scripts/cashflow_check.py examples/data/weeks.csv --opening 180000 --buffer 40000
```

The script adds and subtracts. It does not know the customer, the lag, or a safe buffer.

Next: Mara Chen confirms the Harbor collection date before the offers go out.""",
)


put(
    "spreadsheet-model-review",
    "Review a spreadsheet model for structure, formula errors, and hard-coded values that should be inputs.",
    "Priya Shah, controller at Northline Studio in Calgary, shares the FY2027 operating budget. "
    "Her analyst reports that changing the revenue assumption takes more than forty manual edits.",
    """```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
File: FY2027 Operating Budget.xlsx (12 tabs)

Reported symptom: changing the revenue growth rate requires editing every month column.

Formulas pasted for review:
  P&L!B8   =4200*1.03          (repeated across C8:M8, 47 cells total)
  P&L!D22  =Sheet3!C4          (tab "Sheet3" was renamed to "COGS Detail")
  P&L!K34  =K32/K33            (K33 = headcount, can be 0 in a setup month)
  Assumptions tab: exists, unprotected, no named ranges
  Column A dates: rows 1-6 text "Jan-27", rows 7-12 serial 1/1/2027
```""",
    """**Spreadsheet model review — FY2027 Operating Budget**
To: Priya Shah, controller, Northline Studio · Date: 14 September 2026

**Decision**
Two findings break the model today and must be fixed before anyone trusts Net Income. The rest are structural and can follow.

**Finding 1 — CRITICAL · Revenue hard-coded in 47 formula cells**

`P&L!B8` contains `=4200*1.03`, repeated across `C8:M8`. The growth rate lives inside the formula, so changing it means 47 edits and one of them will be missed.

Fix — move both numbers to inputs, then reference them:

```
Assumptions!B3  =4200     (revenue base, January)
Assumptions!B4  =1.03     (monthly growth rate)

P&L!B8  =Assumptions!$B$3 * (Assumptions!$B$4 ^ (COLUMN()-2))
```

One edit now updates all twelve months.

**Finding 2 — HIGH · COGS reference points at a tab that no longer exists**

`P&L!D22` is `=Sheet3!C4`. The tab was renamed to `COGS Detail`, so this returns `#REF!` and the error propagates silently into Net Income.

Fix: `='COGS Detail'!C4`, then define a named range so the next rename does not break it.

**Finding 3 — MEDIUM · Division with an unguarded zero denominator**

`P&L!K34` is `=K32/K33`, where K33 is headcount. A department in its setup month has zero headcount, which returns `#DIV/0!` and breaks the payroll summary.

Fix: `=IFERROR(K32/K33, 0)` — or `=IF(K33=0, 0, K32/K33)` if a zero should be visibly different from an error.

**Finding 4 — MEDIUM · Assumptions tab is unprotected**

Any user can overtype a formula or delete a range. Lock the formula cells and leave only the assumption inputs editable before this is shared more widely.

**Finding 5 — LOW · Mixed date types in column A**

Rows 1–6 hold the text `"Jan-27"`; rows 7–12 hold real date serials. Charts built on this column will sort wrongly. Standardise on serials with a `mmm-yy` display format.

**Order of work**

| # | Fix | Why first |
| --- | --- | --- |
| 1 | `#REF!` in COGS | It is wrong on screen today |
| 2 | Revenue inputs | Highest effort, highest payoff; everything else depends on it |
| 3 | `IFERROR` guard on K34 | Cheap, prevents a future break |
| 4 | Lock formula cells | Do before wider sharing |
| 5 | Date formats | Cosmetic until someone builds a chart |

**Deliberately not done**
- The model was not restructured beyond what was asked. One change at a time keeps it testable.
- No formula's intent was guessed. Where the purpose of a cell was unclear, it is listed for Priya to confirm rather than rewritten.
- No new tool was proposed. The spreadsheet is the right tool for this; it just needs its inputs separated.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.""",
)


put(
    "video-storyboard",
    "Write a shot-by-shot visual storyboard for a video, naming what is on screen, the motion, and the audio for each shot.",
    "Maya Brooks, creator at Weeknight Table in Calgary, wants a 60-second explainer on compound "
    "interest. She has a rough script and needs it broken into shots she can actually film or build.",
    """```text
From: Maya Brooks, creator
Channel: Weeknight Table, Calgary
Target length: 60 seconds · Format: 16:9, YouTube

Rough script points:
  - savings accounts earn almost nothing
  - interest earns interest: that is compounding
  - $1,000 at 5% grows to about $1,629 over 10 years
  - time matters more than the starting amount
  - subscribe

Assets on hand: screen recording setup, Canva, own spreadsheet
Assets NOT on hand: stock footage licence, animation software
```""",
    """**Video storyboard — "How compound interest works" (60s, 16:9)**
To: Maya Brooks, creator, Weeknight Table · Date: 14 September 2026

| # | Dur | On screen | Motion | Audio / VO |
| --- | ---: | --- | --- | --- |
| 1 | 3s | Title: **"Your $1,000 becomes $4,000 — without doing anything"**, dark background, coin graphics | Coins fade up from the lower edge | No VO. Music in. |
| 2 | 10s | Split frame: left, a piggy bank sitting still; right, empty | Left half fades in, then right, to set up the contrast | "Most people leave money in a savings account earning almost nothing. There's a way to make your money earn money." |
| 3 | 14s | Screen recording of your own spreadsheet. Year 1: $1,000 · Year 2: $1,050 · Year 3: $1,102.50. Formula bar visible. Overlay: **"5% annual interest"** | Rows animate in one at a time, on the VO beat | "Invest $1,000 at 5%. After year one you have $1,050. Year two, you earn interest on the $1,050 — not just the original thousand. That's compounding." |
| 4 | 12s | Bar chart, 10 years, $1,000 rising to about $1,629. Axes labelled. | Bars grow left to right | "Over 10 years that $1,000 grows to over $1,600, without you adding a dollar. Start earlier and the effect multiplies." |
| 5 | 12s | Three cards: $1K/10yr → ~$1,629 · $5K/10yr → ~$8,144 · $1K/30yr → ~$4,322. Footer: *"Illustrative. Rates vary."* | Cards slide in from the right | "Five thousand for ten years becomes over eight thousand. One thousand for thirty years becomes over four. The variable that matters most isn't the amount — it's time." |
| 6 | 9s | **"Subscribe for more money basics"** + channel logo | Logo fades in, subscribe button pulses | "Hit subscribe for more plain-English money explainers every week." Music out. |

**Total: 60 seconds.**

**What you need to build, and how — given your asset list**

| Shot | Source | Note |
| --- | --- | --- |
| 1 | Canva | You have no stock licence, so build the coin graphic rather than pulling footage. |
| 2 | Canva | Simple two-up illustration. No footage needed. |
| 3 | Your own screen recording | Use your own spreadsheet. Do not screen-record someone else's video. |
| 4 | Canva or Flourish | Both do animated bar charts without animation software. |
| 5 | Canva | Three-card template. |
| 6 | Your existing end card | Reuse. |

Every shot is achievable with the tools you listed. Nothing here needs the stock licence or animation software you said you do not have.

**Deliberately not done**
- No shot depends on licensed footage or another creator's video.
- No real person's likeness appears.
- The timings add to 60 seconds, not to 75 with the expectation of cutting later.

**Open items**
- The dollar figures are illustrative. Add the on-screen disclaimer in shot 5 and a sources note in the pinned comment.
- Confirm the 5% rate is the one you want to use before the VO is recorded; it appears in three shots.

Next: Maya Brooks by 30 September 2026. This is a draft, not a sign-off.""",
)
