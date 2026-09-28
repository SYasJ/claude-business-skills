# Complaint Root Cause

`complaint-root-cause`

## What this is for

Analyze a cluster of complaints to the cause the company can fix, without dismissing the customer.

## Scenario

Rita Santos, support lead at Fieldnote in Edmonton, needs a complaint analysis by 30 September 2026. Complaints rose after a pricing page started hiding a fee.

## Example data

```text
From: Rita Santos, support lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

Complaints rose after a pricing page started hiding a fee.

ticket: 4412, 14 Sep 2026
customer words: in the ticket
exception: not approved
card or password: not collected
```

## Example outcome

**Complaint analysis**
To: Rita Santos, support lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Names the hidden fee as the hypothesis to fix and does not blame the customers for writing in.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| ticket | 4412, 14 Sep 2026 | Needs confirmation |
| customer words | in the ticket | Carried into the draft |
| exception | not approved | Carried into the draft |
| card or password | not collected | Needs confirmation |

**How this draft was built**

**1. Define the cluster with their labels and volumes**

**2. Read for the failed job, not for the customer's tone**

**3. Separate a product defect, a policy surprise, and an expectation set by marketing**

**4. Check a recent change that matches the timing**

**5. Recommend one fix**  
policy, product, or message.

**Deliberately not done**
- Blaming tone.
- A fix that does not match the cause.
- Ignoring a recent change.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Rita Santos by 30 September 2026. This is a draft, not a sign-off.
