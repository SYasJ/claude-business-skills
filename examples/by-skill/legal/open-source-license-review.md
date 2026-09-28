# Open-Source License Review

`open-source-license-review`

## What this is for

Triage open-source components the user lists so engineering and counsel can see obligations. Not a compatibility ruling.

## Scenario

Elena Voss, operations lead at Northline Studio in Calgary, needs an open-source triage by 30 September 2026. A release candidate includes a library the scan labels as a reciprocal license, and the team ships binaries to customers.

## Example data

```text
From: Elena Voss, operations lead
Organization: Northline Studio, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A release candidate includes a library the scan labels as a reciprocal license, and the team ships binaries to customers.

The components and versions they listed: Harbor renewal; Contractor NDA; Vendor terms
How the component is used: linked, modified, or distributed: linked: in the file; modified: not in the file; distributed: open
Licenses they already identified: MIT on two files. One file has no header
```

## Example outcome

**Open-source triage**
To: Elena Voss, operations lead, Northline Studio
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Isolates that component, states the usage, and sends the obligation question to counsel instead of clearing the release.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The components and versions they listed | Harbor renewal; Contractor NDA; Vendor terms | Needs confirmation |
| How the component is used: linked, modified, or distributed | linked: in the file; modified: not in the file; distributed: open | Carried into the draft |
| Licenses they already identified | MIT on two files. One file has no header | Carried into the draft |

**How this draft was built**

**1. Use their inventory**  
Do not pretend to scan a codebase unless the user provided the scan output.

**2. Record the license name they supplied**  
If the license text is missing, say the triage cannot classify that component.

**3. Usage matters**  
A tool that runs in development is a different question from code distributed to customers. Use their description.

**4. Obligations in plain language**  
Attribution, source offer, or reciprocal terms only as those duties are commonly described, and mark them for counsel to confirm. Do not give a legal compatibility opinion.

**5. Flag unknowns**  
Custom forks and missing versions are stop points.

**Deliberately not done**
- A blanket 'all MIT, you are fine'.
- Helping strip license notices.
- Classifying a component with no license text.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Elena Voss by 30 September 2026. This is a draft, not a sign-off.
