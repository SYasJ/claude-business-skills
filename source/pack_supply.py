from dense import pack

PACKS = []

PACKS.append(pack(
    {"id": "supply-chain", "title": "Supply chain", "summary": "Demand, inventory, suppliers, and shortages using the user's own lead times.", "keywords": ["supply-chain", "inventory", "suppliers", "logistics", "demand"]},
    """
demand-plan-review | Demand Plan Review | demand plan review
job: Review a demand plan for bias, assumptions, and the one driver that would change supply.
triggers: demand plan; forecast review; demand review; S&OP demand
inputs: The forecast; Recent actuals; Known events; Who owns the number
steps: Compare the plan to recent actuals they supplied. || Separate a one-time event from a run-rate change. || State the assumption that moves supply the most. || Do not invent a market growth rate. || Recommend a bias note if the plan is always high or low in their history. || Send the agreed number to supply with the assumption visible.
anti: A plan with no actuals comparison; An invented growth rate; A hidden bias
example: The plan repeats last year's hockey stick and actuals have missed it three times.
out: A review that flags the bias and refuses to treat the hockey stick as the base.
related: forecast-accuracy; s-and-op

inventory-policy | Inventory Policy | inventory policy note
job: Set an inventory policy from service target, lead time, and demand variability they can show.
triggers: inventory policy; safety stock; min max; inventory target
inputs: Service target; Lead time; Demand variability if known; Cost of a miss they described
steps: Define the item and the service target in their words. || Use their lead time. A generic lead time is labeled a guess. || If variability is unknown, say the safety stock is incomplete rather than inventing a formula result. || Separate cycle stock from safety stock. || Name who may override the target. || Review the policy when lead time changes.
anti: An invented safety-stock percentage; A policy with no owner; Mixing cycle and safety stock
example: A buyer wants six weeks of safety stock because it feels safe, with a two-week lead time.
out: A note that asks for the service target and variability before accepting six weeks.
related: safety-stock; working-capital

supplier-scorecard | Supplier Scorecard | supplier scorecard
job: Score a supplier on the outcomes in the agreement, using evidence rather than the last meeting's mood.
triggers: supplier scorecard; vendor scorecard; supplier performance; supplier review
inputs: The contracted outcomes; Recent evidence; Volumes; The internal owner
steps: Score only contracted outcomes they can evidence. || Separate a one-off miss from a trend. || Include the buyer's own late forecasts if those caused the miss. || Recommend a conversation, a corrective plan, or a sourcing question. || Do not invent a penalty. || Share the score with the supplier only if the user wants a supplier-facing version, and keep it factual.
anti: A mood score; Invented penalties; Ignoring buyer-caused misses
example: A supplier is blamed for shortages after the forecast doubled with no notice.
out: A scorecard that records the forecast change as a buyer cause and limits the supplier miss to evidenced gaps.
related: vendor-ops-review; shortage-playbook

purchase-order-control | Purchase Order Control | PO control review
job: Review purchase-order control so orders are approved, received, and matched without informal side deals.
triggers: purchase order control; PO process; three-way match; buying controls
inputs: Who can raise and approve; Receipt practice; Match exceptions; Known side arrangements
steps: Map raise, approve, receive, and pay. Note where one person does two steps. || A side arrangement with no PO is a finding. || Receipt should evidence that goods or services arrived. || Match exceptions need an owner, not a permanent override. || Do not help conceal a purchase from the required approver. || Recommend the smallest control that would have caught their last miss.
anti: Concealing a purchase; A permanent match override; One person ordering and approving
example: A team lead emails a supplier directly to avoid the PO system.
out: A review that treats the email order as a control break and names the missing approval.
related: accounts-payable-control; procurement-award-note

logistics-exception | Logistics Exception | logistics exception note
job: Handle a logistics exception with the customer impact, the options, and a truthful status.
triggers: logistics exception; delayed shipment; freight exception; missed delivery
inputs: The shipment; The promise made; Options and costs they have; Who must be told
steps: State the promise and the new fact. || List options they can actually buy: wait, reroute, or partial ship. || Show the customer impact in their words. || Draft a status that does not promise a recovery time they do not have. || Name the owner for the next update. || Do not hide the miss behind vague tracking language.
anti: A fake recovery time; No owner; Vague tracking language that hides the miss
example: A carrier missed a pickup and the draft tells the customer the order is on time.
out: A note that states the miss, lists real options, and removes the on-time claim.
related: customer-communication-incident; shortage-playbook

s-and-op | Sales and Operations Planning | S&OP brief
job: Brief an S&OP cycle so demand, supply, and a decision meet in one forum.
triggers: S&OP; SIOP; sales and operations planning; demand supply balance
inputs: The demand number; The supply constraint; The gap; The decision needed
steps: Use one set of numbers. Two unofficial forecasts are a finding. || Show the gap in units and in customer impact. || Options: change demand, add supply, or accept the miss. Recommend one. || Name the decider. || Record assumptions that expire next cycle. || Do not let a side meeting overturn the decision without a note.
anti: Two forecasts; A meeting with no decision; A side deal that ignores the gap
example: Sales brings a new forecast to the meeting that supply has not seen.
out: A brief that stops the decision until both sides use the same number, then records the gap.
related: demand-plan-review; capacity-plan

safety-stock | Safety Stock Review | safety stock review
job: Review safety stock for a few items so cash is not trapped in a habit.
triggers: safety stock review; inventory too high; buffer stock; stock cover
inputs: Current cover; Lead time; Stockout history they have; Service target
steps: Rank items by cash tied up and by stockout pain, using their data. || Identify cover that exceeds their own rule. || Ask what uncertainty the extra cover buys. If nobody knows, it is a candidate to reduce. || Do not cut stock that covers a known supply risk they named. || Recommend a pilot reduction with a stockout check. || Revisit after one lead time.
anti: A blanket cut; Cutting stock that covers a known risk; No stockout check
example: Every item is set to 90 days because the spreadsheet default says so.
out: A review that pilots a reduction on items with no risk story and leaves named risks alone.
related: inventory-policy; working-capital

shortage-playbook | Shortage Playbook | shortage playbook
job: Allocate a shortage fairly against a stated rule, and communicate it without favoritism hidden in a spreadsheet.
triggers: shortage; allocation; fair share; supply shortage playbook
inputs: Available quantity; Demand by customer or channel; The allocation rule they want; Contractual priorities they named
steps: State the available quantity and the date. || Apply the rule they chose: contract first, pro rata, or margin. If no rule exists, recommend they set one before allocating by friendship. || Honor contractual priorities they confirmed. Do not invent a contract. || Show who is cut and by how much. || Draft a truthful customer message. || Record exceptions so the rule does not become theater.
anti: Allocation by friendship with no record; Invented contractual priority; A message that says stock is fine
example: A planner gives the scarce item to the loudest salesperson's account.
out: A playbook that applies a written rule, records exceptions, and tells affected customers the truth.
related: war-room-brief; logistics-exception

supplier-onboarding | Supplier Onboarding | supplier onboarding checklist
job: Onboard a supplier with the documents, access, and first-order check the company actually requires.
triggers: supplier onboarding; new vendor setup; supplier setup; vendor onboarding
inputs: Required documents; Risk tier; System access needed; The first order
steps: Collect only documents their policy requires. || Match the review depth to the risk tier. || Set up access for named people, not a shared login. || Confirm payment details through their verified channel. Do not accept a change from an unverified email. || Define a successful first order. || Refuse any request to skip sanctions or payment verification they already require.
anti: A shared vendor login; Payment detail changes from unverified email; Skipping a required check
example: A supplier emails new bank details from a free mail account and wants the next payment sent there.
out: A checklist that blocks the change until their verified channel confirms it.
related: purchase-order-control; sanctions-compliance-process

returns-process | Returns Process | returns process
job: Design a returns process with a reason code, a disposition, and a customer promise you can keep.
triggers: returns process; RMA; reverse logistics; refund operations
inputs: Reasons they see; Disposition options; Refund authority; Customer promise
steps: Capture a reason code that operations can act on. || Route disposition: restock, repair, or scrap, based on their rules. || State the customer promise and the clock they can meet. || Separate a policy exception from the standard path. || Track fraud concerns as a control question, not as an accusation in the customer message. || Do not help conceal returned goods from inventory records.
anti: A promise they cannot meet; Concealed returns; Accusing a customer in the template
example: The website promises instant refunds and the warehouse has not inspected the unit.
out: A process that aligns the promise with inspection and keeps inventory records honest.
related: service-recovery; inventory-accounting

landed-cost | Landed Cost Review | landed cost note
job: Build a landed-cost view from cost elements the user can support, so a buy decision sees the full cash cost.
triggers: landed cost; total delivered cost; import cost stack; should we source this
inputs: Invoice cost; Freight, duty, and fees they know; Volume; The alternative source
steps: List only cost elements they can support. Mark unknowns. || Show cost per unit at the volume they named. || Compare with the alternative on the same elements. || Note cash timing if duties or freight are paid earlier. || Do not invent a duty rate. || Recommend a buy, a question, or a hold until the unknown cost is filled.
anti: An invented duty rate; A unit cost that ignores freight; A comparison that omits the alternative's freight
example: A cheaper invoice price is recommended, and nobody added international freight.
out: A note that holds the recommendation until freight is included or explicitly unknown.
related: pricing-margin-bridge; supplier-scorecard
"""
))

PACKS.append(pack(
    {"id": "manufacturing", "title": "Manufacturing and quality", "summary": "Quality, production, and shop-floor routines. Do not bypass a safety or hold step.", "keywords": ["manufacturing", "quality", "production", "capa", "safety"]},
    """
quality-control-plan | Quality Control Plan | control plan
job: Draft a control plan for a process step: what is checked, how often, and what happens on a fail.
triggers: control plan; quality plan; inspection plan; process control plan
inputs: The characteristic; The method; The frequency; The reaction to a fail
steps: Name the characteristic that matters to the customer or the safety rule they cited. || Specify method and frequency they can staff. || Write the reaction to a fail: stop, sort, or call. A fail with no reaction is a finding. || Identify the owner of the check. || Do not loosen a limit they said is safety-related. || Link the plan to the work instruction rather than creating a second unofficial standard.
anti: A check with no reaction; Loosening a safety limit; An unstaffed frequency
example: A plan checks a safety dimension weekly because daily checks feel expensive.
out: A plan that keeps the safety check at the frequency their rule requires and flags the cost as a separate decision.
related: incoming-inspection; work-instruction

nonconformance-report | Nonconformance Report | NCR
job: Write a nonconformance report that contains the fact, the containment, and the owner.
triggers: NCR; nonconformance; quality escape; defect report
inputs: What failed; Where it was found; Quantity if known; Immediate containment
steps: Describe the defect in observable terms. || Record quantity and location only from their count. || Containment first: stop the escape path they named. || Do not dispose of evidence they said must be kept. || Separate containment from root-cause work. || Assign an owner and a date. A report with no owner will age in a drawer.
anti: A vague defect description; Disposing of required evidence; No containment
example: A report says 'bad parts' and the suspect lot is still being shipped.
out: An NCR that stops the lot, describes the defect, and names the owner.
related: capa-plan; traceability-lot

capa-plan | CAPA Plan | CAPA plan
job: Plan a corrective action that fixes a cause and checks that the fix worked.
triggers: CAPA; corrective action; preventive action; quality action plan
inputs: The problem statement; Evidence; Suspected cause; How effectiveness will be checked
steps: Write a problem statement with the defect and the impact. || Separate containment already done from corrective action. || Test the suspected cause against evidence. Do not jump to training as the cause by habit. || Define the action, the owner, and the date. || Define the effectiveness check and when it happens. || Close only when the check passes. Training attendance is not effectiveness by itself.
anti: Training as the default cause; Closure without an effectiveness check; A problem statement with no defect
example: A CAPA closes because operators signed a training sheet, and the defect is still appearing.
out: A plan that keeps the CAPA open until the defect measure moves, and looks past the training reflex.
related: nonconformance-report; continuous-improvement

process-fmea | Process FMEA Facilitation | FMEA notes
job: Facilitate a process FMEA on a few high-risk steps, with actions for the failures that lack detection.
triggers: FMEA; process FMEA; failure mode; risk in the process
inputs: The process steps; Failures they have seen; Current controls; Their scoring scale if any
steps: Limit the session to the steps that can hurt the customer or safety. || Write failure modes as what goes wrong, not as one-word fears. || Record current prevention and detection. || Use their scale or a labeled simple scale. Do not pretend a score is precise. || Actions go to high-severity gaps with weak detection. || Do not lower a severity score to make the chart look calm.
anti: Lowering severity to look green; A whole factory in one session; Scores with no action
example: A team wants to mark a safety failure as low severity so the FMEA looks acceptable.
out: Notes that keep the high severity and assign an action instead of editing the score.
related: quality-control-plan; risk-assessment

work-instruction | Work Instruction | work instruction
job: Write a work instruction a new operator can follow, including the stop and the quality check.
triggers: work instruction; standard work; operator instruction; job instruction
inputs: The outcome; The steps as performed safely; The check; The stop conditions
steps: Start with the outcome and the safety precondition they require. || Number steps in the order the work is done. || Include the quality check and what a fail looks like. || Write the stop: when to call a lead. || Use their terms for tools and parts. Do not rename equipment. || Photos only if they supply them. Do not invent a torque or a setting.
anti: An invented setting; No stop condition; A step order that does not match the work
example: An instruction says 'tighten properly' and the torque is unknown.
out: An instruction that marks torque as a required input from engineering rather than inventing a number.
related: sop-writer; quality-control-plan

calibration-control | Calibration Control | calibration control note
job: Review calibration control so instruments used for acceptance are in date, and out-of-date tools are not used.
triggers: calibration; gage control; instrument due; calibration overdue
inputs: The instrument list; Due dates they have; What the instrument accepts; The quarantine practice
steps: Flag overdue instruments used for acceptance. || Quarantine is the default they stated, or recommend it if they have none. || Do not calculate a new calibration interval from memory. || Record the last result they supplied. || Assess impact only if they know the instrument was used while overdue. Do not invent affected lots. || Name the owner of the recall or the review.
anti: Using an overdue gage for acceptance; An invented interval; Invented affected lots
example: A caliper used for final accept is two months overdue and still on the bench.
out: A note that quarantines it and asks for a use review rather than inventing which lots moved.
related: incoming-inspection; nonconformance-report

incoming-inspection | Incoming Inspection | incoming inspection plan
job: Plan incoming inspection for a material based on risk and the reaction to a failed lot.
triggers: incoming inspection; receiving inspection; supplier quality check; incoming QC
inputs: The material risk; The characteristics; Sample practice they use; Fail reaction
steps: Tie inspection to risk. Critical characteristics are not sampled away because the dock is busy, if their rule says so. || Write the accept and fail reaction. || Identify the hold location so failed material cannot be issued. || Feed repeats to supplier quality. || Do not skip a hold to keep a line running unless the user names a deviation owner. || Record results in the system they use, not only on a scrap of paper.
anti: A failed lot left in the issue location; Skipping a critical check for speed; No fail reaction
example: Failed material is left on the issue shelf so the line does not stop.
out: A plan that moves failed material to hold and requires a named deviation before any use.
related: quality-control-plan; supplier-quality

production-schedule | Production Schedule Review | schedule review
job: Review a production schedule against capacity, materials, and the promise that will slip first.
triggers: production schedule; finite schedule; what will we build; schedule review
inputs: Demand; Capacity; Material constraints; Frozen window if any
steps: Show the constraint: labor, machine, or material, from their facts. || Do not schedule over the constraint and call it a plan. || Honor a frozen window they have. Changes inside it need a named approver. || Identify the customer promise that slips first. || Recommend a sequence rule they can repeat, not a daily argument. || Separate a plan from a wish list of every order.
anti: A schedule over known capacity; Silent changes inside a freeze; No view of the first slipped promise
example: The schedule loads 120 hours into an 80-hour cell and the status is on time.
out: A review that cuts or sequences to 80 hours and names the promise that moves.
related: capacity-plan; shortage-playbook

oee-review | OEE Review | OEE review
job: Review overall equipment effectiveness only as far as their data supports, and pick one loss to attack.
triggers: OEE; equipment effectiveness; downtime review; loss tree
inputs: Availability, performance, and quality data they have; The biggest loss they see; The time window; The owner
steps: Use only components they measured. Do not invent an OEE number. || Define the time base they used. || Pick the largest evidenced loss. || Recommend one countermeasure with an owner. || Do not turn OEE into a punishment metric in the write-up. || Recheck after the countermeasure, not after a speech.
anti: An invented OEE; Three losses attacked at once; A blame report
example: A manager wants an OEE of 85 quoted to a customer, and downtime is not recorded.
out: A review that refuses the number and starts a downtime record before any customer claim.
related: continuous-improvement; marketing-claims-review

change-control-manufacturing | Manufacturing Change Control | change-control note
job: Review a manufacturing change for approval, risk, and the point it becomes effective.
triggers: manufacturing change control; process change; engineering change; ECO review
inputs: The change; The risk they see; Approvers; The effective lot or date
steps: Describe the change and the reason. || Identify what must be revalidated or reinspected, using their rules. Do not invent a regulatory filing. || Name approvers. A change without the required approver is not effective. || Set the effective lot or date so old and new do not mix unlabeled. || Update the work instruction as part of done. || Flag customer or regulatory notice as a question if they said it might apply.
anti: An effective change with no approver; Mixed lots with no label; An invented filing
example: A process tweak is already running and the change form is blank.
out: A note that stops the unofficial tweak until approval and an effective point exist.
related: work-instruction; traceability-lot

traceability-lot | Lot Traceability | trace exercise
job: Plan a lot trace from finished goods back to material, or the reverse, and record the breaks.
triggers: traceability; lot trace; mock recall; batch genealogy
inputs: The lot to trace; Systems involved; Time target; Known breaks
steps: Define the question: where did this lot go, or what went into it. || Use their systems. Do not invent genealogy. || Record every break where the link is missing. || Time the exercise. A trace that takes days is a finding if their target is hours. || Name the owner of each break. || Do not tell anyone to ship product they said is on hold.
anti: Invented genealogy; A trace that hides a break; Shipping a held lot
example: A mock recall stops because a component lot was never recorded.
out: A trace report that records the break, times the exercise, and assigns the recording gap.
related: nonconformance-report; inventory-accounting

gemba-walk | Gemba Walk | gemba notes
job: Plan a gemba walk that observes a process and asks why, without turning it into a compliance raid.
triggers: gemba walk; shop floor walk; go and see; process observation
inputs: The process to see; The question; Who will walk; How notes will be used
steps: Pick one process and one question. || Observe before suggesting. Write what you see, not a speech. || Ask why a deviation happens. The answer is information. || Do not use the walk to surprise-punish someone. Say how notes will be used. || Leave with one improvement the team agrees to try, or a clear open question. || Safety issues are stopped or escalated immediately under their rule.
anti: A compliance raid in disguise; Suggestions before observation; Ignoring a safety issue
example: A leader plans a walk to catch operators breaking the instruction.
out: A plan that observes the obstacle, bans surprise punishment, and still escalates safety issues.
related: continuous-improvement; shift-handover

scrap-and-rework | Scrap and Rework Review | scrap review
job: Review scrap and rework so the largest cause gets an owner, and numbers tie to the floor.
triggers: scrap review; rework; yield loss; waste review
inputs: Scrap quantities and reasons; Cost if known; Where it is found; The owner of the top reason
steps: Use their quantities. Do not invent a scrap rate. || Separate scrap from rework. They need different actions. || Rank causes. Attack the largest evidenced one. || Check whether the reason codes are honest or a dumping code. || Assign an owner. || Tie the number to inventory or quality records if they can. A side spreadsheet that does not tie is a finding.
anti: An invented yield; A dumping code ignored; No owner
example: Most scrap is coded 'other' and the team still wants a root cause.
out: A review that makes the dumping code the first problem and assigns an owner to fix the codes.
related: nonconformance-report; inventory-accounting

supplier-quality | Supplier Quality Note | supplier quality note
job: Write a supplier quality note that states the defect, the containment, and the evidence requested.
triggers: supplier quality; SCAR; supplier defect; vendor corrective action
inputs: The defect evidence; Lot information; Containment; What you are asking the supplier to do
steps: State the defect with evidence they have. || Identify lots without inventing shipment history. || Ask for containment and a cause, with a date. || Do not accuse fraud. Ask for facts. || Share only the data the supplier needs. || Link repeats to the scorecard.
anti: A fraud accusation with no evidence; Invented shipment history; A request with no date
example: A note calls the supplier negligent and does not describe the defect.
out: A note that describes the defect, requests containment by a date, and removes the insult.
related: supplier-scorecard; capa-plan
"""
))
