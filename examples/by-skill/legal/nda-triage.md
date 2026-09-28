# NDA Triage

`nda-triage`

## What this is for

Triage a non-disclosure agreement so the user knows what it covers, how long, and what counsel should still check.

## Scenario

Elena Voss, operations lead at Northline Studio in Calgary, needs a NDA triage note by 30 September 2026. A partnership conversation came with a one-way NDA that also assigns IP improvements to the other side.

## Example data

```text
From: Elena Voss, operations lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A partnership conversation came with a one-way NDA that also assigns IP improvements to the other side.

name: Lumen Ledger, word mark, no logo
goods: bookkeeping software for independent shops
already checked: lumenledger.com open on 12 Sep 2026
register search: not in the file
```

## Example outcome

**Nda triage note**
To: Elena Voss, operations lead, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Flag the IP assignment as unexpected, quotes it, and sends that clause to counsel before signature.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| name | Lumen Ledger, word mark, no logo | Needs confirmation |
| goods | bookkeeping software for independent shops | Carried into the draft |
| already checked | lumenledger.com open on 12 Sep 2026 | Carried into the draft |
| register search | not in the file | Needs confirmation |

**How this draft was built**

**1. Identify direction**  
Mutual or one-way, and whether that matches who will actually share information.

**2. Purpose limit**  
What the recipient may do with the information, in the text's words.

**3. Duration and residuals**  
How long duties last, and whether residual-memory language is present. Quote it if it is.

**4. Exclusions**  
Standard exclusions only count if they appear in the text. Do not assume them.

**5. Awkward clauses**  
Non-solicit, IP assignment, or exclusive dealing hidden in an NDA are flagged as out of place for counsel.

**Deliberately not done**
- Assuming mutual exclusions that are not in the file.
- Ignoring a non-solicit buried in the NDA.
- Declaring the NDA safe for every jurisdiction.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Elena Voss by 30 September 2026. This is a draft, not a sign-off.
