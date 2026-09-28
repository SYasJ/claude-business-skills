# Form Design Review

`form-design-review`

## What this is for

Review a form for necessary fields, error recovery, and an honest submit.

## Scenario

Lena Ortiz, design lead at Fieldnote in Edmonton, needs a form review by 30 September 2026. A contact form requires a social security number.

## Example data

```text
From: Lena Ortiz, design lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A contact form requires a social security number.

The purpose of the form: A contact form requires a social security number. Stated once, in the ask. Not written down anywhere else
Fields: Checkout screen v4, last reviewed 14 September 2026. No owner named since
Error states: Checkout screen v4, first seen 14 September 2026. No root cause recorded yet
What submit commits the user to: Colour contrast audit, last reviewed 14 September 2026. No owner named since
```

## Example outcome

**Form review**
To: Lena Ortiz, design lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the number, states the real purpose, and specifies a useful error.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The purpose of the form | A contact form requires a social security number. Stated once, in the ask. Not written down anywhere else | Needs confirmation |
| Fields | Checkout screen v4, last reviewed 14 September 2026. No owner named since | Carried into the draft |
| Error states | Checkout screen v4, first seen 14 September 2026. No root cause recorded yet | Carried into the draft |
| What submit commits the user to | Colour contrast audit, last reviewed 14 September 2026. No owner named since | Needs confirmation |

**How this draft was built**

**1. Cut fields that do not serve the purpose**

**2. Mark required fields and say why**

**3. Specify errors that tell the user how to fix the input**

**4. State the commitment at submit**  
pay, publish, or send.

**5. Do not ask for secrets that do not belong, such as a password to 'confirm identity' by email reply**

**Deliberately not done**
- Extra sensitive fields.
- A submit that hides a charge.
- Errors that only say invalid.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Lena Ortiz by 30 September 2026. This is a draft, not a sign-off.
