from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "data", "title": "Data and analytics", "summary": "Metric definitions, analysis plans, and decision memos grounded in the user's data.", "keywords": ["analytics", "metrics", "sql", "experiments", "data-quality"]},
    """
metric-definition | Metric Definition | metric definition
job: Define a metric so two teams would compute the same number from the same source.
triggers: define a metric; metric definition; what does this KPI mean; single source of truth metric
inputs: The decision the metric serves; The source table or report they trust; Inclusion and exclusion rules they already use; The owner
steps: Write the decision the metric is for before naming the metric. || Define numerator, denominator, time window, and exclusions in words a new analyst can apply. || Name the source. If two reports disagree, the definition is not done until one source is chosen. || Record the known ways the metric can be gamed and add a counter-metric. || Set an owner and a change process. Silent definition changes are a finding. || If the baseline is unknown, say so. Do not invent one.
anti: A metric with no formula; Two teams using different sources without a note; An invented baseline
example: Sales and finance report different revenue for the same month and both call it bookings.
out: A definition that picks one source, writes the formula, and flags the other report as a reconciliation item.
related: data-dictionary; executive-insight

dashboard-spec | Dashboard Spec | dashboard specification
job: Specify a dashboard that answers a few decisions, with an owner and a refresh the team can trust.
triggers: dashboard spec; design a dashboard; KPI dashboard; executive dashboard
inputs: The decisions the dashboard must support; The metrics and their definitions; Who will use it and how often; Known data delays
steps: Limit the dashboard to the decisions named. A gallery of charts is a finding. || Every chart needs a question, a defined metric, and a source. || State the refresh lag. A daily decision on a monthly feed is a mismatch. || Specify filters that change a decision, not every possible slice. || Name the owner who fixes a broken number. || Include an empty-state note for when data is late, so nobody reads a blank chart as zero.
anti: A chart with no question; Hidden refresh lag; No owner for a broken tile
example: A leader wants 30 tiles on one page and cannot name the Monday decision.
out: A spec of a few decision tiles, each with a source, a lag, and an owner.
related: metric-definition; management-reporting-pack

analysis-plan | Analysis Plan | analysis plan
job: Plan an analysis so the question, the data, and the decision rule are fixed before the slicing starts.
triggers: analysis plan; data analysis request; what should we analyze; analytics brief
inputs: The decision; The data available; The comparison they care about; The deadline
steps: Restate the decision. An analysis with no decision is a tour. || Write the comparison: against what period, segment, or control. || List the data you have and the data you do not. Do not plan around a table nobody can access. || Pre-commit the cut that would change the decision. || Name biases in the sample the user described. || Set the deliverable as a memo, not a notebook dump, unless they asked for the notebook too.
anti: Slicing until a flattering story appears; Assuming a dataset you cannot see; A notebook with no decision
example: A team wants to know why conversion fell and plans to look at twelve dimensions with no primary comparison.
out: A plan with one primary comparison, the missing data called out, and a decision rule written first.
related: experiment-readout; decision-memo-from-data

experiment-readout | Experiment Readout | experiment readout
job: Read out an experiment using the pre-written decision rule, the guardrail, and the sample they actually have.
triggers: experiment readout; A/B test results; test results; did the experiment win
inputs: The pre-registered metric and rule if they have one; The results they pasted; Sample size; Guardrail results
steps: Start from the decision rule they wrote. If none exists, say the readout is exploratory. || Report the primary metric and the guardrail before secondary slices. || Do not crown a winner on a slice that was not the plan, unless you label it a hypothesis. || State whether the sample can support the decision they want. || Separate a failed experiment from a broken implementation. || Recommend ship, iterate, or stop, and say what would be fishing if you kept slicing.
anti: Moving the metric after seeing results; Ignoring a broken guardrail; Declaring a tiny sample conclusive
example: The primary metric is flat, a secondary slice looks good, and the team wants to ship.
out: A readout that refuses the secondary-slice ship, notes the flat primary metric, and labels any follow-up as a new hypothesis.
related: experiment-design; analysis-plan

data-quality-check | Data Quality Check | data quality check
job: Check a dataset or pipeline for freshness, completeness, and a tie-out before anyone presents the number.
triggers: data quality; can we trust this number; pipeline check; freshness check
inputs: The dataset and the expected grain; The freshness they expect; A tie-out target if they have one; Known upstream changes
steps: Check grain and freshness first. A stale table cannot support today's decision. || Tie a total to a source they trust. A mismatch is the finding, not a footnote. || Look for duplicates, null keys, and sudden row-count jumps using the evidence they gave. || Separate a pipeline break from a real business movement. Do not guess which without evidence. || Write the user impact: which dashboard or decision is unsafe. || Recommend a block, a caveat, or a fix, with an owner.
anti: Presenting a number that failed its tie-out; Inventing a row count; A quality check with no decision impact
example: Monday's revenue dashboard is empty and the draft note says the business had zero revenue.
out: A check that treats empty as late or broken until a tie-out says otherwise, and names the decision to pause.
related: dashboard-spec; anomaly-investigation

cohort-analysis | Cohort Analysis | cohort analysis
job: Build a cohort view that follows a defined group over time without mixing incompatible cohorts.
triggers: cohort analysis; retention cohort; cohort curve; vintage analysis
inputs: The cohort definition; The event that starts the clock; The success event; The time grain
steps: Define membership and the start event before drawing a curve. || Keep cohorts comparable. Do not mix a pricing change cohort into an older one without a label. || Use only their data. If a week is incomplete, mark it incomplete rather than as a drop. || Show the denominator. A retention rate without a cohort size is not interpretable. || Call out mix shift if they supplied the evidence. || Recommend one action or one next question. A curve alone is not a decision.
anti: An incomplete week drawn as churn; No denominator; Mixing incompatible cohorts silently
example: Last week's cohort looks like it retained worse, but the week is not over.
out: A cohort note that marks the week incomplete and refuses a churn conclusion from it.
related: funnel-analysis; saas-metrics-pack

funnel-analysis | Funnel Analysis | funnel analysis
job: Analyze a funnel with explicit step definitions and a focus on the biggest leak that the team can affect.
triggers: funnel analysis; conversion funnel; drop-off; where do users drop
inputs: The steps and their definitions; Counts they provided; How users are identified; Known tracking gaps
steps: Write the step definitions. If two steps can fire out of order, say the funnel is messy. || Compute conversion only from counts they gave. Show the arithmetic. || Find the largest loss of people, not the largest percentage on a tiny step, and say which one you are using. || Note tracking gaps before blaming the product. || Separate a new-user funnel from a returning-user funnel if they differ in the data. || Recommend one investigation or one product change to test, not five.
anti: Blaming the product when tracking is broken; A funnel with undefined steps; Invented counts
example: A funnel shows a huge drop between two events that can fire in either order.
out: A note that calls the funnel unordered, pauses the product blame, and asks for a sequenced definition.
related: cohort-analysis; event-tracking-spec

sql-review | SQL Review | SQL review
job: Review a query for correctness, grain, and safety, without running it against a database you were not given.
triggers: review this SQL; query review; is this query correct; SQL critique
inputs: The query; The intended grain and metric; The tables they say exist; Whether the query will mutate data
steps: Restate the intended grain and metric. || Check joins and filters against that intent. A fan-out that double-counts is a finding. || Flag non-deterministic filters, missing time zones, and unbounded scans if visible in the text. || If the query mutates or deletes data, require a WHERE and a stated backup. Do not suggest disabling safeguards. || Do not invent table schemas. Mark assumptions. || Recommend a tie-out query they can run, but do not ask for production credentials.
anti: Approving a double-count join; Suggesting a credential share; An unbounded delete with no predicate
example: A revenue query joins invoices to line items and sums invoice totals.
out: A review that flags the double count, asks for the grain, and does not request database passwords.
related: metric-definition; data-quality-check

data-dictionary | Data Dictionary | data dictionary entry
job: Write a data dictionary entry that tells an analyst what a field means, what it does not mean, and who owns it.
triggers: data dictionary; document this field; column definition; semantic layer entry
inputs: The field and table; The business meaning; Known null or sentinel values; The owner
steps: Name the grain of the table before defining the field. || Write the business meaning in plain language, plus a false friend it is often confused with. || Document nulls, sentinels, and units. Do not guess a unit. || State the source system if they know it. || Name an owner. An unowned field will rot. || Add an example value only if they supplied one. Do not invent customer data.
anti: A dictionary that copies the column name as the definition; Invented example customers; No owner
example: A field called status has values 1, 2, and 9, and nobody agrees what 9 means.
out: An entry that records the known values, marks 9 as unresolved, and names the owner who must decide.
related: metric-definition; event-tracking-spec

executive-insight | Executive Insight Memo | insight memo
job: Turn an analysis into a one-page insight a leader can use, with the number, the comparison, and the limit.
triggers: insight memo; executive readout; so what from the data; analytics summary
inputs: The finding; The comparison; The decision it informs; Caveats
steps: Lead with the finding and the comparison in one or two sentences. || Show only numbers they provided. Round only if you say so. || State what the finding does not prove. || Recommend one decision or one question. || Put method in a short note, not in the opening. || Do not add a market explanation you were not given.
anti: A chart dump with no sentence; Causal language the design does not support; Invented context
example: An analyst has a retention drop and wants the memo to say a competitor caused it.
out: A memo that reports the drop, refuses the competitor cause without evidence, and names the next question.
related: analysis-plan; decision-memo-from-data

anomaly-investigation | Anomaly Investigation | anomaly note
job: Investigate a metric anomaly by separating a data break from a real change before anyone acts.
triggers: anomaly; metric spiked; number looks wrong; investigate a drop
inputs: The metric and the unexpected movement; Recent pipeline or tracking changes; Business events they know about; The decision waiting on the number
steps: Confirm the movement against the definition and the source. || Check freshness, duplicates, and tracking changes before a business story. || If a business event is known, test whether its timing matches. Do not invent a campaign or outage. || Quantify who is affected using their slices, and stop if the slice is tiny. || Say whether the number is safe to use today. || Recommend a data fix or a business investigation, not both as if they were the same work.
anti: A business story for a broken pipeline; Ignoring a tracking change; Acting on a tiny slice
example: Conversion halves on the day a tracking change shipped, and marketing wants a new campaign.
out: A note that pauses the campaign idea until tracking is ruled in or out.
related: data-quality-check; funnel-analysis

segmentation-study | Segmentation Study | segmentation note
job: Segment users or customers from supplied data into groups that change an action, not into decorative clusters.
triggers: segmentation; customer segments; cluster analysis; how should we segment
inputs: The action the segment must change; Available fields; Sample limits; Segments they already use
steps: Start from the action: message, offer, or service model. Segments that do not change an action are cut. || Use fields they have. Do not require a model they cannot run. || Keep the number of segments small enough to operate. || Describe each segment with a rule a teammate can apply, not only a cluster id. || Note sample size. A segment of a handful of rows is a list, not a strategy. || Recommend one test, not an immediate company-wide rewrite of the motion.
anti: Clusters with no action; A segment too small to mean anything; Invented demographic attributes
example: A model produced eight clusters and the team cannot say what they would do differently for any of them.
out: A note that collapses to a few actionable rules and parks the rest as unusable.
related: cohort-analysis; personalization-ethics

event-tracking-spec | Event Tracking Spec | tracking spec
job: Specify product or marketing events so a later analyst can trust the trigger, the properties, and the privacy boundary.
triggers: tracking plan; event taxonomy; instrument this flow; analytics events
inputs: The question the events answer; The actions to instrument; Existing naming rules; Privacy limits
steps: Write the question first. Events without a question are rejected. || Define trigger timing precisely: on success, not on click, if success is what matters. || List properties and ban secrets, payment card data, and raw credentials. || Match their naming rules. Do not invent a parallel taxonomy. || Specify how the team will verify the event before release. || Note identity rules they already use. Do not design a covert fingerprint.
anti: Tracking secrets; A parallel naming scheme; Events with no verification step
example: A spec adds the user's national ID as a property to count button clicks.
out: A spec that removes the ID, defines the success trigger, and names the verification step.
related: product-analytics-spec; privacy-by-design

decision-memo-from-data | Decision Memo From Data | decision memo
job: Write a decision memo that uses data the user supplied and labels every non-data judgment.
triggers: decision memo; recommend from this data; data-backed decision; what should we do with these numbers
inputs: The decision; The data; The options; The constraints
steps: State the decision in one sentence. || List the data facts that bear on it, with comparisons. || List judgments separately from facts. || Compare options against the constraint they named, not against an invented benchmark. || Recommend one option and the fact that would change it. || Say what the data cannot see.
anti: A recommendation that ignores the constraint; Benchmarks from memory; Facts and judgments mixed
example: Leadership must cut one of two channels, and the data shows correlation, not incrementality.
out: A memo that recommends a reversible cut or a test, and refuses a causal claim the data cannot support.
related: executive-insight; marketing-attribution

survey-analysis | Survey Analysis | survey analysis
job: Analyze a survey without overclaiming a small or biased sample.
triggers: survey results; questionnaire analysis; NPS analysis; survey readout
inputs: The questions and results; Sample size and how people were recruited; The decision; Any open text they provided
steps: Report the sample and the recruitment bias before the score. || Do not treat a small sample as a population percentage without a caution. || Separate closed scores from themes in open text they actually pasted. || Do not invent themes. || Tie one finding to a decision or say the survey cannot support one. || Protect respondent privacy in small slices.
anti: A precise population claim from a tiny sample; Invented themes; Identifying a respondent
example: An NPS of 80 from 11 self-selected responses is about to go on a board slide as proof of love.
out: A note that blocks the board claim, states the bias, and limits the use of the score.
related: engagement-survey-readout; feedback-synthesis
"""
))

PACKS.append(pack(
    {"id": "security", "title": "Security defense", "summary": "Defensive security requirements, reviews, and response coordination. No exploits, payloads, or bypasses.", "keywords": ["security", "defense", "access", "privacy", "incident"]},
    """
security-requirements | Security Requirements | security requirements
job: Write defensive security requirements for a feature so engineering can build controls without exploit instructions.
triggers: security requirements; secure design requirements; what security does this need; abuse cases to defend
inputs: The feature and its data; Actors; Existing controls; Sensitivity the user described
steps: List assets and actors in plain language. || Write requirements as observable controls: authenticate, authorize, log, limit, and protect data. || Include failure behavior: deny by default, and what the user sees. || Map each requirement to a test the team can run safely, such as an authorized versus unauthorized check. || Do not include exploit steps, payloads, or bypass instructions. || Name the owner who accepts any requirement they choose to defer.
anti: Exploit steps; A requirement list with no tests; Deferring auth with no owner
example: A new export feature has no statement about who may export customer data.
out: Requirements for authorization, audit, and a safe allow-and-deny test, with no attack procedure.
related: threat-model-lite; secure-code-review

secure-code-review | Secure Code Review | secure code review
job: Review a change for defensive security issues and request fixes, without writing an exploit.
triggers: security review a PR; secure code review; auth review; secrets in code
inputs: The change description; Auth and data paths; How secrets are handled; Threats they are worried about
steps: Check authentication and authorization on the new path. Missing checks are a blocking finding. || Look for secrets, tokens, or keys in the diff. Tell them to remove and rotate. Do not copy the secret into the review. || Check input handling at trust boundaries in general terms: validate, encode, and parameterize. Do not provide payloads. || Review logging to ensure secrets and personal data are not written. || Ask for a regression test of the denied path. || If you suspect a vulnerability, describe the impact and the fix, not a working attack.
anti: Payloads or proof-of-concept exploits; Repeating a live secret; Approving a missing authorization check
example: A pull request logs a session token while debugging a login bug.
out: A blocking review that requires the log removed, the token rotated, and no token reprinted in the comment.
related: secrets-handling; code-review-standard

access-review | Access Review | access review
job: Review who has access to a sensitive system and remove access that no longer has a reason.
triggers: access review; user access review; who has admin; recertify access
inputs: The system; The access list they exported; The roles that are still justified; Leavers they know about
steps: Start from an export they provide. Do not ask for passwords to go look. || Flag leavers, shared accounts, and standing admin with no named owner. || Ask for a business reason for each high privilege. No reason, recommend removal. || Shared logins are a finding. Recommend individual accounts. || Record who approved the remaining access and the next review date. || Do not disable accounts yourself. Hand the change list to the owner.
anti: Asking for passwords; A review with no removal list; Shared admin treated as normal
example: A shared admin login is still used after three people left the company.
out: A review that recommends unique accounts, lists the leavers for removal, and does not request the shared password.
related: identity-hardening; offboarding-checklist

incident-response-coord | Incident Response Coordination | incident coordination note
job: Coordinate a security incident response with roles, containment, and communications that do not speculate.
triggers: security incident; possible breach; incident commander notes; response coordination
inputs: What is known; Systems affected; Who is in charge; Legal or regulatory contacts they already have
steps: Separate facts from theories. Write both, labeled. || Assign roles: lead, communications, and a note taker. Everyone else stays available, not in the room. || Containment actions must be authorized and reversible where possible. Do not include intrusion or retaliation steps. || Preserve evidence. Do not tell anyone to wipe logs to hide the event. || Communications: tell affected parties only what counsel or the incident lead has approved as known. || Set the next update time. A response without a clock drifts.
anti: Wiping logs; Speculative customer claims; Retaliation or hacking back
example: A chat is about to tell customers data was stolen before anyone has confirmed access.
out: A coordination note that holds the claim, assigns a lead, and forbids log destruction.
related: incident-postmortem; tabletop-exercise
avoid: Hacking back; Evidence destruction

vulnerability-triage | Vulnerability Triage | vulnerability triage
job: Triage a reported vulnerability for severity, owner, and a patch path. Do not develop the vulnerability.
triggers: vulnerability triage; CVE triage; bug report security; patch priority
inputs: The report or advisory text they shared; Affected component if known; Compensating controls they have; Patch availability
steps: Summarize the impact in plain language from the advisory they supplied. Do not add exploit steps. || Ask whether the component is present and reachable in their environment. Unknown means the triage is incomplete. || Rank the patch against other work using their exposure, not a guessed CVSS you computed from memory. || Recommend upgrade, mitigation, or risk acceptance with an owner and a date. || If no patch exists, recommend a compensating control such as access restriction, not a bypass. || Do not request a proof of concept, and do not write one.
anti: Writing an exploit; Inventing a CVSS from memory; Ignoring whether the component is even installed
example: A bot reports a critical issue in a library the team is not sure they use.
out: A triage that first confirms presence, refuses an exploit, and sets an owner for the confirmation.
related: dependency-upgrade; security-exception

secrets-handling | Secrets Handling | secrets handling review
job: Review how a secret is stored and rotated, and remove it from code, tickets, and chat.
triggers: secrets handling; API key in repo; credential leaked; rotate a secret
inputs: Where the secret was seen; What system it opens; Who can rotate it; Whether it was exposed
steps: Tell them to revoke or rotate the exposed secret. Do not ask them to paste the secret. || Search guidance is about locations they own: repo, CI logs, tickets. Do not widen into unauthorized systems. || Replace the secret with a reference to a secret store. Name the pattern, not a new secret value. || Reduce who can read it. || Set a rotation reminder appropriate to their policy. || Check logs to ensure the value is not still being printed. Redact samples.
anti: Asking them to paste a live secret; Hardcoding a replacement in the repo; Printing the secret back in a summary
example: A key was committed and the user pastes it into chat asking if it looks real.
out: A response that refuses to repeat the key, tells them to rotate it, and describes a store reference.
related: ci-cd-review; secure-code-review

vendor-security-review | Vendor Security Review | vendor security review
job: Review a vendor's security claims against the data you will share, without granting a fake certification.
triggers: vendor security review; security questionnaire; third party security; vendor due diligence
inputs: The data the vendor will see; Their claims and documents; The use case; The deadline
steps: Start from the data shared and the harm if it leaks. || Compare their claims to the questions that matter for that data. A badge is not a review. || Mark unanswered questions as gaps, not as passes. || Recommend accept, accept with limits, or reject for this use. You cannot certify the vendor. || Note contract asks for counsel: breach notice, deletion, and subprocessors. Do not invent legal conclusions. || Do not ask the vendor or the user for passwords to 'verify' controls.
anti: Treating a logo as a certification; A pass on unanswered questions; Asking for vendor passwords
example: A team wants to send customer files to a tool because its website says 'enterprise grade'.
out: A review that lists unanswered questions and refuses to treat the slogan as a control.
related: third-party-risk; data-processing-addendum

security-awareness-brief | Security Awareness Brief | awareness brief
job: Draft a short awareness brief for a real behavior, without fear theater or trick phishing against employees.
triggers: security awareness; teach the team this control; security reminder; phishing awareness brief
inputs: The behavior to change; The recent incident or risk they can describe; The audience; The approved reporting path
steps: Teach one behavior: how to report, how to store a secret, or how to verify a request. || Use a real internal example only if the user approves it and it does not shame a named person. || Give the approved reporting path. || Do not design a deceptive phishing exercise unless their security owner explicitly asked for a training plan, and even then do not write malware or credential-harvest pages. || Keep it short enough to read. || Measure a behavior, such as reports submitted, not a quiz score alone.
anti: Shame a named colleague; Malware or fake login pages; A long lecture with no behavior
example: A manager wants to embarrass an employee who clicked a bad link by naming them in an all-hands.
out: A brief that teaches reporting, omits the name, and refuses public shaming.
related: security-policy-draft; tabletop-exercise
avoid: Building phishing kits or credential-harvest pages

backup-and-restore-test | Backup and Restore Test | restore test plan
job: Plan a restore test that proves a backup can be recovered, not merely that a backup job ran.
triggers: backup test; restore drill; can we recover; backup review
inputs: What must be recoverable; The backup they believe exists; The recovery time they need; Who may run the test
steps: Define the asset and the acceptable loss of data and time, in their words. || A successful backup job is not evidence of a restorable backup. Plan an actual restore into a safe environment. || The test environment must not overwrite production. Say that explicitly. || Record what was restored, how long it took, and what failed. || Name the owner who fixes a failed restore. || Do not ask for backup credentials to be pasted into the plan.
anti: Equating a green backup job with recoverability; A test that can overwrite production; Credentials in the plan
example: The team says backups are fine because the nightly job is green, and nobody has restored one.
out: A restore test into a non-production target, with a recorded time and a ban on production overwrite.
related: business-continuity; disaster-recovery-brief

logging-and-detection | Logging and Detection | detection note
job: Specify defensive logs and alerts for a likely abuse, without writing an intrusion guide.
triggers: detection use case; what should we alert on; security logging; audit logging
inputs: The abuse or failure to detect; The logs they already have; Who responds; Privacy limits
steps: Describe the abuse in outcome language, such as mass export or repeated denied access. No attack procedure. || Specify the event fields needed to investigate, excluding secrets and excessive personal data. || Write the alert in terms of a threshold they choose, and who is paged. || Include a false-positive note so the alert is tunable. || State the response's first safe step, usually verify and contain, and point to the incident skill. || Do not propose stealth monitoring of employees beyond the stated security event.
anti: An intrusion how-to; Logging secrets; Employee surveillance beyond the stated event
example: A team wants an alert on data export but also asks to log every keystroke of a department.
out: A detection note for the export event that refuses the keystroke surveillance.
related: observability-plan; access-review

privacy-by-design | Privacy by Design | privacy design note
job: Review a feature for data minimization, purpose, and user-facing honesty before it ships.
triggers: privacy by design; data minimization; privacy review a feature; collect less data
inputs: The data the feature collects; The purpose; Retention if known; What the user is told
steps: List each data element and the purpose it serves. No purpose, recommend cutting it. || Prefer the least identifying option that still meets the purpose. || Check that the notice or UI matches the collection. A mismatch is a finding. || Retention is a question if unknown. Do not invent a period. || Access, export, and deletion are product questions to flag, not legal conclusions. || Send jurisdiction-specific claims to counsel. Do not declare a law satisfied.
anti: Collecting data for a future maybe; A UI that hides the collection; A fake legal clearance
example: A feature stores a full ID document to personalize a greeting.
out: A note that cuts the document, keeps the display name if needed, and flags the notice gap.
related: privacy-notice-draft; privacy-impact-assessment

security-policy-draft | Security Policy Draft | security policy draft
job: Draft a short security policy for one topic, in language employees can follow, marked for the security owner.
triggers: security policy; acceptable use draft; password policy draft; security rules
inputs: The behavior to govern; Current practice; The owner; Consequences they already use
steps: Cover one topic. A policy for all of security will not be read. || Write the required behavior in plain steps. || State exceptions and who can approve them. || Use only consequences the company already has. Do not invent legal penalties. || Point to the reporting path. || Mark the draft unofficial until the security owner adopts it.
anti: A 40-page policy for one control; Invented penalties; No exception path
example: The company wants a password policy and currently shares a team login.
out: A draft that bans shared logins, sets an owner, and leaves legal penalties to counsel.
related: policy-writer; secrets-handling

tabletop-exercise | Tabletop Exercise | tabletop plan
job: Plan a tabletop exercise that practices decisions under a security scenario without live attacks.
triggers: tabletop exercise; incident drill; security tabletop; response practice
inputs: The scenario type; Participants; Decisions to practice; Time available
steps: Write a scenario as a series of injects: what is known at minute 10, 30, and 60. No attack commands. || Pick decisions: contain, notify, and who has authority. || Invite the real decision makers, not only security staff. || Facilitate facts versus assumptions. || Capture gaps in the contact tree, logs, or authority. || End with a few owned actions. A tabletop with no actions was a meeting.
anti: Live malware or a real phishing run disguised as a tabletop; A scenario with no decisions; No follow-up actions
example: The team wants a 'realistic' exercise that sends malware to employees.
out: A paper inject plan that practices notification decisions and refuses malware.
related: incident-response-coord; business-continuity
avoid: Live attacks; Malware exercises

identity-hardening | Identity Hardening | identity hardening plan
job: Plan identity hardening around administrators, joiners and leavers, and phishing-resistant sign-in where they can support it.
triggers: identity hardening; MFA rollout; admin access; joiner leaver identity
inputs: The identity provider they use; Who has admin; Joiner and leaver process; Exceptions they know about
steps: Start with admins and remote access, not with a poster about passwords. || Map joiner, mover, and leaver to access changes. A leaver delay is a finding. || Recommend phishing-resistant factors if their provider supports them, as a question, not a product pitch. || Shared accounts are replaced or given a named owner and a review date. || Exceptions get an expiry. || Do not ask for one-time codes or passwords to implement the plan.
anti: Asking for one-time codes; A plan that ignores leavers; Permanent exceptions
example: Contractors keep admin access for months after the contract ends.
out: A plan that ties leaver dates to access removal and refuses any request for live codes.
related: access-review; offboarding-checklist

security-exception | Security Exception | security exception record
job: Record a security exception with an owner, an expiry, and a compensating control.
triggers: security exception; risk acceptance; waive a control; temporary exception
inputs: The control; The reason; The compensating step; The requested duration
steps: State the control and the gap in one sentence. || Require a business reason more specific than urgency, or record that the reason is weak. || Name a compensating control that reduces the same harm. || Set an owner and an expiry. No expiry, no exception. || Note what will be true at review time. || Refuse exceptions whose purpose is to hide an incident or deceive a customer or auditor.
anti: A permanent waiver; An exception used to hide an incident; No compensating control
example: A team wants to skip MFA forever because a vendor integration is inconvenient.
out: A time-boxed exception only if a compensating control exists, otherwise a refusal of the permanent waiver.
related: policy-exception-log; vulnerability-triage

sbom-and-supply-chain | Software Supply Chain Note | supply chain note
job: Review a software supply chain concern using the inventory the user has, without pretending a scan you did not run.
triggers: SBOM; supply chain review; dependency inventory; provenance review
inputs: The inventory or SBOM they have; How artifacts are built; Who can publish a release; Known gaps
steps: Use only the inventory they provided. Do not claim you scanned the internet. || Note missing owners, unpinned dependencies, and unpublished build steps. || Recommend a repeatable build and a named publisher. || Secrets in the build are a blocking finding. Do not print them. || If they have no inventory, the first action is to generate one with their tools, not to invent components. || Hand license questions to the open-source review skill rather than ruling on them.
anti: A fake scan result; Invented components; Secrets printed in the note
example: A release is built on a laptop and nobody can list the dependencies.
out: A note that makes inventory and a repeatable build the first actions, with no invented component list.
related: dependency-upgrade; open-source-license-review
"""
))
