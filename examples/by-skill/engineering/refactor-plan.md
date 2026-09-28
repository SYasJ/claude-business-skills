# Refactor Plan

`refactor-plan`

## What this is for

Plan a refactor that improves a named risk without pretending a rewrite is free.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a refactor plan by 30 September 2026. An engineer wants six weeks to rewrite a billing module before adding a small fee change.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

An engineer wants six weeks to rewrite a billing module before adding a small fee change.

The pain: bugs, change fear, or incidents: bugs: in the file; change fear: not in the file; incidents: open
The boundaries of the code: Checkout service, recorded 14 September 2026. No supporting file attached
Tests that exist: Status page, recorded 14 September 2026. No supporting file attached
Deadline pressure: 30 September 2026
```

## Example outcome

**Refactor plan**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Adds characterization tests and a smaller slice that unblocks the fee change, and treats a full rewrite as a separate decision.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| The pain: bugs, change fear, or incidents | bugs: in the file; change fear: not in the file; incidents: open | Needs confirmation |
| The boundaries of the code | Checkout service, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Tests that exist | Status page, recorded 14 September 2026. No supporting file attached | Carried into the draft |
| Deadline pressure | 30 September 2026 | Needs confirmation |

**How this draft was built**

**1. Pain**  
The user-visible or developer-visible pain. 'It is ugly' is not enough unless change is slow or risky because of it.

**2. Characterize**  
What the code does, from tests or the user's description. Do not refactor behavior you cannot name.

**3. Safety**  
Tests or characterization checks to add first. A refactor without a safety net is a rewrite in the dark.

**4. Slices**  
Small steps that keep the system shipping. A big-bang rewrite needs a written reason and a rollback.

**5. Non-goals**  
Behavior you will not change. Call out any behavior change as a product decision.

**Deliberately not done**
- A rewrite because the code is old.
- Refactoring with no tests and no characterization.
- Sneaking behavior changes into a refactor.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
