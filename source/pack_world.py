from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "real-estate", "title": "Real estate", "summary": "Listings, leases, and due-diligence checklists. Not brokerage, appraisal, or legal advice.", "keywords": ["real-estate", "property", "lease", "due-diligence"]},
    """
property-listing-brief | Property Listing Brief | listing brief
job: Brief a property listing from facts the owner confirmed, with no invented features.
triggers: listing brief; property description; write a listing; marketing a property
inputs: Confirmed features; Known defects they disclosed; The audience; Claims they must not make
steps: Use only confirmed features. || Disclose known material defects they told you about. Do not help hide them. || Separate lifestyle copy from measurable facts. || Do not invent school quality, income, or a legal use. || Mark what a buyer must verify. || This is not a valuation.
anti: Hidden defects; Invented income; A valuation disguised as a listing
example: A draft says the unit rents for a number the owner has not achieved.
out: A brief that removes the invented rent and lists defects the owner already disclosed.
related: marketing-claims-review; property-due-diligence

lease-abstract | Lease Abstract | lease abstract
job: Abstract a lease the user provides into dates, money, and notice clauses, without a legal opinion.
triggers: lease abstract; summarize a lease; lease dates; rent roll support
inputs: The lease text; The questions they need answered; Amendments they have; Who will rely on it
steps: Quote dates, rent, and notice periods from the text. || Flag missing pages or amendments. || Do not assume a renewal right that is not written. || Separate what the lease says from what the tenant hopes. || List questions for counsel. || Do not calculate a legal default.
anti: Assumed renewal rights; A legal default opinion; An abstract of a missing page
example: An abstract assumes a five-year renewal the lease only mentions as a negotiation.
out: An abstract that marks renewal as unwritten and lists the counsel question.
related: contract-risk-review; rent-roll-review

property-due-diligence | Property Due Diligence | due-diligence checklist
job: Build a due-diligence checklist from the deal type and the documents the user can obtain.
triggers: property due diligence; acquisition checklist; what should we review; property DD
inputs: The deal type; Documents in hand; Known red flags; The decision date
steps: List documents they already require for this deal type. || Mark missing items as gaps, not as clean. || Separate physical, financial, and legal workstreams. Legal conclusions go to counsel. || Do not invent inspection results. || Recommend a walk-away question if a gap is material and the date is close. || No earnest-money trick and no concealed defect strategy.
anti: A clean opinion with missing documents; Invented inspection results; Concealment advice
example: The checklist is marked complete though no survey was received.
out: A checklist that keeps the survey open and refuses a clean conclusion.
related: ma-screening; lease-abstract

rent-roll-review | Rent Roll Review | rent-roll review
job: Review a rent roll for inconsistencies, expirations, and concessions the user can see.
triggers: rent roll; lease expiration review; commercial rent roll; occupancy review
inputs: The rent roll; What a row is supposed to mean; Known concessions; The questions of the reader
steps: Check that units, rent, and dates are internally consistent. || Flag expirations inside their horizon. || Separate contractual rent from concessions they disclosed. || Do not invent market rent. || Note vacant units and the story they gave. || Send legal interpretation of odd clauses to counsel.
anti: Invented market rent; Concessions hidden in the headline rent; A roll that does not add up
example: A roll shows full occupancy while three units are marked 'free rent' with no end date.
out: A review that separates free rent from paying occupancy and flags the missing end dates.
related: lease-abstract; property-listing-brief

offer-comparison | Offer Comparison | offer comparison
job: Compare property offers on the terms the user cares about, without advising which legal form to sign.
triggers: compare offers; property offers; which offer; offer matrix
inputs: The offers; The seller or buyer priorities; Deadlines they stated; Contingencies visible in the offers
steps: Build a matrix of price, timing, contingencies, and costs they can see. || Rank only on priorities they named. || Do not invent a buyer's financing strength. || Flag a deadline that needs a professional response. || Recommend questions, not a signature. || A licensed local professional must confirm the transaction.
anti: Invented financing strength; A signature recommendation; Hidden contingencies
example: One offer is higher but waives an inspection the seller has not disclosed defects for.
out: A matrix that shows the inspection gap and leaves the signature to the principal and their professional.
related: property-due-diligence; decision-log
"""
))

PACKS.append(pack(
    {"id": "construction", "title": "Construction", "summary": "Site reporting, changes, and safety talks. Do not skip a safety control or invent quantities.", "keywords": ["construction", "site", "safety", "change-order", "estimate"]},
    """
site-daily-report | Site Daily Report | daily report
job: Write a site daily report from observed work, weather, and safety notes, with no invented quantities.
triggers: daily report; site diary; construction daily; superintendent report
inputs: Work performed; Crew and deliveries they counted; Safety notes; Weather they observed
steps: Record only work they observed or documented. || Quantities come from their count. Unknown stays unknown. || Safety incidents and near misses they reported go in plainly. || Delays get a cause they stated. || Note visitors and inspections they named. || Do not backfill a report to hide a delay.
anti: Invented quantities; A hidden delay; A safety note removed to look clean
example: A draft says the slab was poured though the crew was rained out.
out: A report that records the rain delay and leaves the pour unclaimed.
related: shift-handover; schedule-look-ahead

change-order | Change Order Brief | change-order brief
job: Brief a change order with the cause, the cost basis they have, and the time effect.
triggers: change order; variation; extra work; construction change
inputs: The cause; Drawings or instructions they have; Cost backup; Time effect
steps: State the cause and who directed the work. || Attach cost backup they have. Do not invent unit rates. || Show time effect separately from cost. || Identify contract clauses only if they pasted them. || Mark entitlement as a question for the contract administrator. || Do not advise hiding the change in a contingency with no record.
anti: Invented rates; Hidden changes; An entitlement ruling from memory
example: A superintendent wants a change order with a round number and no backup.
out: A brief that blocks the round number until backup exists and records the direction to proceed.
related: scope-change-control; estimate-assumption-log

safety-toolbox-talk | Safety Toolbox Talk | toolbox talk
job: Draft a toolbox talk for a specific site hazard, with the control the crew must use.
triggers: toolbox talk; safety briefing; pre-task briefing; site safety talk
inputs: The hazard; The required control; The crew; Incidents they can mention without blame
steps: Name the hazard in the work they are about to do. || State the control in steps. || Say what to do if the control is missing: stop and tell the supervisor. || Do not tell anyone to skip a guard, a harness, or a lockout. || Keep blame out of the example. || End with a check that the control is in place today.
anti: Advice to skip a safety control; A generic talk with no hazard; Blame
example: A draft says to skip the harness because the task is short.
out: A talk that requires the harness and stops the task if it is missing.
related: gemba-walk; site-daily-report
avoid: Skipping safety controls

rfi-writer | RFI Writer | RFI
job: Write a request for information that states the conflict, the location, and the date the answer is needed.
triggers: RFI; request for information; drawing conflict; design clarification
inputs: The conflict; The drawing or spec location; The date needed; The proposed clarification if any
steps: Describe the conflict with locations they gave. || Ask one question. || State the date the answer is needed and why. || A proposed clarification is labeled as a proposal, not as approval. || Attach references they have. Do not invent a detail. || Track the RFI so work does not proceed on a guess unless they accept that risk in writing.
anti: Three questions in one RFI; An invented detail; Work proceeding on a silent guess
example: An RFI asks the designer to 'see the attached and advise' with no question.
out: An RFI with one located question, a need-by date, and no invented detail.
related: change-order; site-daily-report

schedule-look-ahead | Schedule Look-Ahead | look-ahead
job: Build a short look-ahead from constraints, not from a hopeful bar chart.
triggers: look-ahead; three-week look-ahead; constraint schedule; weekly work plan
inputs: Planned activities; Constraints: design, material, access; Crew available; Inspections
steps: List activities the constraints actually allow. || Mark activities blocked by a missing RFI, material, or inspection. || Match crew to the allowed work. || Do not show blocked work as committed. || Identify the constraint to remove next. || Update from yesterday's actuals they supplied.
anti: Blocked work shown as committed; No constraint column; A look-ahead that ignores yesterday
example: A look-ahead schedules a pour before the inspection the city requires.
out: A look-ahead that parks the pour behind the inspection and names the constraint owner.
related: production-schedule; site-daily-report

punch-list | Punch List | punch list
job: Turn a punch list into items with a location, an owner, and a done standard.
triggers: punch list; snag list; deficiency list; closeout punch
inputs: The observed items; Locations; Responsible parties; The done standard
steps: One item, one location, one owner. || Describe the defect so someone can find it. || Define done as observable, not as 'make good'. || Separate life-safety items and say they are not cosmetic. || Do not invent counts. || Close an item only with evidence they accept.
anti: A vague make-good list; Life-safety mixed with paint nits; Closure without evidence
example: A punch list says 'finish lobby' with no owner.
out: A list of located items, with life-safety called out and an owner on each line.
related: project-closeout; nonconformance-report

estimate-assumption-log | Estimate Assumption Log | assumption log
job: Log estimate assumptions so a bid can be explained without invented quantities.
triggers: estimate assumptions; bid assumptions; quantity assumptions; estimating log
inputs: The scope basis; Quantities they measured; Allowances; Exclusions
steps: State the documents the estimate is based on. || List quantities as measured or as an allowance. || Write exclusions plainly. || Do not invent a productivity rate and call it fact. Label judgments. || Note what a missing drawing would change. || This is not a bid strategy to mislead a client. The log should make the price understandable.
anti: Hidden exclusions; Invented quantities; A log written to mislead
example: An estimate assumes night work is included but the invitation excludes it.
out: A log that records the conflict and refuses to hide the exclusion.
related: change-order; proposal-writer
"""
))

PACKS.append(pack(
    {"id": "entrepreneurship", "title": "Entrepreneurship", "summary": "Offers, experiments, and founder operating reviews. Not a promise of funding.", "keywords": ["startup", "founder", "offer", "experiment", "traction"]},
    """
offer-hypothesis | Offer Hypothesis | offer hypothesis
job: Frame a startup offer as a hypothesis with a buyer, a promise, and a test.
triggers: offer hypothesis; startup offer; what are we selling; test the offer
inputs: The buyer; The promise; The alternative; The test they can run
steps: Name one buyer and one painful job. || Write the promise in concrete terms. || State the alternative they use now. || Design a test that can fail: a paid pilot, a letter, or a concierge week. || Define the kill metric before the test. || Do not invent traction, waitlists, or investor interest.
anti: Invented traction; A test that cannot fail; Five buyers in one hypothesis
example: A deck says thousands of users want the product, and no user has been asked.
out: A hypothesis and a small test, with the invented user count removed.
related: experiment-design; product-brief

founder-operating-review | Founder Operating Review | weekly founder review
job: Run a weekly founder review of cash, pipeline, and the one bottleneck.
triggers: founder review; weekly startup review; founder operating; what matters this week
inputs: Cash facts; Pipeline or user facts; The bottleneck; The team's capacity
steps: Open with cash and the date it changes, from their numbers. || One growth fact, sourced. || Name the bottleneck in the system, not in a person's character. || Choose one move for the week. || Park new ideas that do not relieve the bottleneck. || Do not add fake momentum for morale.
anti: Fake momentum; A character attack; Ten priorities
example: A review adds five new ideas while payroll is the unresolved issue.
out: A review that keeps payroll as the bottleneck and parks the new ideas.
related: runway-and-burn; weekly-review

customer-discovery-sprint | Customer Discovery Sprint | discovery sprint
job: Plan a discovery sprint that books real conversations and writes down disconfirming evidence.
triggers: discovery sprint; customer discovery; founder interviews; problem sprint
inputs: The hypothesis; How they will reach people; The number of conversations; The disconfirming signal
steps: Write the hypothesis so a conversation can kill it. || Recruit people who have the problem, not friends who will be kind, and say so. || Use a script that asks for past behavior. || Log disconfirming notes, not only excitement. || Decide continue, pivot, or stop at the end. || Do not help scrape personal data or misrepresent who they are.
anti: Only talking to friends; Hiding disconfirming notes; Misrepresenting identity
example: A sprint plan interviews the founder's family and calls it validation.
out: A sprint that recruits people with the problem and requires a disconfirming log.
related: discovery-interview; offer-hypothesis

mvp-scope | MVP Scope | MVP scope
job: Cut a product idea to the smallest test that answers the riskiest question.
triggers: MVP; smallest test; scope the first version; what to build first
inputs: The riskiest question; The full idea; What can be done manually; The time box
steps: Name the riskiest question. Demand, delivery, or channel. || Cut every feature that does not answer it. || Prefer a manual concierge step over unbuilt software when that answers the question. || State what the MVP must not do. || Define the evidence that would justify the next slice. || Do not call a large roadmap an MVP.
anti: A roadmap called an MVP; Building software before the question is clear; No non-goals
example: An MVP list includes billing, admin, and a marketplace before one user has paid.
out: A scope that tests payment or the core job manually and parks the rest.
related: prd-writer; experiment-design

investor-update | Investor Update | investor update
job: Draft an investor update that leads with cash, the metric, and the ask, without spin.
triggers: investor update; shareholder update; monthly investor note; fundraising update
inputs: Cash and runway facts; The metric they track; What went wrong; The ask
steps: Lead with cash, runway, and the metric, from their books. || Include the miss. Investors who hear only good news stop trusting the note. || One ask, if any, with a date. || Do not invent a term, a valuation, or interest from other investors. || Keep customer names out unless the user may share them. || Mark forecasts as forecasts.
anti: Invented investor interest; A hidden miss; A valuation presented as fact
example: An update omits a churn spike because the round is opening.
out: An update that includes the spike, the cash fact, and no invented investor interest.
related: fundraising-model; runway-and-burn

pricing-test-startup | Startup Pricing Test | pricing test
job: Design a startup pricing test that learns willingness to pay without deceptive charges.
triggers: pricing test; willingness to pay; test a price; startup pricing
inputs: The offer; The prices to test; The buyer; What must be disclosed
steps: Test a few prices, not a clever matrix they cannot staff. || Disclose what the buyer will pay before they commit. || Define the evidence: paid, not 'interested'. || Do not fake a crossed-out price or a false scarcity timer. || Separate a price test from a promise you cannot deliver. || Record the learning and the next price decision.
anti: Hidden charges; Fake scarcity; Treating interest as payment
example: A test shows a 50 percent discount timer that resets for every visitor.
out: A test design that removes the fake timer and counts paid commitments only.
related: pricing-packaging; marketing-experiment
"""
))

PACKS.append(pack(
    {"id": "productivity", "title": "Productivity", "summary": "Personal and team operating habits that respect focus and do not surveil colleagues.", "keywords": ["productivity", "planning", "meetings", "writing", "focus"]},
    """
weekly-review | Weekly Review | weekly review
job: Run a weekly review that closes open loops and picks next week's outcomes.
triggers: weekly review; plan my week; personal review; Friday review
inputs: Open commitments; Calendar; Waiting-for items; The outcomes that matter
steps: List commitments still open. || Close, defer, or schedule each one. A review that only worries is incomplete. || Pick a few outcomes for next week, not a pile of tasks. || Note what is waiting on others. || Protect time for the outcome that slips every week. || Do not plan a week that ignores meetings already booked.
anti: A wish list longer than the calendar; No closures; Ignoring booked meetings
example: A weekly plan has 40 tasks and 30 hours of existing meetings.
out: A review that cuts to a few outcomes and schedules them in the remaining time.
related: founder-operating-review; meeting-operating-system

deep-work-plan | Deep Work Plan | focus plan
job: Plan focus time around real constraints, with a definition of done for the block.
triggers: deep work; focus plan; time block; distraction plan
inputs: The outcome of the block; Available time; Known interruptions; The environment
steps: Define done for the block so it is not just 'work on the project'. || Place the block where interruptions are actually lowest. || Remove one distraction they control. || Leave a buffer. A plan with no margin will be abandoned. || Say what will be deferred so the block is not stolen by mail. || Do not recommend monitoring other people to protect your focus.
anti: A block with no definition of done; Surveillance of colleagues; No buffer
example: A focus plan depends on coworkers never messaging, with no defer rule.
out: A plan with a done statement, a defer rule for mail, and no monitoring of others.
related: weekly-review; manager-one-on-one

decision-journal | Decision Journal | decision journal entry
job: Write a personal decision journal entry with the choice, the expectation, and a review date.
triggers: decision journal; log my decision; decision diary; review a past decision
inputs: The decision; Options; What you expect to happen; The review date
steps: State the decision and the date. || Record the expectation in a way you can later check. || Note the main uncertainty. || Do not rewrite the entry after the outcome to look wiser. || On review, compare expectation to what happened. || Extract one rule, or explicitly say there is no rule yet.
anti: Rewriting history; An entry with no expectation; A rule from one case
example: A journal entry is edited after a failure to say the risk was always obvious.
out: An entry that keeps the original expectation and sets a review without rewriting the past.
related: decision-log; founder-decision-review

meeting-notes | Meeting Notes | meeting notes
job: Write meeting notes that capture decisions, owners, and open questions.
triggers: meeting notes; minutes; action items; notes from the call
inputs: The purpose; Decisions heard; Owners; Open questions
steps: Start with the purpose and the date. || Record decisions separately from discussion. || Each action has an owner and a date, or it is not an action. || Mark unclear points as questions. Do not invent consensus. || Keep confidential items out of a note that will be widely shared. || Send the note to the people who must act, if the user asks for a distribution list they control.
anti: Invented consensus; Actions with no owner; Confidential details in a broad note
example: Notes say the team agreed though two people dissented.
out: Notes that record the dissent and assign owners only to real actions.
related: board-meeting-facilitator; decision-log

writing-brief | Writing Brief | writing brief
job: Brief a piece of writing so the drafter knows the reader, the point, and the length.
triggers: writing brief; help me outline; draft structure; what should this say
inputs: The reader; The point; The length; The action you want
steps: Name the reader and what they already know. || Write the point in one sentence. || Choose a structure that serves the point. || Set a length. || List facts that must be included and claims that must not. || Do not start drafting until the point is stable, unless the user asked for a rough exploration.
anti: A draft with no point; Unsupported claims required by the brief; No reader
example: A brief says 'write something inspiring about the quarter' with no reader or ask.
out: A brief that names the reader, one point, and the action, or stops until those exist.
related: executive-one-pager; creative-brief

personal-okr | Personal OKRs | personal objectives
job: Set a few personal objectives that fit the week you actually have.
triggers: personal OKRs; personal goals; quarterly personal goals; life planning goals
inputs: The outcomes that matter; Time available; Existing commitments; How you will review
steps: Choose one to three objectives. || Write key results you can observe. || Check them against the calendar. || Cut goals that require time you do not have. || Set a review. || Do not turn personal goals into a surveillance plan for family or coworkers.
anti: Goals that do not fit the calendar; Vanity goals with no review; Surveillance of other people
example: A plan adds a daily two-hour course on top of a 50-hour job with no time removed.
out: A smaller set of objectives that fits the real week and names a review.
related: okrs-and-scorecard; weekly-review

email-triage | Email Triage | email triage
job: Triage an inbox into reply, schedule, delegate, or drop, without pretending every message is urgent.
triggers: email triage; inbox zero help; prioritize email; what should I answer
inputs: The messages or summaries; Deadlines they contain; Your role; What can be delegated
steps: Sort by real deadline and by whether a person is blocked. || Draft replies only where a decision or fact is needed. || Schedule work that does not need a same-day reply. || Delegate with context, not by forwarding a puzzle. || Drop or file noise. || Do not write deceptive delays or fake out-of-office claims.
anti: Treating all mail as urgent; A forward with no context; A fake out-of-office
example: A triage plan answers newsletters before a customer blocked on a decision.
out: A triage that answers the blocked customer first and files the newsletters.
related: support-macro; weekly-review

readme-for-a-process | Process README | process README
job: Write a README for a repeated personal or team process so someone else can run it.
triggers: process README; how I do this; document my workflow; checklist README
inputs: The trigger; The steps; The tools; The failure mode
steps: Open with when to use the process. || Number the steps and the expected result. || Name the failure mode and the fix. || Keep secrets out of the README. || Say who to ask. || Cut steps that are superstition. If they cannot say why a step exists, mark it optional.
anti: Secrets in the README; Steps with no trigger; Superstition presented as required
example: A README includes a personal access token so others can run a report.
out: A README that removes the token, names the secret store, and keeps the real steps.
related: sop-writer; documentation-as-code
"""
))

PACKS.append(pack(
    {"id": "library", "title": "Skill library", "summary": "Find, write, and trust skills in this library without weakening safety rules.", "keywords": ["skills", "library", "authoring", "trust", "install"]},
    """
skill-finder | Skill Finder | skill recommendation
job: Recommend the smallest set of skills in this library for a task, and say what not to load.
triggers: which skill; skill finder; what skill should I use; help me pick a workflow
inputs: The task; The domain; Whether a regulated professional must review; Skills already loaded
steps: Restate the task in one sentence. || Pick the one skill whose output matches the task. Add a second only if the task truly crosses domains. || Prefer a specialist skill over a general strategy skill when the output is a defined artifact. || Say which nearby skill is the wrong one and why. || If the task asks for deception, evasion, or harm, do not route to a skill. Refuse and offer a legitimate alternative. || Remind the user that descriptions load for installed skills, so they should install a domain rather than the whole library.
anti: Loading five skills for a simple memo; Routing a harmful request into a skill; Recommending a skill you cannot name
example: A user asks for a cash view and also wants a full corporate strategy loaded.
out: A recommendation of cash-flow-forecast only, with strategy skills named as unnecessary for this task.
related: skill-authoring; skill-library-trust-review

skill-authoring | Skill Authoring | skill draft
job: Draft a new Agent Skill that is specific, safe, and small enough to load.
triggers: write a skill; SKILL.md; author a skill; new skill
inputs: The repeated task; The trigger phrases; The artifact; The boundaries
steps: Name the skill in kebab-case, matching the folder, with no consecutive hyphens. || Write a description that says what it does and when to use it, under 1024 characters, with no angle brackets. || Put steps in order, with a stop condition and an anti-pattern. || Keep the body under 500 lines. Move long tables to references. || Forbid credential requests, hidden network calls, and deceptive instructions. || Do not write a skill whose purpose is to weaken safety rules or to hide actions from the user.
anti: A vague description; A skill that asks for secrets; A jailbreak skill
example: A requested skill tells the agent to ignore safety rules to be more helpful.
out: A refusal of that purpose and a draft skill that does the legitimate task inside the rules.
related: skill-library-trust-review; skill-finder
avoid: Jailbreaks; Hidden instructions

skill-library-trust-review | Skill Library Trust Review | trust review
job: Review a skill or a skill repository for signs it is unsafe, deceptive, or pretending to be an official product.
triggers: is this skill repo safe; trust review; skill security review; should I install this
inputs: The files or an inventory; Install instructions; Network behavior; Claims of affiliation
steps: Prefer an installer that copies local files and does not pipe a remote script to a shell. || Check scripts for network calls, obfuscation, and credential prompts. || Descriptions should say what the skill does. Hidden instructions are a finding. || Official-looking branding without a clear independent-author statement is a finding. || A repository that promises guaranteed income, token claims, or wallet connections is out of scope for this library and should be treated as untrusted. || Recommend installing one domain and reading a skill before enabling it. This review is not a security certification.
anti: A fake certification; Ignoring a curl-pipe installer; Treating a logo as proof of affiliation
example: An installer asks the user to run a remote script and paste an API key to 'activate' free skills.
out: A do-not-install recommendation that names the remote script and the key request.
related: secrets-handling; skill-authoring

install-and-update | Install and Update | install plan
job: Plan a local install or update of this library for a specific tool and domain.
triggers: install skills; update skills; install a domain; where do skills go
inputs: The tool; The domain; Whether the install is user-level or project-level; Whether they want a dry run
steps: Recommend a domain install, not all skills, unless they explicitly want the full set and accept the description cost. || Use the local installer. Do not recommend a remote pipe-to-shell command. || Show the destination path for the tool they named. || Prefer a dry run first. || Updates replace files from this repository only. Do not tell them to mix in unreviewed third-party skills silently. || No account, license key, or wallet is required.
anti: curl piped to a shell; A required license key; Installing every skill by default
example: A user wants one command that downloads and executes an unknown installer.
out: A plan that uses the local Python installer, names the domain, and starts with a dry run.
related: skill-finder; skill-library-trust-review

domain-enablement | Domain Enablement | enablement note
job: Explain which domain plugin to enable for a team role, and which skills that role should try first.
triggers: which domain; enable a plugin; team skill pack; where should we start
inputs: The role; The repeated tasks; The tool they use; Sensitivity of the work
steps: Map the role to one primary domain and at most one secondary domain. || Name three starter skills, not the whole domain. || Warn that regulated work still needs a qualified human. || Tell them not to enable offensive, deceptive, or jailbreak workflows. This library does not ship those. || Note the context cost of enabling many domains. || Point to the install plan rather than pasting a remote command.
anti: Enabling every domain for every role; A remote install command; Starter skills unrelated to the role
example: A finance analyst is told to enable engineering, healthcare, and security plugins on day one.
out: A note that enables finance, names three starter skills, and leaves the other plugins off.
related: skill-finder; install-and-update
"""
))
