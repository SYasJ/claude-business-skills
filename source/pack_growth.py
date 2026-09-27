from load_cards import parse_cards

def pack(domain, text):
    return {"domain": domain, "skills": parse_cards(text)}

PACKS = []

PACKS.append(pack(
    {
        "id": "sales",
        "title": "Sales",
        "summary": "Discovery, qualification, proposals, and pipeline hygiene for honest selling.",
        "keywords": ["sales", "pipeline", "discovery", "proposal", "negotiation"],
    },
    r'''
== discovery-call | Discovery Call ==
job: Plan and review a discovery call that uncovers the buyer's problem, timing, and authority without pitching over them.
artifact: discovery call plan or review
triggers:
  - discovery call
  - first sales call
  - qualify a lead
  - what should I ask the buyer
inputs:
  - What you already know about the account
  - The meeting length
  - The offer you might eventually discuss
  - Any claim you must not make
steps:
  - Open on their world: Start with why they took the meeting, in their words, before any product tour.
  - Problem evidence: Ask what the problem costs in time, money, or risk, and what they have already tried.
  - Timing: Find the event that makes this urgent now. No event means a nurture, not a forecast commit.
  - People: Who feels the pain, who signs, and who can block. Do not invent a champion.
  - Next step: End with a specific next step the buyer accepts. A vague 'I'll send something' is a miss.
  - Notes: Record facts separately from your interpretation. Do not log personal data you do not need.
anti:
  - A twenty-minute monologue about the product.
  - Scoring a buyer as qualified because they were polite.
  - Inventing a budget they never stated.
example: A salesperson has 30 minutes with an operations lead and usually spends 25 of them on slides.
example_out: A call plan with six questions, a definition of a qualified next step, and a note template that separates facts from guesses.
related:
  - qualification-meddic
  - demo-storyboard

== qualification-meddic | MEDDIC Qualification ==
job: Qualify an opportunity with MEDDIC-style evidence so the forecast is not a mood.
artifact: qualification brief
triggers:
  - MEDDIC
  - is this deal real
  - qualification review
  - sales qualification
inputs:
  - The opportunity notes
  - The economic buyer if known
  - The decision process as told by the buyer
  - The close date the seller hopes for
steps:
  - Metrics: What measurable result does the buyer expect, and who measured the baseline. If nobody measured it, say the metric is unproven.
  - Economic buyer: Name the person who can fund the change. A coach is not an economic buyer.
  - Decision criteria: Write the criteria the buyer stated, not the criteria you wish they had.
  - Decision process: Steps, dates, and paper. A close date with no process is a wish.
  - Identify pain and champion: Pain must be theirs. A champion must have power and a reason to act. Do not label a friendly user a champion without evidence.
  - Gaps: List the missing letters. Recommend the next question, not a stage upgrade.
anti:
  - Filling every MEDDIC box with hope.
  - Moving a stage because the quarter needs it.
  - Calling a friendly user a champion.
example: A deal is forecast for this month, and the only contact is a manager who likes the product but cannot sign.
example_out: A brief that marks economic buyer and process as missing and refuses to call the deal committed.
related:
  - pipeline-review
  - forecast-call

== proposal-writer | Proposal Writer ==
job: Write a proposal that restates the buyer's problem, the offer, the proof, and the ask, without invented ROI.
artifact: customer proposal
triggers:
  - write a proposal
  - sales proposal
  - statement of work narrative
  - proposal draft
inputs:
  - The buyer's stated problem
  - The offer and what is out of scope
  - Proof you actually have
  - Price and terms the user can stand behind
steps:
  - Mirror the problem: Use the buyer's language from discovery. If discovery was thin, say the proposal is premature.
  - Offer: What you will do, by when, and what you will not do. Ambiguous scope is a future dispute.
  - Proof: Only case facts the user supplied. No invented percentages.
  - Commercials: Price, term, and assumptions. Do not hide a material condition in a footnote.
  - Ask: The decision and the date. A proposal with no ask is a brochure.
  - Review: Flag claims that need the marketing-claims skill or counsel. Do not overpromise implementation.
anti:
  - A ROI slide built from invented savings.
  - Scope described only as 'full service'.
  - A proposal written before the problem is known.
example: A seller wants a proposal for a buyer who has not confirmed the problem or the budget.
example_out: A short proposal skeleton that refuses invented ROI and lists the two facts still required before price is presented as final.
related:
  - discovery-call
  - pricing-negotiation

== pricing-negotiation | Pricing Negotiation ==
job: Prepare a negotiation around price and tradeoffs, with a walk-away and no deceptive concessions.
artifact: negotiation plan
triggers:
  - pricing negotiation
  - discount request
  - procurement pushback
  - give-get
inputs:
  - List price and floor the user authorized
  - What the buyer asked for
  - Tradeables: term, scope, timing, reference
  - Walk-away condition
steps:
  - Separate price from value: Restate the outcome the buyer said they wanted before discussing a discount.
  - Give-get: Every concession has a get. A discount for nothing trains the next discount.
  - Floor: Do not go below the authorized floor. If the floor is missing, stop and ask. Do not invent one.
  - Multi-issue: Trade term, scope, or start date rather than only price, when the user can actually deliver those trades.
  - Walk away: Write the sentence the seller can say if the deal is below the floor. No fake competing offers.
  - Record: What was offered, by whom, and when it expires. No silent side letters.
anti:
  - Inventing a competing bid.
  - Discounting before understanding the ask.
  - Unauthorized side deals.
example: Procurement asked for 20 percent off, and the seller's floor is 8 percent with a two-year term available as a trade.
example_out: A give-get plan that offers the term trade, holds the floor, and includes a walk-away line with no fake competitor.
related:
  - deal-desk-review
  - proposal-writer

== objection-handling | Objection Handling ==
job: Answer a sales objection with evidence and a question, not with pressure or made-up proof.
artifact: objection response
triggers:
  - handle this objection
  - buyer said no
  - competitor objection
  - too expensive
inputs:
  - The objection in the buyer's words
  - Evidence you really have
  - What you still do not know
  - The next step you want
steps:
  - Restate: Repeat the objection fairly so the buyer would recognize it.
  - Classify: Price, priority, trust, timing, or fit. Do not treat every no as a price problem.
  - Evidence: Respond only with proof the user has. If proof is missing, say what you will go find.
  - Question: Ask one question that tests whether the objection is the real one.
  - Next step: A small commitment, not a guilt trip.
  - Ethics: No false scarcity, no fake customers, no disparagement you cannot support.
anti:
  - False scarcity.
  - Invented customer logos.
  - Arguing with the buyer before understanding the objection.
example: A buyer says 'you are too expensive' before any outcome has been quantified.
example_out: A response that treats the comment as unquantified, asks what it is being compared with, and does not invent a discount or a logo.
related:
  - discovery-call
  - competitive-battlecard

== pipeline-review | Pipeline Review ==
job: Review a pipeline so stages mean evidence, and stuck deals get a next action or an exit.
artifact: pipeline review
triggers:
  - pipeline review
  - stalled deals
  - stage hygiene
  - sales inspection
inputs:
  - The opportunity list with stages and ages
  - The stage definitions
  - The seller's stated next steps
  - The period being forecast
steps:
  - Check definitions: A stage without an evidence requirement is a label. Say so.
  - Age: Deals older than the user's threshold need a reason to stay. No reason, recommend exit.
  - Next step quality: A next step has a date and a buyer action. 'Follow up' is not a next step.
  - Concentration: Note if the number depends on one deal. Do not hide concentration to make the team look diversified.
  - Hygiene actions: Advance, rewind, or remove. Rewinding is healthy.
  - Coaching point: One skill to practice, based on the pattern in the list, not a lecture on attitude.
anti:
  - Leaving zombie deals because removing them hurts the chart.
  - Next steps with no buyer action.
  - Changing stage definitions mid-meeting to save a forecast.
example: A pipeline has 30 opportunities and 18 have no dated next step.
example_out: A review that rewinds or removes undated deals and names one coaching point about buyer-owned next steps.
related:
  - forecast-call
  - qualification-meddic

== forecast-call | Forecast Call ==
job: Produce a sales forecast from evidence categories, not from a sum of hope.
artifact: forecast call note
triggers:
  - sales forecast
  - commit forecast
  - forecast call
  - what will we close
inputs:
  - Opportunities proposed for commit
  - Evidence for each
  - Historical slippage the user admits
  - The number leadership already hopes for
steps:
  - Define categories: Commit, best case, and pipeline, in the user's definitions. If they have none, propose simple evidence rules and label them as a proposal.
  - Test commit: A commit needs a buyer process and a date the buyer influenced. Seller optimism is not commit.
  - Slippage: If they historically slip, show a haircut as their own history, not as a punishment. Do not invent a history.
  - Range: Give a range and the deals that swing it. A single number hides the risk.
  - Hope gap: If leadership's target exceeds the evidence, say so plainly. Do not backfill fake deals.
  - Actions: The two inspections that would change the number this week.
anti:
  - Sandbagging or inflating to please a room.
  - A single-point forecast with no swing deals.
  - Inventing historical win rates.
example: Leadership wants a number that is 30 percent above the deals with a real buyer process.
example_out: A forecast range, a clear gap to the hoped-for number, and two inspections, with no fake deals added to close the gap.
related:
  - pipeline-review
  - qualification-meddic

== account-plan | Account Plan ==
job: Write an account plan for a named customer that focuses on their goals, the whitespace you can evidence, and the next plays.
artifact: account plan
triggers:
  - account plan
  - strategic account
  - land and expand plan
  - account strategy
inputs:
  - The customer's stated goals
  - Current products and stakeholders
  - Whitespace you can evidence
  - Risks to the relationship
steps:
  - Customer goals first: Their goals, not your quota, open the plan.
  - Map: Stakeholders you actually know, with roles. Do not invent an org chart.
  - Whitespace: Opportunities tied to a goal. A product list is not whitespace.
  - Risks: Champion departure, unresolved support issues, or competitive evaluations they mentioned.
  - Plays: At most three plays this quarter, each with an owner and a buyer action.
  - Internal ask: What the account needs from product or support. No private complaints without a request.
anti:
  - A plan that is only a quota target.
  - Invented stakeholders.
  - Twelve plays and no owner.
example: An account manager owns a renewal and wants a strategic plan, but the only known goal is 'get through this year's audit'.
example_out: A plan anchored on the audit goal, with one evidenced expansion idea and the rest marked unknown.
related:
  - champion-map
  - qbr-customer

== champion-map | Champion Map ==
job: Test whether a supposed champion can actually move a deal, and plan how to support them ethically.
artifact: champion map
triggers:
  - champion map
  - find a champion
  - deal coach
  - internal advocate
inputs:
  - The person the seller thinks is the champion
  - Evidence of their influence
  - What they have asked for
  - The economic buyer
steps:
  - Define champion: Someone with access, influence, and a personal reason to see the problem solved. Friendship is not enough.
  - Evidence: What they have done: introduced a buyer, shared criteria, or scheduled a working session. Intentions do not count.
  - Gap: If they cannot reach the economic buyer, write the introduction you still need.
  - Support: Give them materials that are true. Do not ask them to hide facts from their employer.
  - Multi-thread: Name one other relationship to build so the deal is not a single point of failure.
  - Relabel: If the evidence is thin, call them a coach or a user, not a champion.
anti:
  - Asking a champion to conceal information from their company.
  - Equating responsiveness with power.
  - A single-threaded deal described as covered.
example: The day-to-day user replies quickly but has never met procurement, and the seller calls them the champion.
example_out: A map that relabels the user as a coach and names the missing introduction to the economic buyer.
related:
  - qualification-meddic
  - account-plan

== mutual-action-plan | Mutual Action Plan ==
job: Draft a mutual action plan that shows the buyer's steps and the seller's steps on one timeline.
artifact: mutual action plan
triggers:
  - mutual action plan
  - close plan
  - MAP
  - joint evaluation plan
inputs:
  - The buyer's process steps
  - Dates they have acknowledged
  - Owners on both sides
  - Open risks
steps:
  - Buyer steps first: Their legal, security, and business reviews. If you do not know them, the plan is a seller fantasy. Mark unknowns.
  - Dates: Only dates someone has agreed. Proposed dates are labeled proposed.
  - Owners: A named human on both sides for each step. 'Customer team' is not an owner.
  - Exit criteria: What done means for security review, pilot, or paper.
  - Risks: The step most likely to slip, and the question that would reveal it this week.
  - Tone: A shared project plan, not a pressure schedule. No fake deadlines.
anti:
  - A close plan with only seller tasks.
  - Dates the buyer never acknowledged.
  - Using the plan as a pressure tactic.
example: A seller wants a mutual action plan, but the buyer has not named a security reviewer.
example_out: A plan that leaves security review unowned and refuses to print a close date as agreed.
related:
  - qualification-meddic
  - deal-desk-review

== rfp-response | RFP Response ==
job: Decide whether to answer an RFP and, if yes, draft a response that is compliant, true, and selective.
artifact: RFP response plan or draft
triggers:
  - RFP response
  - RFI
  - security questionnaire narrative
  - bid response
inputs:
  - The questions that matter
  - Facts the company can support
  - Deadline and submission rules
  - Why this RFP is worth answering
steps:
  - Bid decision: If the mandatory requirements do not fit, recommend no-bid or a clarified exception. Do not fake compliance.
  - Answer the question: Each draft answer maps to a question. Do not paste a brochure over a yes-no item.
  - Evidence: Attach or cite only proof the user has. Unknowns stay unknown.
  - Exceptions: List exceptions visibly. Hidden exceptions are how bids are thrown out or, worse, how trust is lost.
  - Owners: Security, legal, and product own their answers. Do not let sales improvise a security claim.
  - Submit checklist: Format, deadline, and signatures the user confirmed. Do not invent a portal workaround.
anti:
  - Claiming a certification the company does not have.
  - A brochure pasted over every question.
  - Hidden exceptions.
example: An RFP asks for a certification the company has not achieved and sales wants to answer 'yes, in progress' in the yes box.
example_out: A plan that answers no or exception, explains the in-progress status outside the yes box, and flags a no-bid choice if the item is mandatory.
related:
  - vendor-security-review
  - proposal-writer

== demo-storyboard | Demo Storyboard ==
job: Storyboard a demo around the buyer's job, with proof points and a stop time, not a feature tour.
artifact: demo storyboard
triggers:
  - demo script
  - product demo
  - storyboard a demo
  - sales demo
inputs:
  - The buyer's job and problem
  - The three things the demo must prove
  - Time available
  - Features that are tempting but irrelevant
steps:
  - Open with their scene: A day-in-the-life moment from discovery. If you lack it, ask before building a tour.
  - Three proofs: Each proof is a scene, a click path, and the line that connects it to their problem.
  - Cut: Remove features that do not serve the three proofs, and list them as parking lot.
  - Risks: Where the demo environment is fragile. Plan a screenshot backup rather than a live apology.
  - Close: The question that checks whether the proof landed, plus the next step.
  - Honesty: Do not demo a roadmap item as if it exists. Label future work as future.
anti:
  - A feature tour with no buyer scene.
  - Showing roadmap as current product.
  - No time left for the buyer to talk.
example: A 45-minute demo deck has 30 features, and the buyer only asked how exceptions get resolved.
example_out: A storyboard with one exception-resolution scene, two supporting proofs, and the other features parked.
related:
  - discovery-call
  - sales-playbook

== sales-email-sequence | Sales Email Sequence ==
job: Write a short, truthful outreach or follow-up sequence that earns a reply without deception.
artifact: email sequence
triggers:
  - sales email
  - follow-up sequence
  - outreach email
  - prospecting note
inputs:
  - Who the reader is
  - The observation that makes this relevant
  - The single ask
  - Proof you can include
steps:
  - Relevance: The first lines show why this person, why now, using a real observation. No 'I noticed you are a leader' filler if you noticed nothing.
  - One ask: A reply, a 20-minute call, or a referral. Not three asks.
  - Proof: One sentence of proof the user can support. No fake mutual connections.
  - Length: Short enough to read on a phone. Cut the company history.
  - Follow-ups: Two or three notes that add a new fact, not 'bumping this'. Then stop.
  - Compliance: No deception about why you are writing. No harvested personal secrets. Respect opt-out language the user must include if they say the law or policy requires it.
anti:
  - Fake mutual connections.
  - A sequence that never stops.
  - Deceptive subject lines.
example: A rep wants a five-email sequence that pretends the buyer asked for information.
example_out: A three-note sequence with a real observation, one ask, and no fake inquiry, plus a stop after the third note.
related:
  - discovery-call
  - objection-handling

== win-loss-review | Win Loss Review ==
job: Review wins and losses to find a pattern the team can change, not a story that flatters the winner.
artifact: win-loss review
triggers:
  - win loss
  - why we lost
  - deal postmortem
  - win review
inputs:
  - The outcome
  - Buyer feedback if any
  - Competitor or status quo facts the user has
  - What the team did at each stage
steps:
  - Facts first: What the buyer said, separately from the seller's theory.
  - Decision criteria: Which criteria actually decided it, if the buyer said so. If they did not, do not invent the reason.
  - Execution versus offer: Was this a selling-process miss or a product and price miss. Recommend the owner accordingly.
  - Pattern: Compare with other reviews only if the user supplied them. One deal is an anecdote until a pattern appears.
  - Change: One behavior or offer change. A list of twelve lessons will not be used.
  - No blame essay: Name the process gap. Do not humiliate a rep.
anti:
  - A single lost deal turned into a new strategy.
  - Blaming price without buyer evidence.
  - A review with no change.
example: The team lost three deals and wants to discount, but buyer notes mention slow security review.
example_out: A review that treats security-review speed as the pattern to test and does not approve a discount from this evidence alone.
related:
  - competitive-battlecard
  - pipeline-review

== territory-plan | Territory Plan ==
job: Plan a territory from the accounts that fit, the capacity of the seller, and a weekly rhythm.
artifact: territory plan
triggers:
  - territory plan
  - patch plan
  - account prioritization
  - sales coverage plan
inputs:
  - The account list
  - Fit criteria
  - Seller capacity
  - Current pipeline already in motion
steps:
  - Fit: Define who belongs in the territory this quarter. A list of every logo is not a plan.
  - Tiers: A small number of accounts get a real plan. The rest get a lighter touch. Say the cut.
  - Capacity: Estimate time for existing deals before adding new logos. Do not overload the week and call it hustle.
  - Whitespace: Note where the user lacks coverage. Do not invent intent data.
  - Rhythm: Weekly actions the seller can finish. Inputs, not slogans.
  - Manager help: The one obstacle that needs manager air cover.
anti:
  - Equal time for every logo.
  - A plan that ignores live deals.
  - Invented buyer intent scores.
example: A rep has 200 accounts and ten hours a week for prospecting after live deals.
example_out: A tiered plan that fully works a small set, parks the rest, and fits the ten hours.
related:
  - account-plan
  - pipeline-review

== sales-playbook | Sales Playbook ==
job: Write one sales play for a repeated situation, with talk track, proof, and exit criteria.
artifact: sales play
triggers:
  - sales playbook
  - sales play
  - talk track
  - how we sell this
inputs:
  - The situation the play covers
  - The buyer
  - Proof
  - The stage exit
steps:
  - Situation: One trigger, such as a renewal risk or a competitive displacement. Do not write a play for 'selling'.
  - Entry and exit: When a rep uses the play, and what evidence ends it.
  - Talk track: Questions first, then a short narrative. Claims must be supportable.
  - Assets: The one-pager or demo scene they should use. Do not link imaginary assets.
  - Landmines: What not to say, including roadmap promises and competitor insults.
  - Coaching: How a manager knows the play was run, from notes, not from vibes.
anti:
  - A playbook that is a product manual.
  - Unsupported claims in the talk track.
  - No exit criterion.
example: Reps keep promising a feature that is not shipped when they hear a competitor's name.
example_out: A competitive play with a question track, a ban on unshipped features, and an exit criterion based on buyer criteria.
related:
  - demo-storyboard
  - competitive-battlecard

== renewal-save | Renewal Save ==
job: Plan a renewal that is at risk by finding the real grievance and offering a remedy inside policy.
artifact: renewal save plan
triggers:
  - renewal risk
  - save a customer
  - churning customer
  - renewal negotiation
inputs:
  - What the customer says is wrong
  - Usage or value evidence the user has
  - What concessions are authorized
  - The renewal date
steps:
  - Grievance: Write the customer's complaint without defending the company first.
  - Value evidence: What outcomes did happen, using their data. Do not invent usage.
  - Cause: Product gap, adoption gap, or commercial mismatch. The remedy depends on the cause.
  - Remedy: A plan, a scope change, or a concession within authority. No unauthorized discount and no blame-the-customer email.
  - Executive path: When a leader should join, and what they should say. No surprise discounts from a founder.
  - Decision date: The date the customer will decide, if they gave one. Do not invent urgency.
anti:
  - A discount as the first response to an adoption problem.
  - Invented usage statistics.
  - A defensive email that argues the customer is wrong.
example: A customer will not renew because nobody completed onboarding, and the rep wants to offer 30 percent off.
example_out: A save plan that leads with an onboarding remedy and holds the discount until a commercial problem is actually shown.
related:
  - churn-interview
  - account-plan

== expansion-play | Expansion Play ==
job: Design an expansion conversation that starts from a realized outcome, not from the seller's quota gap.
artifact: expansion play
triggers:
  - upsell
  - expansion play
  - cross-sell
  - grow the account
inputs:
  - The outcome already achieved
  - The next problem the customer has named
  - Stakeholders
  - Products that honestly fit
steps:
  - Evidence of value: What they already got. If value is unproven, the play is adoption, not expansion.
  - Next problem: Use a problem they named. Do not invent a department's pain.
  - Fit: Which offer matches that problem, and what is a bad fit. Say the bad fit out loud.
  - Stakeholders: Who owns the next problem. The original buyer may be the wrong room.
  - Commercial path: How pricing works, using real packaging. No surprise bundle.
  - Timing: Tie the ask to their calendar, not only to your quarter end.
anti:
  - Expanding before value is real.
  - Inventing a new department's pain.
  - Quarter-end pressure as the only timing logic.
example: A rep wants to cross-sell a second module, but the first module has no confirmed outcome.
example_out: A play that pauses expansion and defines the adoption proof required before a second offer is made.
related:
  - account-plan
  - customer-health-score

== competitive-battlecard | Competitive Battlecard ==
job: Build a battlecard from proof and trap questions, without invented competitor weaknesses.
artifact: competitive battlecard
triggers:
  - battlecard
  - competitive card
  - versus competitor
  - displacement notes
inputs:
  - The competitor or alternative, including the status quo
  - Facts the user can source
  - Where you honestly lose
  - Proof points
steps:
  - Name the alternative: Include do-nothing or spreadsheets if that is who you lose to.
  - Facts only: Product differences the user can support. Mark rumors as rumors and do not put them in the talk track.
  - Where we lose: The buyer for whom the alternative is a better fit. Reps need permission to walk.
  - Trap questions: Questions that reveal fit, not questions designed to humiliate a rival.
  - Proof: The asset that backs each claim. No asset, no claim.
  - Landmines: What not to say, including unshipped features and unverified insults.
anti:
  - Invented competitor revenue or roadmap.
  - Insults with no proof.
  - Hiding the segment where you lose.
example: Reps claim a rival 'is going out of business' with no source.
example_out: A card that deletes the rumor, states a sourced product difference, and names the segment where the rival is a better fit.
related:
  - competitive-strategy
  - objection-handling

== deal-desk-review | Deal Desk Review ==
job: Review a nonstandard deal for margin, precedent, and delivery risk before anyone signs.
artifact: deal desk note
triggers:
  - deal desk
  - nonstandard terms
  - discount approval
  - special deal review
inputs:
  - The asked discount or term
  - Margin math the user can show
  - Delivery implications
  - Precedent they worry about
steps:
  - Restate the ask: What is nonstandard, in one sentence.
  - Margin: Compute from their costs and price. If cost is missing, the review is incomplete. Do not invent a cost.
  - Delivery: Can the team deliver the promised start date and scope. A yes from sales is not a yes from delivery.
  - Precedent: Who else will ask for the same term if this is signed. Write that consequence.
  - Give-get: What the company gets for the concession.
  - Decision: Approve, approve with conditions, or decline. Name the approver role the user said has authority. Do not invent authority.
anti:
  - Approving a discount with no margin math.
  - Ignoring delivery capacity.
  - An approval that pretends not to set a precedent.
example: Sales wants a custom integration included free to win a logo, and delivery has not estimated it.
example_out: A note that conditions any approval on a delivery estimate and names the precedent risk of free custom work.
related:
  - pricing-negotiation
  - proposal-writer
'''
))
