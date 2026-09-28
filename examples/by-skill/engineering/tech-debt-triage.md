# Tech Debt Triage

`tech-debt-triage`

## What this is for

Triage tech debt by the risk and delay it causes, and cut the list to what the team will actually pay down.

## Scenario

Aisha Rahman, engineering lead at Fieldnote in Edmonton, needs a tech debt triage by 30 September 2026. A team has 60 debt tickets and wants them all in next sprint alongside a launch.

## Example data

```text
From: Aisha Rahman, engineering lead
Organization: Fieldnote, Edmonton
Date: 14 September 2026
Needed by: 30 September 2026

A team has 60 debt tickets and wants them all in next sprint alongside a launch.

branch: main, change not merged
tests listed: none
rollback: not written
owner: the person who opened the change
```

## Example outcome

**Tech debt triage**
To: Aisha Rahman, engineering lead, Fieldnote
Date: 14 September 2026 · Needed by: 30 September 2026

**Decision**
Keeps the debt tied to launch risk, parks the rest, and makes the capacity trade explicit.

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
| branch | main, change not merged | Needs confirmation |
| tests listed | none | Carried into the draft |
| rollback | not written | Carried into the draft |
| owner | the person who opened the change | Needs confirmation |

**How this draft was built**

**1. Evidence**  
Each item needs a cost: incidents, slow changes, or a named risk. Vague dislike is parked.

**2. Rank**  
User risk first, then change delay, then cosmetics.

**3. Cut**  
Choose a few items that fit the capacity. A debt program that consumes the quarter needs an explicit product trade.

**4. Shape**  
Paydown as slices inside product work where possible.

**5. Owner**  
One owner per chosen item.

**Deliberately not done**
- A debt list with no capacity cut.
- Ranking by disgust.
- A rewrite program with no product trade made explicit.

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: Aisha Rahman by 30 September 2026. This is a draft, not a sign-off.
