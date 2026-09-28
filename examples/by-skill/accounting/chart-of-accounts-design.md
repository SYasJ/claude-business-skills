# Chart of Accounts Design

`chart-of-accounts-design`

## What this is for

Design a chart of accounts people can code to, with enough detail to manage and not so much that nobody agrees.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a chart of accounts proposal by 30 September 2026. A growing firm has 400 accounts and still cannot see gross margin by service line.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A growing firm has 400 accounts and still cannot see gross margin by service line.

Decisions the accounts must support: A growing firm has 400 accounts and still cannot see gross margin by service line
Current pain: miscoding or useless detail: miscoding: in the file; useless detail: not in the file
External reporting framework they claim to use: the draft sentence is broader than the note
```

## Example outcome

**Chart of accounts proposal**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Uses a dimension for service line, defines the accounts that change, and maps old balances forward.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| Decisions the accounts must support | A growing firm has 400 accounts and still cannot see gross margin by service line | Needs confirmation |
| Current pain: miscoding or useless detail | miscoding: in the file; useless detail: not in the file | Carried into the draft |
| External reporting framework they claim to use | the draft sentence is broader than the note | Carried into the draft |

**How this draft was built**

**1. Start from decisions**  
Which margins, locations, or funding sources must be visible without a side spreadsheet.

**2. Separate posting accounts from reporting groups**  
People post to stable accounts. Reports roll them up. Do not make every report slice a new account.

**3. Write definitions**  
Each new or changed account gets a one-line definition and an example of what does not belong in it.

**4. Cap the depth**  
Recommend a department or class dimension instead of exploding the natural account list, when their system supports it. If you do not know the system, ask before redesigning.

**5. Plan the map**  
Old account to new account. Unmapped balances are how conversions fail.

**Deliberately not done**
- A hundred new accounts with no definitions.
- Redesigning the chart to match a blog diagram.
- No mapping from the old balances.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
