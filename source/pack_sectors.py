from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "consulting", "title": "Consulting", "summary": "Engagement framing, findings, and readouts that separate evidence from advice.", "keywords": ["consulting", "engagement", "findings", "client"]},
    """
engagement-framing | Engagement Framing | engagement brief
job: Frame a consulting engagement with the decision, the evidence, and what is out of scope.
triggers: engagement brief; consulting scope; statement of work narrative; frame the work
inputs: The client decision; Evidence you can access; Time; Out-of-scope items
steps: Write the decision the client must make. || List evidence already available and evidence you will not pretend to have. || Cut scope that does not serve the decision. || Name the client owner. || State what would make the engagement stop early. || Do not promise a finding before the evidence is reviewed.
anti: A promised conclusion; Scope with no decision; Hidden out-of-scope work
example: A proposal promises a 20 percent savings number before any baseline exists.
out: A brief that replaces the number with a baseline task and a decision.
related: proposal-writer; outside-counsel-brief

findings-readout | Findings Readout | findings readout
job: Read out findings with evidence, implications, and a recommendation the sponsor can reject.
triggers: findings readout; client readout; recommendation readout; consulting readout
inputs: The findings; The evidence; The recommendation; The audience
steps: Lead with the answer. || Attach evidence to each finding. No evidence, no finding. || Separate implication from fact. || Give the sponsor a real alternative. || Note limits. || Do not soften a finding to please the sponsor, and do not exaggerate to justify fees.
anti: Findings with no evidence; A readout written to please; No alternative
example: A readout drops a critical finding because the sponsor disliked it in the dry run.
out: A readout that keeps the finding, labels it clearly, and offers the sponsor a decision.
related: executive-one-pager; executive-insight

interview-synthesis-client | Client Interview Synthesis | interview synthesis
job: Synthesize client interviews into themes with quotes the interviewee actually gave.
triggers: interview synthesis; stakeholder interviews; client interviews; theme synthesis
inputs: The notes; The decision; Who was not interviewed; Confidentiality limits
steps: Theme only what the notes support. || Use short quotes they captured. Do not improve a quote into a different meaning. || Say who was not in the room. || Respect confidentiality limits they stated. || Recommend one implication. || Do not attribute a view to a named person if the user said the readout must be anonymous.
anti: Improved quotes; A missing-voice problem ignored; Named comments in an anonymous readout
example: A synthesis says the CFO demanded a cut, and the note was anonymous and less specific.
out: A synthesis that keeps the anonymity rule and narrows the claim to the words in the note.
related: feedback-synthesis; stakeholder-map

workshop-decision-record | Workshop Decision Record | workshop decision record
job: Turn a client workshop into a decision record rather than a photo of sticky notes.
triggers: workshop readout; decision record workshop; sticky note synthesis; working session notes
inputs: The decision sought; Options generated; The choice if one was made; Dissent
steps: State whether a decision was made. If not, say so. || Record options in the client's words. || Note dissent. Do not convert silence into agreement. || Assign owners only for actions the room accepted. || Park ideas that lost. || Do not add recommendations the room did not hear and call them workshop output.
anti: Fake consensus; Owners the room did not accept; A novel of sticky notes
example: Notes say the client chose a market, but the room only brainstormed.
out: A record that labels the market as an idea, not a decision, and lists the open choice.
related: decision-log; workshop-facilitation
"""
))

PACKS.append(pack(
    {"id": "nonprofit", "title": "Nonprofit and public interest", "summary": "Case statements, grants, and program reviews that do not invent impact.", "keywords": ["nonprofit", "fundraising", "program", "impact"]},
    """
nonprofit-case-statement | Case Statement | case statement
job: Write a case for support from real need, real program facts, and a specific ask.
triggers: case for support; fundraising narrative; case statement; donor narrative
inputs: The need they can evidence; The program; The ask; What donors must not be told
steps: Describe the need with evidence they have. || Explain what the program actually does. || Separate outputs from outcomes. || Make one ask. || Do not invent a beneficiary story or a success rate. || Avoid pressure tactics that misstate urgency.
anti: Invented beneficiary stories; A fake urgency; Outcomes they have not measured
example: A case says 90 percent of participants succeed, and no outcome is tracked.
out: A case that removes the percentage and describes the program without a fake rate.
related: grant-narrative; marketing-claims-review

program-logic | Program Logic | logic model
job: Draft a program logic model that shows inputs, activities, and outcomes without pretending impact is proven.
triggers: logic model; theory of change; program logic; outcome model
inputs: Inputs they have; Activities; Intended outcomes; Evidence so far
steps: Start from activities they actually run. || Write outcomes as changes, and label them intended if unmeasured. || Show the assumption between activity and outcome. || Do not draw an impact arrow they have not tested. || Note missing data. || Keep the model to one program.
anti: A proven-impact claim with no measure; Activities that are not real; A model of five programs at once
example: A logic model says the workshop causes employment, and nobody tracked jobs.
out: A model that labels employment as intended and names the missing measure.
related: nonprofit-case-statement; metric-definition

board-fundraising-report | Fundraising Report | fundraising report
job: Report fundraising progress with cash received, pledges, and restrictions kept distinct.
triggers: fundraising report; donor report; campaign progress; gift report
inputs: Cash received; Pledges; Restrictions; The goal
steps: Separate cash from pledges. || Note restrictions that limit use. || Compare to the goal they set. || Do not count a verbal maybe as a pledge. || Name the pipeline only with evidence. || No individual donor's private details beyond what the user said may be shared.
anti: Maybes counted as pledges; Restricted gifts shown as unrestricted; Private details overshared
example: A report counts a dinner conversation as committed revenue.
out: A report that moves the conversation to a prospect note and keeps cash and pledges apart.
related: cash-flow-forecast; nonprofit-case-statement

volunteer-role | Volunteer Role | volunteer role brief
job: Write a volunteer role with the work, the time, and the supervision, without unpaid-staff exploitation hidden in cheerful language.
triggers: volunteer role; volunteer description; unpaid role brief; volunteer handbook section
inputs: The work; Time expected; Supervisor; What volunteers will not do
steps: Describe the work and the time honestly. || Name the supervisor. || State boundaries: what requires staff or a professional. || Do not assign regulated duties to volunteers unless the user says their policy allows it, and even then flag review. || Explain how to stop volunteering. || Keep the tone respectful. Volunteers are not free employees to squeeze.
anti: Hidden time demands; Regulated work pushed to volunteers casually; No supervisor
example: A role asks volunteers to give clinical advice with no clinician present.
out: A brief that removes the clinical duty and names a supervisor for the remaining work.
related: job-description-writer; patient-communication
"""
))

PACKS.append(pack(
    {"id": "banking", "title": "Banking and treasury operations", "summary": "Cash operations and credit-file hygiene. Not a credit decision and not a request for banking passwords.", "keywords": ["banking", "treasury", "credit", "payments"]},
    """
payment-run-review | Payment Run Review | payment run review
job: Review a payment run for duplicates, approvals, and changes to payee details.
triggers: payment run; AP run review; pay cycle review; payment approval
inputs: The run list; Approval limits; Changed payee details; Exceptions
steps: Check the run against approvals they require. || Flag duplicate-looking items for review, not as accusations. || Any payee detail change needs their verified channel. || Do not ask for banking passwords or one-time codes. || Exceptions need a named approver. || Recommend a hold on items that fail the check rather than a silent release.
anti: A password request; A silent release of a failed item; An unverified bank-detail change
example: A payment run includes a new account number received by email this morning.
out: A review that holds that item until the verified channel confirms it.
related: accounts-payable-control; treasury-policy-brief

credit-file-checklist | Credit File Checklist | credit file checklist
job: Checklist a credit file for missing information before a human credit officer decides.
triggers: credit file; loan file checklist; credit memo prep; borrower file
inputs: Their required list; Documents present; The decision owner; Known gaps
steps: Compare the file to their list. || Mark missing items. Do not fill gaps with estimates presented as facts. || This skill does not approve credit. || Note policy exceptions for the officer. || Minimize personal data in the summary. || Do not help a borrower falsify income or identity documents.
anti: A homemade credit approval; Falsified income; Estimates labeled as statements
example: A file is missing current financials and the draft says the borrower is strong.
out: A checklist that leaves the file incomplete and removes the strength claim.
related: debt-capacity-screen; outside-counsel-brief
avoid: Falsifying borrower documents; Unauthorized credit approval

account-opening-ops | Account Opening Operations | account-opening checklist
job: Review an account-opening checklist for identity steps they require, without collecting secrets into the chat.
triggers: account opening; KYC checklist; onboarding a customer bank; new account ops
inputs: Their required steps; What is complete; Exceptions; The reviewer
steps: Use their checklist. Do not invent a regulator's rule. || Note missing identity steps as gaps. || Do not ask customers to send passwords or full card data by chat. || Exceptions need their compliance owner. || A possible sanctions match follows their screening process. Do not suggest altering a name. || This is operations support, not a license to open the account.
anti: Invented regulatory rules; Name changes to dodge screening; Secrets collected in chat
example: Staff want to skip an identity step because the customer is in a hurry.
out: A checklist that keeps the step and routes any exception to the compliance owner.
related: sanctions-compliance-process; customer-onboarding-success-plan

liquidity-ladder | Liquidity Ladder | liquidity ladder
job: Build a simple liquidity ladder from cash, committed inflows, and committed outflows.
triggers: liquidity ladder; cash ladder; treasury forecast; short-term liquidity
inputs: Cash by account; Committed inflows; Committed outflows; Available facilities they described
steps: Group by the buckets they care about, such as this week and this month. || Include only committed items unless an uncommitted item is clearly labeled. || Show facilities separately from cash. || Flag the first bucket that fails their minimum. || Do not move money or request credentials. || Recommend a decision for the treasurer, not a trade.
anti: A facility shown as cash; Uncommitted inflow shown as certain; A credential request
example: A ladder treats an undrawn line as money already in the account.
out: A ladder that separates the line from cash and flags the first short bucket.
related: cash-flow-forecast; treasury-policy-brief
"""
))

PACKS.append(pack(
    {"id": "insurance", "title": "Insurance operations", "summary": "Claims files and coverage questions organized for a licensed professional. Not a coverage determination.", "keywords": ["insurance", "claims", "policy", "broker"]},
    """
claim-file-checklist | Claim File Checklist | claim file checklist
job: Organize a claim file so a handler can see facts, documents, and open questions.
triggers: claim file; insurance claim checklist; FNOL file; claims documentation
inputs: The reported facts; Documents on hand; The policy form they have; The handler
steps: Record facts separately from opinions. || List missing documents. || Do not decide coverage. || Do not coach anyone to inflate a loss or omit a material fact. || Note the next handler action and date. || Minimize sensitive data in summaries.
anti: A coverage determination; Inflated loss advice; Omitted material facts
example: A customer asks how to describe the loss so the payout is higher than the damage.
out: A checklist that refuses the inflation and lists the facts the handler still needs.
related: dispute-intake; outside-counsel-brief
avoid: Claims fraud; Inflating a loss

coverage-question-brief | Coverage Question Brief | coverage brief
job: Brief a coverage question for a licensed professional, with the policy words the user supplied.
triggers: coverage question; does this policy cover; insurance interpretation; coverage brief
inputs: The question; The policy words they pasted; The facts; The licensed reviewer
steps: Quote the policy words they supplied. || State the facts. || List the question for the licensed reviewer. || Do not say the person is covered or not covered. || If the policy text is missing, stop. || Do not invent an endorsement.
anti: A coverage yes or no; An invented endorsement; A brief without the policy words
example: A colleague wants a firm yes on flood coverage from a brochure.
out: A brief that refuses the yes and asks for the policy form instead of the brochure.
related: claim-file-checklist; contract-risk-review

broker-renewal-prep | Renewal Preparation | renewal prep
job: Prepare an insurance renewal packet from the expiring facts and the changes the insured reported.
triggers: insurance renewal; renewal submission; broker renewal; market submission
inputs: Expiring terms they have; Changes in operations; Losses they reported; The deadline
steps: List changes the insured actually reported. || Include losses they documented. Do not omit a known loss. || Mark unknown values as unknown. || Note the questions underwriters asked last time if the user has them. || Do not invent a premium. || This packet does not bind coverage.
anti: An omitted known loss; An invented premium; A claim that coverage is bound
example: A renewal draft leaves off a recent claim to keep the story clean.
out: A packet that includes the claim and labels any premium figure as not yet quoted.
related: claim-file-checklist; risk-assessment

loss-run-summary | Loss Run Summary | loss-run summary
job: Summarize a loss run the user provided, without forecasting a premium or hiding a large loss.
triggers: loss run; claims history summary; loss summary; insurance history
inputs: The loss run; The years it covers; Large losses; What the reader needs
steps: State the period and the source. || Summarize counts and amounts from the run. || Call out large or open items. || Do not drop a loss to improve the picture. || Do not predict an insurer's price. || Note gaps in the years if the run is incomplete.
anti: A dropped loss; A premium prediction; An incomplete run treated as complete
example: A summary averages away one severe open claim.
out: A summary that shows the severe claim separately and makes no price prediction.
related: claim-file-checklist; management-reporting-pack
"""
))

PACKS.append(pack(
    {"id": "public-sector", "title": "Public sector", "summary": "Briefing notes and consultation records that are accurate and suitable for the public record.", "keywords": ["public-sector", "briefing", "consultation", "government"]},
    """
briefing-note | Briefing Note | briefing note
job: Write a briefing note that states the issue, the options, and the recommendation for a public decision-maker.
triggers: briefing note; ministerial brief; decision note public; options brief
inputs: The decision; The facts they can publish; The options; The audience
steps: Lead with the purpose and the recommendation. || Use facts they can stand behind on the record. || Give real options, including do nothing. || State the public impact and the implementation constraint. || Do not draft deceptive messaging or a plan to manipulate a consultation. || Mark classified or personal data as not for this note.
anti: Deceptive public messaging; Personal data in the brief; A recommendation with no option
example: A brief omits a known cost because it would be unpopular.
out: A note that includes the cost and a plain recommendation.
related: executive-one-pager; board-memo-writer
avoid: Deceptive public communications; Voter manipulation

consultation-summary | Consultation Summary | consultation summary
job: Summarize a consultation without burying dissenting views.
triggers: consultation summary; public comments; hearing summary; feedback summary public
inputs: The question consulted; The responses they have; How people were invited; The decision still open
steps: State the question and the invitation method. || Count responses only from their log. || Summarize themes and include dissent. || Do not claim the public agreed if the sample is self-selected. Say so. || Separate comments from the decision. || Do not identify private individuals beyond their public submission rules.
anti: Buried dissent; A false claim of public agreement; Identifying private people against their rules
example: A summary says residents support a plan when most comments opposed it.
out: A summary that reports the opposition and refuses the support claim.
related: survey-analysis; feedback-synthesis

public-meeting-minutes | Public Meeting Minutes | public minutes
job: Draft minutes of a public meeting that record motions, votes, and conflicts.
triggers: public minutes; council minutes; board minutes public; meeting record
inputs: The agenda; Motions and votes they recorded; Conflicts declared; The approver
steps: Record motions and votes as given. || Note declared conflicts. || Do not invent attendance or a vote. || Summarize discussion without caricature. || Mark the draft for the clerk or chair to approve. || Keep the tone suitable for the public record.
anti: An invented vote; A missing declared conflict; Color commentary
example: Minutes say a motion passed unanimously though a dissent was recorded.
out: Minutes that include the dissent and wait for the clerk's approval.
related: board-meeting-facilitator; decision-log

records-request-triage | Records Request Triage | records request triage
job: Triage a records request for scope, search, and exemptions their officer must decide.
triggers: records request; FOI triage; public records request; information request
inputs: The request; Systems that may hold records; Their exemption list if any; The officer
steps: Restate the scope. Ask one clarifying question if it is too broad to search. || List likely locations. Do not search systems the user did not authorize. || Flag exemptions as questions for the officer. Do not withhold records on a homemade theory. || Note personal data that may need redaction by the officer. || Do not destroy records because a request arrived. || Give a realistic search plan, not a promise of a legal deadline you invented.
anti: Destroying records after a request; A homemade exemption ruling; An invented legal deadline
example: A manager wants to delete drafts because a request might cover them.
out: A triage that forbids deletion and lists locations for the officer to decide.
related: records-retention; legal-hold-notice
avoid: Destroying records; Evading a lawful request
"""
))

PACKS.append(pack(
    {"id": "sustainability", "title": "Sustainability", "summary": "Emissions and supplier questionnaires that do not invent factors or certifications.", "keywords": ["sustainability", "emissions", "esg", "suppliers"]},
    """
emissions-inventory-brief | Emissions Inventory Brief | inventory brief
job: Brief an emissions inventory from activity data they have, with factors labeled and gaps visible.
triggers: emissions inventory; carbon footprint; GHG inventory; scope 1 2 3
inputs: Activity data; Factors they are using; Organizational boundary; Known gaps
steps: Define the boundary they chose. || List activity data they actually have. || Apply only factors they supplied, and show the source. Do not invent a factor. || Mark missing categories as gaps. || Separate a number from an assurance opinion. || Recommend the next data improvement, not a claim of net zero.
anti: An invented emissions factor; A net-zero claim from a partial inventory; Hidden gaps
example: A report states net zero because one office bought offsets, and no inventory exists.
out: A brief that refuses the claim and lists the missing activity data.
related: marketing-claims-review; metric-definition

supplier-sustainability-questionnaire | Supplier Sustainability Questionnaire | questionnaire review
job: Review supplier sustainability answers for evidence, not for a score that hides missing proof.
triggers: supplier sustainability; ESG questionnaire; supplier carbon data; sustainability survey review
inputs: The questions; The answers; Evidence attached; The decision the score would feed
steps: Score evidence, not adjectives. || A missing answer is a gap, not a zero that looks precise. || Do not invent a supplier's emissions. || Note claims of certification only if the certificate is in the file. || Recommend follow-up questions. || Do not use the questionnaire to accuse a supplier of fraud. Ask for evidence.
anti: An invented supplier footprint; A certification assumed; A precise score on missing data
example: A supplier says it is certified and attaches no certificate.
out: A review that marks the certification unverified and asks for the document.
related: supplier-scorecard; vendor-security-review

sustainability-claim-review | Sustainability Claim Review | claim review
job: Review a sustainability claim for substantiation before it is published.
triggers: sustainability claim; green claim; ESG claim review; net zero wording
inputs: The claim; The evidence; Where it will appear; The reviewer
steps: Quote the claim. || Match each factual part to evidence. || Qualifiers such as net zero or carbon neutral need the basis they can show. If the basis is missing, cut the words. || Avoid vague 'eco' language that implies a standard they do not meet. || Send legal and advertising questions to counsel if they said the jurisdiction requires it. || Do not help greenwash.
anti: Greenwashing; A standard implied but not held; A claim with no evidence
example: Packaging says 'carbon neutral' and the only support is an intention.
out: A review that removes the phrase until the basis exists.
related: marketing-claims-review; emissions-inventory-brief

esg-disclosure-outline | ESG Disclosure Outline | disclosure outline
job: Outline an ESG disclosure around metrics the company can evidence this year.
triggers: ESG disclosure; sustainability report outline; nonfinancial disclosure; impact report
inputs: The audience; Metrics they can evidence; Framework language they already chose; Gaps
steps: Include only metrics with a definition and a source. || If they name a framework, use their mapping. Do not invent compliance with a standard. || Put gaps in the outline so the report does not imply completeness. || Separate targets from results. || Avoid double-counting a story in every chapter. || This outline is not assurance.
anti: Implied certification; Targets written as results; Metrics with no source
example: A report outline claims alignment with a standard nobody has mapped.
out: An outline that labels alignment as not yet assessed and lists only sourced metrics.
related: emissions-inventory-brief; management-reporting-pack
"""
))

PACKS.append(pack(
    {"id": "media", "title": "Media and communications", "summary": "Editorial briefs and corrections that do not fabricate quotes or sources.", "keywords": ["media", "editorial", "communications", "corrections"]},
    """
editorial-brief | Editorial Brief | editorial brief
job: Brief a story or communication with the reader, the news, and the sources that exist.
triggers: editorial brief; story brief; comms brief; article brief
inputs: The reader; The news or point; Sources on hand; What is off the record
steps: Write the point in one sentence. || List sources they have. Do not plan a quote you will invent. || Note what is off the record and must not be used. || State the fairness check: who else should be asked. || Set length and deadline. || Do not brief a piece whose method is deception or impersonation.
anti: Planned fabricated quotes; Ignoring off-the-record; Impersonation
example: A brief says to write a quote from a CEO who has not spoken.
out: A brief that replaces the quote with a request for a real interview.
related: writing-brief; pr-pitch
avoid: Fabricated quotes; Impersonation

correction-note | Correction Note | correction
job: Draft a correction that states what was wrong, what is right, and where it ran.
triggers: correction; retraction note; fix a published error; correction wording
inputs: The original claim; The correct fact; Where it appeared; Who must approve
steps: State the error plainly. || State the correct fact they can support. || Say where the error appeared. || Do not bury the correction in a new story. || Note if a quote was wrong. Do not quietly rewrite history. || Mark the draft for the editor to approve.
anti: A buried correction; A rewritten quote with no note; An unsupported replacement fact
example: A correction draft says 'updated for clarity' when a number was wrong.
out: A correction that says the number was wrong and gives the supported figure.
related: marketing-claims-review; editorial-brief

interview-prep-comms | Spokesperson Prep | spokesperson prep
job: Prepare a spokesperson with the known facts, the bridge to the point, and the questions they must not bluff.
triggers: spokesperson prep; media training notes; interview prep; press Q&A
inputs: The point; Known facts; Likely questions; Off-limit topics
steps: Write the point and three supporting facts they can say. || List likely questions, including the hostile fair one. || For unknowns, the answer is that they do not know yet. || Do not script a lie or a no-comment that hides a safety issue already confirmed. || Bridge back to the point without dodging a factual question they can answer. || Remind them not to invent a number on camera.
anti: A scripted lie; An invented live number; Dodging a confirmed safety fact
example: Prep says to deny an outage that engineering has confirmed.
out: Prep that tells the truth about the outage and refuses the denial script.
related: customer-communication-incident; pr-pitch

editorial-calendar-newsroom | Newsroom Planning Note | planning note
job: Plan a newsroom or content desk day around the stories that are ready and the slots that should stay empty.
triggers: newsroom planning; desk plan; what do we run; editorial meeting
inputs: Ready stories; Open reporting; Slots; Legal or standards flags
steps: Run only stories with a sourced point. || Leave a slot empty rather than fill it with an unsourced piece. || Flag legal review where they said it is required. || Separate opinion from news in the plan. || Do not assign a story that requires deception to report. || Name the editor for each slot.
anti: Filling a slot with an unsourced piece; Opinion labeled as news; A deceptive reporting assignment
example: The plan assigns a trend piece with no sources because the slot is empty.
out: A plan that kills or holds the piece and leaves the slot open.
related: content-calendar; editorial-brief
"""
))

PACKS.append(pack(
    {"id": "procurement", "title": "Procurement", "summary": "Sourcing events and award notes that follow authority and do not steer a bid unfairly.", "keywords": ["procurement", "sourcing", "rfp", "award"]},
    """
sourcing-event-brief | Sourcing Event Brief | sourcing brief
job: Brief a sourcing event with the need, the evaluation criteria, and the rules before vendors are contacted.
triggers: sourcing event; RFP brief; tender brief; go to market procurement
inputs: The need; Constraints; Evaluation criteria; Authority
steps: Define the need as an outcome. || Write criteria before seeing vendor pitches. || State must-haves versus scored items. || Name who may talk to vendors. || Do not tailor criteria to a favorite after bids arrive. || Publish the timeline they can honor.
anti: Criteria written after seeing a favorite; Undisclosed must-haves; A timeline they will miss
example: A brief is edited so only the incumbent can score full marks, after drafts were shared.
out: A brief that freezes fair criteria and discloses must-haves before bids.
related: rfp-response; procurement-award-note

procurement-award-note | Award Note | award note
job: Write an award note that shows scores, price, and the authority to award.
triggers: award note; source selection; procurement award; bid evaluation
inputs: The criteria; The scores and prices they have; Conflicts; The approver
steps: Show scores against the published criteria. || Separate price from non-price scores. || Record conflicts and recusals. || Recommend an award only if the evaluation supports it. || Do not change scores to fit a preferred vendor. || Name the approver. This note does not itself sign the contract.
anti: Scores changed to fit a favorite; A missing conflict; An award with no approver
example: A low-scoring friend of the buyer is moved to first after evaluation.
out: An award note that refuses the move and records the original scores.
related: conflict-of-interest; deal-desk-review

vendor-question-log | Vendor Question Log | question log
job: Log vendor questions and publish answers so every bidder sees the same clarification.
triggers: vendor questions; bidder Q&A; tender clarification; RFP questions
inputs: The questions; The answers they can give; What must stay confidential; The publication owner
steps: Log each question. || Draft an answer that does not reveal another bidder's confidential approach. || Publish answers to all bidders when their process requires it. || Do not give one bidder a private hint. || Mark questions you cannot answer yet. || Correct the solicitation if an answer changes it.
anti: A private hint to one bidder; An answer that leaks another bid; A changed requirement left unpublished
example: A buyer wants to email the incumbent a clarification the others will not see.
out: A log that publishes the clarification to every bidder.
related: sourcing-event-brief; rfi-writer

savings-tracking | Procurement Savings Tracking | savings note
job: Track procurement savings against a baseline the user can defend.
triggers: procurement savings; cost avoidance; savings tracking; sourcing savings
inputs: The baseline; The new price; Volume; One-time versus run-rate
steps: Define the baseline before claiming savings. || Separate unit-price savings from volume changes. || Mark cost avoidance as avoidance, not as cash, unless cash actually moved. || Note one-time credits separately. || Do not count a budget cut that reduced service as savings unless they want that labeled honestly. || Show the arithmetic.
anti: Savings with no baseline; Avoidance counted as cash; A service cut hidden as savings
example: A report claims savings because the department stopped the service.
out: A note that refuses the savings claim or labels it a service cut.
related: cost-reduction-sprint; budget-variance-review
"""
))

PACKS.append(pack(
    {"id": "agriculture", "title": "Agriculture operations", "summary": "Farm records, seasonal plans, and food-safety documentation. Not a recipe for pesticides, toxins, or pathogens.", "keywords": ["agriculture", "farm", "season", "food-safety"]},
    """
season-plan | Season Plan | season plan
job: Plan a season from fields, labor, and cash the farm can actually commit.
triggers: season plan; crop plan; planting plan; farm season
inputs: Fields or enterprises; Labor; Cash constraints; Rotation or withdrawal limits they already follow
steps: List enterprises they will run. || Match labor and equipment to the calendar they supplied. || Note cash needs at the expensive weeks. || Respect withdrawal or rotation limits they stated. Do not provide instructions to synthesize pesticides or bypass a label. || Identify the week that breaks if labor is short. || This is an operating plan, not agronomic or veterinary advice.
anti: Pesticide synthesis; A plan that ignores a stated label limit; No labor check
example: A plan adds a crop the only operator cannot harvest in the same week as the existing one.
out: A plan that shows the labor clash and asks which enterprise to cut.
related: cash-flow-forecast; workforce-plan
avoid: Pesticide or toxin synthesis; Pathogen production

farm-record-review | Farm Record Review | record review
job: Review farm records for completeness before a buyer, auditor, or lender asks.
triggers: farm records; spray records review; livestock records; traceability farm
inputs: The records they keep; The asker's list; Gaps they know; The period
steps: Compare records to the list they were given. || Flag missing dates, lots, or animal IDs. || Do not backfill a record with invented applications or treatments. || Note withdrawal or treatment questions for their agronomist or veterinarian. || Separate a paperwork gap from a food-safety conclusion. || Recommend a simple habit so the next period is complete.
anti: Backfilled invented treatments; A food-safety clearance; Missing lots ignored
example: A buyer asks for treatment records and the draft invents dates to look complete.
out: A review that lists the gap and refuses the invented dates.
related: traceability-lot; audit-prep-pbc

food-safety-pack | Food Safety Pack | food-safety pack
job: Assemble a food-safety document pack from the practices they already run, for their auditor or buyer.
triggers: food safety pack; farm audit pack; GAP pack; buyer food safety
inputs: Practices they documented; The buyer's checklist; Known gaps; The owner
steps: Map their documents to the checklist. || Missing items stay missing. || Do not write a procedure for a practice they do not perform and present it as current. || Escalate hazards they named to the person responsible. Do not provide pathogen growth or toxin instructions. || Name the owner of each gap. || This pack is not a certification.
anti: A fake current procedure; Pathogen or toxin instructions; A certification claim
example: A pack includes a handwashing SOP the farm does not use, to satisfy a checklist.
out: A pack that marks the SOP as not in place and assigns an owner if they choose to adopt it.
related: audit-prep-pbc; sop-writer
avoid: Pathogen production; Toxin instructions

farm-cash-week | Farm Cash Week | weekly farm cash note
job: Review a farm's coming weeks of cash against known receipts and bills.
triggers: farm cash; seasonal cash; harvest cash; farm treasury
inputs: Cash; Expected receipts they consider real; Bills due; The buffer they want
steps: List receipts only if a buyer or program has confirmed them, or label them hoped. || List bills by date. || Show the week the buffer breaks. || Separate a capital buy from operating bills. || Do not advise a lender fraud or a concealed sale. || Recommend a conversation with their lender or advisor if the break is inside the buffer.
anti: Hoped receipts shown as certain; Concealed sales; A capital buy hidden in operations
example: A note treats an unsigned grain contract as cash already coming.
out: A weekly view that labels the contract hoped and shows the break week without it.
related: cash-flow-forecast; season-plan
"""
))

PACKS.append(pack(
    {"id": "hospitality", "title": "Hospitality", "summary": "Service recovery and shift briefs for hotels and restaurants, inside policy.", "keywords": ["hospitality", "hotel", "restaurant", "guest"]},
    """
guest-recovery | Guest Recovery | guest recovery note
job: Plan guest recovery after a service miss, with a truthful apology and a remedy inside authority.
triggers: guest recovery; hotel complaint; restaurant complaint; service miss hospitality
inputs: The miss; The guest's ask; Authorized remedies; The manager
steps: Acknowledge the specific miss. || Do not invent a cause. || Offer only an authorized remedy. || Say what will change for the rest of the stay or meal if you know. || Do not ask the guest to delete a review for compensation. || Feed a repeated miss to the shift brief.
anti: A review-deletion bargain; An unauthorized comp; A fake cause
example: A manager wants to offer a free stay if the guest removes a public review.
out: A recovery note that refuses the bargain and stays inside the authorized remedy.
related: service-recovery; csat-recovery
avoid: Paying to remove a review

shift-brief-hospitality | Hospitality Shift Brief | shift brief
job: Write a hospitality shift brief covering VIPs they named, misses, and eighty-six items.
triggers: shift brief; pre-shift; hotel briefing; restaurant pre-shift
inputs: Covers or occupancy; Items they cannot sell; Guest issues; Staffing gaps
steps: Lead with safety and eighty-six items. || Note guest issues without gossip. || State staffing gaps that change service. || Assign the person who handles a known problem. || Do not include a guest's sensitive personal data. || End with the one standard to watch this shift.
anti: Gossip; Sensitive personal data; A brief with no eighty-six list when items are down
example: A brief shares a guest's medical details with the whole dining team.
out: A brief that removes the medical details and keeps the operational accommodation only if needed.
related: shift-handover; guest-recovery

event-run-of-show | Event Run of Show | event run of show
job: Write a run of show for a hosted event with owners, cues, and a guest-impact backup.
triggers: run of show; banquet event order; event cues; hospitality event plan
inputs: The guest promise; Cues and times; Owners; The backup if a cue fails
steps: List cues in order with owners. || State the guest promise that cannot slip. || Add a backup for the fragile cue. || Note dietary or access needs they confirmed, without extra personal detail. || Do not promise a vendor who has not confirmed. || Name the person who may change the plan during the event.
anti: An unconfirmed vendor presented as certain; No backup; Extra personal details
example: A run of show promises a speaker who has not confirmed.
out: A plan that marks the speaker unconfirmed and names a backup cue.
related: webinar-run-of-show; shift-brief-hospitality
"""
))

PACKS.append(pack(
    {"id": "retail", "title": "Retail and commerce", "summary": "Assortment, promotions, and store operations without deceptive pricing.", "keywords": ["retail", "store", "promotion", "assortment"]},
    """
promotion-review | Promotion Review | promotion review
job: Review a promotion for margin, inventory, and honest terms.
triggers: promotion review; retail promo; discount event; offer review retail
inputs: The offer terms; Margin they can show; Inventory; Customer-facing rules
steps: State the terms a shopper will see. || Check margin from their cost. If cost is missing, say so. || Confirm inventory can support the advertised depth. || No fake was-prices or fake end times. || Define the exception path for rain checks if they offer them. || Name the owner who stops the promo if terms cannot be honored.
anti: Fake was-prices; Advertising stock they do not have; Hidden exclusions
example: A banner shows a crossed-out price the item never sold for.
out: A review that removes the crossed-out price and checks inventory before the banner runs.
related: offer-design; marketing-claims-review

store-opening-checklist | Store Opening Checklist | opening checklist
job: Write a store opening checklist that confirms safety, cash, and the floor before doors open.
triggers: store opening; open the store; morning checklist retail; shop opening
inputs: Safety checks they require; Cash process; Floor standards; Who may open
steps: Safety and exits first. || Cash counted under their dual-control rule if they have one. || Floor standards that affect a shopper today. || Do not write the safe combination or passwords into the checklist. || Note who to call if a check fails. || A failed safety check means delay opening, not a workaround.
anti: Passwords on the checklist; Opening through a failed safety check; No owner for a failed check
example: A checklist says to prop an alarmed exit so deliveries are easier.
out: A checklist that forbids propping the exit and names the person who can delay opening.
related: shift-brief-hospitality; safety-toolbox-talk

assortment-review | Assortment Review | assortment review
job: Review an assortment for the customer job, the duplicate, and the item that does not earn its space.
triggers: assortment review; range review; what to drop; planogram logic
inputs: Items and sales they have; Space; The customer job; Known stockouts
steps: Group items by the job the shopper is solving. || Flag duplicates that do not change a choice. || Note stockouts separately from slow sellers. || Recommend a drop, a keep, or a test using their sales. || Do not invent a trend to justify a pet product. || Leave seasonal exit dates visible.
anti: An invented trend; Cutting a stocked-out item as if it were unwanted; No customer job
example: A slow-seller list includes an item that was empty for a month.
out: A review that separates the stockout from true slow sellers before any drop.
related: inventory-policy; demand-plan-review

returns-desk-script | Returns Desk Script | returns script
job: Script a returns conversation that follows policy and does not accuse the shopper.
triggers: returns script; refund script; retail returns; desk conversation
inputs: The policy; What the colleague can see; Authorized exceptions; Tone
steps: State the policy they supplied. || Ask only for information the return requires. || Do not accuse theft in the script. Route suspected fraud to their loss-prevention process. || Offer the next step: refund, exchange, or decline, as policy allows. || Escalate when the shopper's case does not fit the script. || Do not collect unrelated personal data.
anti: A theft accusation in the script; Invented policy; Unrelated personal data
example: A script tells associates to shame the shopper into keeping the item.
out: A script that states the policy calmly and escalates exceptions without shame.
related: returns-process; support-macro
"""
))

PACKS.append(pack(
    {"id": "energy", "title": "Energy and utilities operations", "summary": "Outage communication and work planning. Not a permit and not a bypass of isolation rules.", "keywords": ["energy", "utilities", "outage", "isolation"]},
    """
outage-communication | Outage Communication | outage message
job: Draft an outage message with the area, the known cause label, and the next update time.
triggers: outage message; power outage update; utility customer message; restoration update
inputs: The affected area; What is confirmed; The next update time; The approver
steps: State who is affected in the terms they confirmed. || Do not guess a cause. || Give the next update time. || Include safety instructions they already approved, such as staying away from downed lines. Do not invent technical bypass steps. || Avoid promising a restoration minute they do not have. || Keep the log of what was said.
anti: A guessed cause; A fake restoration minute; Bypass instructions for equipment
example: A message promises power in 30 minutes because that sounded reassuring.
out: A message that removes the 30-minute promise and commits to a next update.
related: customer-communication-incident; service-recovery

isolation-work-plan | Isolation Work Plan Review | isolation plan review
job: Review an isolation or lockout plan for named points and a prove-dead step, without telling anyone to skip it.
triggers: lockout plan; isolation review; permit to work review; energy isolation
inputs: The equipment; Isolation points they listed; The prove-dead step; The issuer
steps: Check that isolation points are named, not implied. || Require the prove-dead step they use. || Do not suggest a shortcut around a lock or a tag. || Identify a missing point as a stop. || Name the issuer and the worker role they described. || This review is not a permit to start work.
anti: A shortcut around lockout; Implied isolation points; A review treated as a permit
example: A plan says to isolate 'as usual' and skip the test because the crew is experienced.
out: A review that blocks the skip and requires named points and the test.
related: safety-toolbox-talk; work-instruction
avoid: Bypassing lockout or isolation

asset-maintenance-priority | Maintenance Priority | maintenance priority
job: Prioritize maintenance work by safety and customer impact, using their defect list.
triggers: maintenance priority; work order triage; asset backlog; utility maintenance
inputs: The defect list; Safety flags; Customer impact; Crew capacity
steps: Put safety defects they flagged first. || Then customer-impacting defects. || Capacity-cut the rest visibly. || Do not defer a known safety defect to make a metric look better. || Assign an owner and a date to the kept work. || Note what information is missing before a crew is sent.
anti: Deferring a known safety defect for a metric; No capacity cut; A crew sent with no location
example: A cosmetic backlog is scheduled ahead of a known leak on a safety device.
out: A priority list that puts the safety device first and parks cosmetics over capacity.
related: portfolio-prioritization; capacity-plan
"""
))

PACKS.append(pack(
    {"id": "transport", "title": "Transport and logistics operations", "summary": "Dispatch and exception handling that follow the safety rules the user states.", "keywords": ["transport", "dispatch", "fleet", "delivery"]},
    """
dispatch-plan | Dispatch Plan | dispatch plan
job: Plan a dispatch from orders, hours, and equipment limits the user stated.
triggers: dispatch plan; route plan; fleet dispatch; delivery plan
inputs: Orders; Hours rules they follow; Equipment limits; Known delays
steps: Assign work inside the hours and equipment limits they stated. || Do not advise concealing hours or cargo. || Show which order slips if a vehicle is down. || Name the customer promise at risk. || Include a check-in rule. || Replan from actual departures, not from the morning hope.
anti: Concealed hours; A plan over a stated limit; No view of the slipped order
example: A dispatcher is told to log a break that did not happen so the route stays legal on paper.
out: A plan that refuses the false log and shows which order must move instead.
related: logistics-exception; schedule-look-ahead
avoid: Concealing hours or cargo; Evading inspections

delivery-exception | Delivery Exception | delivery exception
job: Handle a failed delivery with a new promise you can keep and a reason the customer can understand.
triggers: failed delivery; delivery exception; missed stop; redelivery plan
inputs: The failure reason; The customer's instruction; Options; The next honest window
steps: Record the reason they know. || Offer options they can perform: redelivery, pickup, or hold. || Do not promise a window the route cannot make. || Tell the customer the truth without blaming them for a company miss. || Update the order status so the next driver sees it. || Escalate perishable or sensitive loads under their rule.
anti: A window the route cannot make; A blame-the-customer template; A status left stale
example: A text says the parcel was delivered though the driver marked an access failure.
out: An exception plan that corrects the status and offers a real redelivery window.
related: logistics-exception; customer-communication-incident

fleet-safety-review | Fleet Safety Review | fleet safety review
job: Review a fleet safety pattern from incidents they logged, and pick one control.
triggers: fleet safety; driver incident review; vehicle incident pattern; transport safety
inputs: The incidents; The pattern they see; Current controls; The owner
steps: Use their incident log. Do not invent rates. || Describe the pattern in conditions, not in insults. || Recommend one control: rest, maintenance, or route design, based on the pattern. || Do not recommend hiding incidents from an insurer or regulator. || Name the owner. || Recheck after the next period.
anti: Hidden incidents; An invented rate; A blame poster with no control
example: A review suggests not reporting a minor crash so the score stays clean.
out: A review that refuses the non-report and assigns a control for the actual pattern.
related: safety-toolbox-talk; incident-postmortem
avoid: Hiding incidents
"""
))
