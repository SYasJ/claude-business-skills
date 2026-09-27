from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "operations", "title": "Operations", "summary": "SOPs, capacity, service levels, and the weekly operating system.", "keywords": ["operations", "sop", "capacity", "sla", "process"]},
    """
sop-writer | SOP Writer | standard operating procedure
job: Write a standard operating procedure a new person can run, with the stop conditions included.
triggers: write an SOP; standard operating procedure; document this process; operating procedure
inputs: The outcome of the process; The steps as performed today; Exceptions; The owner
steps: Name the outcome and the trigger that starts the work. || Write steps in the order a new person would do them, including where the file or tool actually lives if the user said so. || Add the check that shows the step worked. || Write stop conditions: when to halt and ask. || Put exceptions in the procedure, not in someone's memory. || Name the owner and the review date. A procedure with no owner will drift.
anti: A procedure only the author understands; No stop condition; Steps that invent a system path
example: A finance SOP says 'process the file' and the file location lives in one person's head.
out: A procedure with the trigger, the check, a stop condition, and an owner.
related: process-map; knowledge-base-article

process-map | Process Map | process map
job: Map a process as it is, including handoffs and waits, before anyone redesigns it.
triggers: process map; current state map; handoff map; where does this process break
inputs: The start and end; The people who touch it; The waits they complain about; The systems
steps: Map the current state, not the wished state. Label it current. || Show handoffs and queues. The wait is often the process. || Mark rework loops the user described. || Do not add a control that does not exist and call it current. || Identify one bottleneck with evidence from their description. || Recommend a future change separately from the map.
anti: A future-state map labeled current; Ignoring queues; A map with no handoffs
example: A team draws a five-box happy path and omits the two-day wait for approval.
out: A current-state map that includes the approval wait and separates any future idea.
related: sop-writer; continuous-improvement

capacity-plan | Capacity Plan | capacity plan
job: Plan capacity from demand and real throughput, and show the constraint before hiring or buying.
triggers: capacity plan; do we have capacity; throughput plan; staffing versus demand
inputs: Demand they expect; Current throughput; The constraint; Time horizon
steps: Define the unit of work and the horizon. || Use their throughput, not an industry benchmark. || Name the constraint: people, a tool, a supplier, or a policy. || Show the gap between demand and throughput in their units. || Options: smooth demand, remove a wait, or add capacity. Adding capacity is not the default if a wait is the constraint. || State what would make the plan wrong.
anti: An invented benchmark; Hiring as the only option; A plan with no unit of work
example: A team wants three hires because the queue is long, and approvals sit for two days.
out: A plan that tests the approval wait before treating hires as the answer.
related: workforce-plan; queue-health

sla-design | SLA Design | service level design
job: Design a service level that matches a customer promise the team can measure and staff.
triggers: SLA design; service level; define an SLA; support response target
inputs: The promise customers already hear; Current performance if known; Staffing; Exceptions
steps: Start from the promise already made. If operations cannot meet it, the finding is the promise or the staffing, not a prettier SLA. || Define the clock: when it starts and stops, and which tickets count. || Set a target from their history or mark it as a proposal. || Add an exception path for cases the SLA should not pretend to cover. || Name the measure and the owner. || Do not hide a missed SLA by reclassifying work after the fact. Recommend against that.
anti: An SLA nobody measures; Reclassifying misses; A target copied from a competitor
example: Sales promises a one-hour response and the queue currently averages a day.
out: A design that exposes the gap and proposes either a truthful promise or a staffed path, with no silent reclassification.
related: service-catalog; ticket-quality-review

vendor-ops-review | Vendor Operations Review | vendor operations review
job: Review a vendor's operational performance against the outcomes the company bought.
triggers: vendor review; supplier performance; vendor QBR; operations vendor scorecard
inputs: The outcomes contracted; Recent misses they know; Volumes; The internal owner
steps: Score outcomes, not the relationship vibe. || Use their incidents, delays, and volumes. Do not invent a score. || Separate a one-time miss from a pattern. || Ask whether the internal team kept its side of the process. || Recommend continue, fix with a dated plan, or replace as a question for procurement. || Do not invent contract penalties. Flag them for the contract owner.
anti: A score with no data; Blaming the vendor for an internal miss; Invented penalties
example: A vendor is labeled difficult, but the internal briefs arrive late every week.
out: A review that records the late briefs as an internal cause and limits the vendor claim to evidenced misses.
related: supplier-scorecard; procurement-award-note

business-continuity | Business Continuity Plan | continuity plan
job: Draft a continuity plan for a named disruption, with a manual path and a named leader.
triggers: business continuity; BCP; what if this system is down; continuity plan
inputs: The disruption they want to survive; The critical process; Manual workaround if any; The leader
steps: Name the disruption and the process that must continue. A plan for 'anything' is not a plan. || Define the acceptable pause in their words. || Write the workaround with the people and tools it actually needs. || Name the leader and the alternate. || List who must be told. || Test the workaround on a date. An untested workaround is a rumor.
anti: A plan with no leader; An untested workaround presented as ready; A plan so broad it cannot be used
example: The team has a continuity binder and nobody knows who declares the workaround in effect.
out: A plan for one disruption, with a leader, a manual path, and a test date.
related: backup-and-restore-test; disaster-recovery-brief

knowledge-base-article | Knowledge Base Article | knowledge article
job: Write a knowledge article that answers one question and tells the reader when to stop and escalate.
triggers: knowledge base article; help center article; internal KB; how-to article
inputs: The question; The correct steps; The audience; The escalation path
steps: Use the reader's question as the title. || Number the steps. Include the expected result of the key step. || Add the symptoms that mean this article is the wrong one. || Tell them when to escalate, and to whom. || Remove internal jargon or explain it. || Do not include secrets, internal-only credentials, or a workaround that violates policy.
anti: An article that answers three questions badly; A secret in a help article; No escalation line
example: A help draft includes an admin password so customers can 'fix it themselves'.
out: An article that removes the password, answers one question, and gives an escalation path.
related: support-macro; sop-writer

shift-handover | Shift Handover | shift handover
job: Write a shift handover that carries open issues, safety notes, and the next check.
triggers: shift handover; shift report; production handover; operations handover
inputs: Open issues; Safety or quality notes; What the next shift must check; Staffing gaps
steps: List open issues with status and the next action. || Highlight safety and quality holds first. || Say what was completed so the next shift does not redo it. || Name the fragile item to recheck and when. || Note staffing gaps that change what is possible. || Keep rumors out. Unknowns are labeled unknown.
anti: A handover that says nothing happened while a hold is open; Rumors; No next check
example: An outgoing shift leaves a quality hold unmentioned because the note says 'quiet night'.
out: A handover that leads with the hold, the next check, and an explicit not-quiet status.
related: oncall-handoff; gemba-walk

continuous-improvement | Continuous Improvement | improvement brief
job: Frame an improvement from a measured problem, a small countermeasure, and a check.
triggers: continuous improvement; kaizen; process improvement; fix this recurring issue
inputs: The recurring problem; The measure; The suspected cause; The time box
steps: State the problem as a gap in a measure they have. || Go see the work before proposing a tool. Ask for the observation if they have not made one. || Pick one suspected cause to test. A fishbone with no test is a poster. || Propose a small countermeasure the team can run in the time box. || Define the check that says it worked. || Plan how the new way becomes the standard if the check passes.
anti: A tool purchase as the first countermeasure; No measure; A brainstorm with no test
example: A team wants new software because a weekly report is late, and nobody has watched the report being built.
out: A brief that requires an observation of the current report path before any purchase.
related: process-map; capa-plan

raci-design | RACI Design | RACI
job: Assign one accountable owner to a decision or process and stop at the roles that matter.
triggers: RACI; who owns this; decision rights; accountable owner
inputs: The decision or process; The people involved; Where work stalls; Who is currently blamed
steps: Define the decision narrowly. A RACI for a whole department is too vague. || Assign exactly one accountable owner. Two A's are the finding. || Consulted and informed lists stay short. A crowd is not a control. || Check the stall: the missing A or the extra C is usually visible in their story. || Write what the owner may decide without another meeting. || Revisit only if the decision rights are still unclear after a real case.
anti: Two accountable owners; A RACI that includes everyone; No decision written down
example: A launch is late because product and marketing both think the other owns the date.
out: A RACI with one owner for the date and a short consulted list.
related: operating-cadence; stakeholder-map

meeting-operating-system | Meeting Operating System | meeting system
job: Redesign a meeting so it produces a decision or a documented exception, or cancel it.
triggers: meeting redesign; too many meetings; operating review; meeting system
inputs: The meeting's supposed purpose; Who attends; What decisions stall; The pre-read if any
steps: Write the decision the meeting exists to make. If there is none, recommend cancellation or a written update. || Cut attendees to deciders and the person with the facts. || Require a one-page pre-read. No pre-read, no meeting. || Exceptions only. Do not tour green metrics. || End with owners and dates. || Review the meeting itself after a few cycles and kill it if the decisions are still made in the hallway.
anti: A status meeting with no decision; Inviting everyone; No pre-read
example: A weekly meeting has 18 people and has not made a decision in a month.
out: A redesign that cuts attendees, requires a pre-read, and cancels the meeting if no decision remains.
related: operating-cadence; status-report

internal-comms-plan | Internal Communications Plan | internal comms plan
job: Plan an internal message for a change people must understand, with the hard part said plainly.
triggers: internal comms; announce a change; staff communication; leadership message
inputs: The change; The audience; What they will lose or must do; The speaker
steps: State the change in one sentence a frontline person can repeat. || Include what it means for their Tuesday. || Say the hard part if the user has confirmed it: timing, workload, or role impact. Do not hide a layoff or a pay change in soft language, and do not help deceive staff. || Choose the speaker who can answer questions. || Provide a question path. || Follow with a short FAQ grounded in decisions already made, not in hopes.
anti: A message that hides a confirmed hard impact; No question path; Jargon in the first line
example: A memo announces 'exciting operating model evolution' and never says whose work changes.
out: A message that says whose work changes, who will answer questions, and what stays the same.
related: change-leadership; stakeholder-map

service-catalog | Service Catalog Entry | service catalog entry
job: Write a service catalog entry that tells an internal customer what they can request, how long it takes, and what is not included.
triggers: service catalog; internal service definition; what does this team offer; request path
inputs: The service; Who may request it; The standard lead time they can meet; Exclusions
steps: Describe the service as an outcome, not as a department name. || Say who may request it and how. || Publish a lead time they have evidence they can meet. If they cannot, mark the time as unknown. || List exclusions so hidden work does not arrive as emergencies. || Name the owner and the escalation. || Add how demand is reviewed when the queue exceeds capacity.
anti: A catalog with no exclusions; A lead time they cannot meet; A request path only insiders know
example: An internal team is judged on a two-day turnaround it has never hit.
out: An entry with a truthful lead time or an explicit unknown, plus exclusions.
related: sla-design; queue-health

ops-scorecard | Operations Scorecard | operations scorecard
job: Build an operations scorecard of a few measures that predict pain, with owners and a review cadence.
triggers: ops scorecard; operations KPIs; weekly ops metrics; service scorecard
inputs: The pains to reduce; Measures they can collect weekly; Owners; The review forum
steps: Choose measures that move before customers escalate, if they have such signals. || Cap the scorecard. More than seven numbers will not be reviewed. || Define each measure. || Pair a volume measure with a quality or aging measure so speed cannot hide rework. || Assign an owner and a threshold that triggers a conversation, not an automatic blame. || Retire a measure that never changes a decision.
anti: A 40-metric scorecard; A speed metric with no quality pair; Thresholds used only to punish
example: A team tracks tickets closed and ignores reopen rate.
out: A short scorecard that pairs closed tickets with reopens and names the review forum.
related: kpi-tree-finance; sla-design

queue-health | Queue Health | queue health review
job: Review a queue's age, arrival, and handling so the team fixes flow instead of only urging people to work faster.
triggers: queue health; backlog aging; ticket backlog; work in process
inputs: Arrivals and completions; Age of the oldest items; Who is blocked; Special handling rules
steps: Show arrivals versus completions. A pep talk will not fix a queue that arrives faster than it leaves. || Age the oldest items. The tail matters more than the average if they have the data. || Find blocked work and name the blocker. || Check whether special handling is jumping the queue and starving older work. || Recommend a WIP limit, a policy change, or a demand cut before adding people, if the math shows a flow problem. || Set the review cadence.
anti: Blaming individuals for an arrival-rate problem; Managing only the average; Ignoring blocked work
example: Leaders want the team to stay late, but arrivals have exceeded completions for six weeks.
out: A review that names the imbalance and recommends a demand or policy change before overtime becomes the system.
related: capacity-plan; ticket-quality-review

disaster-recovery-brief | Disaster Recovery Brief | disaster recovery brief
job: Brief a disaster recovery choice for one system, including the recovery point they are actually buying.
triggers: disaster recovery; RPO RTO; DR brief; recovery objective
inputs: The system; The recovery point and time they need; What they have tested; Dependencies
steps: Define the business process the system serves. || Record the recovery point and time they want, labeled as a want until a test proves it. || List dependencies. A restored app with no identity provider is not recovered. || Note the last test and its result. No test, no claim of readiness. || Identify the gap between the want and the evidenced capability. || Hand the investment decision to finance with the gap visible. Do not invent a vendor price.
anti: Claiming a recovery time that was never tested; Ignoring a dependency; An invented price
example: A team claims a four-hour recovery and has never failed over the identity provider.
out: A brief that downgrades the claim to untested and names the identity dependency.
related: business-continuity; backup-and-restore-test
"""
))

PACKS.append(pack(
    {"id": "delivery", "title": "Project delivery", "summary": "Charters, plans, risks, and status that tell the truth about commitments.", "keywords": ["project", "delivery", "sprint", "risk", "status"]},
    """
project-charter | Project Charter | project charter
job: Write a project charter that names the outcome, the sponsor, the constraint, and what is out of scope.
triggers: project charter; initiate a project; project brief; charter draft
inputs: The outcome; The sponsor; The constraint; Known non-goals
steps: Write the outcome as a change in the world, not as 'deliver the project'. || Name one sponsor who can resolve priority. || State the binding constraint: date, cost, or scope. All three cannot be sacred. || List non-goals. || Record assumptions that would cancel the work if false. || Define done at the charter level so later status has something to point at.
anti: A charter with no sponsor; All of scope, date, and cost marked fixed; No non-goals
example: A sponsor wants a fixed date, fixed scope, and fixed cost with no contingency.
out: A charter that forces a binding constraint and writes the non-goals.
related: milestone-plan; raid-log

sprint-plan | Sprint Plan | sprint plan
job: Plan a sprint from capacity and a clear sprint goal, not from whoever added tickets last.
triggers: sprint plan; plan the sprint; sprint goal; iteration plan
inputs: Team capacity; Candidate work; The sprint goal; Known absences
steps: Write one sprint goal that a stakeholder can understand. || Subtract absences from capacity before pulling work. || Pull work that serves the goal until capacity is full. Park the rest visibly. || Each selected item needs a done statement. || Name dependencies that sit outside the team. || Do not fill the sprint with unestimated 'small' work that has no owner.
anti: A sprint with no goal; Ignoring absences; A plan over capacity
example: A team plans a full sprint while two people are out and the board is already full.
out: A plan that cuts scope to the remaining capacity and states one goal.
related: definition-of-done; estimation-review

raid-log | RAID Log | RAID log
job: Maintain a RAID log that separates risks, assumptions, issues, and dependencies, each with an owner.
triggers: RAID log; risk issue dependency; project RAID; assumptions log
inputs: Current worries; Owners; Dates; Which items are already issues
steps: Classify each item: risk, assumption, issue, or dependency. An issue is already happening. || Give each item one owner and a next date. || Write the impact in delivery terms. || Close items that are no longer true rather than letting the log rot. || Escalate dependencies the team cannot move. || Do not hide an issue inside a risk to keep a status green.
anti: A log with no owners; An issue disguised as a risk; A log nobody closes
example: A dependency has already missed its date and is still labeled a risk.
out: A log that reclassifies it as an issue, names the owner, and shows the delivery impact.
related: risk-register; status-report

status-report | Status Report | status report
triggers: status report; project status; weekly status; steerco update
job: Write a status report that leads with the decision needed and the variance from plan.
artifact: status report
inputs: Plan versus actual; Decisions needed; Risks that changed; The audience
steps: Lead with the period, the overall status, and the decision needed. || Define the status rule they use. If they have none, propose one and label it a proposal. || Report variance in milestone, scope, or cost using their facts. || Separate a new risk from an issue. || Ask for the decision in a sentence the sponsor can answer. || Do not turn a late milestone green because the team worked hard.
anti: A green status on a missed milestone; Activity with no variance; A buried ask
example: A report lists many completed tasks while the customer milestone slipped two weeks.
out: A report that marks the slip, leads with the needed decision, and refuses effort as a substitute for status.
related: stakeholder-update; raid-log

stakeholder-update | Stakeholder Update | stakeholder update
job: Draft a stakeholder update that tells each audience what changed for them and what you need.
triggers: stakeholder update; project update email; sponsor update; client status note
inputs: What changed; Who is affected; What you need from them; What must not be overclaimed
steps: Segment the update if audiences need different actions. || Lead with the change, not the backstory. || State what you need and by when. || Include a delay or a cut if one exists. Do not imply you are on track. || Keep promises limited to decisions already made. || Offer a path for questions.
anti: A single vague update for audiences with different decisions; Hiding a delay; A promise not yet made
example: A client update draft says the launch is on track after scope was cut.
out: An update that states the cut and asks the client to confirm the reduced scope.
related: status-report; internal-comms-plan

scope-change-control | Scope Change Control | change request
job: Write a scope change so the sponsor sees the trade before the team absorbs it silently.
triggers: scope change; change request; gold plating; can we add this
inputs: The requested change; The current baseline; The impact on date, cost, or scope; The decider
steps: Restate the request and who asked. || Show the impact on the binding constraint. || Offer options: add time, add cost, or remove something else. || Recommend one option. Silent absorption is not an option to hide. || Name the decider. The delivery team does not accept scope by being polite. || Record the decision so the baseline stays honest.
anti: Absorbing scope with no record; A change with no impact; The team acting as the decider by default
example: A stakeholder adds a report and says it is tiny, with no estimate.
out: A change request that refuses the silent add and offers a trade against the baseline.
related: project-charter; sprint-plan

retrospective | Retrospective | retrospective
job: Run a retrospective that produces one system change, not a pile of feelings and no owner.
triggers: retrospective; retro; iteration review of process; what should we change
inputs: What happened in the period; What the team already tried; The metric or pain; Time available
steps: Open with the sprint goal or project outcome, so the retro is about the work. || Collect observations, not character judgments. || Cluster and pick one change the team can finish next cycle. || Write the change as an experiment with a check. || Assign an owner. || Park the rest. A retro with ten actions will repeat itself.
anti: A blame round; Ten actions; No check on the chosen change
example: A retro produces a list of twelve improvements every sprint and none are present the next week.
out: One owned experiment and an explicit parking of the other eleven.
related: continuous-improvement; lessons-learned

milestone-plan | Milestone Plan | milestone plan
job: Build a milestone plan from dependencies and evidence of done, not from evenly spaced dates.
triggers: milestone plan; project timeline; phase plan; delivery plan
inputs: The outcome; Dependencies; Real constraints on dates; What done means for each milestone
steps: Define done for each milestone as evidence, not as a meeting. || Sequence from dependencies. Do not spray dates evenly unless the work is actually even. || Put external dependencies on the plan with owners. || Include a buffer only if the user accepts one, and label it. || Mark any date that is a wish rather than a commitment. || Identify the milestone that will slip first if the top risk hits.
anti: Evenly spaced dates with no dependencies; A milestone that is only a meeting; Wish dates labeled as commitments
example: A plan shows design, build, and test as three equal months with no dependency on a vendor.
out: A plan that places the vendor dependency, defines evidence of done, and labels uncommitted dates.
related: project-charter; dependency-map

risk-register | Risk Register | risk register
job: Write a risk register with a few real risks, owners, and responses, not a copied list of generic fears.
triggers: risk register; project risks; log a risk; risk review
inputs: The risks the team can describe; Likelihood and impact in their scale; Current responses; Owners
steps: Write risks as events that could happen, with a cause they believe. || Score only on their scale. If they have no scale, use a simple high-medium-low and label it. || Prefer a response that reduces the risk over a response that only watches it, when they can act. || Give each open risk an owner and a review date. || Close risks that have passed or been accepted. || Do not add generic risks like 'resource risk' with no scenario.
anti: Generic risks with no scenario; A register with no responses; Scores with no scale
example: A register contains 'resources' and 'communication' and nothing a sponsor can act on.
out: A shorter register of specific events, each with an owner and a response.
related: raid-log; risk-assessment

lessons-learned | Lessons Learned | lessons note
job: Capture lessons that change a template or a checklist, not lessons that only blame a completed project.
triggers: lessons learned; after action review; project lessons; retrospective of a project
inputs: What surprised the team; Decisions that aged badly; Evidence; The template or checklist to change
steps: Describe the surprise as a fact. || Ask what the plan assumed that turned out false. || Write the lesson as a change to a checklist, estimate, or template. || Assign someone to make that change. A lesson with no template change will be repeated. || Keep personalities out. || Limit the note to a few lessons the next project will actually use.
anti: A blame narrative; Lessons with no template change; A novel nobody will read
example: A project learned that vendor review takes a month, and the next template still assumes a week.
out: A lesson that changes the template's vendor-review duration, with an owner for the edit.
related: retrospective; project-closeout

steering-committee-pack | Steering Committee Pack | steering pack
job: Prepare a steering pack that asks for decisions and shows exceptions, in a few pages.
triggers: steering committee; steerco pack; project board pack; governance pack
inputs: Decisions required; Exception status; Options; Pre-read length they will tolerate
steps: Open with the decisions and the recommendation. || Show only exceptions against the charter baseline. || For each decision, give options and a recommendation. || Put detail in an appendix the pack points to. || Note decisions the committee made last time and whether they landed. || Do not bring a decision the sponsor already delegated unless the delegation failed.
anti: A steerco that is a status tour; No recommendation; Ignoring last meeting's actions
example: A 40-page pack buries a request for more budget on page 31.
out: A short pack that leads with the budget decision, the options, and the recommendation.
related: board-memo-writer; status-report

definition-of-done | Definition of Done | definition of done
job: Write a definition of done that a team can apply to a backlog item without a debate each time.
triggers: definition of done; DoD; when is it done; acceptance versus done
inputs: The work type; Quality bars they already require; Review steps; Exceptions
steps: List the checks that apply to this work type: tested, reviewed, documented, monitored, as they actually require. || Separate acceptance criteria, which are specific to a story, from done, which is the team's bar. || Cut checks the team does not perform. A fictional done definition will be ignored. || Say who confirms each check. || Note exceptions, such as a spike, so they are explicit. || Review the definition when it causes repeated arguments.
anti: A done definition nobody follows; Mixing story acceptance into the team bar; A check with no owner
example: The definition requires a help article, but nobody has written one in six months.
out: A definition that either restores the article check with an owner or removes it until the team means it.
related: sprint-plan; release-checklist

project-closeout | Project Closeout | closeout note
job: Close a project by confirming outcomes, handing over operations, and releasing the team.
triggers: project closeout; project closure; handover to operations; end a project
inputs: The charter outcome; What was delivered; Open issues; The operational owner
steps: Compare delivery to the charter outcome. Partial delivery is labeled partial. || List open issues and who owns them after close. || Hand over runbooks, access, and support paths. Do not share passwords in the closeout note. || Release people and budget explicitly so the project does not linger. || Record a few lessons that change a template. || Thank-you notes are optional. A fake success statement is not.
anti: Closing with open issues and no owner; A success claim that ignores the charter; Passwords in the note
example: A project is declared done while operations does not know how to support the new workflow.
out: A closeout that blocks full closure until the operational owner and open issues are named.
related: lessons-learned; sop-writer

dependency-map | Dependency Map | dependency map
job: Map delivery dependencies so external waits have owners and dates, not just arrows.
triggers: dependency map; cross-team dependencies; who are we waiting on; dependency review
inputs: The work packages; External teams or vendors; Dates they have given; The consequence of a slip
steps: List dependencies that can slip the outcome. Internal niceties stay off the map. || Each dependency needs a giver, a receiver, a date, and evidence of done. || Mark dates that were not confirmed. || Show the consequence of the top slip. || Escalate unowned dependencies. An arrow is not an owner. || Review the map at the operating cadence, not only when it is already late.
anti: Unowned arrows; Unconfirmed dates drawn as promises; A map that includes every minor task
example: A Gantt chart shows a vendor delivery with no named vendor owner.
out: A map that marks the date unconfirmed and assigns an internal owner to chase it.
related: milestone-plan; raid-log
"""
))
