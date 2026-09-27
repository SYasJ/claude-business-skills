from load_cards import parse_cards

def pack(domain, text):
    return {"domain": domain, "skills": parse_cards(text)}

PACKS = [pack(
    {
        "id": "product",
        "title": "Product",
        "summary": "Discovery, requirements, prioritization, and launch decisions for product teams.",
        "keywords": ["product", "prd", "roadmap", "discovery", "prioritization"],
    },
    r'''
== product-brief | Product Brief ==
job: Write a product brief that frames the problem, the user, and the bet before anyone argues about features.
artifact: product brief
triggers:
  - product brief
  - opportunity brief
  - one-pager product
  - should we build
inputs:
  - The user and the situation
  - Evidence of the problem
  - The business constraint
  - What is already known to be out of scope
steps:
  - User and situation: Who hits the problem, and when. A persona name with no situation is not enough.
  - Problem evidence: Quotes, tickets, or data the user supplied. Mark guesses as guesses.
  - Bet: The change you believe will help, stated as a hypothesis.
  - Non-goals: At least three things this brief will not solve.
  - Risks: The assumption that would kill the bet if false.
  - Decision: Discover more, build a small slice, or stop. One recommendation.
anti:
  - A feature list titled as a brief.
  - Invented user quotes.
  - No non-goals.
example: A stakeholder hands over a feature list and asks for a brief by tomorrow.
example_out: A brief that restates the missing problem evidence and refuses to pretend the feature list is a validated bet.
related:
  - opportunity-assessment
  - prd-writer

== opportunity-assessment | Opportunity Assessment ==
job: Assess whether an opportunity is worth a discovery sprint, using evidence rather than enthusiasm.
artifact: opportunity assessment
triggers:
  - opportunity assessment
  - is this worth building
  - product opportunity
  - discovery go or no-go
inputs:
  - The proposed opportunity
  - Evidence in hand
  - Strategic bets it must serve
  - Cost of a sprint
steps:
  - Strategic fit: Does it serve a stated bet. If there is no strategy, say the assessment is local only.
  - Evidence grade: Strong, weak, or absent, based only on supplied evidence.
  - Alternatives: Include doing nothing and fixing adoption of what already exists.
  - Cost of learning: A small sprint with a question, not a quarter of build by default.
  - Kill criteria: What result would stop the work.
  - Recommendation: Sprint, park, or kill, with the missing fact named.
anti:
  - A yes because a customer shouted.
  - Skipping the do-nothing option.
  - A quarter-long build disguised as discovery.
example: A large customer requested a feature that fits none of the current bets.
example_out: An assessment that parks the feature, names the strategy conflict, and defines the evidence that would reopen it.
related:
  - product-brief
  - portfolio-prioritization

== prd-writer | PRD Writer ==
job: Write a product requirements document with a problem, scope, acceptance signals, and explicit non-goals.
artifact: PRD
triggers:
  - write a PRD
  - product requirements
  - feature spec
  - requirements document
inputs:
  - Problem and user
  - Proposed scope
  - Constraints
  - Open questions
steps:
  - Problem and outcome: What will be true for the user if this ships. No outcome, no PRD.
  - Scope: The smallest slice that tests the outcome. Cut the rest into non-goals.
  - Flows: The main path and the important failure path. Do not specify every pixel unless the user asked for design detail.
  - Acceptance: Observable signals that the slice works. 'Feels better' is not acceptance.
  - Analytics and risks: What you will measure, and the risk you are accepting. Do not invent baseline numbers.
  - Open questions: Owner and date for each. A PRD that hides questions will slip in build.
anti:
  - A PRD that is only a solution.
  - Hidden non-goals.
  - Acceptance criteria nobody can test.
example: A PRD draft lists 15 features and no user outcome.
example_out: A rewritten PRD with one outcome, a small slice, testable acceptance, and the other features as non-goals.
related:
  - user-story-map
  - product-analytics-spec

== user-story-map | User Story Map ==
job: Map the user's journey into slices of value so a release is a story, not a pile of tickets.
artifact: story map
triggers:
  - story map
  - user story map
  - slice a release
  - journey to tickets
inputs:
  - The user and the job
  - The backbone steps they take
  - Candidate stories
  - The first release goal
steps:
  - Backbone: The steps the user takes, in order. Internal tasks do not lead the map.
  - Stories under steps: Place each story under the step it serves. Orphan stories are a finding.
  - Slice: Draw a first release that completes a thin journey. A release that finishes only the left half of the journey is not releasable.
  - Later slices: What waits, and why.
  - Risks: The step with the least evidence.
  - Language: Stories a customer would recognize. No internal code names as the only label.
anti:
  - A backlog dump called a map.
  - A first release that cannot be used end to end.
  - Stories with no user step.
example: A team has 80 tickets and wants a release that builds the admin console before the user can finish the core job.
example_out: A map whose first slice completes the core job thinly, and parks the admin console.
related:
  - prd-writer
  - definition-of-done

== discovery-interview | Discovery Interview ==
job: Plan a discovery interview that learns the user's current behavior without pitching the solution.
artifact: interview guide
triggers:
  - discovery interview
  - customer interview
  - user interview guide
  - problem interview
inputs:
  - The decision the interview must inform
  - Who to talk to
  - Hypotheses
  - What you must not pitch
steps:
  - Decision: What you will do differently after five interviews. If nothing would change, do not run the interviews.
  - Participants: The people who have the problem, not only fans. Note how they will be recruited without deception.
  - Guide: Questions about recent behavior, not hypothetical love of your idea.
  - No pitching: The solution mention, if any, comes after the story. Do not lead the witness.
  - Notes: Capture quotes and concrete incidents. Interpretations go in a separate column.
  - Synthesis rule: What pattern across interviews would support or kill the hypothesis.
anti:
  - Asking 'would you use this' as the main question.
  - Pitching in the first five minutes.
  - Treating one enthusiastic interview as proof.
example: A founder wants interview questions that ask customers to rate a feature idea from one to ten.
example_out: A guide that replaces the rating with questions about the last time the problem occurred.
related:
  - jobs-to-be-done
  - feedback-synthesis

== jobs-to-be-done | Jobs To Be Done ==
job: Frame a job-to-be-done from a real situation, including the hire and the fire.
artifact: job story
triggers:
  - jobs to be done
  - JTBD
  - job story
  - what job is the user hiring
inputs:
  - A recent incident the user described
  - What the person was trying to achieve
  - What they used instead
  - Forces they mentioned
steps:
  - Situation: When and where the struggle showed up. No situation, no job story.
  - Motivation: The progress they wanted, in their words if available.
  - Hire: What they used, including spreadsheets and workarounds.
  - Fire: What was awkward about the old way, from evidence, not from your pitch.
  - Anxieties: What made a new approach feel risky, if they said so. Do not invent psychology.
  - Implication: What the product must be hired to do, and what it should not pretend to do.
anti:
  - A job story that is a feature request in costume.
  - Invented anxieties.
  - Ignoring the workaround they already hired.
example: A team writes the job as 'use our dashboard' after a customer described exporting to a spreadsheet.
example_out: A job story about the export moment, with the spreadsheet as the current hire.
related:
  - discovery-interview
  - product-brief

== prioritization-rice | RICE Prioritization ==
job: Prioritize a short list with RICE or a simpler cut, and show the math instead of hiding behind it.
artifact: prioritization note
triggers:
  - RICE
  - prioritize the roadmap
  - score these ideas
  - what should we build next
inputs:
  - The candidate list
  - Evidence for reach and impact
  - Effort estimates
  - Constraints
steps:
  - Bound the list: Prioritize items that serve the current bet. Off-strategy items are parked, not scored into existence.
  - Score honestly: Reach, impact, confidence, and effort use the user's evidence. Low confidence stays low. Do not inflate confidence to win an argument.
  - Show the arithmetic: The score is visible. A black-box rank is not RICE.
  - Override in the open: If strategy or a commitment overrides the score, write the override. Do not fudge the inputs.
  - Cut: A ranked list with no cut is not a decision. Recommend now, next, and not now.
  - Revisit: The date the scores expire.
anti:
  - Inflated confidence scores.
  - A ranking with no cut.
  - Fake precision to three decimals.
example: A stakeholder wants their idea scored 100 percent confidence so it sorts to the top.
example_out: A note that keeps confidence low, shows the math, and records any strategic override separately.
related:
  - portfolio-prioritization
  - roadmap-narrative

== roadmap-narrative | Roadmap Narrative ==
job: Write a roadmap narrative that explains outcomes and sequencing, with dates only where they are real.
artifact: roadmap narrative
triggers:
  - roadmap narrative
  - explain the roadmap
  - roadmap communication
  - now next later
inputs:
  - The outcomes
  - The sequence and why
  - Dates that are actually committed
  - What is not on the roadmap
steps:
  - Outcomes over features: Lead with the customer or business outcome. Features are evidence of the bet, not the headline.
  - Now, next, later: Use this shape unless the user has a better one. Later is not a promise.
  - Dates: Only committed dates get dates. Everything else is a sequence without a fake quarter.
  - Why this order: The dependency or learning that forces the sequence.
  - Not on the roadmap: Items people will ask about, and the reason they wait.
  - Audience: A board version and a team version may differ in detail, not in truth.
anti:
  - A feature laundry list with fake dates.
  - A roadmap that hides the delays.
  - Different truths for different audiences.
example: Sales wants every prospect request placed on next quarter's roadmap.
example_out: A narrative that keeps uncommitted requests in later or off-roadmap, with the reason.
related:
  - outcome-roadmap
  - stakeholder-prd-review

== experiment-design | Experiment Design ==
job: Design a product experiment with a hypothesis, a guardrail, and a decision rule written in advance.
artifact: experiment design
triggers:
  - experiment design
  - product experiment
  - A/B test design
  - hypothesis test
inputs:
  - The hypothesis
  - The change
  - The primary metric and guardrail
  - The available sample
steps:
  - Hypothesis: The user behavior you expect to change, and why.
  - Change: One treatment. Name the control.
  - Metrics: A primary metric and a guardrail that would make a 'win' unacceptable, such as errors or complaints.
  - Decision rule: Ship, iterate, or stop, written before results.
  - Sample: If the sample is too small, call the work a probe, not a conclusive test.
  - Ethics: No experiment that tricks users about price, privacy, or safety.
anti:
  - Peeking and moving the metric.
  - No guardrail.
  - Calling a tiny sample conclusive.
example: A team wants to ship the winner of a three-day test on a rare flow.
example_out: A design that labels the work a probe, adds a guardrail, and refuses a conclusive ship decision.
related:
  - marketing-experiment
  - experiment-readout

== usability-test-plan | Usability Test Plan ==
job: Plan a usability test that watches someone attempt a task, instead of asking if they like the design.
artifact: usability test plan
triggers:
  - usability test
  - user test plan
  - prototype test
  - task-based test
inputs:
  - The task that matters
  - The prototype or product state
  - Who should attempt it
  - The questions the design must answer
steps:
  - Tasks: Write tasks as goals, not as click instructions. Do not give away the path.
  - Participants: People who have the problem. Five focused sessions beat a survey of opinions.
  - Script: Consent, think-aloud, tasks, and follow-ups. No 'do you like it' as the core.
  - Success: What completing the task looks like, observed, not self-reported.
  - Notes: Where they hesitate or fail. Quotes, not scores alone.
  - Limits: Say what a small test cannot prove, including market demand.
anti:
  - A preference poll called a usability test.
  - Tasks that reveal the answer.
  - Treating five users as a market proof.
example: A designer wants to ask ten coworkers whether they like a new color scheme and call it usability.
example_out: A plan with a real task, the right participants, and an explicit note that color preference is not the test.
related:
  - prototype-test-script
  - usability-findings

== launch-readiness | Launch Readiness ==
job: Run a launch-readiness review that checks support, measurement, rollback, and the promise.
artifact: launch readiness review
triggers:
  - launch readiness
  - go-live checklist
  - release readiness
  - ship review
inputs:
  - What will be announced
  - Support and docs status
  - Measurement
  - Rollback path
steps:
  - Promise check: The announcement matches what the build does. Cut the rest.
  - Support: Agents have an FAQ and a known issue list. No launch to a blind support team.
  - Measurement: The event that tells you the launch worked is instrumented, or the gap is explicit.
  - Rollback: Who can stop the launch, and how customers are told if you do.
  - Legal and claims: Unapproved claims block the public line, not the internal note.
  - Decision: Go, go with limits, or hold. One decision, with the owner.
anti:
  - A launch checklist that ignores support.
  - Announcing unshipped scope.
  - No one empowered to hold.
example: Product wants to announce automation that still requires a manual file from support.
example_out: A hold or a limited launch that tells the truth about the manual step.
related:
  - launch-plan
  - release-checklist

== pricing-packaging | Pricing and Packaging ==
job: Frame a pricing and packaging decision as a set of fences and a test, not as a number pulled from a competitor.
artifact: packaging recommendation
triggers:
  - pricing and packaging
  - package tiers
  - price a product
  - packaging review
inputs:
  - The buyer and the value unit
  - Current price and packaging
  - Costs that constrain price
  - What sales keeps conceding
steps:
  - Value unit: What the customer expects to pay for. Seat, usage, or outcome, in their language.
  - Fences: What differs between packages, and why a buyer would upgrade. Cosmetic fences are a finding.
  - Cost floor: Use their cost facts. Do not invent a margin target.
  - Concessions: What sales gives away is part of the real price. Include it.
  - Test: A limited price or package test with a decision rule, rather than a company-wide leap, when evidence is thin.
  - Honesty: No hidden fees in the recommendation. Counsel reviews consumer-facing terms if the user says they are required.
anti:
  - Copying a competitor's price with no context.
  - Hidden fees.
  - Tiers that do not change the value.
example: The company has three tiers that differ only by a feature nobody uses, and discounting is constant.
example_out: A recommendation that treats the discount as the real price and proposes a clearer fence to test.
related:
  - pricing-margin-bridge
  - offer-design

== feedback-synthesis | Feedback Synthesis ==
job: Synthesize feedback from tickets, calls, or notes into themes with evidence, not a word cloud.
artifact: feedback synthesis
triggers:
  - synthesize feedback
  - voice of customer themes
  - ticket themes
  - interview synthesis
inputs:
  - The raw notes or tickets
  - The decision this informs
  - How the sample was gathered
  - What volume means in their context
steps:
  - Sample bias: Say who is missing from the pile. A pile of detractors is not the whole market.
  - Themes: Group by the job or failure, not by the feature name alone.
  - Evidence: Each theme has quotes or ticket counts from the supplied material. No theme without evidence.
  - Severity: Distinguish frequency from pain. A rare data-loss report can outrank a common color complaint.
  - Implication: What product should do next, and what should be a support macro instead.
  - Do not invent: If the notes do not support a favorite theme, say it is not in the evidence.
anti:
  - A word cloud as the analysis.
  - Ignoring sample bias.
  - Themes with no quotes.
example: A team wants to build a feature because one executive mentioned it, and the ticket pile is about export failures.
example_out: A synthesis that leads with export failures, counts only supplied evidence, and parks the executive idea as unproven.
related:
  - voice-of-customer
  - discovery-interview

== north-star-and-input-metrics | Product Metric Tree ==
job: Define a product outcome metric and the input metrics a team can move this month.
artifact: product metric tree
triggers:
  - product metrics
  - input metrics
  - activation metric
  - product KPI
inputs:
  - The user value moment
  - Candidate metrics and definitions
  - What the team can change
  - Known ways to game the metric
steps:
  - Value moment: The observable moment the user gets value. Registration is rarely that moment.
  - Definition: Numerator, denominator, and source. No definition, no metric.
  - Inputs: Three metrics the team can move with product work this month.
  - Counter-metric: The quality or cost signal that keeps the main metric honest.
  - Gaming: How a team could hit the number and hurt the user. Close that door in the definition.
  - Baseline: Use their baseline or mark it unknown. Do not invent one.
anti:
  - Signups as the value metric by default.
  - No counter-metric.
  - An invented baseline.
example: A team wants to optimize signups, but activated users are the ones who finish a first export.
example_out: A tree that uses the first successful export as the value moment and signups as a funnel input, with a failure counter-metric.
related:
  - north-star-metric
  - product-analytics-spec

== beta-program | Beta Program ==
job: Design a beta that learns a specific risk, with participant criteria and an exit.
artifact: beta plan
triggers:
  - beta program
  - design partners
  - early access
  - pilot program
inputs:
  - The risk the beta must retire
  - Participant criteria
  - Support capacity
  - Exit criteria
steps:
  - Learning goal: The question the beta answers. A beta with no question is a soft launch.
  - Participants: Who is in and who is out. Do not recruit people who cannot hit the risk you care about.
  - Expectations: What beta users are promised, including roughness. No implied production SLA unless the user is offering one.
  - Feedback path: How issues arrive, and who triages them.
  - Exit: The evidence that ends the beta, successfully or not.
  - Reference use: Do not turn a beta quote into a public claim without approval.
anti:
  - A beta that is an unlimited free launch.
  - No exit criteria.
  - Public claims from an unhappy pilot.
example: Sales wants to call twenty unpaid pilots a beta and quote them on the website.
example_out: A plan with a learning goal, a cap matched to support capacity, and a ban on public quotes without approval.
related:
  - customer-story
  - launch-readiness

== sunset-plan | Sunset Plan ==
job: Plan the retirement of a feature or product so users are told the truth and given a path.
artifact: sunset plan
triggers:
  - sunset a feature
  - deprecate
  - end of life
  - retire a product
inputs:
  - What is being retired
  - Who uses it, if known
  - The replacement, if any
  - Contractual constraints the user mentioned
steps:
  - Why: The reason to retire, in plain language. Cost, risk, or focus. Do not invent usage data.
  - Who is affected: Use their data. If you do not know who uses it, the first step is to find out before announcing.
  - Path: The replacement or the workaround, including what it does not cover.
  - Timeline: Notice, migration window, and removal date that the user can honor. No fake date.
  - Support: Who answers migration questions. A sunset email with no owner creates a support incident.
  - Commitments: Flag contracts or promises the user says exist, and send those to counsel or account owners. Do not advise breaking a contract.
anti:
  - A surprise removal.
  - Advising the company to ignore a contract.
  - An announcement with no migration path and no owner.
example: Engineering wants to delete an API next week that three customers still call.
example_out: A plan that blocks the deletion until notice and a migration owner exist, and flags contract questions.
related:
  - change-leadership
  - customer-communication-incident

== accessibility-review | Accessibility Product Review ==
job: Review a product flow for accessibility barriers and turn them into concrete fixes, not a vague pledge.
artifact: accessibility review
triggers:
  - accessibility review
  - a11y review
  - screen reader flow
  - inclusive product review
inputs:
  - The flow
  - Known barriers
  - The standard the team says it targets
  - User impact already reported
steps:
  - Scope the flow: One important path, not the whole product in one sitting.
  - Barriers: Keyboard, labels, contrast, errors, and media alternatives, based on the material provided. Do not claim a conformance audit you did not perform.
  - Impact: Who is blocked from the job, in practical terms.
  - Fixes: Specific design or engineering changes, ordered by who is completely blocked.
  - Tests: How the team can recheck the flow. Automated scans are a start, not a certificate.
  - No certificate: Do not claim WCAG conformance unless a qualified review the user supplied says so.
anti:
  - Claiming compliance from a glance.
  - A pledge with no fixes.
  - Ignoring a reported blocker because the visual design looks fine.
example: A checkout cannot be completed by keyboard, and the team wants a statement saying the product is accessible.
example_out: A review that blocks the statement, names the keyboard barrier, and lists the fix and retest.
related:
  - accessibility-engineering
  - accessibility-design

== product-analytics-spec | Product Analytics Spec ==
job: Specify the events and properties a product change needs so the team can tell whether it worked.
artifact: analytics spec
triggers:
  - tracking plan
  - event spec
  - analytics specification
  - what should we instrument
inputs:
  - The decision the data must support
  - The user actions that matter
  - Existing events
  - Privacy limits they already follow
steps:
  - Decision first: Write the question, then the events. Do not add events with no question.
  - Event definitions: Name, trigger, and properties. A vague 'button clicked' with no context is a finding.
  - Identity: How a user is recognized, using their existing approach. Do not invent a tracking identity that violates their privacy rules.
  - Privacy: Collect the minimum. Do not specify secrets, full card numbers, or health details as event properties.
  - QA: How an engineer will know the event fired correctly before release.
  - Naming: Match their existing convention. Do not rename the warehouse for one feature.
anti:
  - Events with no decision behind them.
  - Tracking secrets or card numbers.
  - A spec that ignores the current naming convention.
example: A spec adds a property for a user's full home address to measure a button click.
example_out: A revised spec that removes the address, defines the click in context, and names the decision it serves.
related:
  - event-tracking-spec
  - privacy-by-design

== stakeholder-prd-review | Stakeholder PRD Review ==
job: Review a PRD with stakeholders by separating decisions from opinions and parking out-of-scope demands.
artifact: PRD review notes
triggers:
  - PRD review
  - stakeholder review
  - spec review meeting
  - requirements review
inputs:
  - The PRD
  - The attendees and their concerns
  - Decisions already made
  - The open questions
steps:
  - Outcome check: Can every reviewer state the user outcome. If not, fix that before debating details.
  - Classify comments: Decision, risk, or preference. Preferences do not silently change scope.
  - Conflicts: Where two stakeholders demand incompatible scope, write the tradeoff and the decider.
  - Parking lot: Out-of-scope requests go to the parking lot with a reason, not into the PRD out of politeness.
  - Open questions: Owner and date. Unowned questions are the real launch risk.
  - Close: Restate the scope that survived the review so nobody leaves with a private version.
anti:
  - Adding every comment to the spec.
  - Leaving the review with two different scopes in people's heads.
  - Treating every preference as a requirement.
example: Sales adds six prospect requests during a PRD review, and engineering thinks they are now committed.
example_out: Notes that park the six requests, restate the surviving scope, and name the decider for any conflict.
related:
  - prd-writer
  - roadmap-narrative

== outcome-roadmap | Outcome Roadmap ==
job: Rebuild a feature roadmap into an outcome roadmap with bets, evidence, and kill criteria.
artifact: outcome roadmap
triggers:
  - outcome roadmap
  - roadmap rewrite
  - bets not features
  - product strategy roadmap
inputs:
  - The current roadmap items
  - The outcomes they are supposed to serve
  - Evidence
  - Capacity
steps:
  - Cluster: Group features under the outcome they claim to serve. Features with no outcome are parked.
  - Bet statement: For each outcome, the bet, the audience, and the evidence grade.
  - Sequence: Order bets by learning and constraint, not by who shouted.
  - Capacity: Cut bets until the team could actually run them. A roadmap over capacity is fiction.
  - Kill criteria: What would stop a bet. Write it on the roadmap.
  - Communication: A version stakeholders can read without decoding internal names.
anti:
  - Renaming features as outcomes without changing the plan.
  - A roadmap that exceeds capacity.
  - No kill criteria.
example: A roadmap of 25 features is relabeled with four outcomes, but the team can staff one bet.
example_out: An outcome roadmap that keeps one staffed bet, parks the rest, and writes a kill criterion.
related:
  - roadmap-narrative
  - portfolio-prioritization
'''
)]
