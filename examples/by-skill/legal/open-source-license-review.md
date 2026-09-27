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
Date: 14 September 2026

**Decision**
Isolates that component, states the usage, and sends the obligation question to counsel instead of clearing the release.

**From the file**
- The components and versions they listed: Harbor renewal; Contractor NDA; Vendor terms
- How the component is used: linked, modified, or distributed: linked: in the file; modified: not in the file; distributed: open
- Licenses they already identified: MIT on two files. One file has no header

Nothing in this draft was added from outside that file.
Next: Elena Voss by 30 September 2026. This is not a sign-off.
