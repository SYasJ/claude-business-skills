from dense import pack
from scenario_bank import put

PACKS = []

PACKS.append(pack(
    {"id": "supply-chain", "title": "Supply chain", "summary": "Demand, inventory, suppliers, and shortages using the user's own lead times.", "keywords": ["supply-chain", "inventory", "suppliers", "logistics", "otif"]},
    """
supplier-risk-note | Supplier Risk Note | risk note
job: Note a supplier risk from the evidence the buyer has, without a mood score.
triggers: supplier risk; vendor risk; single source; supply risk
inputs: The supplier; The part; The evidence; The alternate if they have one
steps: State the part and the supplier. || Use only the miss, the lead time, or the single-source fact they showed. || If there is no alternate, say so. || Do not invent a financial score. || Recommend a cover action they can take this month. || Do not blame the supplier for a forecast they doubled.
anti: A credit score from memory; A risk color with no evidence; Ignoring buyer-caused misses
example: SKU 1044 has one supplier and a 28-day lead time. Last month they missed 14 units.
out: A note that names the single source and the 14-unit miss, with no invented score.
related: supplier-scorecard; shortage-playbook

lead-time-review | Lead Time Review | lead-time note
job: Compare the lead time in the system to the receipts the user can show.
triggers: lead time review; supplier lead time; system lead time wrong; receipt lag
inputs: The system lead time; Recent receipts; The buyer; The date the PO was placed
steps: Use receipt dates they have. || If they have fewer than three receipts, say the review is thin. || Do not average in a receipt they excluded. || Recommend a system change only if the gap repeats. || Name who edits the system. || Do not quietly pad the lead time with no receipt.
anti: A padded lead time with no receipts; One late truck treated as the new standard; No owner for the system field
example: The system says 14 days. Three receipts took 26, 28, and 27 days.
out: A note to change the system only after those three receipts are accepted as the pattern.
related: inventory-policy; supplier-scorecard

otif-review | OTIF Review | OTIF note
job: Review on-time-in-full from the shipments the user counted, split by cause.
triggers: OTIF; on time in full; supplier OTIF; delivery score
inputs: The shipments; Their on-time rule; Causes they coded; The target
steps: Count from their file. || Use their on-time rule, not a generic one. || Split buyer-caused late orders from supplier misses if they coded them. || Do not invent a penalty. || Compare to the target they set. || Name the largest cause.
anti: A score with no file; Penalties invented; Buyer lateness hidden
example: 94 shipments, 86 on time in full, target 95. 6 of the misses followed a same-week forecast change.
out: A review that reports 86 percent and separates those 6.
related: supplier-scorecard; demand-plan-review

sku-cut-review | SKU Cut Review | cut list
job: Propose SKUs to stop reordering from the movement and the stock the user shows.
triggers: SKU rationalization; what should we stop buying; dead stock; range cut
inputs: The SKUs; Units sold in their window; Stock on hand; A SKU they must keep
steps: Rank by the movement they showed. || A must-keep SKU stays even if it is slow. || Do not cut a SKU because a template says so. || Separate a seasonal item if they said it is seasonal. || Recommend stop-reorder, not a fake write-off. || Name who approves the cut.
anti: A cut list with no sales file; Cutting a protected SKU; A write-off invented as savings
example: Four SKUs sold zero in 90 days. One is a winter blade they must keep. Stock is still on the shelf.
out: A stop-reorder list of three, with the winter blade held.
related: inventory-policy; assortment-review

customs-packet-check | Customs Packet Check | packet check
job: Check a shipment packet for the documents the user says the lane requires.
triggers: customs documents; shipping packet; commercial invoice check; export packet
inputs: Their required list; Documents in the packet; The lane; Who files
steps: Compare the packet to their list. || Mark missing items. || Do not suggest a false description or a lower value. || Do not advise hiding goods. || Name who must complete a missing form. || This is a checklist, not a brokerage opinion.
anti: A false commodity description; A lowered value; A packet marked complete with a hole
example: A Calgary-to-US packet is missing the commercial invoice. Someone suggested describing the filters as samples.
out: A check that holds the packet and rejects the samples description.
related: landed-cost; logistics-exception

dock-exception-note | Dock Exception | dock note
job: Record a dock exception with the count, the PO, and the photo or tally they have.
triggers: dock exception; short shipment; receiving discrepancy; OS&D
inputs: The PO; The tally; The carrier; The photo or note
steps: Record counted versus billed. || Attach the PO line. || Do not accuse theft from a short count alone. || Say whether the trailer was sealed, if they noted it. || Name who tells the buyer. || Hold the difference out of available stock until it is resolved.
anti: Available stock increased to match the PO; A theft claim with no evidence; No PO line
example: PO 5521 said 40 filters. The tally is 32. The seal note says intact.
out: A note for 8 short, stock available 32, no theft claim.
related: logistics-exception; incoming-inspection
"""
))

put(
    "supplier-risk-note",
    "Note a supplier risk from the evidence the buyer has, without a mood score.",
    "Harbor Goods buys SKU 1044 cabin filters only from Redline Parts. Lead time is 28 days. In August they were short 14 units. There is no second supplier in the file.",
    """```text
supplier: Redline Parts
sku: 1044 cabin filter
lead time in system: 28 days
August miss: 14 units, receipt 28 Aug 2026
alternate: none on file
buyer-caused forecast change: not in this file
cover Diane can place: a 2-week bridge buy if she finds a second quote
```""",
    """**Risk note — SKU 1044**
Single source. 28-day lead time. August miss: 14 units. That is the evidence. No credit score is in the file, so none is written.

No alternate is on file. That is the risk, not a mood.
Cover this month: Diane gets one second quote, or she accepts the 28-day exposure. This note does not pick a vendor for her.
Do not add a forecast-blame line. None was in the file.""",
)

put(
    "lead-time-review",
    "Compare the lead time in the system to the receipts the user can show.",
    "The system lead time for Redline Parts on SKU 1044 is 14 days. Diane has three receipts: 26, 28, and 27 days from PO to dock.",
    """```text
system lead time: 14 days
receipts: PO 12 Jul to dock 7 Aug (26 days); PO 2 Aug to dock 30 Aug (28); PO 18 Aug to dock 14 Sep (27)
excluded: one air freight in June, she said it is not the pattern
who edits the system: Diane Cho
```""",
    """**Lead-time note**
Three ground receipts: 26, 28, 27 days. The system says 14. The gap repeats.
The June air freight stays out, as she asked.
Recommendation: Diane changes the system to 28 days, matching the slow receipt, not the average dressed up as exact.
Thin? No. Three receipts agree. Still her edit, not an automatic write.
Do not pad further without another receipt.""",
)

put(
    "otif-review",
    "Review on-time-in-full from the shipments the user counted, split by cause.",
    "Diane counted 94 shipments in August. 86 were on time in full. Her rule is on the promised day and full quantity. Target is 95 percent. She coded 6 misses to a same-week forecast change.",
    """```text
shipments: 94
on time in full: 86
rule: promised day and full quantity
target: 95 percent
coded buyer forecast change: 6 misses
other misses: 2, not coded
penalty clause: none in the file
```""",
    """**OTIF note — August**
86 of 94 is 91 percent, under her 95 percent target. Count is hers. I am not inventing a penalty.

| Misses | Code in her file |
| --- | --- |
| 6 | same-week forecast change |
| 2 | not coded |

Do not give the supplier all 8. Six are coded to the buyer. Two are open.
Next: Diane codes the two before any supplier meeting.""",
)

put(
    "sku-cut-review",
    "Propose SKUs to stop reordering from the movement and the stock the user shows.",
    "Four SKUs sold zero units in 90 days. One is a winter blade Diane says they must keep for November. All four still have stock on the shelf.",
    """```text
window: 16 Jun to 14 Sep 2026
SKU 1044 filters: 0 sold, 18 on hand
SKU 2201 wiper: 0 sold, 6 on hand
SKU 2208 mat: 0 sold, 4 on hand
SKU 3310 winter blade: 0 sold, 20 on hand, must keep for November
approver: Diane
```""",
    """**Stop-reorder**
| SKU | Sold | On hand | Call |
| --- | --- | --- | --- |
| 1044 | 0 | 18 | stop reorder |
| 2201 | 0 | 6 | stop reorder |
| 2208 | 0 | 4 | stop reorder |
| 3310 | 0 | 20 | keep, winter |

This is not a write-off and not a savings number. Stock stays on the shelf until she decides a clearance. Approver: Diane.""",
)

put(
    "customs-packet-check",
    "Check a shipment packet for the documents the user says the lane requires.",
    "A packet for filters from Calgary to a US customer is missing the commercial invoice. A note in the folder suggests describing them as samples so the value line can be blank.",
    """```text
lane: Calgary to US customer, her required list
required: commercial invoice, packing list, COO if the customer asked
in the packet: packing list, no invoice, no COO ask on file
suggestion in the folder: call them samples
value on the PO: 40 filters, $18 each
who files: the forwarder, after her packet is complete
```""",
    """**Packet check**
Hold. The commercial invoice is missing.
Do not describe the filters as samples. The PO says 40 filters at $18. A false description is not a fix.
COO: not required in her list for this shipment. Do not add one to look busy.
Who completes the invoice: Diane, then the forwarder files. This check is not a brokerage opinion.""",
)

put(
    "dock-exception-note",
    "Record a dock exception with the count, the PO, and the photo or tally they have.",
    "PO 5521 billed 40 filters. The dock tally is 32. The seal note says intact. No photo. Diane needs the exception before the 32 are marked as 40 in stock.",
    """```text
PO: 5521
billed: 40 of SKU 1044
tally: 32
seal: noted intact
photo: none
carrier: Kite Freight
date: 14 Sep 2026
```""",
    """**Dock note — PO 5521**
Short 8. Available stock from this receipt: 32, not 40.
Seal was noted intact. That is not a theft finding. No photo is in the file.
Tell the buyer: Diane. Tell the carrier: after she sends this count, not before.
Do not raise available stock to match the PO while the 8 are open.""",
)

PACKS.append(pack(
    {"id": "oil-gas", "title": "Oil and gas operations", "summary": "Production, nominations, and site notes for operators. Not a permit and not a way around a safety control.", "keywords": ["oil", "gas", "production", "nomination", "hse"]},
    """
production-variance | Production Variance | variance note
job: Compare produced volumes to the nomination using the meters the user provides.
triggers: production variance; actual versus nomination; daily production; volume miss
inputs: The nomination; The meter volumes; The day; Who explains the gap
steps: Use their meters. || Show nomination, actual, and gap. || Do not invent a reservoir cause. || Separate a meter they flagged as bad. || Name the person who explains a gap over their threshold. || Do not adjust a number to match the nomination.
anti: A volume changed to match the nom; A cause with no meter; A bad meter treated as good
example: Pad 14-22 was nominated at 4.2 mmcf and metered at 3.6. The meter note is clean.
out: A variance of 0.6 with no invented cause.
related: gas-nomination; gas-balance

turnaround-ready | Turnaround Readiness | readiness note
job: Check a turnaround checklist against the items the site says must be done before isolation.
triggers: turnaround readiness; shutdown ready; outage checklist; TA ready
inputs: Their checklist; Items still open; The start date; The isolation owner
steps: List open items. || A start date does not close an item. || Isolation and lockout stay with the named owner. || Do not tell anyone to skip a hold point. || Separate materials from permits. || Recommend a slip if a safety item is open.
anti: A start with an open isolation item; A skipped hold; A percent complete with open safety items
example: Monday's start has two open items: a permit signature and a blind list.
out: A note that Monday does not start until those two are closed.
related: isolation-work-plan; hse-observation

hse-observation | HSE Observation | observation log
job: Log a safety observation in the words the observer used, with the immediate step they took.
triggers: HSE observation; safety observation; near miss log; site observation
inputs: What they saw; Where; The immediate step; Who owns the follow-up
steps: Use their words for what they saw. || Do not diagnose a medical outcome. || Record the immediate step. || Name the follow-up owner. || Do not name a worker in a wide report if they asked not to. || Do not bury a stop-work in soft language.
anti: A medical diagnosis; A stop-work rewritten as a suggestion; No owner
example: An observer stopped a job because a lock was missing. The draft calls it a coaching moment.
out: A log that says the job was stopped for a missing lock.
related: turnaround-ready; safety-toolbox-talk

gas-nomination | Gas Nomination | nomination check
job: Check a nomination against the confirmed volume and the cycle time the user states.
triggers: gas nomination; nom cycle; pipeline nomination; confirm the nom
inputs: The cycle deadline; The volume they will nominate; The confirmed production; Who submits
steps: Compare the nom to the confirmed volume. || A wish volume is labeled a wish. || Record the cycle deadline in their time zone. || Do not submit a nom after the deadline and call it on time. || Name the submitter. || Flag a gap over their threshold.
anti: A late nom called on time; A wish volume submitted as confirmed; No submitter
example: The cycle closes at 11:00. The confirmed volume is 3.6. The draft nom is 4.2.
out: A check that holds 4.2 and names 3.6 as the confirmed figure.
related: production-variance; gas-balance

flare-volume-note | Flare Volume Note | flare note
job: Report flare volumes from the meter the user has, with the reason code they supplied.
triggers: flare report; flaring volume; flare log; gas flared
inputs: The meter; The volume; The reason code they use; The period
steps: Use the meter volume. || Use their reason code. Do not invent a regulatory factor. || If the meter was down, say the volume is missing. || Do not estimate a flare to fill a report. || Name who signs the report. || This is not an emissions assurance opinion.
anti: An estimated flare presented as metered; A factor from memory; A down meter called zero
example: The flare meter was down on 12 September. A draft enters zero.
out: A note that leaves the 12th blank and rejects zero.
related: emissions-inventory-brief; production-variance

site-induction-brief | Site Induction Brief | induction brief
job: Brief a contractor on the site rules the user listed, including what they must not bypass.
triggers: site induction; contractor induction; site rules; orientation brief
inputs: The rules they listed; Required tickets; The muster point; Who stops a job
steps: List only rules they provided. || Name the tickets required before entry. || State the muster point. || Say who can stop a job. || Do not shorten a lockout rule. || Do not add a rule you remember from another site.
anti: A shortened lockout rule; Entry without the ticket they require; Muster left blank
example: A draft induction drops the lockout step to save ten minutes.
out: A brief that keeps the lockout step and the muster point.
related: hse-observation; isolation-work-plan

spill-notice | Spill Notice | notice draft
job: Draft the internal notice for a release the user has already described, with the facts they have.
triggers: spill notice; release notification draft; incident notice; what do we report internally
inputs: What they saw; When; Where; Who has already been told
steps: Use their description. Do not add a volume they did not measure. || Record the time and place. || List who has been told. || Do not write language that hides the release. || Do not give cleanup chemistry or a way to avoid a report. || Say which facts are still unknown.
anti: A hidden release; An invented volume; Cleanup instructions that bypass the site procedure
example: A draft says 'minor sheen, no need to log' and nobody measured the area.
out: A notice that logs the sheen, leaves the volume unknown, and does not say it need not be logged.
related: hse-observation; outage-communication

gas-balance | Gas Balance | balance note
job: Balance inlet, sales, fuel, and flare from the meters the user provides.
triggers: gas balance; inlet sales fuel flare; volume balance; plant balance
inputs: Inlet; Sales; Fuel; Flare; Their tolerance
steps: Add the outlets they gave. || Compare to inlet. || A gap inside tolerance is still shown. || A missing meter is a gap, not a zero. || Do not force the balance. || Name who explains a gap over tolerance.
anti: A forced balance; A down meter entered as zero; A gap hidden inside fuel
example: Inlet 10.0, sales 8.1, fuel 0.4, flare meter down. Tolerance is 0.3.
out: A balance that will not close and does not put the gap in fuel.
related: production-variance; flare-volume-note
"""
))

put(
    "production-variance",
    "Compare produced volumes to the nomination using the meters the user provides.",
    "Devon has Tuesday's numbers for pad 14-22. The nomination was 4.2 mmcf. The meter, which he flagged as clean, read 3.6. He wants the variance without a reservoir story.",
    """```text
day: 16 Sep 2026
pad: 14-22
nomination: 4.2 mmcf
meter: 3.6 mmcf
meter note: clean, no fault flag
threshold for a call: 0.3 mmcf
who explains: Devon Hale
```""",
    """**Variance — pad 14-22, 16 September**
Nomination 4.2. Meter 3.6. Gap 0.6. Over his 0.3 threshold.
Meter note is clean, so this note does not blame the meter and does not invent a reservoir cause.
No adjustment to make 3.6 look like 4.2.
Next: Devon writes the explanation. This note only records the gap.""",
)

put(
    "turnaround-ready",
    "Check a turnaround checklist against the items the site says must be done before isolation.",
    "The plant turnaround is on the board for Monday 22 September. Two items are open: a permit signature and the blind list. The isolation owner is Devon.",
    """```text
start on the board: Mon 22 Sep 2026
open: permit signature, blind list
closed: materials on site, scaffold tagged
isolation owner: Devon Hale
percent a slide showed: 90 percent
```""",
    """**Readiness**
Monday does not start. Two items are open, and one of them is the blind list.

| Item | Status |
| --- | --- |
| Permit signature | open |
| Blind list | open |
| Materials | closed |
| Scaffold tag | closed |

The 90 percent slide does not close a safety item. Isolation stays with Devon. Nobody skips the blind list to hold the date.""",
)

put(
    "hse-observation",
    "Log a safety observation in the words the observer used, with the immediate step they took.",
    "An observer stopped a job at pad 14-22 because a lock was missing on a valve. A draft for the weekly pack calls it a coaching moment and names the worker.",
    """```text
when: 15 Sep 2026 10:20
where: pad 14-22, valve on the fuel gas line
what they saw: no lock, job in progress
immediate step: job stopped
observer asked: do not name the worker in the wide pack
follow-up owner: Devon Hale
```""",
    """**Observation**
15 September, 10:20, pad 14-22. No lock on the fuel-gas valve. Job was in progress. The job was stopped.
This is a stop-work, not a coaching moment.
Worker name: omitted from the wide pack, as asked.
Follow-up owner: Devon Hale. The lock stays the issue until he closes it.
No medical description. None was reported.""",
)

put(
    "gas-nomination",
    "Check a nomination against the confirmed volume and the cycle time the user states.",
    "The cycle closes at 11:00 America/Edmonton. Confirmed production for the pad is 3.6 mmcf. A draft nomination still says 4.2. It is 10:40.",
    """```text
cycle deadline: 11:00 America/Edmonton, 16 Sep 2026
now: 10:40
confirmed: 3.6 mmcf
draft nom: 4.2 mmcf
submitter: Devon Hale
threshold: 0.3
```""",
    """**Nomination check**
Do not submit 4.2. Confirmed is 3.6. The gap is 0.6, over his threshold.
4.2 is a wish from yesterday's nom. It is not confirmed production.
There is time before 11:00 to submit 3.6. A nom after 11:00 is late. Do not call it on time.
Submitter: Devon.""",
)

put(
    "flare-volume-note",
    "Report flare volumes from the meter the user has, with the reason code they supplied.",
    "The flare meter was down on 12 September. A draft report enters zero so the month still adds up. Devon has a reason code for a compressor trip on the 11th, when the meter worked.",
    """```text
period: 11 and 12 Sep 2026
11 Sep: meter 0.18 mmcf, reason code CT-compressor, his code
12 Sep: meter down, no reading
draft: 12 Sep entered as 0
signer: Devon Hale
```""",
    """**Flare note**
11 September: 0.18 mmcf, reason CT-compressor, from his code. Use that.
12 September: blank. The meter was down. Zero is rejected. An estimate is not in this note.
This is not an emissions-factor calculation and not an assurance opinion.
Signer: Devon, after the 12th stays blank or a real reading replaces it.""",
)

put(
    "site-induction-brief",
    "Brief a contractor on the site rules the user listed, including what they must not bypass.",
    "A contractor starts Thursday. Their draft induction drops the lockout step to save ten minutes. The site rules Devon sent include lockout, a muster point at the south gate, and a H2S ticket before entry.",
    """```text
start: Thu 18 Sep 2026
rules he sent: lockout before any line is opened, muster south gate, stop-work authority is any person on site
ticket required: H2S, checked at the gate
draft change: drop lockout to save 10 minutes
```""",
    """**Induction brief**
Before entry: H2S ticket checked at the gate. No ticket, no entry.
Lockout stays in the brief. It is not cut to save ten minutes.
Muster: south gate.
Who can stop a job: any person on site.
This brief uses his list only. It does not add another site's rules, and it does not shorten his.""",
)

put(
    "spill-notice",
    "Draft the internal notice for a release the user has already described, with the facts they have.",
    "A night operator saw a sheen at the pad flare knock-out at 02:10. Nobody measured the area. A draft says it was minor and does not need a log.",
    """```text
what was seen: sheen, flare knock-out, pad 14-22
when: 16 Sep 2026 02:10
measured volume: none
already told: night lead, by radio at 02:15
draft line: minor, no need to log
```""",
    """**Notice**
Sheen seen at the flare knock-out, pad 14-22, 02:10 on 16 September. Volume: unknown. Do not write a litre figure.
Already told: night lead, radio, 02:15.
The line 'no need to log' comes out. This notice is the log.
Unknown: area, cause, whether it left the pad. Leave them unknown.
This draft does not tell anyone how to clean it up or how to avoid a report.""",
)

put(
    "gas-balance",
    "Balance inlet, sales, fuel, and flare from the meters the user provides.",
    "Devon's plant day: inlet 10.0, sales 8.1, fuel 0.4, flare meter down. His tolerance is 0.3. A colleague wants the gap parked in fuel so the day closes.",
    """```text
day: 15 Sep 2026
inlet: 10.0 mmcf
sales: 8.1
fuel: 0.4
flare: meter down, no reading
tolerance: 0.3
who explains a miss: Devon Hale
```""",
    """**Balance — 15 September**
Outlets that can be added: sales 8.1 plus fuel 0.4 = 8.5. Inlet 10.0. Gap 1.5, and the flare meter is missing.
Do not put 1.5 into fuel. Do not enter flare as zero.
The day does not close. Tolerance is 0.3. This gap is over it even before flare is known.
Next: Devon. The note does not force a balance.""",
)

PACKS.append(pack(
    {"id": "automotive", "title": "Automotive", "summary": "Dealer, service, and recall notes. Not a safety-system repair procedure and not a recall determination.", "keywords": ["automotive", "dealer", "service", "recall", "fleet"]},
    """
dealer-morning-review | Dealer Morning Review | morning note
job: Set the service morning from the appointments and the parts the dealer can see.
triggers: dealer morning; service morning huddle; shop board; advisor huddle
inputs: Today's appointments; Parts not in; Techs on shift; A job that must not be promised
steps: List appointments they can start. || Hold jobs whose parts are not in. || Match techs on shift, not the full roster. || Do not promise a same-day finish the parts cannot support. || Name the advisor who calls the customer. || Do not invent a capacity number.
anti: A promise with parts missing; A tech counted who is off; A full board that cannot be worked
example: 14 appointments, 2 techs in, brake parts for RO 4418 are not in.
out: A board that holds 4418 and does not promise it today.
related: service-lane-plan; parts-backorder-note

service-lane-plan | Service Lane Plan | lane plan
job: Plan the lane so promised times match the techs and the parts on hand.
triggers: service lane; promise time; shop capacity; lane plan
inputs: Promise times; Tech hours; Parts status; Jobs that are waiting on approval
steps: Add the hours they estimated. || Compare to tech hours on shift. || A job with parts missing gets no promise time. || Waiting-on-approval does not take a bay. || Do not pull a safety recall forward of a booked job unless they said to. || Name the overflow.
anti: Promise times that exceed the shift; A bay held for an unapproved job; A made-up efficiency rate
example: Promised hours are 22. Two techs have 16 hours. Three jobs have no parts.
out: A plan that cuts the board to 16 hours and parks the parts-missing jobs.
related: dealer-morning-review; parts-backorder-note

recall-owner-note | Recall Owner Note | owner note
job: Draft the customer note for a recall using the notice the dealer has, not a homemade defect claim.
triggers: recall letter; recall customer note; campaign notice; owner notification
inputs: The notice; The VINs they have; The remedy the notice states; What they must not add
steps: Use the notice wording for the defect and the remedy. || List only VINs they matched. || Do not add a failure rate. || Do not tell the owner to keep driving if the notice says park. || Say how to book. || This note does not decide that a recall exists.
anti: A homemade defect claim; A VIN that did not match; Advice that contradicts the notice
example: Notice 26-118 says park the vehicle. A draft tells the owner they can drive until the part arrives.
out: A note that repeats the park instruction and the booking path.
related: dealer-morning-review; warranty-file-review

parts-backorder-note | Parts Backorder | backorder note
inputs: The RO; The part; The promise date; The customer promise already made
job: Tell the advisor what to say when a part is not in and a promise date is already on the RO.
triggers: parts backorder; part not in; customer waiting on a part; ETA
steps: State the part and the RO. || Use the ETA they have. If none, say none. || Do not invent a delivery date. || Compare to the promise already made. || Give the advisor one sentence for the customer. || Offer a loaner only if they said one is available.
anti: An invented ETA; A loaner that does not exist; A promise left unchanged when parts slipped
example: RO 4418 brakes were promised today. The pads are backordered with no ETA.
out: A sentence that pulls today's promise and does not invent a date.
related: service-lane-plan; dealer-morning-review

warranty-file-review | Warranty File Review | file review
job: Check a warranty file for the documents their checklist requires before it is submitted.
triggers: warranty file; claim packet; warranty submission; OEM claim
inputs: Their checklist; Documents in the file; The failed part; The tech notes
steps: Compare to their checklist. || A missing photo or code is a hole. || Do not write a cause the tech did not write. || Do not change the odometer. || Name who submits. || This review does not decide goodwill.
anti: A cause the tech did not write; An altered odometer; A file marked ready with a hole
example: The file has no photo of the failed pad and the cause line is blank.
out: A review that holds the claim until the photo and the tech's cause are in.
related: recall-owner-note; service-lane-plan

fleet-replace-note | Fleet Replacement Note | replacement note
job: Compare fleet units the user listed on age, cost, and downtime, without a forced replacement.
triggers: fleet replacement; which vans to replace; unit replacement; fleet plan
inputs: The units; Age or kilometres they have; Downtime; The budget they named
steps: Rank only on the figures they gave. || A unit with no downtime stays unranked on that column. || Do not invent a residual value. || Stay inside the budget count they named. || Separate a safety hold from a cost preference. || Name who approves the order.
anti: An invented residual; A safety hold delayed for budget optics; A full fleet replacement they cannot fund
example: They can replace two vans. Three are old. One is on a safety hold for brakes.
out: A note that puts the safety-hold van first and leaves the third unfunded.
related: dealer-morning-review; parts-backorder-note

handover-checklist-auto | Vehicle Handover | handover checklist
job: Check a handover against the items the dealer says the customer must see.
triggers: vehicle handover; delivery checklist; customer delivery; new car handover
inputs: Their handover list; Items done; The recall status they checked; The salesperson
steps: Walk their list. || A missed item is open. || Recall status is whatever the check showed, including not checked. || Do not say a recall is clear if they did not run it. || Name who hands over the keys. || Do not skip a safety item to make a delivery time.
anti: Keys handed over with an open safety item; A recall marked clear without a check; A checklist copied as done
example: The car is due at 3 p.m. The recall check was not run. The draft marks it clear.
out: A checklist that blocks the keys until the recall check is actually run.
related: recall-owner-note; dealer-launch-check

dealer-launch-check | Dealer Launch Check | launch check
job: Check whether a local launch day has the cars, the staff, and the offer the dealer can honor.
triggers: dealer launch; model launch day; sales event ready; launch checklist
inputs: Cars on the ground; Staff roster; The offer; The date
steps: Count cars they can demo. || Match staff to the date. || The offer must be one they can honor on the day. || Do not advertise a payment they did not calculate. || Hold the event claim if the cars are in transit. || Name the owner.
anti: An ad for cars that are not on the ground; A payment invented for the ad; Staff who are not rostered
example: The ad says six test-drive cars. Two are on the ground. The payment in the ad was not calculated.
out: A check that cuts the ad to two cars and removes the payment.
related: dealer-morning-review; local-service-offer
"""
))

put(
    "dealer-morning-review",
    "Set the service morning from the appointments and the parts the dealer can see.",
    "Bright Axle has 14 appointments today and 2 techs on shift. RO 4418 is a brake job. The pads are not in. Carla needs the board before 7:30.",
    """```text
date: 16 Sep 2026
appointments: 14
techs on shift: 2
off: 1 tech
RO 4418: brake pads not in, customer was told today
advisor who calls: Carla Singh
```""",
    """**Morning board**
Do not promise RO 4418 today. Pads are not in. Carla calls before 8:00.
Techs on the board: 2. The third name stays off.
The other appointments stay only if parts are in. This note does not invent a capacity number beyond those two techs.
Next: Carla, the 4418 call.""",
)

put(
    "service-lane-plan",
    "Plan the lane so promised times match the techs and the parts on hand.",
    "Promised hours on today's board are 22. Two techs have 8 hours each. Three jobs, including RO 4418, have no parts. Two more are waiting on customer approval.",
    """```text
promised hours: 22
tech hours: 16
parts missing: RO 4418, RO 4422, RO 4430
waiting on approval: RO 4401, RO 4404
loaner: none free
```""",
    """**Lane plan**
Work up to 16 hours. The 22-hour promise does not fit the shift.
Park 4418, 4422, and 4430. No parts, no promise time.
4401 and 4404 do not take a bay until the customer approves.
No loaner is offered. None is free.
Overflow: Carla calls the three parts-missing customers. She does not pull a recall ahead of a booked job. Nobody asked for that.""",
)

put(
    "recall-owner-note",
    "Draft the customer note for a recall using the notice the dealer has, not a homemade defect claim.",
    "Notice 26-118 says park the vehicle and wait for the remedy. Bright Axle matched two VINs. A draft tells those owners they can keep driving until the part arrives.",
    """```text
notice: 26-118
remedy in the notice: park, wait for the part, dealer will call
VINs matched: 2, both in her sold file
failure rate: not in the notice
booking: Carla's desk, 403-555-0199
draft line: you can drive until the part arrives
```""",
    """**Owner note**
Notice 26-118 says park the vehicle. This note repeats that. It does not say they can keep driving.

We matched two VINs in our file. This note goes to those two owners only.
The notice does not give a failure rate. None is added.
To book: call Carla's desk, 403-555-0199.
This note does not decide that a recall exists. It follows the notice they have.""",
)

put(
    "parts-backorder-note",
    "Tell the advisor what to say when a part is not in and a promise date is already on the RO.",
    "RO 4418 was promised today. The brake pads are backordered. The supplier ETA field is blank. No loaner is free.",
    """```text
RO: 4418
part: front pads
promise already made: today, 16 Sep 2026
ETA: blank
loaner: none free
advisor: Carla Singh
```""",
    """**What Carla can say**
The pads for RO 4418 are not in. I do not have a date. I am pulling today's promise.

Do not add a Friday ETA. The field is blank.
Do not offer a loaner. None is free.
Next: Carla makes the call. The RO promise date comes off today's board.""",
)

put(
    "warranty-file-review",
    "Check a warranty file for the documents their checklist requires before it is submitted.",
    "A warranty file for the failed pads has the RO and the odometer. The photo is missing. The cause line is blank. A clerk offered to write 'worn' so the claim can go tonight.",
    """```text
checklist: RO, odometer, photo of failed part, tech cause line
in the file: RO 4418, odometer 61240
missing: photo, tech cause
offered wording: worn
submitter: Carla, not the clerk
```""",
    """**File review**
Hold. Photo missing. Cause line blank.
Do not type 'worn'. The tech did not write it. Do not touch the odometer.
Submitter is Carla, after the photo and the tech's own words are in the file.
This review does not grant goodwill and does not submit the claim.""",
)

put(
    "fleet-replace-note",
    "Compare fleet units the user listed on age, cost, and downtime, without a forced replacement.",
    "Harbor Goods can replace two vans this year. Three are old. Van 4 is on a safety hold for brakes. No residual values are in the file.",
    """```text
budget count: 2
van 2: 11 years, downtime 6 days this quarter
van 4: 9 years, safety hold, brakes, downtime 14 days
van 7: 12 years, downtime not recorded
residual values: none in the file
approver: Diane Cho
```""",
    """**Replacement note**
First: van 4. It is on a safety hold. Budget optics do not delay that.
Second: van 2, because downtime is in the file: 6 days.
Van 7: unranked on downtime. The cell is empty. It is the one that stays if only two can be ordered.
No residual is in this note. None was supplied.
Approver: Diane. This is not a purchase order.""",
)

put(
    "handover-checklist-auto",
    "Check a handover against the items the dealer says the customer must see.",
    "A delivery is booked for 3 p.m. The handover list includes a recall check. It was not run. The draft checklist marks recall clear so the keys can go.",
    """```text
delivery: 16 Sep 2026 15:00
list: walkaround, recall check, second key, payment receipt
done: walkaround, second key
not done: recall check
payment receipt: in the file
salesperson: Jon
draft mark: recall clear
```""",
    """**Handover**
Keys do not go at 3 p.m. The recall check was not run. Clear is a false mark. Remove it.
Done: walkaround, second key, payment receipt in the file.
Open: recall check.
Who hands the keys after the check: Jon. Not before.""",
)

put(
    "dealer-launch-check",
    "Check whether a local launch day has the cars, the staff, and the offer the dealer can honor.",
    "Saturday's ad says six cars to test-drive and a $299 payment. Two cars are on the ground. The payment was not calculated. Four staff are rostered.",
    """```text
date: Sat 20 Sep 2026
ad: 6 test-drive cars, $299 a month
on the ground: 2
in transit: 4, no arrival date
staff rostered: 4
payment worksheet: none
owner: Carla Singh
```""",
    """**Launch check**
Cut the ad to two test-drive cars. The other four are not on the ground.
Remove $299. Nobody calculated it.
Staff: four are rostered. That part can stand.
Owner: Carla. She does not run the six-car line on Saturday.""",
)
