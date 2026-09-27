from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "healthcare", "title": "Healthcare practice operations", "summary": "Clinic operations, documentation quality, and patient communication drafts. Not medical advice or a treatment protocol.", "keywords": ["healthcare", "clinic", "operations", "documentation", "privacy"]},
    """
clinic-schedule-design | Clinic Schedule Design | clinic schedule
job: Design a clinic schedule around visit types and staffing, without pretending to triage medical urgency.
triggers: clinic schedule; appointment template; provider schedule; clinic capacity
inputs: Visit types and lengths they use; Provider availability; Room limits; No-show experience they shared
steps: Separate visit types they already use. Do not invent clinical priorities. || Fit the template to rooms and staffing they named. || Hold a small portion for same-day access only if they asked for that operational goal. || Show what happens on a provider absence. || Do not promise a wait time the template cannot support. || This is scheduling, not triage. Medical urgency belongs to a licensed clinician.
anti: Clinical triage disguised as a template; A template that ignores rooms; A promised wait they cannot meet
example: A manager wants to double-book every slot because the wait list is long.
out: A template that shows the double-book harm and offers an access hold only within real room capacity.
related: patient-experience-clinic; capacity-plan
avoid: Medical diagnosis; Treatment protocols

patient-intake-sop | Patient Intake SOP | intake procedure
job: Write an intake procedure that collects only what the visit needs and tells staff when to stop and ask a clinician.
triggers: patient intake; front desk procedure; registration SOP; intake checklist
inputs: The visit types; Data they truly need; Their privacy rules; Escalation to a clinician
steps: List data elements required for registration and billing they described. Cut the rest. || Write the script for missing information without pressuring a patient in distress. || Tell staff which answers must go to a clinician rather than be interpreted at the desk. || Include identity-check steps they already use. Do not invent a legal ID rule. || Protect the conversation from the waiting room when the topic is sensitive. || No passwords, no treatment advice, no doses.
anti: Desk staff giving treatment advice; Collecting data with no purpose; A public conversation about a sensitive issue
example: An intake script asks the front desk to decide if chest pain can wait.
out: A procedure that stops and escalates urgent symptoms to a clinician instead of scoring them at the desk.
related: hipaa-privacy-ops; patient-communication
avoid: Diagnosis; Drug doses

clinical-documentation-quality | Clinical Documentation Quality | documentation quality review
job: Review documentation quality for completeness and clarity against their template, not for a diagnosis.
triggers: documentation quality; chart quality; note review; clinical documentation
inputs: Their template; The note or a description of gaps; Who signs; The handoff risk
steps: Compare the note to their required elements. Missing elements are findings. || Flag ambiguity that would confuse the next clinician, without supplying a diagnosis. || Do not rewrite a note to add clinical facts that were not observed. || Separate a billing-motivated addendum request from a clarity fix. Refuse invented history. || Name who must correct the note under their policy. || This review is not a coding maximization exercise and not medical advice.
anti: Invented history; A diagnosis added by the assistant; Coding pressure that changes the facts
example: A manager asks to add a symptom the clinician did not record so a claim pays more.
out: A refusal of the invented symptom and a list of only the template gaps that are truly missing.
related: medical-billing-review; referral-workflow
avoid: Upcoding; Invented clinical facts

referral-workflow | Referral Workflow | referral workflow
job: Map a referral workflow so the sending and receiving sides know the packet, the owner, and the clock.
triggers: referral workflow; referral leakage; specialist referral process; referral SOP
inputs: The packet they require; Who sends and receives; Clocks they use; What patients are told
steps: Define a complete packet from their list. Do not invent clinical requirements. || Name the owner of each handoff. || State what the patient is told and when. || Track a stalled referral as an operations issue with an aging rule. || Close the loop back to the sender when they say that is required. || Escalate clinical questions to a clinician. Do not decide medical necessity.
anti: A referral with no owner; Invented medical-necessity rulings; Patients left without a status
example: Referrals leave the clinic and nobody knows which ones were received.
out: A workflow with a packet, an owner, and an aging check, and no medical-necessity ruling.
related: patient-intake-sop; prior-authorization-ops

prior-authorization-ops | Prior Authorization Operations | authorization operations checklist
job: Organize a prior-authorization packet and clock from the payer rules the user supplied.
triggers: prior authorization; payer authorization; auth packet; authorization checklist
inputs: The payer requirements they have; The documents on hand; The internal owner; The requested date
steps: Use only requirements the user supplied. Do not invent payer rules. || List missing documents as gaps, not as reasons to fabricate a note. || Assign an owner and a follow-up clock. || Tell the patient the status in plain language without promising approval. || Refuse any request to alter a clinical record to win an authorization. || Clinical criteria questions go to a clinician or the payer, not to a guessed answer.
anti: Fabricated clinical notes; A promised approval; Invented payer rules
example: Staff want to change a note so the authorization is more likely to pass.
out: A checklist of real gaps and a refusal to alter the record.
related: medical-billing-review; clinical-documentation-quality
avoid: Altering records; Fraudulent billing

hipaa-privacy-ops | Privacy Operations for a Clinic | privacy operations checklist
job: Review a clinic privacy practice for minimum necessary access and a real incident path. Not a legal opinion.
triggers: HIPAA operations; clinic privacy; minimum necessary; privacy incident clinic
inputs: Who can open a chart; The reason they need it; How incidents are reported; Known gaps
steps: Compare access to the job. Curiosity access is a finding. || Check that conversations, screens, and printouts match their privacy rule. || Write the incident path they have, or say it is missing. || Do not declare HIPAA compliance. Send legal questions to counsel. || Minimize identifiers in examples and tickets. || Refuse any request to snoop in a chart for a non-care reason.
anti: A compliance badge; Snooping instructions; Identifiers in a training example
example: A scheduler wants standing access to full clinical notes 'just in case'.
out: A finding that limits access to the scheduling need and refuses a compliance badge.
related: privacy-by-design; patient-communication

medical-billing-review | Medical Billing Review | billing review checklist
job: Review a billing packet for missing elements and coding questions, without upcoding or inventing services.
triggers: medical billing review; claim checklist; coding question operations; clean claim
inputs: The services they say were provided; The codes they are considering; Payer edits they supplied; The documentation present
steps: Match codes only to services they say were documented. || List missing documentation. Do not suggest adding a service that did not happen. || Use payer edits they pasted. Do not invent a payer rule. || Flag questions for a certified coder. This skill is not a coder's final assignment. || Separate a patient estimate from a coverage promise. || Refuse upcoding, unbundling schemes, and false claims.
anti: Upcoding; Invented services; A coverage promise
example: A biller wants a higher code because the visit 'felt complex' though the note does not support it.
out: A review that keeps the supported code and sends the complexity question to a coder with the note gap visible.
related: clinical-documentation-quality; prior-authorization-ops
avoid: Upcoding; False claims

patient-communication | Patient Communication Draft | patient message
job: Draft a patient message in plain language that a clinician or clinic lead approves before sending.
triggers: patient message; clinic letter; patient instructions draft; portal message
inputs: The purpose; Facts a clinician confirmed; The reading level they want; The approval owner
steps: State the purpose in the first line. || Include only facts a clinician or the record confirmed. Do not add advice, doses, or a diagnosis. || Tell the patient who to call if symptoms worry them, using their escalation line. || Avoid blame and jargon. || Mark the draft unsent until the named clinician or lead approves it. || Do not include another patient's information.
anti: Doses or new diagnoses; An unapproved clinical instruction; Another patient's data
example: A draft tells a patient to double a medicine because the refill is late.
out: A message that removes the dose change, explains the operational status, and waits for clinician approval.
related: patient-experience-clinic; clinical-documentation-quality
avoid: Medication changes; Diagnosis

care-team-huddle | Care Team Huddle | huddle agenda
job: Plan a short care-team huddle around flow and safety flags, not a full case conference.
triggers: huddle agenda; care team huddle; morning huddle; clinic huddle
inputs: Today's schedule issues; Safety flags they already use; Staffing gaps; The time box
steps: Limit the huddle to the time box. || List schedule risks: missing results they already know about, interpreter needs, and staffing gaps. || Safety flags are read from their list. Do not invent clinical risk. || Assign one owner for each flow problem. || Park teaching and long cases for another forum. || End with who will tell the front desk.
anti: A huddle that becomes a meeting; Invented clinical risks; No owner for a flow problem
example: A 10-minute huddle is packed with three teaching topics and no staffing note.
out: An agenda that keeps the staffing gap, drops the teaching, and names the front-desk owner.
related: clinic-schedule-design; shift-handover

staff-credentialing | Credentialing File Checklist | credentialing checklist
job: Checklist a credentialing file for missing documents and expirations, without declaring someone privileged.
triggers: credentialing; provider file; license expiration; privileging checklist
inputs: The required documents they listed; Expiry dates they have; The reviewer; Known gaps
steps: Compare the file to their required list. || Flag expired or missing items. Do not guess an expiry. || A complete file is not a privileging decision. Say who must decide. || Track a reappointment date. || Do not fabricate a license number or a verification result. || Escalate a lapse that their policy says stops scheduling.
anti: A homemade privileging decision; Fabricated license data; A lapse left off the schedule note
example: A file is missing a current license and the team wants to assume it renewed.
out: A checklist that marks the license unverified and blocks any assumption of renewal.
related: clinic-schedule-design; compliance-calendar

patient-experience-clinic | Clinic Experience Review | clinic experience review
job: Review a clinic experience problem using waits, communication, and respect, without blaming the patient.
triggers: patient experience; clinic complaint; waiting room experience; visit experience
inputs: The complaint or observation; Wait data if any; What staff can change; Privacy constraints
steps: Describe the failed moment: wait, confusion, or disrespect. || Use their wait data or mark it unknown. || Separate a capacity problem from a courtesy problem. || Recommend one change staff can make this month. || Do not identify a patient in a broader share-out. || Clinical complaints go to the clinical lead, not to a scripted apology alone.
anti: Blaming the patient; Identifying a patient in a public note; A courtesy script for a capacity failure
example: Patients wait 70 minutes and the draft response tells staff to smile more.
out: A review that treats the wait as a capacity problem and limits the script to truthful status updates.
related: clinic-schedule-design; complaint-root-cause

telehealth-visit-ops | Telehealth Visit Operations | telehealth operations checklist
job: Write the operations checklist for a telehealth visit: identity, consent, backup, and privacy.
triggers: telehealth operations; virtual visit checklist; video visit SOP; remote clinic visit
inputs: Their identity check; Consent practice; Backup if video fails; Privacy expectations
steps: Confirm identity the way they already require. Do not invent a legal standard. || State where consent is recorded if they said it is required. || Give the patient a backup path when video fails. || Remind staff about who else is in the room and what the camera shows. || Do not provide clinical advice for the visit content. || Escalate emergencies to their emergency instruction, which should be to local emergency services when they say that.
anti: Clinical advice in the ops checklist; No backup path; A camera angle that exposes a waiting room
example: A checklist has no plan for a dropped call and tells staff to improvise medical advice.
out: A checklist with a callback path and a clear line that clinical content belongs to the clinician.
related: patient-intake-sop; patient-communication
"""
))

PACKS.append(pack(
    {"id": "education", "title": "Education and training", "summary": "Lesson design, assessment, and facilitation for teachers and trainers. Not a service for cheating.", "keywords": ["education", "teaching", "assessment", "curriculum", "training"]},
    """
lesson-plan | Lesson Plan | lesson plan
job: Plan a lesson from an objective, a practice task, and a check for understanding.
triggers: lesson plan; plan a class; teaching plan; session plan
inputs: The learners; The objective; Time available; Materials they have
steps: Write an objective learners can demonstrate, not a topic label. || Open with a reason the objective matters to their work or course. || Teach one model, then a practice task. A lecture with no practice is a finding. || Check understanding before the end. || Plan the likely misconception they named, or mark it unknown. || Fit the plan to the minutes. Cut content before cutting the check.
anti: An objective that is only a topic; No practice; A plan that overruns and skips the check
example: A 40-minute plan has 30 slides and no task.
out: A plan with one objective, one practice task, and a check, with slides cut to fit.
related: learning-objectives; assessment-design

learning-objectives | Learning Objectives | learning objectives
job: Write learning objectives that name the performance, the condition, and the standard.
triggers: learning objectives; write objectives; course outcomes; training objectives
inputs: The performance needed on the job or in the course; The conditions; The standard they will accept; The level of the learner
steps: Use a verb the learner can be seen doing. || Add the condition: with what notes, tools, or data. || Add the standard: how good is good enough, if the user knows it. || Cut objectives the time budget cannot assess. || Align each objective to a later practice or assessment. || Do not write 'understand' as the only verb.
anti: Understand as the only verb; Objectives with no assessment path; A list longer than the course can teach
example: Objectives say 'understand compliance' for a one-hour briefing.
out: Objectives that name a visible performance, such as spotting a missing control, and drop the vague verb.
related: lesson-plan; assessment-design

assessment-design | Assessment Design | assessment
job: Design an assessment that matches the objective and resists cheating without becoming a trap.
triggers: design an assessment; quiz design; test blueprint; check for understanding
inputs: The objectives; The format; The time; Integrity constraints they care about
steps: Map every item to an objective. Unmapped items are cut. || Prefer a task that resembles the real performance when that is possible. || Write a rubric or answer key from the objective, not from trick wording. || Include a reasonable time box. || State the integrity rules they want: open notes or not. Do not design a surveillance product. || This skill does not write answers for a student to submit as their own.
anti: Trick questions with no objective; A cheating service; Surveillance as the assessment
example: A manager wants an assessment that catches cheaters by using hidden webcams.
out: An assessment mapped to objectives, with integrity rules that do not require covert cameras.
related: rubric-builder; academic-integrity
avoid: Completing graded work for a student; Covert exam surveillance

rubric-builder | Rubric Builder | rubric
job: Build a rubric with levels a second marker could apply to the same work.
triggers: rubric; marking guide; scoring guide; assessment criteria
inputs: The task; The qualities that matter; The scale they use; Examples of strong and weak work if any
steps: Criteria come from the objective, not from personal taste. || Describe each level with observable features. || Weight criteria they say matter more. If they have no weights, keep them equal and say so. || Add one example descriptor only from work they supplied. || Test the rubric against two samples if they have them. || Cut criteria that reward polish unrelated to the objective unless they intend that.
anti: Vague levels such as good and excellent with no features; Hidden criteria; A rubric that rewards length only
example: A rubric says 'excellent analysis' with no description of what excellent contains.
out: A rubric whose top level names the comparisons or evidence a marker must see.
related: assessment-design; feedback-on-work

syllabus-outline | Syllabus Outline | syllabus outline
job: Outline a syllabus with outcomes, assessments, and policies the instructor actually uses.
triggers: syllabus; course outline; module outline; class policies
inputs: Outcomes; Assessment list; Schedule constraints; Policies they want included
steps: Lead with outcomes and how students will be assessed. || Map weeks or modules to outcomes. A week with no outcome is a candidate to cut. || Include late, integrity, and support policies only as the instructor stated them. Do not invent an institutional rule. || Show the workload honestly. || Mark required materials they confirmed. || Note what the institution must still approve if they said approval is required.
anti: Invented institutional rules; A week-by-week with no assessment map; Hidden workload
example: A syllabus lists readings for fifteen weeks and one grade at the end.
out: An outline that maps assessments to outcomes and refuses to invent a university policy.
related: curriculum-map; learning-objectives

feedback-on-work | Feedback on Work | feedback note
job: Give feedback on a learner's work that names the next improvement against the rubric.
triggers: feedback on student work; coaching feedback; critique this assignment; formative feedback
inputs: The work; The rubric or objective; The learner's level; What they may revise
steps: Start with what the work already achieves, specifically. || Name the highest-leverage gap against the rubric. || Show one concrete revision, not a rewrite of the whole piece for them to submit as their own. || Limit comments. A margin full of nits hides the point. || Invite a question. || Do not complete a graded submission for the learner.
anti: Rewriting their graded work; Feedback with no next step; Comments unrelated to the rubric
example: A teacher wants the assistant to rewrite a student's essay so it will pass.
out: Feedback that points to the rubric gap and shows a small example revision the student must still do themselves.
related: rubric-builder; coaching-session
avoid: Completing graded work for submission

curriculum-map | Curriculum Map | curriculum map
job: Map a curriculum so outcomes, courses, and assessments line up without gaps or pointless overlap.
triggers: curriculum map; program map; course sequence; outcome alignment
inputs: Program outcomes; Courses or modules; Existing assessments; Constraints
steps: List program outcomes the user confirmed. Do not invent accreditation standards. || Show where each outcome is taught and assessed. An outcome with no assessment is a gap. || Mark redundant assessments that do not add evidence. || Sequence prerequisites they actually require. || Note workload spikes. || Flag external approval as a question if they said a regulator or institution must sign.
anti: Invented accreditation clauses; An outcome never assessed; A map that hides workload spikes
example: A program claims a communication outcome and no course assesses it.
out: A map that shows the gap and recommends where an assessment should sit.
related: syllabus-outline; learning-objectives

workshop-facilitation | Workshop Facilitation | workshop plan
job: Plan a workshop that produces a shared artifact, with timing and a way to hear quiet people.
triggers: facilitate a workshop; workshop plan; training facilitation; working session
inputs: The artifact the room must leave with; Participants; Time; Sensitive topics
steps: Define the artifact: a decision, a list, or a draft. || Design activities that create the artifact, not icebreakers that consume the hour. || Timebox. Leave a close that assigns owners. || Plan a way for quiet people to contribute without putting anyone on the spot in a harmful way. || Handle disagreement as a recorded option, not as a forced consensus. || Do not run a workshop that pretends people consented to a decision they did not make.
anti: No artifact; Fake consensus; An agenda of icebreakers
example: A two-hour workshop has no decision and six get-to-know-you games.
out: A plan aimed at one recorded decision, with a dissent line and owners.
related: executive-offsite-design; lesson-plan

training-needs-analysis | Training Needs Analysis | training needs note
job: Decide whether a performance gap is a training problem or a job-design problem.
triggers: training needs; skills gap; do they need training; needs analysis
inputs: The performance gap; Evidence; What training already exists; Constraints on the job
steps: Describe the gap as observable work. || Ask whether people could do the task with enough time and tools. If not, training is the wrong first fix. || If the skill is missing, define the smallest training that builds it. || Name who needs it and who does not, so you do not train the whole company by habit. || State how you will know the gap closed. || Recommend a job-design fix when the evidence points there.
anti: Training as the answer to a tooling or workload problem; A course with no success check; Training everyone by default
example: Errors rose after a tool change that hides the needed field, and the draft recommends a full-day course.
out: A note that fixes the field first and limits training to the people who still lack the skill.
related: learning-path; lesson-plan

instructional-design-brief | Instructional Design Brief | design brief for learning
job: Brief a designer or trainer on a learning experience with audience, objective, and constraints.
triggers: instructional design brief; training brief; e-learning brief; course brief
inputs: Audience; Objective; Time and format; Assessment
steps: Describe the audience by what they already do. || Write the objective as a performance. || Choose a format that fits the objective. A video is not automatically better. || Include practice and assessment in the brief, not as an afterthought. || List source material they may use. Do not tell anyone to copy a third-party course. || State review and update ownership.
anti: A brief with no practice; Copying a proprietary course; Format chosen for fashion
example: A brief asks for a fun video and has no objective.
out: A brief that blocks production until the performance and the practice are written.
related: creative-brief; lesson-plan

academic-integrity | Academic Integrity Conversation | integrity conversation plan
job: Plan an academic integrity conversation that is fair, specific, and not a trap.
triggers: academic integrity; plagiarism conversation; cheating concern; integrity process
inputs: The concern and evidence; The institution's process they supplied; The student-facing next step; Support available
steps: Stick to the evidence. Do not accuse beyond it. || Follow the process they supplied. Do not invent a sanction. || Tell the student the concern and how to respond, if their process allows that at this stage. || Separate a citation skill gap from a deception concern when the evidence allows it. || Do not help a student conceal misconduct, and do not help staff run a dishonest hearing. || Point to support for writing skills when the issue is skill.
anti: A sanction invented from memory; A trap conversation; Help concealing misconduct
example: A teacher wants to fail a student immediately with no process because a paragraph looks similar.
out: A plan that follows their stated process, limits the claim to the evidence, and refuses a made-up sanction.
related: assessment-design; feedback-on-work
avoid: Helping conceal misconduct; Invented sanctions

course-evaluation | Course Evaluation Readout | evaluation readout
job: Read a course evaluation without overreacting to a small sample or a single cruel comment.
triggers: course evaluation; training feedback; class survey; workshop feedback
inputs: The results; Response rate; The objectives; Comments they pasted
steps: Report response rate before scores. || Tie low scores to a specific objective or logistics issue if the comments support it. || Do not let one abusive comment rewrite the course. Quote only what is useful and safe. || Recommend one change before the next run. || Protect respondent identity in small groups. || Ignore requests to punish a teacher from anonymous venting with no process.
anti: A redesign from three responses; Identifying a respondent; Punishment from an anonymous vent
example: A leader wants to remove a trainer because one unnamed comment was harsh and the response rate was low.
out: A readout that refuses the removal, states the sample limit, and proposes one evidence-based change.
related: survey-analysis; lesson-plan
"""
))
