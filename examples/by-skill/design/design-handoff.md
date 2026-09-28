# Design Handoff

`design-handoff`

## What this is for

Hand a design to engineering with states, content, and open decisions explicit.

## Scenario

Lena Ortiz, design lead at Fieldnote in Edmonton, needs a handoff note by 30 September 2026. A handoff includes the success screen only for a payment flow.

## Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A handoff includes the success screen only for a payment flow.

The screens: Checkout screen v4, recorded 14 September 2026. No supporting file attached
States: Empty-state copy and one other, both unconfirmed as of 14 September 2026
Content: Colour contrast audit, last reviewed 14 September 2026. No owner named since
Known decisions still open: A handoff includes the success screen only for a payment flow
```

## Example outcome

**Handoff note**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Adds failure, empty, and the unauthorized state, and lists open decisions.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The screens | Checkout screen v4, recorded 14 September 2026. No supporting file attached | Needs confirmation |
| States | Empty-state copy and one other, both unconfirmed as of 14 September 2026 | Carried into the draft |
| Content | Colour contrast audit, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Known decisions still open | A handoff includes the success screen only for a payment flow | Needs confirmation |

**How this draft was built**

**1. List what is in scope for this handoff**

**2. Include empty, error, and loading states**

**3. Write the content, not lorem, unless a field is truly dynamic, and then say so**

**4. Mark open decisions so engineering does not guess**

**5. Note accessibility expectations for the flow**

**Deliberately not done**
- Lorem on a commitment screen.
- Hidden open decisions.
- No error state.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.
