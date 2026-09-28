# Accessibility Design Review

`accessibility-design`

## What this is for

Review a design for access barriers before build, without issuing a conformance certificate.

## Scenario

Lena Ortiz, design lead at Fieldnote in Edmonton, needs an accessibility design note by 30 September 2026. A mock uses placeholder color as the only label.

## Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A mock uses placeholder color as the only label.

The flow: the one named in the ask. Version and owner not recorded
Text and controls: their one-page rule dated 2 Mar 2026. No exception log since
Known barriers: Checkout screen v4 is open. Empty-state copy was raised verbally and never logged
The target they claim: 140
```

## Example outcome

**Accessibility design note**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Requires a visible label and refuses a conformance claim.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The flow | the one named in the ask. Version and owner not recorded | Needs confirmation |
| Text and controls | their one-page rule dated 2 Mar 2026. No exception log since | Carried into the draft |
| Known barriers | Checkout screen v4 is open. Empty-state copy was raised verbally and never logged | Carried into the draft |
| The target they claim | 140 | Needs confirmation |

**How this draft was built**

**1. Check the flow for keyboard order, names, and focus as far as the mock shows**

**2. Flag text that will fail contrast if the values are visible. Do not invent a pass**

**3. Error identification must not depend on color alone**

**4. Touch and target size are noted if they specified a platform**

**5. Write fixes a designer can make now**

**Deliberately not done**
- A conformance badge from a glance.
- Errors shown by color only.
- No focus order on a custom control.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.
