# Event Tracking Spec

`event-tracking-spec`

## What this is for

Specify product or marketing events so a later analyst can trust the trigger, the properties, and the privacy boundary.

## Scenario

Noah Berger, data lead at Fieldnote in Edmonton, needs a tracking spec by 30 September 2026. A spec adds the user's national ID as a property to count button clicks.

## Example data

```text
From: Noah Berger, data lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A spec adds the user's national ID as a property to count button clicks.

The question the events answer: A spec adds the user's national ID as a property to count button clicks
The actions to instrument: orders_daily; customers. Both unassigned as of 14 September 2026
Existing naming rules: their one-page rule dated 2 Mar 2026. No exception log since
Privacy limits: email and billing address. They said no health data
```

## Example outcome

**Tracking spec**
To: Noah Berger, data lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the ID, defines the success trigger, and names the verification step.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The question the events answer | A spec adds the user's national ID as a property to count button clicks | Needs confirmation |
| The actions to instrument | orders_daily; customers. Both unassigned as of 14 September 2026 | Carried into the draft |
| Existing naming rules | their one-page rule dated 2 Mar 2026. No exception log since | Carried into the draft |
| Privacy limits | email and billing address. They said no health data | Needs confirmation |

**How this draft was built**

**1. Write the question first. Events without a question are rejected**

**2. Define trigger timing precisely**  
on success, not on click, if success is what matters.

**3. List properties and ban secrets, payment card data, and raw credentials**

**4. Match their naming rules. Do not invent a parallel taxonomy**

**5. Specify how the team will verify the event before release**

**Deliberately not done**
- Tracking secrets.
- A parallel naming scheme.
- Events with no verification step.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Noah Berger by 30 September 2026. This is a draft, not a sign-off.
