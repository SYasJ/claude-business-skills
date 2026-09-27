from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "customer", "title": "Customer experience", "summary": "Journeys, support quality, recovery, and honest customer communication.", "keywords": ["customer", "support", "cx", "success", "journey"]},
    """
voice-of-customer | Voice of Customer | voice-of-customer brief
job: Assemble a voice-of-customer brief from real quotes and tickets, with the sample bias visible.
triggers: voice of customer; VOC brief; customer themes; what are customers saying
inputs: The sources; The decision; Sample sizes; Quotes they can share
steps: List sources and who is missing, such as quiet renewals or lost deals. || Theme by the job or failure, and attach only supplied quotes. || Separate frequency from severity. || Do not invent a quote to make a theme neater. || Recommend one product, policy, or support change. || Note what sales anecdotes cannot prove.
anti: Invented quotes; A brief with no sample bias; Themes with no evidence
example: A briefing uses one loud customer's words as if they were the whole base.
out: A brief that labels the sample and refuses to generalize from one voice.
related: feedback-synthesis; journey-map

journey-map | Journey Map | journey map
job: Map a customer journey around a real job, including waits, handoffs, and backstage failures.
triggers: journey map; customer journey; experience map; map the onboarding journey
inputs: The job the customer is trying to finish; Stages they actually pass; Evidence of pain; Backstage teams
steps: Define the job and the actor. A map of 'the customer' in general is too vague. || Use stages they can evidence. Do not add a delightful stage they wish existed and call it current. || Mark waits and repeats. || Show the backstage handoff that causes a frontstage failure. || Pick one moment to fix first, based on severity or drop-off they can show. || Keep emotions only if a customer stated them. Do not invent a feeling.
anti: A fantasy journey labeled current; Invented emotions; No backstage handoff
example: A map shows effortless onboarding while support tickets cluster on setup.
out: A current-state map that includes the setup failure and picks that moment to fix.
related: service-blueprint; onboarding-success-plan

support-macro | Support Macro | support reply
job: Draft a support reply that answers the question, states the limit, and does not invent a policy.
triggers: support macro; canned reply; help desk reply; customer reply draft
inputs: The customer's question; The policy that applies; What the agent can offer; The tone
steps: Answer the question in the first lines. || State the policy they supplied. If no policy was supplied, do not invent one. || Say what the customer should do next. || Include what you cannot do, plainly. || Keep a human tone without fake empathy padding. || Do not ask for passwords, full card numbers, or one-time codes.
anti: Invented policy; Asking for a password; A reply that never answers
example: A customer asks for a refund and the draft apologizes for three paragraphs without stating the refund rule.
out: A reply that states the known rule or says the agent must check it, and asks for no secrets.
related: service-recovery; knowledge-base-article

ticket-quality-review | Ticket Quality Review | ticket quality review
job: Review support ticket quality for resolution, tone, and whether the article or product should change.
triggers: ticket quality; QA support tickets; review these tickets; support QA
inputs: The tickets or summaries; The rubric they use; Recurring issues; What agents are allowed to do
steps: Score against their rubric. If they have none, use resolution, accuracy, and next step, and label that as a proposal. || Check that the reply answered the ask and did not invent a policy. || Look for repeated issues that belong in a macro or a product fix. || Note if agents are asking for secrets. That is a finding. || Give coaching on the pattern, not a pile of nits. || Recommend one article or product change if the tickets show a system gap.
anti: Coaching style before checking accuracy; Ignoring a secret request; A review with no pattern
example: Several tickets ask customers for their password to 'speed up' the fix.
out: A review that flags the password request as a stop-now finding and names the pattern.
related: support-macro; knowledge-base-article

csat-recovery | Low Score Recovery | recovery follow-up
job: Plan a follow-up to a low satisfaction score that seeks the cause and stays inside the remedy policy.
triggers: CSAT recovery; low survey score; detractor follow-up; unhappy customer follow-up
inputs: The score and any comment; What the company can offer; The owner; Whether the customer opted into contact
steps: Contact only if their process allows it. Do not help evade an opt-out. || Open with the specific issue if they wrote one. Do not be vague if the comment was specific. || Ask what done looks like. || Offer only remedies the user authorized. || Record the cause so the tenth similar score becomes a system fix. || Do not bribe a customer to change a public review. Refuse that request.
anti: Changing a review for a perk; Contacting someone who opted out; An offer the team cannot honor
example: A manager wants to offer a gift card if the customer edits a public review.
out: A follow-up that refuses the review edit, asks about the cause, and stays inside authorized remedies.
related: service-recovery; complaint-root-cause
avoid: Paying for review manipulation

escalation-playbook | Escalation Playbook | escalation playbook
job: Write an escalation path with levels, clocks, and the decision each level can make.
triggers: escalation playbook; escalate a ticket; severity path; customer escalation
inputs: Severity definitions; Who is on each level; Clocks they can staff; Customer communication owner
steps: Define severity by impact, not by who shouted. || Each level has a clock and a decision it can make. || Name the customer communication owner so engineering is not surprised by a promise. || Include how to de-escalate when impact falls. || Record what must be true before waking an executive. || Do not design a path that hides a safety or security issue from the proper owner.
anti: Severity set by loudness; An executive ping with no path; Hidden security issues
example: Every angry email is marked severe, so the on-call ignores the queue.
out: A playbook that defines severity by impact and reserves executive escalation for a written trigger.
related: incident-response-coord; sla-design

qbr-customer | Customer QBR | customer QBR
job: Plan a customer quarterly review around their outcomes, not around a product tour.
triggers: QBR; quarterly business review; customer business review; success review
inputs: Outcomes the customer wanted; Usage or results they confirmed; Open issues; The ask
steps: Open with their goal, not your roadmap. || Show only results they confirmed or that come from data they accept. || Address open issues before asking for an expansion. || Make one ask, tied to a next outcome. || Leave with owners on both sides. || Do not surprise them with a price change they have not been prepared for. Flag it as a separate conversation.
anti: A product tour labeled a QBR; Unconfirmed results; A surprise commercial ask
example: A QBR deck leads with new features and never mentions the customer's failed onboarding.
out: A review that leads with the onboarding gap, uses only confirmed results, and parks the feature tour.
related: account-plan; customer-health-score

onboarding-success-plan | Customer Onboarding Plan | customer onboarding plan
job: Plan customer onboarding to a first value moment, with owners on both sides.
triggers: customer onboarding; implementation plan; time to value; success plan
inputs: The first value moment; Steps to get there; Customer owners; Internal owners
steps: Define the first value moment in the customer's language. || Sequence only the steps required to reach it. Park the rest. || Assign a customer owner and an internal owner to each step. || State the evidence that value happened. || Name the stall that usually happens, if they know it, and the check-in that catches it. || Do not promise a go-live date operations has not accepted.
anti: An onboarding plan with no value moment; Unowned steps; A date operations did not accept
example: A plan lists 30 setup tasks and never says what the customer can do at the end.
out: A plan aimed at one value moment, with owners and a stall check.
related: journey-map; thirty-sixty-ninety

churn-interview | Churn Interview | churn interview
job: Prepare a churn or cancellation interview that learns the real reason without arguing.
triggers: churn interview; cancellation reason; why they left; exit interview customer
inputs: What you already know; What the team suspects; Who will talk; What remedy is still possible
steps: Open with curiosity, not a save pitch. || Ask about the moment they decided, and what they use instead, if they will say. || Do not argue them out of their reason. || Separate a product gap, a value gap, and a commercial mismatch. || Record the reason in their words. || If a save is allowed, offer it after the reason is understood, and only within policy.
anti: Arguing with the reason; A save offer before listening; Inventing the replacement they chose
example: A script opens by telling the customer they are making a mistake.
out: An interview guide that asks for the decision moment first and holds any save offer until after.
related: renewal-save; feedback-synthesis

service-recovery | Service Recovery | recovery plan
job: Plan recovery from a service failure with a truthful apology, a fix, and a remedy inside authority.
triggers: service recovery; we failed a customer; apology and remedy; make it right
inputs: What failed; Who was affected; The fix; The remedy the team is allowed to offer
steps: State the failure plainly. Do not bury it in an apology paragraph. || Say what you know and what you are still checking. || Describe the fix and the time, if known. Do not invent a restoration time. || Offer only an authorized remedy. || Tell them how to ask a follow-up question. || Feed the cause to the problem-management path so recovery is not the only response.
anti: A fake restoration time; An unauthorized remedy; An apology that hides the failure
example: A draft says 'everything is resolved' while the queue is still failing.
out: A message that states the ongoing failure, omits the fake resolution, and offers only an authorized remedy.
related: csat-recovery; customer-communication-incident

cx-metric-tree | CX Metric Tree | CX metric tree
job: Build a customer-experience metric tree that connects a relationship metric to operational inputs.
triggers: CX metrics; customer metric tree; NPS driver tree; experience KPIs
inputs: The relationship metric they use; Operational inputs they can measure weekly; Owners; Known gaming risks
steps: Define the relationship metric they actually collect. Do not install a new score by fashion. || Add inputs a team can move: wait time, reopen rate, or time to value, if they have them. || Pair speed with quality. || Name the owner of each input. || Note how the metric is gamed, such as survey begging. Recommend against it. || Use their baseline or mark it unknown.
anti: A new vanity score with no inputs; Survey begging; No owner
example: The company tracks NPS and wants the number up, with no operational input on the tree.
out: A tree that keeps their relationship metric and adds owned operational inputs, and bans survey begging.
related: north-star-metric; ops-scorecard

complaint-root-cause | Complaint Root Cause | complaint analysis
job: Analyze a cluster of complaints to the cause the company can fix, without dismissing the customer.
triggers: complaint analysis; root cause of complaints; repeated complaints; why are tickets rising
inputs: The complaint cluster; Volumes; What agents already do; Recent changes
steps: Define the cluster with their labels and volumes. || Read for the failed job, not for the customer's tone. || Separate a product defect, a policy surprise, and an expectation set by marketing. || Check a recent change that matches the timing. || Recommend one fix: policy, product, or message. || Do not blame the customer in the write-up.
anti: Blaming tone; A fix that does not match the cause; Ignoring a recent change
example: Complaints rose after a pricing page started hiding a fee.
out: An analysis that names the hidden fee as the hypothesis to fix and does not blame the customers for writing in.
related: voice-of-customer; marketing-claims-review

customer-health-score | Customer Health Score | health score definition
job: Define a customer health score from signals that predict renewal risk, and show the formula.
triggers: health score; customer health; red account logic; success score
inputs: Signals they can collect; What happened before past churn if known; Who will act on red; The formula they use today
steps: Start from the action a red score triggers. A score with no action is a toy. || Choose signals they can collect without creepy surveillance. || Show the formula. Hidden points are a finding. || Weight only with evidence they have. If they have no history, call the score a hypothesis. || Set a review so a red account gets a human, not only a color. || Do not include sensitive personal data in the score.
anti: A hidden formula; A score nobody acts on; Sensitive personal data as an input
example: A health score marks accounts red and no one has a play for red.
out: A visible formula and a required human play for red, or a recommendation not to launch the score yet.
related: renewal-save; cx-metric-tree

customer-communication-incident | Customer Incident Communication | incident communication
job: Draft customer incident updates that say what is known, what is not, and when the next update will come.
triggers: incident communication; status page update; outage email; customer incident update
inputs: Known impact; Unknowns; Next update time; Approver
steps: State the impact a customer would notice. || Separate confirmed facts from work in progress. || Give the next update time even if there is no fix yet. || Do not speculate about cause or blame a supplier unless that statement is approved. || Tell customers what to do if anything, such as retry after a time, only if support confirmed it. || Keep a log of what was said so later updates do not contradict earlier ones.
anti: A cause guess; A silent gap with no next update; Contradicting the previous update
example: A draft blames a vendor and promises a fix in 15 minutes without engineering confirmation.
out: An update that removes the blame and the unconfirmed clock, and commits to a next update time.
related: service-recovery; war-room-brief
"""
))

PACKS.append(pack(
    {"id": "risk", "title": "Risk and compliance", "summary": "Risk assessments, controls, and compliance operations. Not a certification and not legal advice.", "keywords": ["risk", "compliance", "controls", "audit", "privacy"]},
    """
risk-assessment | Risk Assessment | risk assessment
job: Assess a few real risks with a scenario, a control, and an owner, using the organization's own scale.
triggers: risk assessment; assess this risk; risk workshop; enterprise risk item
inputs: The objective at risk; Scenarios they can describe; Existing controls; Their scale
steps: Write scenarios as events, not as one-word categories. || Use their likelihood and impact scale. If none exists, propose a simple one and label it. || Name the current control and whether they have evidence it operates. || Rate residual risk only after the control is described. || Recommend mitigate, accept, or transfer as a question for the owner. Insurance transfer is not confirmed unless they say a policy exists. || Do not claim a certification because a risk was written down.
anti: One-word risks; A certification claim; Ratings with no scale
example: A workshop list says 'cyber' and 'talent' with no scenario.
out: An assessment that rewrites those into specific events or drops them until a scenario exists.
related: risk-register; control-design

control-design | Control Design | control design
job: Design a control that prevents or detects a named failure, and specify the evidence it leaves.
triggers: design a control; control activity; preventive control; detective control
inputs: The failure to prevent; How the work happens today; Who can perform the control; Evidence available
steps: State the failure in one sentence. || Choose preventive or detective based on when the harm becomes irreversible. || Assign a performer who is not the only person benefiting from a bypass, when they can staff that. || Specify the evidence: a review note, a system log, or a sign-off. || Define the frequency. || A control with no evidence is a hope. Say so.
anti: A control with no evidence; The beneficiary is the only reviewer; A policy sentence with no activity
example: The control is 'management reviews revenue' with no sample and no sign-off.
out: A design that names the sample, the reviewer, and the evidence left behind.
related: internal-controls-walkthrough; sox-walkthrough

policy-writer | Policy Writer | policy draft
job: Draft a policy people can follow, with an owner, an exception path, and a review date.
triggers: write a policy; policy draft; governance policy; company policy
inputs: The behavior to govern; The owner; The audience; Related procedures
steps: State the purpose and who it applies to. || Write requirements as behaviors. || Point to the procedure for how. The policy should not be a novel. || Add an exception path and an owner. || Set a review date. || Mark it draft until the owner adopts it. Do not invent regulatory citations.
anti: A policy with no owner; Invented legal citations; Requirements nobody can perform
example: A draft cites several laws from memory to sound serious.
out: A draft that removes the invented citations, names an owner, and stays short enough to follow.
related: handbook-policy-draft; security-policy-draft

compliance-calendar | Compliance Calendar | compliance calendar
job: Build a calendar of obligations the organization already knows it has, with owners and lead time.
triggers: compliance calendar; obligations calendar; filing calendar; compliance dates
inputs: Known obligations; Owners; External dates they have confirmed; Last year's misses
steps: Record only obligations they confirmed. Do not invent a filing. || Mark unconfirmed dates as unconfirmed. || Put an internal due date earlier than the external one so review can happen. || Assign an owner and a reviewer. || Note evidence saved when the obligation is met. || Send new-jurisdiction questions to counsel rather than answering them from memory.
anti: Invented deadlines; A calendar with no owners; Dates stored with portal passwords
example: A team wants every possible global filing listed just in case.
out: A calendar of confirmed obligations, with unknowns flagged for counsel instead of invented.
related: tax-calendar; regulatory-change-log

sox-walkthrough | SOX Walkthrough Prep | SOX walkthrough prep
job: Prepare a walkthrough of a financial control so the performer can show what they actually do.
triggers: SOX walkthrough; control walkthrough prep; audit walkthrough; ICFR prep
inputs: The control description; The performer; The evidence; The period
steps: Restate the risk and the control in plain language. || Ask the performer to walk a real transaction, not a theoretical one. || Match the walk to the control description. Differences are findings, not things to hide. || Identify missing evidence before the auditor does, and say so to management. || Do not coach anyone to misrepresent the control. || Note samples you did not test. A prep is not a test of operating effectiveness.
anti: Coaching a false story; Hiding a gap; Claiming effectiveness from a prep chat
example: A manager wants the performer to describe a review that does not happen.
out: A prep note that refuses the false story and writes the gap for management.
related: control-design; audit-response
avoid: Misleading an auditor

privacy-impact-assessment | Privacy Impact Assessment | privacy impact note
job: Prepare a privacy impact note for a process that collects personal data, for counsel to complete.
triggers: privacy impact; PIA; DPIA prep; new processing review
inputs: The process; Data elements; People affected; Recipients they named
steps: Describe the process and the purpose. || List data elements and who they are about. Cut elements with no purpose. || List recipients the user named. Do not invent vendors. || Note retention if known, otherwise mark it unknown. || Flag high-harm contexts they mentioned, such as children or precise location, for counsel. Do not complete a legal DPIA conclusion. || Recommend a product change where minimization is obvious.
anti: A legal conclusion dressed up as a PIA; Invented vendors; Keeping data with no purpose
example: A new form collects date of birth to personalize a color theme.
out: A note that cuts the date of birth and sends any remaining legal question to counsel.
related: privacy-by-design; privacy-notice-draft

third-party-risk | Third-Party Risk | third-party risk note
job: Screen a third party for the risk created by the access and data you will give them.
triggers: third-party risk; vendor risk; supplier risk review; outsourcing risk
inputs: The service; Data and access involved; Their evidence; The business owner
steps: Rate inherent risk from access and data, in plain tiers you label as a proposal if they have no method. || Review only evidence they collected. A missing questionnaire is a gap. || Recommend a lighter review for low access and a deeper one for sensitive data. || Name the business owner who accepts residual risk. || Tie contract questions to the legal and security skills. Do not duplicate a fake certification. || Re-review on a date or when the service changes.
anti: The same heavy review for every vendor regardless of data; A pass with no evidence; No business owner
example: A design tool and a payroll processor are put through an identical unread checklist.
out: A note that deepens the payroll review, lightens the design-tool review, and names the owner.
related: vendor-security-review; vendor-ops-review

records-retention | Records Retention Schedule | retention schedule draft
job: Draft a retention schedule from the record types they know they keep, with owners and legal questions marked.
triggers: records retention; retention schedule; how long do we keep this; record series
inputs: Record types; Where they live; Business need they stated; Legal holds they know about
steps: List record types they actually keep, not a generic encyclopedia. || Record the business reason to keep each one. || Mark the legal period as a question for counsel unless they supplied it. Do not invent a statutory period. || Note systems so people can find and delete on purpose. || Holds override deletion. Say that, and do not help delete held records. || Name an owner for the schedule.
anti: Invented statutory periods; Deleting records under a known hold; A schedule of records they do not have
example: A team wants a seven-year rule on everything because it sounds safe.
out: A draft that refuses the blanket rule, separates business need from legal questions, and protects holds.
related: legal-hold-notice; policy-writer

ethics-hotline-triage | Ethics Hotline Triage | hotline triage
job: Triage a hotline report toward the right independent handler, without retaliation or a verdict.
triggers: ethics hotline; speak-up report; ethics triage; hotline intake
inputs: The allegation summary; Who it names; Safety issues; The company's routing rules
steps: If someone is in immediate danger, point to emergency services and their safety process. || Record the allegation without adding motive. || Route away from anyone named in the report. || Minimize personal data in the routing note. || Refuse any request to identify or punish the reporter for reporting. || This triage is not an investigation finding.
anti: A verdict at triage; Retaliation; Routing to the accused
example: A report names the division president, and the president asks to handle it personally.
out: A triage that routes around the president and refuses retaliation against the reporter.
related: whistleblower-intake; employee-relations-intake
avoid: Retaliation; Cover-up

regulatory-change-log | Regulatory Change Log | regulatory change log
job: Log a regulatory change the user has identified, with impact questions and an owner, without giving a legal opinion.
triggers: regulatory change; new rule log; compliance change; regulation tracker
inputs: The source they provided; The date they believe applies; Products or processes affected; The owner
steps: Record the source they gave. Do not invent a citation. || Summarize the change in their words and mark uncertainties. || List impact questions for counsel or compliance: does it apply, by when, and to which process. || Assign an owner to get those answers. || Do not tell the business to ignore a rule, and do not declare them compliant. || Review the log on a cadence so a noted change does not sit unread.
anti: An invented citation; A compliance declaration; An instruction to ignore a rule
example: A blog post says a rule changed, and the team wants to mark the company compliant today.
out: A log entry that sources the blog as unverified, assigns counsel questions, and makes no compliance claim.
related: compliance-calendar; outside-counsel-brief

audit-response | Audit Response | audit response
job: Draft a response to an audit request that is complete, tied to evidence, and not misleading.
triggers: audit response; auditor question; management response; finding response
inputs: The request or finding; The evidence; The process owner; The due date
steps: Restate the request so you answer the question asked. || Point to evidence. Do not describe a control that the evidence does not show. || If the finding is fair, say what will change, with an owner and a date. || If the finding is wrong, explain with evidence, not with adjectives. || Do not coach anyone to alter evidence. || Mark drafts for the process owner to approve before they go to the auditor.
anti: Misleading the auditor; Altering evidence; A promise with no owner
example: A draft response describes a monthly review that exists only in the policy, not in practice.
out: A response that tells the truth about the gap and commits to an owned fix instead of a fictional review.
related: sox-walkthrough; audit-prep-pbc
avoid: Misleading an auditor; Altering evidence

conflict-of-interest | Conflict of Interest Disclosure | conflict disclosure
job: Structure a conflict-of-interest disclosure so a reviewer can see the interest and the decision it touches.
triggers: conflict of interest; COI disclosure; related party; disclose a conflict
inputs: The interest; The decision or process it touches; Who else knows; The review path
steps: Describe the interest in plain language: financial, family, or outside role, as the user stated. || Name the decision or vendor it could affect. || Propose recusal or a review, using their policy if they supplied one. || Do not help hide the interest. || Minimize unrelated personal details. || Record the reviewer's decision once they make it. Do not invent an approval.
anti: Hiding an interest; Unrelated personal details; A fake approval
example: An employee wants the disclosure to omit that their sibling owns the bidding vendor.
out: A disclosure that includes the sibling relationship and recommends recusal from the award.
related: gifts-and-entertainment; procurement-award-note

gifts-and-entertainment | Gifts and Entertainment | gift decision note
job: Apply a gifts and entertainment rule to a specific offer, and record the decision.
triggers: gift policy; can we accept this; entertainment request; hospitality gift
inputs: The offer and its value if known; Who offered it; The decision pending with that party; Their policy
steps: State the offer, the giver, and whether a decision is pending with that party. || Apply their policy thresholds. If they have no policy, recommend a decision from leadership rather than inventing a legal rule. || A pending procurement or hiring decision raises the risk. Say so. || Recommend accept, decline, or accept with disclosure, for their approver to confirm. || Record it. || Do not help disguise a gift as something else.
anti: Disguising a gift; Inventing a legal threshold; Accepting a gift during a live bid without flagging it
example: A bidder offers tickets during an open RFP and the draft calls them a friendly dinner.
out: A note that names the open RFP, refuses the disguise, and recommends decline or disclosure under their policy.
related: conflict-of-interest; procurement-award-note

issue-management | Issue Management | issue record
job: Record a compliance or control issue with severity, owner, and a dated remediation.
triggers: issue management; control issue; remediation plan; audit issue
inputs: The issue; The failed control or obligation; The harm; The proposed fix
steps: Describe the issue as a fact, not as a softening adjective. || Link it to the control or obligation. || Rate severity with their scale or a labeled proposal. || Write remediation with an owner and a date. A plan without either is a wish. || Note compensating control until the fix lands. || Verify closure with evidence, not with an email that says done.
anti: Closure without evidence; No owner; A softened description that hides the gap
example: An issue is marked closed because the owner said the spreadsheet was updated, with no sample.
out: An open issue until a sample shows the control operating, with a dated owner.
related: control-design; audit-response

sanctions-compliance-process | Sanctions Screening Operations | screening operations note
job: Describe how a legitimate screening process should handle a possible match, for compliance staff. Not evasion advice.
triggers: sanctions screening; possible match; screening operations; name match review
inputs: The match information they are allowed to share; Their escalation policy; The business process paused; The compliance owner
steps: Treat a possible match as unresolved until their compliance owner clears it. || Do not advise altering a name, address, or ownership record to avoid a match. || List the documents their policy already uses to distinguish a false positive. || Pause the prohibited transaction if their policy says to pause. || Record the decision and the reviewer. || This skill does not determine whether a person is sanctioned and does not help anyone evade screening.
anti: Advice to alter records to dodge a match; A homemade legal clearance; Skipping the compliance owner
example: Sales wants to tweak a customer name so the screening tool stops flagging it.
out: A refusal of the tweak, a pause recommendation, and a handoff to the compliance owner.
related: third-party-risk; ethics-hotline-triage
avoid: Sanctions evasion; Altering records to defeat screening
"""
))
