from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "research", "title": "Research", "summary": "Questions, evidence tables, and citations that do not invent sources.", "keywords": ["research", "evidence", "citations", "interviews", "surveys"]},
    """
literature-review-plan | Literature Review Plan | review plan
job: Plan a literature review around a question, with sources the user can actually obtain and no fabricated papers.
triggers: literature review; review plan; evidence review; what should I read
inputs: The question; Inclusion rules; Databases or shelves they can access; Time
steps: Write the question so a paper can be in or out. || Define inclusion and exclusion. || Plan a search from sources they can open. Do not pretend you searched a database you did not search. || Keep a log of queries they run. || A paper you cannot identify precisely is not cited. Say it is missing. || Synthesize by theme after screening, not before.
anti: Fabricated citations; A review with no inclusion rule; Claiming a search you did not run
example: A draft cites three articles with confident titles the user cannot find.
out: A plan that removes unverified citations and sets an inclusion rule before more reading.
related: citation-hygiene; evidence-table

research-question | Research Question | research question
job: Sharpen a research question so it is answerable with the methods and access the user has.
triggers: research question; sharpen my question; study question; is this researchable
inputs: The draft question; The decision or knowledge gap; Available access; Time and skill limits
steps: Separate a topic from a question. || Name the population, phenomenon, and comparison or change, as applicable. || Check that the user can reach the evidence. A question they cannot observe needs a redesign. || State what the question will not answer. || Flag ethics review if people are involved. Do not invent an approval. || Recommend the smallest study that would answer it.
anti: A topic pretending to be a question; A design they cannot access; Skipping ethics when people are involved
example: The question is 'is remote work good' with no population or outcome.
out: A narrower question with a population, an outcome, and an explicit non-answer.
related: literature-review-plan; ethics-review-prep

citation-hygiene | Citation Hygiene | citation check
job: Check citations so every claim that needs a source has one the user can verify.
triggers: citation check; references; bibliography hygiene; source this claim
inputs: The draft; The sources they have; The citation style if required; Claims that sound factual
steps: Mark factual claims that lack a source the user provided. || Do not invent a citation to fill a gap. Ask for a source or rewrite the claim as an assumption. || Match quotations to text they supplied. A quote you cannot see is not used. || Note style errors only after existence is confirmed. || Separate the user's analysis from cited facts. || Flag a citation that does not support the sentence it is attached to, if you can see both.
anti: Invented papers; A quotation you cannot verify; A citation that does not support the claim
example: A paragraph says 'studies show' and lists no study the user has.
out: A revision that replaces the phrase with an assumption or a request for the actual study.
related: literature-review-plan; research-memo

interview-guide-research | Research Interview Guide | research interview guide
job: Write a research interview guide that asks about lived events and records consent the user already requires.
triggers: research interview; qualitative interview guide; interview protocol; field interview
inputs: The question; The participant type; Consent requirements they stated; Sensitive topics
steps: Open with consent in the form they specified. Do not invent a legal consent standard. || Ask about recent events, not hypothetical ideals. || Order questions from safer context to more sensitive topics. || Plan probes that do not put words in the participant's mouth. || State how notes will be stored, using their plan. Do not design covert recording. || This is research, not a sales discovery call, unless they said it is both.
anti: Covert recording; Leading questions that supply the finding; Skipping their consent step
example: A guide starts by asking participants to agree that the product is essential.
out: A guide that asks for the last real incident and includes their consent step.
related: discovery-interview; qualitative-coding

survey-instrument | Survey Instrument | survey draft
job: Draft a survey that measures a defined construct without double-barreled or leading items.
triggers: survey design; questionnaire; write a survey; instrument draft
inputs: The decision; The constructs; The population; Length they will tolerate
steps: Write the decision the survey must inform. || One idea per item. Split double-barreled questions. || Avoid leading wording and false precision. || Use scales they can explain. || Pilot plan: who will try it before launch. || Do not add demographic items you do not need. Minimize sensitive data.
anti: Double-barreled items; Leading wording; Sensitive items with no purpose
example: An item asks whether the helpful and innovative service was satisfying.
out: A draft that splits the ideas, removes the leading praise, and cuts unused demographics.
related: survey-analysis; research-question

qualitative-coding | Qualitative Coding Plan | coding plan
job: Plan qualitative coding so themes come from the data they have, with a second-coder check when it matters.
triggers: qualitative coding; codebook; thematic analysis; code these interviews
inputs: The question; The transcripts or notes they have; Whether a second coder exists; The decision
steps: Start from the question, not from a favorite theme. || Define codes with inclusion and exclusion examples from their text only. || Do not invent quotations. || If reliability matters for the decision, plan a second coder on a sample. || Separate codes from themes. A theme needs more than one code name. || Note what the sample cannot support.
anti: Invented quotations; Themes decided before reading; A codebook with no examples
example: A report lists themes and the user has not provided the supporting lines.
out: A coding plan that blocks the report until each theme has a supplied excerpt.
related: interview-guide-research; research-memo

research-memo | Research Memo | research memo
job: Write a research memo that separates evidence, interpretation, and what is still unknown.
triggers: research memo; findings memo; synthesize this research; evidence memo
inputs: The question; The evidence they gathered; The method limits; The audience
steps: Restate the question. || Summarize evidence with sources they provided. || Put interpretation in a labeled section. || Write the limits: sample, access, and time. || Do not upgrade a small study into a law of the market. || End with the next question or decision, not with a padded conclusion.
anti: A law-of-the-market claim from a small sample; Sources you cannot see; Interpretation disguised as fact
example: Five interviews are written up as proof an entire industry is shifting.
out: A memo that limits the claim to those five interviews and lists what a larger study would need.
related: executive-insight; evidence-table

grant-narrative | Grant Narrative | grant narrative draft
job: Draft a grant narrative from the funder's questions and the project's real evidence, without inflated impact.
triggers: grant narrative; proposal narrative; funder questions; grant draft
inputs: The funder's questions; The project facts; Evidence of need and capacity; What they cannot promise
steps: Answer the funder's questions in their order. || Use only outcomes the user can support. || Separate past results from hoped-for results. || Name capacity: who will do the work. || Budget talk must match the budget they supplied. Do not invent costs. || Do not help misstate eligibility or fabricate a partner letter.
anti: Fabricated partner letters; Inflated past results; Costs that do not match the budget
example: A draft claims a partner committed staff, and no letter exists.
out: A narrative that moves the partner to 'in discussion' or cuts the claim.
related: nonprofit-case-statement; research-memo
avoid: Fabricated commitments

ethics-review-prep | Ethics Review Prep | ethics review brief
job: Prepare an ethics review brief for a study involving people, for the review board to judge.
triggers: ethics review; IRB prep; human subjects brief; research ethics
inputs: What participants will be asked to do; Risks they can foresee; Consent plan; Data storage plan
steps: Describe the procedure in plain language. || List burdens and risks they identified. Do not minimize them. || Explain consent and the right to stop, using their plan. || Describe data storage without collecting secrets into the brief. || Note vulnerable participants if they said any are included, and send that to the board. || Do not tell the user to skip review, and do not draft deceptive consent.
anti: Deceptive consent; Advice to skip review; Minimized risks
example: A team wants consent language that hides the real purpose from participants.
out: A brief that refuses hidden purpose and sends the design to the proper review.
related: research-question; privacy-impact-assessment
avoid: Deceptive consent; Skipping required review

evidence-table | Evidence Table | evidence table
job: Build an evidence table from sources the user supplied, with columns that match the question.
triggers: evidence table; extraction table; study table; literature matrix
inputs: The question; The sources they have; The fields to extract; Inclusion status
steps: Columns follow the question: population, method, finding, limit. || Extract only what the source they provided actually says. || Mark a field unknown rather than filling it from memory. || Keep excluded sources in a short log with the reason. || Do not add a source you cannot identify. || Note if the table is too thin for a conclusion.
anti: Cells filled from memory; Ghost sources; A conclusion the table does not support
example: A table has effect sizes the user never found in the papers.
out: A table with those cells marked unknown and a warning against a numeric conclusion.
related: literature-review-plan; citation-hygiene

desk-research | Desk Research Brief | desk research brief
job: Brief desk research so secondary sources are scoped, credited, and not mistaken for primary proof.
triggers: desk research; secondary research; landscape scan; background research
inputs: The decision; Sources they can use; Time; What would count as good enough
steps: Define the decision and the facts that would change it. || List source types they will accept. || Credit every fact with the source they found. Unknown stays unknown. || Separate a vendor's marketing from independent reporting. || Stop when the decision is informed or the time box ends. || Do not present desk research as a customer study.
anti: Vendor copy treated as independent proof; Unsourced facts; Desk research sold as interviews
example: A landscape scan quotes a vendor's homepage as market share.
out: A brief that labels the homepage as a claim, not as market share, and lists the missing independent source.
related: market-entry-assessment; citation-hygiene
"""
))

PACKS.append(pack(
    {"id": "design", "title": "Design", "summary": "Critique, content design, and handoff that respect users and accessibility.", "keywords": ["design", "ux", "content", "accessibility", "handoff"]},
    """
design-critique | Design Critique | design critique
job: Critique a design against the user job and the constraints, with changes ranked.
triggers: design critique; UX critique; review this design; critique the mock
inputs: The user job; The design or a description; Constraints; Known evidence
steps: Restate the job the screen must finish. || Name what works, specifically, so the critique is usable. || Rank issues by whether they block the job, not by taste. || Recommend a change for each blocking issue. || Separate evidence from taste. || Do not redesign the brand for sport, and do not copy a third party's branded work.
anti: Taste comments with no job impact; A copy of a famous product; No ranked issues
example: A critique debates the font while the primary action is below the fold on the task's only screen.
out: A critique that leads with the blocked action and treats the font as secondary.
related: usability-findings; visual-hierarchy-review

ux-writing | UX Writing | interface copy
job: Write interface copy that tells the user what happened, what to do, and what they are committing to.
triggers: UX writing; microcopy; button label; empty state copy; error message
inputs: The user action; The system state; The tone guide if any; Legal lines they must include
steps: Label the action as the outcome, not as OK, when the outcome matters. || Error text says what went wrong and how to fix it, if known. || Empty states teach the next action. || Commitment moments state the consequence before the click. || Use their required legal line verbatim. Do not invent one. || Cut cleverness that hides meaning.
anti: An OK button on a destructive action; Cute error text with no fix; Invented legal lines
example: A delete dialog says 'Let's do this' and does not name the deletion.
out: Copy that names the deletion and the consequence before confirm.
related: brand-voice-guide; empty-state-design

design-system-token | Design Token Decision | token decision
job: Decide whether a new visual style becomes a token or stays a one-off, based on reuse.
triggers: design token; design system decision; should this be a component; style decision
inputs: The style in question; Where it is used; Existing tokens; The owner of the system
steps: Count real reuse. One screen does not automatically earn a token. || Match an existing token before adding one. || Name the token by purpose, not by a hex value alone. || Note accessibility contrast as a requirement, not a later wish, when text is involved. || Record who may add tokens. || Do not fork the system in a product file and call it a token.
anti: A token for a one-off; A hex-named token with no purpose; A fork called a system
example: A campaign color is about to become a global brand token after one banner.
out: A decision that keeps the campaign color local until reuse is real.
related: design-handoff; brand-guidelines-apply

wireframe-spec | Wireframe Spec | wireframe specification
job: Specify a wireframe's structure, priority, and states so visual design does not have to guess.
triggers: wireframe spec; low fidelity spec; screen structure; UX spec
inputs: The task; The content priority; States: empty, error, success; Constraints
steps: Order content by the decision on the screen. || Specify primary and secondary actions. || Include empty, loading, and error states. A happy path only is incomplete. || Note what data is required. Do not invent personal data in examples. || Mark open questions. || Hand off the job of the screen, not a prescription of every pixel, unless the user asked for visual design.
anti: A happy path only; Fake personal data in the example; No primary action
example: A wireframe shows a full dashboard and no empty state for a new account.
out: A spec that adds the empty state and names the primary action.
related: empty-state-design; design-handoff

usability-findings | Usability Findings | findings note
job: Write usability findings from observed task failures, with severity and a recommended change.
triggers: usability findings; test findings; user test readout; what did the test show
inputs: The tasks; What participants did; Severity clues; What the test cannot prove
steps: Report the task and the observed failure. || Quote or describe only what was observed. || Rate severity by whether the task was blocked. || Recommend a design change for each blocking finding. || State the sample limit. Do not claim market proof. || Do not identify participants beyond what consent allows.
anti: Market-proof claims from five tests; Findings with no observation; Identified participants
example: A readout says users love the brand because three people finished a task.
out: A note that reports task completion, refuses the love claim, and ranks blocking issues.
related: usability-test-plan; design-critique

information-architecture | Information Architecture | IA recommendation
job: Recommend an information architecture from user tasks, not from the company's org chart.
triggers: information architecture; site map; navigation; IA review
inputs: Top tasks; Current labels; Evidence of confusion; Constraints
steps: List tasks users come to finish. || Group by those tasks, not by internal departments. || Label in the user's words if you have them. || Show what moves or gets cut. || Note search versus navigation. Do not hide a bad structure behind a search box as the only plan. || Test labels with a simple card sort or tree test plan if the stakes are high and they can run one.
anti: Navigation that mirrors the org chart; A search box as the only fix; Labels nobody outside the company uses
example: The nav has a tab for each internal department and users cannot find billing.
out: An IA that groups billing under the task users named and demotes the org chart.
related: journey-map; design-critique

empty-state-design | Empty State Design | empty state spec
job: Design an empty state that explains why it is empty and offers the next honest action.
triggers: empty state; blank screen; zero data state; first-run screen
inputs: Why the screen is empty; The action a user can take; What they cannot do yet; Tone
steps: Say why the screen is empty: new user, filter, or no permission. || Offer the next action only if it is really available. || Do not fake sample data that looks like the user's own data. || If a filter caused the empty state, show how to clear it. || Keep the tone calm. || Match the empty state to the permission model. Do not invite an action the role cannot perform.
anti: Fake data that looks real; An action the role cannot do; An empty screen with no reason
example: A dashboard shows sample revenue that looks like the customer's numbers.
out: A spec that labels or removes the sample and explains the true empty reason.
related: ux-writing; wireframe-spec

form-design-review | Form Design Review | form review
job: Review a form for necessary fields, error recovery, and an honest submit.
triggers: form review; form design; checkout form; signup form
inputs: The purpose of the form; Fields; Error states; What submit commits the user to
steps: Cut fields that do not serve the purpose. || Mark required fields and say why. || Specify errors that tell the user how to fix the input. || State the commitment at submit: pay, publish, or send. || Do not ask for secrets that do not belong, such as a password to 'confirm identity' by email reply. || Mobile and keyboard paths are part of the review if they described those users.
anti: Extra sensitive fields; A submit that hides a charge; Errors that only say invalid
example: A contact form requires a social security number.
out: A review that removes the number, states the real purpose, and specifies a useful error.
related: privacy-by-design; ux-writing

design-handoff | Design Handoff | handoff note
job: Hand a design to engineering with states, content, and open decisions explicit.
triggers: design handoff; spec for engineering; developer handoff; design QA notes
inputs: The screens; States; Content; Known decisions still open
steps: List what is in scope for this handoff. || Include empty, error, and loading states. || Write the content, not lorem, unless a field is truly dynamic, and then say so. || Mark open decisions so engineering does not guess. || Note accessibility expectations for the flow. || Do not treat a static mock as permission to skip the unauthorized state.
anti: Lorem on a commitment screen; Hidden open decisions; No error state
example: A handoff includes the success screen only for a payment flow.
out: A handoff that adds failure, empty, and the unauthorized state, and lists open decisions.
related: wireframe-spec; accessibility-design

accessibility-design | Accessibility Design Review | accessibility design note
job: Review a design for access barriers before build, without issuing a conformance certificate.
triggers: accessibility design; a11y design review; inclusive design review; contrast and focus
inputs: The flow; Text and controls; Known barriers; The target they claim
steps: Check the flow for keyboard order, names, and focus as far as the mock shows. || Flag text that will fail contrast if the values are visible. Do not invent a pass. || Error identification must not depend on color alone. || Touch and target size are noted if they specified a platform. || Write fixes a designer can make now. || Do not claim WCAG conformance from a visual review.
anti: A conformance badge from a glance; Errors shown by color only; No focus order on a custom control
example: A mock uses placeholder color as the only label.
out: A note that requires a visible label and refuses a conformance claim.
related: accessibility-review; design-critique

service-blueprint | Service Blueprint | service blueprint
job: Blueprint a service so frontstage customer steps and backstage failures sit on one page.
triggers: service blueprint; service design; backstage map; blueprint a service
inputs: The customer job; Frontstage steps; Backstage teams; Evidence of failure
steps: Start with the customer steps. || Add the backstage actions and systems that support each step. || Mark the fail points they have evidence for. || Show the handoff that drops the ball. || Pick one fail point to redesign. || Do not draw a blueprint of a service they do not operate and call it current.
anti: A frontstage-only journey called a blueprint; Invented backstage steps; No fail point
example: The blueprint shows a smooth handoff, but tickets pile up between sales and onboarding.
out: A blueprint that draws the pile-up and assigns the handoff to fix.
related: journey-map; process-map

visual-hierarchy-review | Visual Hierarchy Review | hierarchy review
job: Review visual hierarchy so the next action and the key fact win, within the brand constraints they have.
triggers: visual hierarchy; layout review; what should stand out; scan review
inputs: The primary action; The key fact; The layout; Brand constraints
steps: Name the first thing a busy user must see. || Check whether size, position, and contrast support that order, from what you can see. || Demote decorations that compete with the action. || Keep required legal text visible enough to read. || Recommend the smallest change that fixes the order. || Do not restyle the brand for taste.
anti: A restyle with no hierarchy problem; Legal text hidden; Decoration competing with the action
example: A hero image buries the price and the purchase action.
out: A review that brings the price and action forward and leaves the brand system alone.
related: design-critique; landing-page-cro

prototype-test-script | Prototype Test Script | prototype test script
job: Write a prototype test script that gives the participant a goal and does not reveal the clicks.
triggers: prototype test; usability script; test script; moderated test
inputs: The prototype scope; The goal; The participant; Time
steps: Set the scene without naming the button. || Give a goal and a definition of done. || Plan neutral probes for hesitation. || Do not ask if they like it until the task is done, if at all. || Note what the prototype cannot do so the facilitator does not fake a path. || End with consent-respecting notes and no identity beyond the study id.
anti: Click-by-click instructions; A likeability question as the test; A fake path the prototype cannot do
example: A script says 'click the blue button in the corner' as the task.
out: A script that gives the goal and removes the click path.
related: usability-test-plan; usability-findings
"""
))
