# Audit PBC Preparation

`audit-prep-pbc`

## What this is for

Build a provided-by-client list that answers the auditor's request without dumping the entire file room.

## Scenario

Priya Shah, controller at Northline Studio in Calgary, needs a PBC list and evidence index by 30 September 2026. The external auditor asked for revenue samples and the team is about to export every invoice with no index.

## Example data

```text
From: Priya Shah, controller
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

The external auditor asked for revenue samples and the team is about to export every invoice with no index.

The auditor's request list, if any: Operating cash; Undeposited funds; Sales tax payable
Systems and owners: Priya Shah, controller
The period under audit: month ending 14 September 2026
```

## Example outcome

**Pbc list and evidence index**
To: Priya Shah, controller, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
An indexed PBC with owners, report parameters, tie-out notes, and no shared passwords.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The auditor's request list, if any | Operating cash; Undeposited funds; Sales tax payable | Needs confirmation |
| Systems and owners | Priya Shah, controller | Carried into the draft |
| The period under audit | month ending 14 September 2026 | Carried into the draft |

**How this draft was built**

**1. Restate each request**  
What evidence answers it, who owns it, and the period it covers. A request you do not understand gets a clarifying question, not a random export.

**2. Prefer system reports**  
Name the report and the parameters. A spreadsheet recreation is a last resort and should be labeled.

**3. Tie-out notes**  
For key numbers, say which report ties to the trial balance. Auditors will ask anyway.

**4. Sensitive access**  
Provide exports, not shared logins. Do not hand over production credentials.

**5. Track status**  
Open, provided, and follow-up. A list without status is a wish.

**Deliberately not done**
- Sending a login instead of an export.
- A data dump with no tie-out.
- Inventing an audit conclusion in the cover note.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Priya Shah by 30 September 2026. This is a draft, not a sign-off.
