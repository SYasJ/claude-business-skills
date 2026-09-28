# Knowledge Base Article

`knowledge-base-article`

## What this is for

Write a knowledge article that answers one question and tells the reader when to stop and escalate.

## Scenario

Diane Cho, operations manager at Harbor Goods in Airdrie, needs a knowledge article by 30 September 2026. A help draft includes an admin password so customers can 'fix it themselves'.

## Example data

```text
From: Diane Cho, operations manager
Organization: Harbor Goods, Airdrie
Date: 14 September 2026
Needed by: 30 September 2026

A help draft includes an admin password so customers can 'fix it themselves'.

shift: two people
SOP: one page, 2 Mar 2026
exception: not logged
queue: the items in the ask
```

## Example outcome

**Knowledge article**
To: Diane Cho, operations manager, Harbor Goods
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Removes the password, answers one question, and gives an escalation path.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| shift | two people | Needs confirmation |
| SOP | one page, 2 Mar 2026 | Carried into the draft |
| exception | not logged | Carried into the draft |
| queue | the items in the ask | Needs confirmation |

**How this draft was built**

**1. Use the reader's question as the title**

**2. Number the steps. Include the expected result of the key step**

**3. Add the symptoms that mean this article is the wrong one**

**4. Tell them when to escalate, and to whom**

**5. Remove internal jargon or explain it**

**Deliberately not done**
- An article that answers three questions badly.
- A secret in a help article.
- No escalation line.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Diane Cho by 30 September 2026. This is a draft, not a sign-off.
