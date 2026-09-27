from load_cards import parse_cards

def pack(domain, text):
    return {"domain": domain, "skills": parse_cards(text)}

PACKS = [pack(
    {
        "id": "engineering",
        "title": "Engineering",
        "summary": "Design, review, reliability, and delivery practices for software teams. Defensive and repository-honest.",
        "keywords": ["engineering", "architecture", "review", "reliability", "delivery"],
    },
    r'''
== technical-design-doc | Technical Design Doc ==
job: Write a technical design that states the problem, the constraints, the chosen approach, and the rejected alternative.
artifact: technical design doc
triggers:
  - technical design
  - design doc
  - system design writeup
  - engineering design
inputs:
  - The problem and users
  - Constraints: scale, security, deadline, existing systems
  - The proposed approach
  - Alternatives considered
steps:
  - Problem: What must change for the user or operator, and why now.
  - Context: The current system only as far as the decision needs. Do not invent architecture that is not in the repo or the user's description.
  - Decision: The approach, the tradeoff, and one rejected alternative. A design with no alternative is a preference.
  - Interfaces: Data, APIs, and failure behavior. Include the unhappy path.
  - Risks: Migration, security, and operability. Security risks get a defensive control, not an exploit note.
  - Rollout: How it ships and how it rolls back. No design is done without a rollback story.
anti:
  - A design that invents the current system.
  - No rejected alternative.
  - Security described as 'we will add it later' with no owner.
example: An engineer proposes a new service but has not said what happens when the dependency is down.
example_out: A design doc with the failure behavior, one rejected alternative, and a rollback path.
related:
  - architecture-decision-record
  - threat-model-lite

== code-review-standard | Code Review Standard ==
job: Review a change for correctness, risk, and clarity, and write comments a teammate can act on.
artifact: code review
triggers:
  - code review
  - review this PR
  - pull request review
  - review comments
inputs:
  - The change and its stated intent
  - Tests included or missing
  - Risky areas: data, auth, migrations
  - Team conventions the user pointed to
steps:
  - Intent: Restate what the change is for. If the description is empty, ask for it before nitpicking style.
  - Correctness: Walk the main path and the failure path. Point to the line and the concrete failure.
  - Risk: Call out auth, data loss, migrations, and secrets. Do not request a bypass of a security control.
  - Tests: Name the missing test that would have caught the bug you see. Do not demand tests for their own sake with no risk.
  - Comments: Specific, kind, and ranked. Blocking issues are separate from nits.
  - Scope: A drive-by rewrite is a suggestion, not a block, unless the change is unsafe.
anti:
  - Style nits before understanding intent.
  - Approving a migration with no rollback note.
  - Asking the author to disable a security check to get the diff smaller.
example: A PR changes an authorization check and has no test for the denied path.
example_out: A review that blocks on the missing denied-path test and does not suggest skipping the check.
related:
  - pr-description
  - secure-code-review

== incident-postmortem | Incident Postmortem ==
job: Write a blameless postmortem that records the timeline, the impact, and the corrective actions that change a system.
artifact: postmortem
triggers:
  - postmortem
  - incident review
  - writeup of an outage
  - blameless review
inputs:
  - Timeline of facts
  - User impact
  - What detection showed
  - Actions already taken
steps:
  - Facts: A timeline with times and sources. Unknowns stay unknown. Do not invent a root cause to close the doc.
  - Impact: Who was affected and how, using the user's data. No inflated or minimized impact.
  - Contributing factors: System and process, not a villain. Human error is a prompt to ask why the system allowed it.
  - Detection: How it was found, and how it could be found sooner without a surveillance program on people.
  - Actions: A few actions with owners that change code, config, or process. A lesson with no owner is a wish.
  - Follow-up: A date to check that actions landed. No action, no closure.
anti:
  - A blame essay.
  - An invented root cause.
  - Twenty actions and no owners.
example: A draft postmortem says the outage happened because 'Alex was careless'.
example_out: A rewrite that replaces the blame line with the missing guardrail and one owned system fix.
related:
  - oncall-handoff
  - incident-response-coord

== oncall-handoff | On-Call Handoff ==
job: Write an on-call handoff that tells the next person what is on fire, what is quiet, and how to escalate.
artifact: on-call handoff
triggers:
  - oncall handoff
  - handoff notes
  - pager handoff
  - shift handoff engineering
inputs:
  - Open incidents
  - Fragile systems
  - Recent changes
  - Escalation path
steps:
  - Open items: What is paging or degraded, the current theory, and the next check. Theories are labeled.
  - Recent changes: Deploys or migrations the next person should know about, from the user's list.
  - Fragile spots: Known risks for this shift, with the runbook link if one exists. Do not invent a runbook.
  - Escalation: Who to wake and for what. A handoff with no escalation path is incomplete.
  - Noise: Alerts that are known noise, so the next person does not chase them blind. Do not tell them to ignore a security alert without an owner.
  - Tone: Short and operational. No heroics required.
anti:
  - A handoff that says 'all quiet' when an incident is open.
  - Invented runbook links.
  - Telling the next person to silence a security page with no owner.
example: The outgoing engineer writes 'should be fine' after a migration that has not been verified.
example_out: A handoff that lists the unverified migration, the check to run, and the escalation owner.
related:
  - runbook-writer
  - incident-postmortem

== api-design-review | API Design Review ==
job: Review an API for consistency, failure behavior, and compatibility, without turning the review into a style hobby.
artifact: API review
triggers:
  - API review
  - API design
  - endpoint review
  - breaking change review
inputs:
  - The proposed contract
  - Consumers
  - Compatibility promises
  - Auth model they use
steps:
  - Consumer job: What the caller is trying to do. Endpoints that do not serve a job are a finding.
  - Contract: Names, types, and error shapes. Inconsistent errors are a finding if their standard exists.
  - Failure: What the client should do on timeout, conflict, and unauthorized. Silence is a gap.
  - Compatibility: What breaks existing callers. A breaking change needs a version or a migration note.
  - Auth: Which identity is required. Do not suggest making an endpoint public to simplify a client.
  - Idempotency: Where retries could double-charge or double-create, ask for an idempotency story.
anti:
  - A public endpoint suggested for convenience.
  - A breaking change with no migration.
  - No error behavior.
example: A new billing endpoint has no idempotency key and retries would create a second charge.
example_out: A review that blocks on the double-charge retry and refuses any suggestion to skip authentication.
related:
  - technical-design-doc
  - secure-code-review

== database-change-review | Database Change Review ==
job: Review a schema or data change for safety, rollback, and lock risk before it reaches production.
artifact: database change review
triggers:
  - schema review
  - migration review
  - database change
  - backfill review
inputs:
  - The change
  - Table size and traffic if known
  - Rollback idea
  - Data correctness risk
steps:
  - Intent: What user or reporting problem the change serves.
  - Safety: Locks, rewrites, and nullability. If size is unknown, say the risk is unknown rather than approving.
  - Backfill: How existing rows become valid. A constraint added before a backfill is a finding.
  - Rollback: How to get back, or an explicit statement that the change is forward-only and who accepts that.
  - Observability: What to watch during the migration.
  - Secrets: No production connection strings in the review notes. Ask for redacted plans.
anti:
  - Approving a lock-heavy migration with unknown table size.
  - A constraint before the backfill.
  - Pasting production credentials into the plan.
example: A migration adds a NOT NULL column with a default on a table of unknown size and has no rollback.
example_out: A review that marks risk unknown, requires a batched plan, and rejects credential pasting.
related:
  - data-migration-plan
  - release-checklist

== test-strategy | Test Strategy ==
job: Choose a test strategy for a change that matches risk, instead of demanding every kind of test.
artifact: test strategy note
triggers:
  - test strategy
  - what tests do we need
  - test plan
  - coverage argument
inputs:
  - The change and its risk
  - Existing tests
  - What has broken before
  - Time available
steps:
  - Risk: Where a bug would hurt users, money, or data. Tests follow risk.
  - Layer: Unit, integration, or end-to-end, chosen for the risk. Do not demand an end-to-end test for a pure function by reflex.
  - Gaps: The specific case that is untested. Name it.
  - Flakes: Do not add a known-flaky test as the only safety net. Say so.
  - Non-goals: What you will not automate now, and why.
  - Done: The test list that would make the change reviewable.
anti:
  - Coverage percentage as the goal.
  - A flaky end-to-end test as the only check.
  - No test on a payments or auth change.
example: A team argues about coverage percent while a refund path has no test.
example_out: A strategy that prioritizes the refund path and treats the coverage number as secondary.
related:
  - code-review-standard
  - definition-of-done

== ci-cd-review | CI/CD Review ==
job: Review a delivery pipeline for repeatability, secrets handling, and a safe production gate.
artifact: pipeline review
triggers:
  - CI review
  - CD pipeline
  - deployment pipeline review
  - GitHub Actions review
inputs:
  - The pipeline description or config the user shared
  - Environments
  - Who can deploy
  - Secret handling as described
steps:
  - Repeatability: Can a new teammate see what runs on a change. Hidden manual steps are a finding.
  - Gates: What must pass before production. A pipeline that deploys on red tests is a finding.
  - Secrets: Secrets come from a named store, not from the repo. Do not ask the user to paste live secrets into the chat.
  - Environments: What differs between staging and production, as they described it. Do not assume parity.
  - Rollback: How a bad deploy is undone, and who can do it.
  - Access: Who can change the pipeline. A world-writable deploy script is a finding.
anti:
  - Asking for live secrets.
  - Approving a deploy-on-red pipeline.
  - No rollback.
example: A pipeline file contains a copied cloud key and deploys even when tests fail.
example_out: A review that requires the key to be removed and rotated, and blocks deploy-on-red. Do not repeat the key.
related:
  - secrets-handling
  - release-checklist

== observability-plan | Observability Plan ==
job: Specify the logs, metrics, and traces a service needs to debug a user-facing failure.
artifact: observability plan
triggers:
  - observability plan
  - what should we log
  - metrics and traces
  - instrumentation plan
inputs:
  - The user-facing failure you must detect
  - Existing signals
  - Cardinality and privacy limits
  - Who is on call
steps:
  - Question: The production question the signal must answer. Signals without a question are noise.
  - Golden signals: Latency, errors, traffic, and saturation only where they match the service. Do not dump a template.
  - Logs: Structured fields that help debug, excluding secrets, tokens, and full payment data.
  - Traces: Where a trace would beat another log line, if they already use tracing. Do not mandate a vendor.
  - Alerts: Page only on user pain or imminent user pain. A page on every warning trains people to ignore pages.
  - Ownership: Who responds, and where the runbook will live.
anti:
  - Logging secrets or card numbers.
  - Paging on every warning.
  - A vendor mandate disguised as a plan.
example: A plan logs the full Authorization header to 'make debugging easier'.
example_out: A plan that forbids that header, specifies a request id, and pages only on user-facing errors.
related:
  - logging-and-detection
  - slo-error-budget

== slo-error-budget | SLO and Error Budget ==
job: Draft an SLO from a user journey and explain how the error budget changes release behavior.
artifact: SLO draft
triggers:
  - SLO
  - error budget
  - service level objective
  - reliability target
inputs:
  - The user journey
  - Current performance if known
  - The pain that matters
  - Release cadence
steps:
  - Journey: The user action the SLO protects. Internal CPU is not an SLO by default.
  - Indicator: A measurable signal they can actually collect. If they cannot collect it, the first task is instrumentation.
  - Target: Use their history or mark the target as a proposal. Do not invent a 99.99 because it sounds serious.
  - Budget: What the target implies for unavailability in the window, shown as arithmetic from their numbers.
  - Policy: What the team does when the budget is gone: slow releases, fix reliability, or accept the burn explicitly.
  - Exclusions: Maintenance windows only if the user already has that policy. Do not hide outages in exclusions.
anti:
  - A 99.99 target with no baseline.
  - An SLO on a vanity metric.
  - No policy when the budget burns.
example: A team copies a 99.99 SLO from a blog and has no latency metric.
example_out: A draft that refuses the copied target, names the missing metric, and proposes a journey-based indicator.
related:
  - observability-plan
  - release-checklist

== refactor-plan | Refactor Plan ==
job: Plan a refactor that improves a named risk without pretending a rewrite is free.
artifact: refactor plan
triggers:
  - refactor plan
  - rewrite versus refactor
  - pay down this code
  - code health plan
inputs:
  - The pain: bugs, change fear, or incidents
  - The boundaries of the code
  - Tests that exist
  - Deadline pressure
steps:
  - Pain: The user-visible or developer-visible pain. 'It is ugly' is not enough unless change is slow or risky because of it.
  - Characterize: What the code does, from tests or the user's description. Do not refactor behavior you cannot name.
  - Safety: Tests or characterization checks to add first. A refactor without a safety net is a rewrite in the dark.
  - Slices: Small steps that keep the system shipping. A big-bang rewrite needs a written reason and a rollback.
  - Non-goals: Behavior you will not change. Call out any behavior change as a product decision.
  - Stop: When the pain is reduced enough to return to product work.
anti:
  - A rewrite because the code is old.
  - Refactoring with no tests and no characterization.
  - Sneaking behavior changes into a refactor.
example: An engineer wants six weeks to rewrite a billing module before adding a small fee change.
example_out: A plan that adds characterization tests and a smaller slice that unblocks the fee change, and treats a full rewrite as a separate decision.
related:
  - tech-debt-triage
  - test-strategy

== dependency-upgrade | Dependency Upgrade ==
job: Plan a dependency upgrade around risk, changelog, and rollback, not around a version number badge.
artifact: upgrade plan
triggers:
  - dependency upgrade
  - bump this library
  - framework upgrade
  - renovate plan
inputs:
  - The dependency and versions
  - Why the upgrade is happening
  - Breaking changes the user found
  - How the app is tested
steps:
  - Reason: Security fix, bug, or support window, as the user stated. Do not invent a CVE.
  - Breaking changes: List the ones they found in notes or a changelog they pasted. If none were read, the plan starts by reading them.
  - Blast radius: Which parts of the product use it.
  - Test: The regression checks that matter for that blast radius.
  - Rollback: How to return to the old version, and what data changes would make rollback hard.
  - Secrets and scripts: Do not run untrusted upgrade scripts blindly. Read install scripts before recommending them. No curl-pipe-shell.
anti:
  - Inventing a CVE.
  - Recommending curl piped to a shell.
  - An upgrade with no rollback story.
example: A bot opened a major upgrade and nobody has read the changelog.
example_out: A plan that blocks the merge until breaking changes are read and a rollback is named.
related:
  - sbom-and-supply-chain
  - test-strategy

== feature-flag-rollout | Feature Flag Rollout ==
job: Plan a feature-flag rollout with an audience, a kill switch, and a cleanup date.
artifact: rollout plan
triggers:
  - feature flag
  - rollout plan
  - gradual release
  - kill switch
inputs:
  - The change
  - The first audience
  - How to disable it
  - What you will watch
steps:
  - Audience: Who sees it first, and why. A 100 percent launch is a choice, not the default, when risk is unclear.
  - Kill switch: Who can turn it off, and how long that takes. A flag with no kill path is a config liability.
  - Watch: The user-facing signal that means stop. Use their metrics. Do not invent a dashboard.
  - Stages: The next audience and the evidence required to expand.
  - Cleanup: The date the flag is removed if the launch succeeds or fails. Permanent flags are debt.
  - Access: Do not put the flag service credentials in the plan.
anti:
  - A flag nobody can turn off.
  - No cleanup date.
  - Expanding while the watch signal is red.
example: A team wants to enable a payments change for everyone and has no way to disable it without a deploy.
example_out: A rollout that starts with a small audience and names a disable path that does not require a heroic deploy.
related:
  - release-checklist
  - observability-plan

== architecture-decision-record | Architecture Decision Record ==
job: Record an architecture decision with context, the decision, and the consequences, in a page.
artifact: architecture decision record
triggers:
  - ADR
  - architecture decision record
  - record this technical decision
  - why did we choose this design
inputs:
  - The decision
  - The context
  - Alternatives
  - Consequences
steps:
  - Title and status: Proposed, accepted, or superseded. Do not mark accepted if the user has not accepted it.
  - Context: The forces, from their system. No fictional scale numbers.
  - Decision: One paragraph. What you will do.
  - Alternatives: At least one rejected option and why.
  - Consequences: What becomes easier, what becomes harder, and the security or operability effect.
  - Revisit: What would supersede this record.
anti:
  - An ADR that is a tutorial.
  - No alternative.
  - Marking a draft as accepted.
example: A team chose a queue technology in a meeting and nobody wrote why the simpler option lost.
example_out: A one-page ADR with the rejected option, consequences, and status left as proposed until they accept it.
related:
  - decision-log
  - technical-design-doc

== threat-model-lite | Lightweight Threat Model ==
job: Sketch a defensive threat model for a feature: assets, actors, abuses, and controls. No exploit steps.
artifact: threat model note
triggers:
  - threat model
  - what could go wrong security
  - abuse cases
  - security design review
inputs:
  - The feature and its assets
  - Actors
  - Existing controls
  - Data sensitivity they described
steps:
  - Assets: What must be protected: credentials, personal data, money, or availability, as they described.
  - Actors: Users, admins, and unauthenticated callers. Do not build a persona of a criminal how-to.
  - Abuses: What could go wrong in plain language, such as unauthorized access or tampering. No payloads, bypasses, or step-by-step intrusion.
  - Controls: Preventive and detective controls they can implement. Prefer known controls over novel tricks.
  - Gaps: The abuse with no control. That is the work list.
  - Hand-off: Residual risk is accepted by a named owner or sent to the security skill for review. This note is not a penetration test.
anti:
  - Exploit steps or payloads.
  - A model with no assets.
  - Claiming the feature is secure because the note exists.
example: A file-sharing feature has no answer for who can access a link.
example_out: A note that lists unauthorized access as a gap, recommends an access control and audit event, and includes no exploit procedure.
related:
  - security-requirements
  - secure-code-review

== performance-budget | Performance Budget ==
job: Set a performance budget for a user journey and a plan for what happens when a change blows it.
artifact: performance budget
triggers:
  - performance budget
  - latency budget
  - page weight
  - performance regression
inputs:
  - The user journey
  - Current measurements if any
  - The pain users feel
  - The constraint: mobile, warehouse network, or checkout
steps:
  - Journey: The page or action that matters. A budget on an unused admin page is optional.
  - Metric: A user-centered metric they can measure. If they have no measurement, the first step is to measure, not to invent a number.
  - Budget: Set the budget from their baseline or a stated user need. Label proposals as proposals.
  - Guard: Where in CI or review the budget is checked. A budget nobody checks is a slide.
  - Blow-up policy: Who may exceed it, and what must be fixed first.
  - No theater: Do not recommend a micro-optimization before the measurement exists.
anti:
  - An invented millisecond target presented as fact.
  - A budget with no guard.
  - Optimizing before measuring.
example: A team wants a 100 millisecond budget because a talk recommended it, and they have never measured the checkout.
example_out: A plan that measures checkout first and treats 100 milliseconds as an unadopted proposal.
related:
  - observability-plan
  - slo-error-budget

== migration-plan | Migration Plan ==
job: Plan a migration from one system or contract to another with a dual-run, a cutover, and a backout.
artifact: migration plan
triggers:
  - migration plan
  - cutover plan
  - move off this system
  - contract migration
inputs:
  - Source and target
  - Data or traffic involved
  - Downtime tolerance
  - Verification method
steps:
  - Inventory: What moves, and what must not move, from their description.
  - Dual run: How both sides can be compared before cutover. If comparison is impossible, say the risk is higher.
  - Cutover: The steps, the owner, and the go/no-go check.
  - Backout: The point of no return. Before it, how to return. After it, who accepts forward-only.
  - Communication: Who is told, including support. No customer claim you cannot honor.
  - Verification: The check that the new path is correct, using their data, not a hope.
anti:
  - A cutover with no backout and no accepted point of no return.
  - Inventing record counts.
  - A migration communicated as zero-risk.
example: A team plans to switch billing systems over a weekend with no way to compare invoices.
example_out: A plan that adds a comparison phase and names the point of no return before any weekend cutover is approved.
related:
  - data-migration-plan
  - database-change-review

== runbook-writer | Runbook Writer ==
job: Write a runbook a tired on-call engineer can follow, with checks, stops, and escalation.
artifact: runbook
triggers:
  - write a runbook
  - ops procedure
  - on-call runbook
  - support procedure engineering
inputs:
  - The alert or symptom
  - The checks that are safe
  - The fix that is allowed
  - Who to escalate to
steps:
  - Symptom: What the human sees, in the alert's language.
  - Impact: How to tell whether users are hurt, using signals they have.
  - Checks: Safe, read-only checks first. Do not include destructive commands as the first step.
  - Mitigation: The allowed mitigation, with the stop condition. No improvised production surgery.
  - Escalation: When to stop and call the owner.
  - After: What to record for the postmortem. Keep secrets out of the runbook.
anti:
  - Destructive commands with no stop condition.
  - A runbook that requires hero knowledge.
  - Secrets embedded in the steps.
example: A draft runbook starts by deleting a production table if an alert fires.
example_out: A runbook that starts with read-only checks, removes the destructive first step, and escalates before any data deletion.
related:
  - oncall-handoff
  - incident-postmortem

== tech-debt-triage | Tech Debt Triage ==
job: Triage tech debt by the risk and delay it causes, and cut the list to what the team will actually pay down.
artifact: tech debt triage
triggers:
  - tech debt
  - debt triage
  - engineering backlog cleanup
  - what debt matters
inputs:
  - The debt items
  - The incidents or delays they cause
  - Team capacity
  - Upcoming product bets
steps:
  - Evidence: Each item needs a cost: incidents, slow changes, or a named risk. Vague dislike is parked.
  - Rank: User risk first, then change delay, then cosmetics.
  - Cut: Choose a few items that fit the capacity. A debt program that consumes the quarter needs an explicit product trade.
  - Shape: Paydown as slices inside product work where possible.
  - Owner: One owner per chosen item.
  - Review: A date to see if the cost actually dropped.
anti:
  - A debt list with no capacity cut.
  - Ranking by disgust.
  - A rewrite program with no product trade made explicit.
example: A team has 60 debt tickets and wants them all in next sprint alongside a launch.
example_out: A triage that keeps the debt tied to launch risk, parks the rest, and makes the capacity trade explicit.
related:
  - refactor-plan
  - portfolio-prioritization

== release-checklist | Release Checklist ==
job: Run a release checklist that confirms scope, migrations, monitoring, and rollback before tagging.
artifact: release checklist
triggers:
  - release checklist
  - ship checklist
  - release review
  - go no-go release
inputs:
  - The intended scope
  - Migrations
  - Monitoring
  - Rollback
steps:
  - Scope: What is in the release, matched to what was tested. Surprise commits are a stop.
  - Migrations: Order, backup or rollback, and the owner watching them.
  - Config and flags: What must be set in production. Do not include secret values. Name the keys only.
  - Monitoring: The dashboard or alert the owner will watch for the first hour.
  - Rollback: The command or flag path, already known, not invented during the incident.
  - Decision: Ship or hold, with the hold reason written.
anti:
  - Secret values in the checklist.
  - A ship decision with no rollback.
  - Scope nobody tested.
example: A release includes a migration that the on-call has not seen, and the checklist says LGTM.
example_out: A hold until the migration owner is named and the rollback is written, with no secret values added.
related:
  - launch-readiness
  - feature-flag-rollout

== debugging-protocol | Debugging Protocol ==
job: Debug a defect by stating the symptom, the hypothesis, and the next observation, instead of changing five things at once.
artifact: debugging note
triggers:
  - debug this
  - debugging help
  - why is this failing
  - defect investigation
inputs:
  - The symptom
  - What changed recently
  - Evidence already collected
  - The environment
steps:
  - Symptom: What the user or system does, and what was expected. Include the error text they provided. Do not invent logs.
  - Boundary: Where it last worked. Version, user, or data slice.
  - Hypothesis: One hypothesis that predicts a new observation.
  - Observation: The safest check that would confirm or kill it. Read-only before write actions.
  - Change: Only after the observation. One change at a time.
  - Record: What you learned, so the next person does not repeat the loop. No exploit development and no bypass of auth to 'make it easier'.
anti:
  - Changing five things at once.
  - Inventing log lines.
  - Disabling auth to debug.
example: A bug appears only for one customer, and the draft plan changes three services before reading that customer's error.
example_out: A note with one hypothesis, a read-only check, and a ban on disabling auth as a debugging shortcut.
related:
  - incident-postmortem
  - code-review-standard

== pr-description | Pull Request Description ==
job: Write a pull request description that explains the why, the risk, and how to test.
artifact: pull request description
triggers:
  - PR description
  - pull request text
  - write the PR
  - changelog for a change
inputs:
  - What changed
  - Why
  - How to test
  - Risks and rollout
steps:
  - Why: The user or operator problem, not a restatement of the diff.
  - What: The approach in a few lines. Point to the design if there is one.
  - Test: The steps a reviewer can run, and the cases you did not test.
  - Risk: Migrations, flags, and user-visible changes.
  - Screens or samples: Only if the user supplied them. Do not invent output.
  - Rollback: One line on how to undo the change.
anti:
  - A description that says 'fix bug'.
  - Claiming tests you did not run.
  - Hidden migration risk.
example: A PR titled 'updates' changes a payment calculation and the description is empty.
example_out: A description that states the payment behavior, the missing test if none was run, and the rollback.
related:
  - code-review-standard
  - release-checklist

== estimation-review | Estimation Review ==
job: Review an engineering estimate by exposing assumptions, slices, and the unknown, not by demanding false precision.
artifact: estimate review
triggers:
  - engineering estimate
  - story points argument
  - how long will this take
  - estimation review
inputs:
  - The work as scoped
  - Similar work they have done
  - Unknowns
  - Who is doing it
steps:
  - Scope: Restate the slice. An estimate of an unbounded idea is not an estimate. Cut scope first.
  - Assumptions: List the assumptions. The estimate is valid only while they hold.
  - Reference: Compare with a past piece of work they name. Do not invent a velocity number.
  - Unknowns: The spike that would shrink the range. Recommend a range, not a fake single day.
  - Capacity: Calendar time is not effort time. Include review and release if they matter.
  - Update: When the estimate should be replaced, after the spike or the first slice.
anti:
  - A single-day estimate for an unbounded project.
  - Invented velocity.
  - Hiding unknowns to look confident.
example: A stakeholder wants a date for a rewrite with no scope and no prior art.
example_out: A review that refuses the date, proposes a scoped spike, and offers a range only after that spike.
related:
  - sprint-plan
  - refactor-plan

== platform-readiness | Platform Readiness ==
job: Review whether a platform or internal tool is ready for other teams to depend on.
artifact: platform readiness review
triggers:
  - platform readiness
  - internal platform review
  - is this ready for other teams
  - paved road review
inputs:
  - The users inside the company
  - The promised interface
  - Support model
  - Docs and SLOs they claim
steps:
  - User: The internal team and the job they will do on the platform.
  - Interface: The stable contract. If every consumer forks the internals, it is not ready.
  - Operability: On-call, migration path, and a stated limit. Do not invent an SLO.
  - Docs: A new team can complete the golden path from the docs the user has. Gaps are the finding.
  - Support: Who answers in the first month, and what is not supported.
  - Adoption: One team first, then a wider invite. A mandate with no golden path will be bypassed.
anti:
  - A company-wide mandate with no docs.
  - An invented uptime promise.
  - No owner for questions.
example: A platform team wants every service to migrate next month, and the quickstart is a stub.
example_out: A review that blocks the mandate, names the quickstart gap, and recommends one adopting team.
related:
  - technical-design-doc
  - documentation-as-code

== data-migration-plan | Data Migration Plan ==
job: Plan a data migration with reconciliation counts, a freeze or dual-write choice, and a stop condition.
artifact: data migration plan
triggers:
  - data migration
  - backfill plan
  - move this table
  - reconcile a migration
inputs:
  - Source and target
  - Volume if known
  - Correctness rules
  - Downtime tolerance
steps:
  - Rules: What makes a row correct in the target. Write the rule before writing the job.
  - Method: Dual-write, backfill, or freeze, chosen from their tolerance. Do not pick a method they cannot operate.
  - Reconciliation: Counts and checksums or samples they can actually run. A migration without reconciliation is a guess.
  - Stop: The mismatch that halts the job.
  - Privacy: Do not copy data into a less protected place for convenience. No exports of secrets into tickets.
  - Cutover: Who signs that the reconciliation passed.
anti:
  - A migration with no reconciliation.
  - Copying sensitive data into a ticket.
  - A method the team cannot operate.
example: A script copies customer records to a new store and the plan says 'check a few rows'.
example_out: A plan with a written correctness rule, a stop condition, and reconciliation that is more than a glance.
related:
  - migration-plan
  - database-change-review

== accessibility-engineering | Accessibility Engineering ==
job: Turn an accessibility barrier into an engineering fix with a test, without claiming a conformance certificate.
artifact: accessibility engineering note
triggers:
  - accessibility bug
  - a11y fix
  - keyboard trap
  - screen reader bug
inputs:
  - The barrier
  - The user impact
  - The code or component involved
  - The team's stated target
steps:
  - Reproduce: The exact barrier, such as a keyboard trap or a missing name. Do not claim you ran an assistive technology you did not run.
  - Fix: The specific code or component change. Prefer the platform's accessible primitive over a custom widget.
  - Test: A check the team can repeat, automated where it fits and manual where it does not.
  - Regression: Where this should live so it does not return.
  - Limits: What this fix does not prove. No blanket WCAG certificate.
  - Priority: Blockers to completing a task outrank cosmetic contrast issues, unless their policy says otherwise.
anti:
  - A conformance certificate from a guess.
  - A custom widget when a native control would do.
  - Closing the bug with no regression check.
example: A modal traps keyboard focus, and the proposed fix is a README badge that says 'accessible'.
example_out: A note that specifies the focus fix and a keyboard test, and rejects the badge as proof.
related:
  - accessibility-review
  - test-strategy

== documentation-as-code | Documentation As Code ==
job: Write or repair technical docs so a new teammate can complete a task without a hallway conversation.
artifact: documentation update
triggers:
  - write docs
  - README review
  - developer documentation
  - runbook versus docs
inputs:
  - The task a new person must complete
  - The current doc
  - The commands or paths that are true
  - The owner
steps:
  - Audience and task: What the reader is trying to do. A doc with no task becomes a junk drawer.
  - Truth: Steps match the repo or the user's confirmation. Do not invent flags, paths, or environment variables.
  - Prerequisites: What must exist first, including access, without asking for secrets to be pasted into the doc.
  - Failure: The common failure and the next check.
  - Ownership: Who updates the doc when the system changes.
  - Cut: Remove stale sections rather than adding a warning on top of a wrong step.
anti:
  - Invented commands.
  - Secrets in the example env file.
  - A README that does not say how to run the project.
example: A README says 'run the script' and the script path does not exist.
example_out: A doc that either uses the real path the user confirmed or marks the step unknown, and removes the stale command.
related:
  - runbook-writer
  - platform-readiness
'''
)]
