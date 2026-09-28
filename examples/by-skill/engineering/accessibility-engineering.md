# Accessibility Engineering

`accessibility-engineering`

## What this is for

Turn an accessibility barrier into an engineering fix with a test, without claiming a conformance certificate.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs an accessibility engineering note by 30 September 2026. A modal traps keyboard focus, and the proposed fix is a README badge that says 'accessible'.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A modal traps keyboard focus, and the proposed fix is a README badge that says 'accessible'.

The barrier: Checkout service is open. Invoice job was raised verbally and never logged
The user impact: Checkout service, recorded 14 September 2026. No supporting file attached
The code or component involved: Checkout service, recorded 14 September 2026. No supporting file attached
The team's stated target: 140
```

## Example outcome

**Accessibility engineering note**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Specifies the focus fix and a keyboard test, and rejects the badge as proof.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The barrier | Checkout service is open. Invoice job was raised verbally and never logged | Needs confirmation |
| The user impact | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The code or component involved | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| The team's stated target | 140 | Needs confirmation |

**How this draft was built**

**1. Reproduce**  
The exact barrier, such as a keyboard trap or a missing name. Do not claim you ran an assistive technology you did not run.

**2. Fix**  
The specific code or component change. Prefer the platform's accessible primitive over a custom widget.

**3. Test**  
A check the team can repeat, automated where it fits and manual where it does not.

**4. Regression**  
Where this should live so it does not return.

**5. Limits**  
What this fix does not prove. No blanket WCAG certificate.

**Deliberately not done**
- A conformance certificate from a guess.
- A custom widget when a native control would do.
- Closing the bug with no regression check.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
