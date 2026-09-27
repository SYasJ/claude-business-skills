from dense import pack
from scenario_bank import put

PACKS = []

PACKS.append(pack(
    {"id": "ai", "title": "AI in the business", "summary": "Use-case, eval, cost, and review gates for AI work. No invented scores and no weakened safety rules.", "keywords": ["ai", "llm", "eval", "rag", "automation"]},
    """
ai-use-case | AI Use Case | use-case note
job: Decide whether a task should use a model, who owns the failure, and what stays manual.
triggers: AI use case; should we use a model; automation brief; AI opportunity
inputs: The task; What a wrong answer costs; Who reviews the output; Data that would be sent
steps: Name the task in one sentence. || State the cost of a wrong answer in the user's words. || Say what a person still reviews before the output is used. || List data that must not be sent. || Recommend use, pilot, or do not use. || Do not invent an accuracy number.
anti: An accuracy claim with no test; Private data sent by default; No human owner
example: Support wants a bot to issue refunds with no review.
out: A note that keeps refunds with a person and limits the model to a draft.
related: ai-review-gate; ai-data-note

ai-eval-plan | AI Eval Plan | eval plan
job: Plan an evaluation from examples the user already has, with a pass rule they can apply.
triggers: AI eval; test the model; evaluation set; how will we know it works
inputs: Ten or more real examples they can share; What a pass looks like; Who labels; What they will not test yet
steps: Use their examples. Do not invent gold answers. || Write the pass rule as something a reviewer can mark. || Separate a smoke test from a full eval. || Name who labels and how disagreements are kept. || State what this plan does not prove. || Do not publish a score from a plan that has not been run.
anti: Invented test cases presented as customer data; A score with no labeled set; A pass rule that is 'looks good'
example: A team wants to claim 95 percent accuracy before any example is labeled.
out: A plan that refuses the 95 percent and names the examples still to label.
related: ai-output-check; prompt-revision

ai-review-gate | AI Review Gate | review gate
job: Place a human review where a model output can move money, a customer message, or a record.
triggers: human in the loop; AI approval; review gate; who signs the model output
inputs: The output type; The decision it can trigger; The reviewer role; The hours they can actually review
steps: List outputs that can leave the building. || Put a named role on each, not 'the team'. || Match the gate to the hours they have. A gate no one staffs is a finding. || Say what the reviewer is checking. || Say what happens if the reviewer is absent. || Do not let a model approve its own output.
anti: A gate with no named role; After-hours auto-send; The model marking its own work approved
example: Refund drafts are set to send at night with no reviewer on shift.
out: A gate that holds night drafts until the morning reviewer.
related: ai-use-case; ai-incident-note

ai-data-note | AI Data Note | data-handling note
job: Say what may be pasted into a model and what must stay in the source system.
triggers: AI data handling; what can we paste; model privacy; prompt data rules
inputs: The fields in the task; Which fields are personal or secret; The vendor terms they actually have; The retention they were promised
steps: Split fields into allowed, redacted, and forbidden. || Forbidden includes secrets, payment numbers, and health details unless their counsel already approved that vendor. || Do not invent a vendor promise that is not in their terms. || Say where the source of truth stays. || Name who may paste a row. || If terms are missing, the note says the vendor question is open.
anti: A blanket 'our vendor is private'; Pasting card numbers; Invented retention periods
example: Agents want to paste full tickets, including card last-fours and a home address.
out: A note that allows the complaint text and strips the card and address.
related: ai-vendor-note; privacy-by-design

ai-cost-note | AI Cost Note | cost note
job: Estimate the cost of a proposed AI workflow from the user's prices and volumes.
triggers: AI cost; model bill; token budget; what will this automation cost
inputs: Their price per call or token; Monthly volume they can show; Human minutes saved, if measured; What is not in the price
steps: Use their price sheet. A remembered price is labeled a guess. || Multiply by the volume they showed. || Keep human review time in the cost if they still review. || Do not count saved minutes they have not measured. || Show a low and a high if volume is a range. || Recommend a cap.
anti: A vendor's sample price treated as their contract; Saved-time dollars with no study; No cap
example: A pitch says the bot will save $40,000 a month. No volume or price is attached.
out: A note that leaves the savings blank and prices only the calls they can count.
related: ai-use-case; saas-weekly-metrics

ai-vendor-note | AI Vendor Note | vendor note
job: Compare AI vendors on data use, exit, and support the user can point to in a document.
triggers: AI vendor; model vendor review; which LLM vendor; AI procurement
inputs: The vendors; The documents they have; Data-use questions; How they would leave
steps: Compare only documents they uploaded. || Mark a missing security or data term as missing. || Ask how content is retained and whether it trains a model, and record their answer or the gap. || State the exit: can they take prompts and outputs with them. || Do not invent a certification. || Recommend a pilot limit, not a company-wide switch, when terms are thin.
anti: Invented SOC reports; A logo count as proof; Ignoring data retention
example: A one-pager says the vendor is SOC 2 because the website has a badge.
out: A note that treats the badge as unverified until the report is in the file.
related: vendor-security-review; ai-data-note

ai-incident-note | AI Incident Note | incident note
job: Write up a bad model output the user observed, with the prompt, the harm, and the hold.
triggers: AI incident; model error writeup; bad model output; AI miss
inputs: What the user saw; The prompt or task; Who received the output; What they did next
steps: Describe the output they saw. Do not embellish. || Attach the task, not a theory about the model. || Say who saw it and whether it was sent. || Record the hold: what is paused now. || Separate a one-off from a pattern only if they have more than one case. || Do not include secrets from the prompt in the note.
anti: A cause claimed with no log; A customer name copied into a wide memo; No hold
example: A draft refund of $20 was sent. The agent had not approved it. One case.
out: A note that records the sent draft, pauses auto-send, and does not call it a pattern yet.
related: ai-review-gate; incident-postmortem

ai-output-check | AI Output Check | output check
job: Check a model draft against the source text the user supplied.
triggers: check the AI draft; hallucination check; did the model add facts; output QA
inputs: The source text; The draft; The claims that matter; Who will send it
steps: Line each material claim to a sentence in the source. || Mark claims with no source as added. || Do not 'fix' the draft by adding facts you know from elsewhere. || Say whether it can be sent, sent after cuts, or redone. || Keep the source quote short. || If the source is missing, stop.
anti: Filling gaps from general knowledge; A pass with unmatched claims; Editing the source to match the draft
example: A reply says the order shipped on 12 September. The ticket does not mention shipping.
out: A check that cuts the ship date and leaves the reply unsent.
related: ai-eval-plan; prompt-revision

rag-source-note | RAG Source Note | source pack note
job: Decide which documents may sit in a retrieval set and which are stale or out of bounds.
triggers: RAG sources; what can the bot search; knowledge base for AI; retrieval set
inputs: The collection list; The as-of date of each doc; Topics the bot must not answer; The owner of the set
steps: List documents with dates. Undated is a gap. || Cut documents the user says are drafts or superseded. || Name topics the bot should refuse rather than guess. || Say who updates the set. || Do not add web pages they did not approve. || Recommend a review date.
anti: An undated policy treated as current; The open web as a silent source; No owner
example: A refund policy from 2023 is in the set next to the 2026 version.
out: A note that removes the 2023 file and names the 2026 file as the only refund source.
related: ai-data-note; knowledge-base-article

agent-task-card | Agent Task Card | task card
job: Bound an agent task: the inputs, the tools, the stop rules, and the human owner.
triggers: agent task; what may the agent do; agent boundary; tool use card
inputs: The task; Tools they want it to call; Actions that need a person; The owner
steps: Write the task so a stranger could tell when it is done. || List tools by name. No implied tools. || Put money movement, sending, and deletes behind a person. || State the stop rule when a fact is missing. || Name the owner of a bad run. || Do not grant a tool the user did not name.
anti: An agent that sends or pays alone; Hidden tools; A task of 'help the team'
example: An agent spec lets the bot email the customer and issue a credit.
out: A card that allows a draft and requires a person to send or credit.
related: ai-review-gate; prompt-boundary-check
"""
))

put(
    "ai-use-case",
    "Decide whether a task should use a model, who owns the failure, and what stays manual.",
    "Fieldnote support wants a bot to issue refunds under $30 with no reviewer, because the night queue is slow. Jonah has one week of tickets and no accuracy test.",
    """```text
task: read a ticket and issue a refund under $30
wrong-answer cost: a refund the lead did not approve
reviewer today: Rita Santos, on shift 08:00-17:00 America/Edmonton
night volume: 14 tickets, 8-14 Sep 2026, none reviewed
data that would be sent: full ticket, including the card last-four on 6 of 14
test set: none
```""",
    """**Use-case note**
Do not let the model issue refunds.

| Piece | Call |
| --- | --- |
| Draft a reply from the complaint text | Pilot, after the card last-four is stripped |
| Decide or send a refund | Stays with Rita |
| Night auto-send | No. 14 tickets is a queue fact, not a test |

Owner of a bad draft: Jonah. Reviewer before send: Rita.
Open: no labeled examples, so no accuracy claim.
Next: Rita confirms the day gate by 30 September 2026.""",
)

put(
    "ai-eval-plan",
    "Plan an evaluation from examples the user already has, with a pass rule they can apply.",
    "A slide says the support draft model is 95 percent accurate. Jonah has 12 real tickets and no labels. He needs a plan, not the slide.",
    """```text
examples on hand: tickets 4401-4412, exported 14 Sep 2026
labels: none
pass rule the lead will accept: no invented refund, no date that is not in the ticket
labeler: Rita, 2 hours on 22 Sep
will not test yet: tone score, legal advice, other languages
```""",
    """**Eval plan**
The 95 percent comes off the slide. Nothing has been labeled.

Pass on each ticket: every dollar amount and date in the draft appears in the ticket. If not, fail.
Who labels: Rita, 22 September, tickets 4401-4412.
This is a 12-ticket smoke test. It does not prove a rate for the whole queue.
Not in this plan: tone, legal questions, languages other than the English in these tickets.
Next: Jonah does not quote a percent until Rita's marks are in a sheet.""",
)

put(
    "ai-review-gate",
    "Place a human review where a model output can move money, a customer message, or a record.",
    "Fieldnote set refund drafts to send at 22:00 if no one clicks. Rita works 08:00 to 17:00. Jonah needs the gate written down.",
    """```text
output: customer email draft
can trigger: a refund mention and a send
reviewer role: support lead
hours staffed: 08:00-17:00 America/Edmonton, weekdays
current rule: auto-send at 22:00
queue last week: 14 night tickets
```""",
    """**Review gate**
Night drafts wait.

| Output | Reviewer | If absent |
| --- | --- | --- |
| Reply draft | Rita Santos | Holds until next staffed morning |
| Refund or credit | Rita Santos | Not sent. Not a model decision |
| Internal summary | Jonah Park | May sit unread. Does not email the customer |

Remove the 22:00 auto-send. A gate no one staffs is not a gate.
Next: Jonah turns auto-send off before 18 September.""",
)

put(
    "ai-data-note",
    "Say what may be pasted into a model and what must stay in the source system.",
    "Agents want to paste the whole ticket into a model. Six of fourteen sample tickets include a card last-four and a home address. Vendor terms are not in the folder.",
    """```text
fields in a ticket: complaint text, order id, card last-four, home address, agent notes
vendor terms in the folder: none
retention promised: not documented
who pastes today: any agent on shift
sample: 14 tickets, 8-14 Sep 2026
```""",
    """**Data note**
Allowed in the paste: complaint text and order id.
Strip before paste: card last-four, home address.
Agent notes: stay in the help desk until Jonah says otherwise.
Vendor retention: open. No terms in the folder, so do not write 'they don't train on it'.
Who may paste: an agent on shift, after the strip.
Source of truth: the help desk, not the chat window.""",
)

put(
    "ai-cost-note",
    "Estimate the cost of a proposed AI workflow from the user's prices and volumes.",
    "A vendor demo says the bot will save $40,000 a month. Jonah has a price of $0.01 per call and last month's ticket count. He has not measured minutes saved.",
    """```text
price: $0.01 CAD per call, quote dated 2 Sep 2026, not a signed order
volume: 3,200 tickets in August 2026
calls per ticket if they draft once: 1
human review: still required, minutes not measured
claimed savings: $40,000 a month, no worksheet
cap they can stomach: $100 a month
```""",
    """**Cost note**
August calls at one draft each: 3,200 x $0.01 = $32. Under the $100 cap if they stay at one call and this quote.

The $40,000 savings is not in this note. Minutes saved were not measured.
Not in the price: retries, a second model, or a seat fee. None were on the quote.
High case: if they call the model three times per ticket, $96. Still under the cap, still not a savings claim.
Next: Jonah does not repeat the $40,000 figure.""",
)

put(
    "ai-vendor-note",
    "Compare AI vendors on data use, exit, and support the user can point to in a document.",
    "Fieldnote is looking at two model vendors. One website shows a SOC 2 badge. Neither report is in the folder. Jonah has a one-page quote from each.",
    """```text
vendor A quote: $0.01 per call, 2 Sep 2026, data terms not attached
vendor B quote: $0.04 per call, 3 Sep 2026, says "no training" in the email, no contract
SOC 2 reports: none in the folder
exit question: unanswered by both
pilot limit Jonah wants: one queue, 30 days
```""",
    """**Vendor note**
Do not treat the badge as a report. It is not in the file.

| Question | A | B |
| --- | --- | --- |
| Price in hand | $0.01 / call | $0.04 / call |
| Training use | not in the file | email says no, contract missing |
| SOC 2 | badge only | not mentioned |
| Exit with prompts | unanswered | unanswered |

Pilot, if any: one queue, 30 days, no card data, no company-wide switch.
Next: ask both for the data term in a document before a second pilot week.""",
)

put(
    "ai-incident-note",
    "Write up a bad model output the user observed, with the prompt, the harm, and the hold.",
    "On 14 September a support draft offered a $20 refund on ticket 4412 and the night rule sent it. The customer wrote back to accept. Rita had not approved the refund.",
    """```text
when: 14 Sep 2026, 22:04
ticket: 4412
what the draft added: a $20 refund
source ticket: customer said they were charged twice, no refund amount
sent: yes, by the 22:00 rule
customer reply: accepted the $20
other cases: none pulled yet
```""",
    """**Incident note**
One sent draft. Not yet a pattern. Only one case is in the file.

What happened: ticket 4412 asked about a double charge. The draft added a $20 refund. The night rule sent it. The customer accepted.
Hold now: auto-send off. Refunds stay with Rita.
Not in this note: a model 'cause'. No log of why it picked $20.
Customer name: omitted. Ticket number is enough.
Next: Rita decides the $20 already accepted. Jonah pulls any other night sends before calling it a pattern.""",
)

put(
    "ai-output-check",
    "Check a model draft against the source text the user supplied.",
    "Jonah has ticket 4418 and a model reply. The reply says the order shipped on 12 September and offers a $15 credit. The ticket does not say either.",
    """```text
ticket 4418: "charged twice on 12 Sep, order 4418. Please look."
draft: "Your order shipped on 12 September. I have applied a $15 credit."
claims that matter: ship date, credit
sender if approved: Rita
```""",
    """**Output check**
Do not send.

| Draft claim | In the ticket? |
| --- | --- |
| Charged twice | Yes, customer said it |
| Order 4418 | Yes |
| Shipped 12 September | No |
| $15 credit | No |

Cut both added lines. A person may say they will look. They may not add a ship date or a credit from this check.
Next: Rita sends her own sentence, or a draft with those two lines gone.""",
)

put(
    "rag-source-note",
    "Decide which documents may sit in a retrieval set and which are stale or out of bounds.",
    "The support bot's folder has a 2023 refund policy and the 2026 policy, plus a draft price list marked 'do not share'. Jonah needs the set cut down.",
    """```text
files: refund-policy-2023.pdf, refund-policy-2026-03.pdf, price-draft-2026-08 marked do not share, shipping-faq undated
owner: Jonah Park
topics the bot must not answer: legal threats, medical, card numbers
review date wanted: 1 Oct 2026
```""",
    """**Source pack**
In the set: refund-policy-2026-03.pdf only, for refund questions.
Out: the 2023 policy. Out: the August price draft.
Shipping FAQ: out until someone dates it.
Refuse rather than guess: legal threats, medical questions, anything with a card number.
Owner: Jonah. Review the set on 1 October 2026.
Do not add web pages to fill a gap.""",
)

put(
    "agent-task-card",
    "Bound an agent task: the inputs, the tools, the stop rules, and the human owner.",
    "A spec says the support agent may read the ticket, email the customer, and issue a credit under $30. Jonah wants a card that a person can enforce.",
    """```text
task: turn one ticket into a reply draft
tools named: help desk read, model draft
tools in the spec that he will not grant: send email, issue credit
stop if: the ticket has no order id, or a card number is present
owner of a bad run: Jonah Park
done looks like: a draft Rita can accept or reject
```""",
    """**Task card — support-reply-draft**
Done: a draft is waiting for Rita. Not done: an email sent, a credit posted.

Tools: read the ticket, write a draft. No other tool.
Stop: no order id, or a card number is still in the text. Do not draft. Ask a person.
Person required: sending, credits, refunds, deletes.
Owner: Jonah Park.
The earlier spec's send and credit lines are not on this card.""",
)
