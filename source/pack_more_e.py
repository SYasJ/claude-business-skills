from dense import pack
from scenario_bank import put

PACKS = []

PACKS.append(pack(
    {"id": "airline", "title": "Airline operations", "summary": "Irregular operations, delays, and station notes. Not a way around duty limits or a maintenance release.", "keywords": ["airline", "station", "delay", "irrops", "baggage"]},
    """
irrops-brief | Irregular Ops Brief | ops brief
job: Brief the station on a disrupted flight using the facts the controller has.
triggers: irregular operations; IRROPS; disrupted flight; station brief
inputs: The flight; The reason they can state; Passengers booked; What is not known
steps: State the flight and the time. || Use only the reason they have. || Count passengers from their figure. || Say what the station can do today. || Do not invent a crew or a spare aircraft. || Name the next update time.
anti: A cause they do not have; A spare aircraft that is not assigned; A passenger count from memory
example: KA412 is late. The only fact is a ground hold. A draft blames maintenance.
out: A brief that says ground hold and drops the maintenance line.
related: delay-message; station-turn-note

delay-message | Delay Message | passenger message
job: Write the passenger message from the delay facts the station can say.
triggers: delay message; passenger announcement; flight delay text; gate announcement
inputs: The flight; The new time if they have one; The reason they may say; Care they are allowed to offer
steps: Lead with the flight and the time. || If the new time is unknown, say unknown. || Use only the reason they authorized. || Offer only the care they listed. || Do not promise a connection. || Do not blame a person.
anti: A fake new time; A hotel they cannot offer; A connection promise
example: KA412 has no new departure. A draft says 18:40 and a free hotel.
out: A message that says the new time is unknown and drops the hotel.
related: irrops-brief; disruption-message

crew-duty-limit | Crew Duty Check | duty check
job: Check a duty figure against the limit the user provides. Do not advise exceeding it.
triggers: crew duty; duty limit; pairing hours; crew legality check
inputs: The hours they calculated; The limit they stated; The pairing; Who releases the crew
steps: Compare their hours to their limit. || If they are over, say stop. || Do not suggest a workaround. || If the hours are incomplete, say the check cannot pass. || Name who releases the crew. || This is not a regulatory opinion beyond the limit they stated.
anti: A workaround over the limit; A pass with incomplete hours; A homemade legal opinion
example: The pairing is 14 hours. The limit they stated is 13. A note asks how to make it legal.
out: A check that says stop, with no workaround.
related: irrops-brief; station-open-check

station-turn-note | Station Turn Note | turn note
job: Record a turn delay with the minute it started and the cause the ramp lead wrote.
triggers: turnaround delay; aircraft turn; gate delay; ramp delay
inputs: The flight; The scheduled turn; The actual; The cause they wrote
steps: Show scheduled and actual. || Use their cause words. || Do not add a department to blame. || Note if the next flight is the same aircraft. || Name who updates control. || Do not hide a minute to protect a target.
anti: A cause rewritten to protect a target; Missing minutes; Blame with no note
example: The turn was 55 minutes against 40. The ramp note says a late bag cart. A draft says cabin cleaning.
out: A note that keeps the bag cart and the 15 minutes.
related: irrops-brief; route-result-note

route-result-note | Route Result | route note
job: Report a route day from the flights and the loads the user exported.
triggers: route performance; flight results; load factor note; route day
inputs: The flights; The loads; The cancellations; The target they use
steps: Count flights from the export. || A cancellation stays a cancellation. || Do not invent a yield. || Compare load to their target only if both are in the file. || Name the worst flight by their metric. || Do not drop a cancel to improve the day.
anti: A dropped cancellation; An invented yield; A target they did not set
example: Four flights, one cancel, loads 80, 91, and 70 on the three that flew. Target load 85.
out: A day note that keeps the cancel and does not average it away.
related: irrops-brief; saas-weekly-metrics

baggage-irregularity | Baggage Irregularity | bag note
job: Record a bag irregularity with the tag, the flight, and the status they know.
triggers: baggage claim; delayed bag; bag irregularity; lost bag file
inputs: The tag; The flight; The status; What the passenger was told
steps: Record the tag and the flight. || Use the status they know: delayed, not lost, unless they said lost. || Do not promise a delivery hour they do not have. || Match the passenger message to the status. || Name the owner of the file. || Do not ask for a passport number in the note.
anti: Lost written when the status is delayed; A delivery hour invented; Identity documents in the note
example: Tag 8812 is delayed off KA412. A text told the passenger it would be at the house by 8 p.m.
out: A file that says delayed, and a correction that 8 p.m. was not known.
related: delay-message; customer-communication-incident

station-open-check | Station Open Check | open check
job: Check the station open items against the list the station uses.
triggers: station opening; open checklist; first wave; station ready
inputs: Their open list; Items done; The first wave; Who signs
steps: Walk their list. || A fuel or security item left open blocks the first wave. || Do not mark an item done because the time has arrived. || Name the signer. || Separate a commercial item from a safety item. || Do not skip a check to make the first departure.
anti: A safety item marked done by the clock; A first wave released against an open check; No signer
example: Fuel paperwork is open. The first wave is KA188 at 06:10. A draft says open the station anyway.
out: A check that holds KA188 until the fuel item is signed.
related: crew-duty-limit; irrops-brief

disruption-message | Disruption Message | disruption note
job: Write the customer message for a cancellation with the rebooking fact they have.
triggers: cancellation message; disruption text; flight cancelled note; rebooking message
inputs: The flight; The rebooking they can offer; Care they can offer; What they cannot promise
steps: Say the flight is cancelled. || Offer only the rebooking in the file. || Say if no seat is confirmed. || Care follows their rule. || Do not promise a refund amount. || Do not blame crew or maintenance unless they authorized that reason.
anti: A confirmed seat that is not confirmed; A refund amount invented; A cause they did not authorize
example: KA188 is cancelled. No seat is confirmed. A draft promises the 10:00 and a full refund.
out: A message that says cancelled, no seat yet, and no refund figure.
related: delay-message; irrops-brief
"""
))

put(
    "irrops-brief",
    "Brief the station on a disrupted flight using the facts the controller has.",
    "KA412 YYZ-YYC is late. The controller's note says a ground hold. A draft brief blames maintenance. Booked passengers are 142. No spare aircraft is assigned.",
    """```text
flight: KA412 YYZ-YYC
fact: ground hold, note timed 16 Sep 2026 14:05
passengers booked: 142
spare aircraft: none assigned
next update promised: 15:00
station: YYC, Luis Ortega
```""",
    """**Station brief — KA412**
Ground hold. That is the reason in the note. Maintenance comes out of the draft.
Passengers booked: 142.
No spare is assigned. Do not tell the station one is coming.
Next update: 15:00. Luis owns the board until then.""",
)

put(
    "delay-message",
    "Write the passenger message from the delay facts the station can say.",
    "Gate staff want a message for KA412. There is no new departure time. A draft says 18:40 and a free hotel. The station may offer water. It may not offer a hotel.",
    """```text
flight: KA412
new time: unknown
reason authorized: ground hold
care authorized: water at the gate
care not authorized: hotel, meal voucher
connections: not confirmed
```""",
    """**Gate message**
KA412 is delayed for a ground hold. We do not have a new departure time.

Water is available at the gate. We cannot confirm a connection on this message.

**Not in the message**
18:40. A hotel. A meal voucher. A person to blame.""",
)

put(
    "crew-duty-limit",
    "Check a duty figure against the limit the user provides. Do not advise exceeding it.",
    "A pairing is calculated at 14 hours. The limit Luis was given for this duty is 13. Someone asked how to make the pairing legal.",
    """```text
pairing: KA412 turn plus KA188
hours calculated: 14
limit stated: 13
hours complete: yes, his sheet
release owner: crew scheduling, not the station agent
ask: how to make it legal
```""",
    """**Duty check**
Stop. 14 is over the 13 they stated.
No workaround is in this check. Do not split, waive, or reword the hours to pass.
Release sits with crew scheduling. The station does not release this pairing.
This is not a regulatory opinion beyond the limit in the file.""",
)

put(
    "station-turn-note",
    "Record a turn delay with the minute it started and the cause the ramp lead wrote.",
    "KA412's turn was scheduled at 40 minutes and took 55. The ramp note says the bag cart was late. A draft blames cabin cleaning so the ramp target holds.",
    """```text
flight: KA412
scheduled turn: 40 minutes
actual: 55
ramp note: late bag cart
draft cause: cabin cleaning
same aircraft next: KA188
who updates control: Luis Ortega
```""",
    """**Turn note**
55 against 40. Fifteen minutes. Cause in the ramp note: late bag cart.
Cabin cleaning is not in the note. It does not replace the cart.
Next flight on the same aircraft: KA188. Control needs the 15 minutes, not a cleaned-up cause.
Updater: Luis.""",
)

put(
    "route-result-note",
    "Report a route day from the flights and the loads the user exported.",
    "Luis exported 16 September for the YYC routes he watches. Four flights were planned. One cancelled. The three that flew had loads of 80, 91, and 70 percent. His target is 85. No yield is in the export.",
    """```text
day: 16 Sep 2026
planned: 4
cancelled: KA188
flew: loads 80, 91, 70
target load: 85
yield: not in the export
```""",
    """**Route day**
Four planned. KA188 cancelled. Do not drop it to make the day look full.

| Flight | Load |
| --- | --- |
| three that flew | 80, 91, 70 |
| target | 85 |
| KA188 | cancelled |

Two of the three that flew are under 85. No yield is in this note.
Worst by his metric: the cancel, then the 70.""",
)

put(
    "baggage-irregularity",
    "Record a bag irregularity with the tag, the flight, and the status they know.",
    "Tag 8812 did not arrive on KA412. Status in the system is delayed. A text already told the passenger the bag would be at the house by 8 p.m. Nobody has a delivery time.",
    """```text
tag: 8812
flight: KA412
status: delayed
passenger told: at the house by 20:00
delivery time on file: none
owner: station baggage desk
passport number: do not collect
```""",
    """**Bag file — 8812**
Status: delayed, off KA412. Do not write lost.
The 20:00 house delivery was not known. Send a correction: we do not have a delivery time.
Owner: the baggage desk.
Do not put a passport number in this file.""",
)

put(
    "station-open-check",
    "Check the station open items against the list the station uses.",
    "The first wave is KA188 at 06:10. Fuel paperwork is still open. A draft says open the station because the clock says 05:40.",
    """```text
first wave: KA188 at 06:10
open: fuel paperwork
done: security walk, gate screens
signer required: Luis Ortega
draft: open anyway, it is 05:40
```""",
    """**Open check**
Hold KA188. Fuel paperwork is open. The clock does not close it.
Done: security walk, gate screens.
Signer: Luis. He does not sign the fuel line blank.
A commercial wish to leave on time is not a reason to skip the check.""",
)

put(
    "disruption-message",
    "Write the customer message for a cancellation with the rebooking fact they have.",
    "KA188 is cancelled. No replacement seat is confirmed. A draft promises the 10:00 departure and a full refund. The station may say they are still searching for a seat.",
    """```text
flight: KA188
status: cancelled
rebooking confirmed: none
care authorized: say they are searching for a seat
refund amount: not in the file
reason authorized: none
```""",
    """**Message**
KA188 is cancelled. We do not have a confirmed seat yet. We are still searching.

**Not in the message**
The 10:00. A full refund. A cause. None of those are in the file.""",
)

PACKS.append(pack(
    {"id": "energy", "title": "Energy", "summary": "Operational energy advice is not a permit and not a safety case.", "keywords": ["energy", "utility", "outage", "tariff", "power"]},
    """
tariff-change-note | Tariff Change Note | tariff note
job: Explain a tariff change from the sheet the user has, in the units on that sheet.
triggers: tariff change; rate change; utility rate; price plan change
inputs: The old rate; The new rate; The date; Who is affected
steps: Use the sheet. || Show old and new in the same unit. || Do not invent a bill impact without their usage. || Name the date it starts. || Say who it applies to, from the sheet. || This is not a regulatory filing.
anti: A bill impact with no usage; A rate from memory; A start date they do not have
example: A note says bills will rise 20 percent. The sheet shows a rate change and no usage.
out: A note with the rate change only, and the 20 percent removed.
related: utility-bill-check; pricing-margin-bridge

grid-connection-brief | Grid Connection Brief | connection brief
job: Brief a connection request with the site facts and the studies the user already has.
triggers: grid connection; interconnection; connect a site; queue brief
inputs: The site; The size they are requesting; Studies in hand; The queue status they were given
steps: State the site and the size. || List studies they have. || A missing study is a gap. || Use the queue status they were given, not a guessed date. || Do not promise interconnection. || Name the owner of the next filing.
anti: A guessed in-service date; A study marked done that is not in the file; A promise of connection
example: A brief says the site will connect in March. The only status is 'application received'.
out: A brief that keeps the status and drops the March date.
related: tariff-change-note; project-charter

utility-bill-check | Utility Bill Check | bill check
job: Check a bill against the meter read and the rate the user has.
triggers: utility bill; check this bill; energy invoice; bill audit
inputs: The bill; The meter read; The rate sheet; The prior bill if they have it
steps: Compare the billed units to the read they have. || Apply the rate from their sheet. || A mismatch is a finding, not a fraud claim. || Do not invent a tax. || Say which line cannot be checked. || Name who calls the utility.
anti: A fraud claim from a mismatch; A rate from memory; A tax invented to force the total
example: The bill shows 1,200 kWh. The read difference is 1,050. The rate sheet is in the folder.
out: A check that flags 150 kWh and does not call it fraud.
related: tariff-change-note; invoice-review

demand-response-offer | Demand Response Offer | offer note
job: Review a demand-response offer against the load the user can actually drop.
triggers: demand response; curtailment offer; load shed offer; DR contract
inputs: The offer; The load they can drop; The hours; The penalty they highlighted
steps: Compare the offer's drop to the load they can show. || If they cannot drop that much, say so. || Note the hours. || Put the penalty in the note if they highlighted it. || Do not invent a payment. || Recommend sign only if the drop fits.
anti: A drop they cannot make; A payment not in the offer; A penalty left out
example: The offer pays for 500 kW. The site can drop 200 kW. The penalty is in the offer.
out: A note that says do not sign for 500.
related: curtailment-note; tariff-change-note

curtailment-note | Curtailment Note | curtailment note
job: Record a curtailment the user was instructed to make, with the volume and the time.
triggers: curtailment; generation curtailment; instructed down; grid instruction
inputs: The instruction; The volume; The time; The meter after
steps: Record the instruction as given. || Record the volume they were told and the meter they have. || Do not invent a compensation rate. || Note if the meter does not show the drop. || Name who acknowledges. || This is not a dispute letter unless they ask for one.
anti: A compensation rate from memory; A meter that does not match, ignored; An instruction rewritten
example: They were told to drop 2 MW from 14:00 to 16:00. The meter dropped 1.4.
out: A note with both figures and no compensation rate.
related: demand-response-offer; production-variance
"""
))

put(
    "tariff-change-note",
    "Explain a tariff change from the sheet the user has, in the units on that sheet.",
    "Prairie Line's small-site rate sheet shows energy at 9.2 cents per kWh until 30 September and 9.8 cents from 1 October. A draft says bills will rise 20 percent. No usage file is attached.",
    """```text
old: 9.2 cents/kWh through 30 Sep 2026
new: 9.8 cents/kWh from 1 Oct 2026
who: small commercial sites on this sheet
usage: not attached
draft claim: bills up 20 percent
```""",
    """**Tariff note**
From 1 October 2026 the sheet shows 9.8 cents per kWh, up from 9.2. Same unit.
The 20 percent bill line comes out. No usage was attached, so no bill impact is calculated.
Who: small commercial sites on this sheet. Do not extend it to every account.
This is not a filing.""",
)

put(
    "grid-connection-brief",
    "Brief a connection request with the site facts and the studies the user already has.",
    "A site in Grand Prairie is requesting 5 MW. The utility status email says application received. A brief promises connection in March. The only study in the folder is a draft one-line, marked draft.",
    """```text
site: east of Grande Prairie, their file name Site 4
size requested: 5 MW
status email: application received, 8 Sep 2026
studies in folder: one-line, marked draft
promised in the brief: connected March 2027
owner of the next filing: Devon Hale
```""",
    """**Connection brief**
Site 4, 5 MW requested. Status: application received, 8 September. That is the status. March is not in the email. It comes out.
Study in the folder: a draft one-line. It is not a completed study.
No interconnection is promised.
Next filing owner: Devon. He does not send the March date.""",
)

put(
    "utility-bill-check",
    "Check a bill against the meter read and the rate the user has.",
    "The September bill for site meter 4 shows 1,200 kWh. The read book shows 48,200 minus 47,150, which is 1,050. The rate sheet is 9.2 cents. Devon wants the check before anyone calls it fraud.",
    """```text
bill: Sep 2026, meter 4, 1200 kWh
read: 48200 end, 47150 start
rate sheet: 9.2 cents/kWh
prior bill: not in the folder
who calls: Devon Hale
```""",
    """**Bill check**
Read difference: 47,150 to 48,200 is 1,050 kWh. Bill says 1,200. Gap 150 kWh.
At 9.2 cents that is a dollar gap, not a fraud finding. This note does not accuse anyone.
Lines not checked: riders and tax. The prior bill is not in the folder.
Next: Devon asks the utility about the 150 kWh. He does not short-pay from this note alone.""",
)

put(
    "demand-response-offer",
    "Review a demand-response offer against the load the user can actually drop.",
    "An offer pays for a 500 kW drop on weekday afternoons. The site log shows they can shed 200 kW by turning off two pumps. The offer includes a penalty if they miss the drop. The payment figure is $40 per kW-month.",
    """```text
offer drop: 500 kW
hours: weekdays 14:00-18:00
load they can drop: 200 kW, two pumps, log from August
penalty: in the offer, highlighted
payment: $40 per kW-month, in the offer
```""",
    """**Offer note**
Do not sign for 500 kW. The log shows 200.
If they sign, the number has to be a drop they have shown. 200 is the figure in the file.
Penalty: it is in the offer. Do not leave it out of the conversation.
Payment in the offer: $40 per kW-month. This note does not improve it.
Hours match a window they can staff only if Devon says the pumps can stop at 14:00. He has not said that yet.""",
)

put(
    "curtailment-note",
    "Record a curtailment the user was instructed to make, with the volume and the time.",
    "The grid instruction was to drop 2 MW from 14:00 to 16:00 on 16 September. The meter shows a 1.4 MW drop. Compensation is not in the instruction.",
    """```text
instruction: drop 2 MW, 14:00-16:00, 16 Sep 2026
meter after: 1.4 MW below the prior hour
compensation rate: not in the instruction
who acknowledges: Devon Hale
```""",
    """**Curtailment note**
Told: 2 MW, 14:00 to 16:00, 16 September.
Meter: 1.4 MW below the prior hour. Both figures stay. The gap is not edited away.
No compensation rate is in the instruction, so none is written.
This is a record, not a dispute letter.
Acknowledged by: Devon.""",
)

PACKS.append(pack(
    {"id": "small-business", "title": "Small business", "summary": "Owner-level cash, hiring, and local offers. Not legal, tax, or bylaw advice.", "keywords": ["small-business", "owner", "local", "shop"]},
    """
owner-cash-huddle | Owner Cash Huddle | cash huddle
job: Set the week's cash picture from the till, the bills due, and the owner's buffer.
triggers: weekly cash; owner huddle; can I pay this bill; shop cash
inputs: Cash on hand; Bills due this week; Expected receipts; The buffer they will not go under
steps: Start from cash they counted. || List bills by date. || Receipts are expected, not spent. || Flag any day under the buffer. || Do not tell them to skip a tax remittance. || One decision for the week.
anti: A tax skipped to make the week work; Receipts treated as cash; No buffer
example: The till has $4,200. Rent of $3,000 is Thursday. A customer might pay $2,000.
out: A huddle that does not spend the $2,000 and shows Thursday against the buffer.
related: cash-flow-forecast; owner-draw-note

first-employee-note | First Employee Note | hire note
job: List what an owner must decide before a first hire, without inventing employment law.
triggers: first hire; first employee; should I hire; hiring a helper
inputs: The hours; The wage they can pay; The work; What they have not checked
steps: State the hours and the wage they named. || List the work. || Flag checks they have not done: tax account, insurance, a contract review. || Do not invent a legal requirement. || Say what stays the owner's job. || Recommend a pause if the wage is not in the cash file.
anti: Invented employment law; A hire the cash file cannot show; The owner assuming the person knows the rules
example: Diane wants a Saturday helper at $18 an hour. She has not checked payroll or insurance.
out: A note that lists the open checks and does not say the hire is legal.
related: owner-cash-huddle; job-description-writer

local-service-offer | Local Service Offer | offer
job: Write a local offer from the price and the hours the owner can honor.
triggers: local offer; shop special; service offer; what should I advertise
inputs: The service; The price they will honor; The dates; The limit
steps: Use their price. || Limit the dates. || State how many they can do. || Do not add a discount they did not set. || Match the hours on the door. || No fake scarcity.
anti: A price they cannot honor; A fake countdown; Hours that contradict the door
example: An ad says half-price oil changes all month. She can do six a day and only priced Friday.
out: An offer for Friday, six cars, at the price she set.
related: local-seo-note; dealer-launch-check

books-handoff | Books Handoff | handoff
job: Hand a bookkeeper the accounts, the open items, and the access that is not a shared password.
triggers: bookkeeper handoff; catch up the books; accountant package; monthly books
inputs: The period; Accounts that do not tie; Documents missing; How they will share access
steps: Name the period. || List accounts that do not tie, from their words. || List missing documents. || Share access by a user of their own, not a shared password. || Do not ask the bookkeeper to invent a receipt. || State the due date.
anti: A shared password; A missing receipt invented; A period with no open-item list
example: August does not tie on the till. Two supplier bills are missing. She offered her bank password.
out: A handoff that lists the two bills and refuses the shared password.
related: month-end-close; owner-cash-huddle

busy-season-plan | Busy Season Plan | season plan
job: Plan the busy weeks from last year's pattern and this year's staff.
triggers: busy season; holiday rush; season plan; peak weeks
inputs: The weeks; Last year's volume if they have it; Staff they can roster; Stock they have
steps: Use their last-year figures if they have them. || Match staff to those weeks. || A stock gap is a finding. || Do not promise a volume they did not have. || Name the week they will not discount. || Cut a plan that needs people who are not hired.
anti: A peak plan with no staff; Invented last-year sales; A discount that wipes the busy week
example: Last December Saturdays did 40 cars. She has two techs this year, not four.
out: A plan sized to two techs, not to last year's 40.
related: local-service-offer; workforce-plan

local-supplier-pick | Local Supplier Pick | supplier pick
job: Pick between quotes the owner has, on price, lead time, and the terms on the page.
triggers: pick a supplier; compare quotes; local vendor; which quote
inputs: The quotes; Lead times; Return terms; A supplier they will not use
steps: Compare only quotes in the file. || Note lead time and returns, not just price. || A missing term is a gap. || Do not invent a quality score. || Honor a supplier they said they will not use by leaving them out. || Recommend one, with the reason.
anti: A quality score from memory; A quote that is not in the file; Ignoring returns
example: Two oil quotes. One is cheaper and has no return term. The other is local and takes returns.
out: A pick that shows both and does not hide the missing return term.
related: supplier-scorecard; books-handoff

owner-draw-note | Owner Draw Note | draw note
job: Separate an owner draw from wages and from money the business still owes.
triggers: owner draw; owner pay; can I take money out; draw versus wage
inputs: Cash after bills; Draws already taken; Bills still due; What their bookkeeper calls a draw
steps: Start from cash after the bills they listed. || List draws already taken. || Do not label a draw as a wage. || Do not skip a tax bill to fund a draw. || If they have no bookkeeper rule, say the label is unset. || Recommend an amount only from the cash that is left.
anti: A draw that skips a tax bill; A draw called a wage to look cleaner; No cash figure
example: She wants $2,000 out. Rent is unpaid. The bookkeeper calls these draws, not wages.
out: A note that holds the draw until rent is paid.
related: owner-cash-huddle; first-employee-note

permit-checklist-local | Local Permit Checklist | permit checklist
job: List the permits the owner already knows they need, and the ones they have not checked.
triggers: local permit; business license checklist; do I need a permit; sidewalk permit
inputs: The activity; Permits they already hold; The fee sheet if they have one; What they have not asked the town
steps: List permits they hold. || List the activity. || If they have a fee sheet, use that fee. || Do not invent a bylaw. || Mark unchecked items as unchecked. || Tell them to ask the town before they build the plan on a guess.
anti: An invented bylaw; A fee from memory; A checklist that says they are approved
example: She has a business licence and a fee sheet for a sidewalk display at $75. She has not asked about a sign.
out: A list that includes the licence and the $75 sheet, and leaves the sign unchecked.
related: blog-refresh; local-service-offer
"""
))

put(
    "owner-cash-huddle",
    "Set the week's cash picture from the till, the bills due, and the owner's buffer.",
    "Diane counted $4,200 in the Harbor Goods till on Monday. Rent of $3,000 is due Thursday. A customer said they might pay $2,000. Her buffer is $1,500. A tax remittance of $800 is also due Friday.",
    """```text
counted: 4200 CAD, Mon 15 Sep 2026
rent: 3000, Thu 18 Sep
tax remittance: 800, Fri 19 Sep
maybe receipt: 2000, not in the bank
buffer: 1500
```""",
    """**Week huddle**
Do not spend the $2,000. It is not in the till.

| Day | Cash if nothing else arrives | Bill |
| --- | --- | --- |
| Mon | 4,200 | — |
| Thu | 1,200 after rent | rent 3,000 |
| Fri | 400 after tax | tax 800 |

Thursday after rent is $1,200, under the $1,500 buffer, before Friday's tax. Friday's tax still gets paid. It is not the lever.
Decision: no owner draw and no new order this week unless the $2,000 actually arrives.""",
)

put(
    "first-employee-note",
    "List what an owner must decide before a first hire, without inventing employment law.",
    "Diane wants a Saturday helper from 9 to 5 at $18 an hour. She has not opened a payroll account and has not asked her insurer. The cash file shows Saturday till money, not a wage reserve.",
    """```text
hours: Saturday 09:00-17:00
wage she named: $18 an hour
work: front counter, not the oil bay
payroll account: not opened
insurer asked: no
cash reserve for the wage: not in the file
```""",
    """**Hire note**
Not a yes. The wage is not in the cash file, and two checks are open.

Open, and not invented as law: payroll account, insurer. She has not done them. This note does not say which statute applies.
Work: front counter. The oil bay stays hers until she writes that down.
Pause the offer until the $18 is in the weekly cash huddle as a bill, not as a hope.
This note is not a contract and not an employment-law opinion.""",
)

put(
    "local-service-offer",
    "Write a local offer from the price and the hours the owner can honor.",
    "An ad draft says half-price oil changes all month. Diane priced $49 for Fridays only, and the lane can do six cars a day. The door is closed Sunday.",
    """```text
service: oil change
price she will honor: $49, Fridays in September 2026
capacity: 6 cars
door: closed Sunday
draft ad: half price, all month
half-price figure: she did not set one
```""",
    """**Offer**
Friday oil changes, $49, six cars. September Fridays only.

Not the offer: half price, all month, Sunday.
Six is the cap. When six are booked, the ad stops for that Friday. No fake 'only two left' if the book is empty.
The door hours stand. Sunday is closed.""",
)

put(
    "books-handoff",
    "Hand a bookkeeper the accounts, the open items, and the access that is not a shared password.",
    "August does not tie. The till was $180 short on the 12th and $40 long on the 28th. Two supplier bills are missing. Diane offered her bank password so the bookkeeper could 'just look'.",
    """```text
period: August 2026
till: 12 Aug short 180, 28 Aug long 40
missing: supplier invoice 188, supplier invoice 204
access offered: her bank password
due: 25 Sep 2026
```""",
    """**Handoff**
Period: August 2026.
Does not tie: till, 12 August short $180, 28 August long $40.
Missing documents: invoices 188 and 204. Do not invent them.
Access: a separate user the bank can issue. Not her password.
Due: 25 September. The bookkeeper does not close August by guessing the two bills.""",
)

put(
    "busy-season-plan",
    "Plan the busy weeks from last year's pattern and this year's staff.",
    "Last December Saturdays did about 40 cars when four techs were on. This December she has two techs. She has not hired the Saturday helper. Stock of filters is 18.",
    """```text
last year: about 40 cars each December Saturday, 4 techs, her memory not a printout
this year staff: 2 techs
Saturday helper: not hired
filters on hand: 18
weeks: 6, 13, 20 Dec 2026
```""",
    """**Season plan**
Do not plan for 40. That was four techs, and it is her memory, not a printout.
Size the three Saturdays to two techs. She has not named that number. Leave the car count blank until she writes what two techs finished on a recent Saturday.
Filters: 18 on hand. That is a gap if those Saturdays are busy. It is not a purchase order yet.
The unhired helper is not on the roster.""",
)

put(
    "local-supplier-pick",
    "Pick between quotes the owner has, on price, lead time, and the terms on the page.",
    "Diane has two quotes for oil. Redline is $4.10 a litre, 14 days, no return term on the page. A local yard is $4.40, 2 days, returns within 30 days. She will not use a third supplier who missed August.",
    """```text
quote A: Redline, $4.10/L, 14 days, return term not on the page
quote B: local yard, $4.40/L, 2 days, returns in 30 days
excluded: the August miss supplier
quality scores: none
```""",
    """**Pick**
| Quote | Price | Lead | Returns |
| --- | --- | --- | --- |
| Redline | $4.10 | 14 days | not on the page |
| Local yard | $4.40 | 2 days | 30 days |

Recommend the local yard if she needs oil inside a week. The cheaper quote does not say she can send it back.
The August supplier stays out, as she asked.
No quality score. None was in the file.""",
)

put(
    "owner-draw-note",
    "Separate an owner draw from wages and from money the business still owes.",
    "Diane wants $2,000 for herself on Thursday. Rent of $3,000 is unpaid. The bookkeeper labels these transfers as draws, not wages. The till count is $4,200.",
    """```text
wanted: 2000 draw, Thu 18 Sep 2026
rent unpaid: 3000
till: 4200
label in the books: draw, not wage
tax bill Friday: 800
```""",
    """**Draw note**
Hold the $2,000. Rent is unpaid, and Friday's $800 tax bill is still due.
A draw is not a wage. Do not relabel it.
Cash after rent would be $1,200 before tax. That is not a draw week.
Next: revisit after rent and the tax bill are paid, not before.""",
)

put(
    "permit-checklist-local",
    "List the permits the owner already knows they need, and the ones they have not checked.",
    "Diane has a business licence on the wall and a 2026 fee sheet that lists a sidewalk display at $75. She wants a sign and has not asked the town. A blog said signs under a certain size are free. She has no bylaw text.",
    """```text
holds: business licence, number on the wall copy
fee sheet: sidewalk display $75, effective 1 Jan 2026
activity she wants: a new sign, plus the sidewalk display
bylaw text: not in the folder
blog line: small signs are free
```""",
    """**Checklist**
| Item | Status |
| --- | --- |
| Business licence | she holds one, wall copy |
| Sidewalk display | fee sheet says $75. Not the same as approved. |
| Sign | unchecked. Ask the town. |

The blog line about free signs is not a bylaw. It comes off the list.
This checklist is not an approval.""",
)

PACKS.append(pack(
    {"id": "saas", "title": "SaaS", "summary": "Weekly metrics, activation, and pricing notes from the export. No invented retention or certification.", "keywords": ["saas", "subscription", "churn", "activation", "pricing"]},
    """
saas-weekly-metrics | SaaS Weekly Metrics | metrics note
job: Read a weekly SaaS export and say what moved, without a benchmark from memory.
triggers: SaaS metrics; weekly SaaS; MRR review; subscription metrics
inputs: The export; The definitions they use; Last week's figures; A metric that is missing
steps: Use their definitions. || Show this week and last week from the export. || A missing metric stays blank. || Do not add a benchmark. || Name the one move that matters. || Do not annualize a noisy week.
anti: A benchmark from memory; A blank filled with a guess; An annualized run-rate from one week
example: The export has MRR and churn. Activation is blank. A slide adds a 120 percent NRR from memory.
out: A note with the export figures and a blank activation and NRR.
related: net-retention-note; metric-definition

churn-save-plan | Churn Save Plan | save plan
job: Plan a save offer from the cancel reasons in the export and the offer they can honor.
triggers: churn save; cancel flow; save offer; why are they leaving
inputs: Cancel reasons; Counts; The offer they can honor; Who approves a credit
steps: Rank reasons by their counts. || Match an offer only to a reason it can fix. || A price save does not fix a missing feature. || Use only credits they authorized. || Do not invent a save rate. || Name the approver.
anti: One offer for every reason; An unauthorized credit; A fake save rate
example: 40 cancels. 22 said a missing export. A draft offers 20 percent off to all of them.
out: A plan that does not discount the 22 until the export exists.
related: saas-weekly-metrics; renewal-save

activation-gap | Activation Gap | activation note
job: Find where new workspaces stall, from the step counts the user exported.
triggers: activation; time to value; onboarding drop; activation gap
inputs: The steps; The counts; The definition of activated; The week
steps: Use their definition of activated. || Show the count at each step. || Name the largest drop. || Do not invent a reason for the drop. || Recommend one step to fix, not a redesign. || Say if the export is one week only.
anti: A reason with no interview; A redesign from one week; A definition they do not use
example: 200 trials, 90 created a project, 20 invited a teammate. Activated means the invite.
out: A note that the gap is the invite, with no invented reason.
related: trial-to-paid; onboarding-success-plan

pricing-page-note | Pricing Page Note | page note
job: Check a pricing page against the plans and the limits they actually enforce.
triggers: pricing page; plan page; public pricing; pricing copy
inputs: The plans; The limits in the product; The page copy; A claim they cannot support
steps: Match each plan to the limit in the product. || Cut a limit the page states that the product does not enforce. || Do not add a competitor's price. || A discount needs an end date they set. || Say who edits the page. || Do not hide a limit in a footnote they did not write.
anti: A limit the product does not enforce; A fake comparison; A discount with no end
example: The page says unlimited exports. The product stops at 5,000 rows.
out: A note to change the page to 5,000 rows.
related: plan-limit-note; marketing-claims-review

trial-to-paid | Trial To Paid | conversion note
job: Report trial-to-paid from the cohort dates in the export.
triggers: trial conversion; trial to paid; free trial results; cohort conversion
inputs: The trial start dates; Paid counts; The trial length; Cohorts still inside the trial
steps: Exclude cohorts that have not finished the trial. || Use their paid definition. || Do not count a trial that is still running as a failure. || Show the finished cohort only. || Do not invent a channel split they did not export. || Name the date the next cohort closes.
anti: An open cohort counted as lost; A channel story with no export; A blended rate that hides the definition
example: September trials are still inside a 14-day trial. August finished at 18 of 100.
out: A note that reports August and leaves September open.
related: activation-gap; saas-weekly-metrics

plan-limit-note | Plan Limit Note | limit note
job: Write the limit a plan enforces, and the message the user sees when they hit it.
triggers: usage limit; plan limit; fair use; quota message
inputs: The limit in the product; The plan name; The message they want; What happens at the limit
steps: Use the limit in the product. || Write the message a person sees at the limit. || Say whether the action blocks or warns. || Do not promise an overage price they have not set. || Match the pricing page. || Name who changes the limit.
anti: A message that says unlimited; An overage price invented; A limit that does not match the page
example: The product blocks at 5,000 rows. The message still says they can export everything.
out: A message that names 5,000 and the block.
related: pricing-page-note; activation-gap

net-retention-note | Net Retention Note | retention note
job: Compute net retention only from the starting and ending revenue they provide for the same accounts.
triggers: net retention; NRR; net revenue retention; expansion and churn
inputs: Starting revenue for the cohort; Ending revenue for the same accounts; What is excluded; The period
steps: Use the same accounts at the start and the end. || Do not add new logos to the ending number. || Show expansion and churn only if they split them. || If they did not split them, give one ratio and say it is not split. || Do not annualize. || Do not borrow a benchmark.
anti: New logos in the NRR math; A benchmark; A split they did not provide
example: A slide says 120 percent NRR. The file has one revenue pool and no same-account cohort.
out: A note that refuses the 120 percent until the same accounts are identified.
related: saas-weekly-metrics; expansion-play

security-answer-sheet | Security Answer Sheet | answer sheet
job: Answer a security questionnaire from documents the company has, and leave the rest blank.
triggers: security questionnaire; customer security review; SIG lite answers; vendor security answers
inputs: The questions; The documents they have; Certifications they hold; Questions they cannot answer
steps: Answer only from a document. || A missing report is 'not in the file', not a yes. || Do not claim SOC 2, ISO, or HIPAA without the report. || Say who may send the sheet. || Do not paste secrets into answers. || Mark follow-ups.
anti: A certification they do not hold; A guessed control; Secrets in the answer
example: A question asks for the SOC 2 report. The folder has no report. A draft says yes, in progress.
out: An answer of not in the file, with no in-progress claim they did not document.
related: vendor-security-review; ai-vendor-note
"""
))

put(
    "saas-weekly-metrics",
    "Read a weekly SaaS export and say what moved, without a benchmark from memory.",
    "Jonah's week of 8 September export shows MRR of $42,000, up from $40,500, and logo churn of 3.8 percent. Activation is blank. A slide adds 120 percent NRR from a blog.",
    """```text
week: 8-14 Sep 2026
MRR: 42000, prior week 40500
logo churn: 3.8 percent, their definition, logos not revenue
activation: blank
NRR in the slide: 120 percent, no cohort file
definitions note: churn is logos, not dollars
```""",
    """**Week of 8 September**
MRR $42,000, from $40,500. That is the move in the export.
Logo churn 3.8 percent. Their definition is logos, so this note does not call it revenue churn.
Activation: blank.
NRR: blank. The 120 percent is not in the export.
No benchmark. One week is not an annual run-rate.""",
)

put(
    "churn-save-plan",
    "Plan a save offer from the cancel reasons in the export and the offer they can honor.",
    "Forty cancels in August. Twenty-two said the export they need does not exist. Ten said price. Eight gave no reason. A draft offers 20 percent off to all forty. Jonah can approve a 10 percent credit, not 20.",
    """```text
cancels: 40, August 2026
missing export: 22
price: 10
no reason: 8
credit he can approve: 10 percent, one month
20 percent draft: not approved
```""",
    """**Save plan**
Do not discount the 22. A cheaper plan does not create the missing export.
Price reason, 10 accounts: a 10 percent credit for one month is the offer he can honor. Not 20.
No reason, 8: no offer. Ask, or leave them.
No save rate is claimed. None was measured.
Approver for the credit: Jonah.""",
)

put(
    "activation-gap",
    "Find where new workspaces stall, from the step counts the user exported.",
    "Fieldnote defines activated as inviting a teammate. In the week of 8 September, 200 trials started, 90 created a project, and 20 sent an invite.",
    """```text
week: 8-14 Sep 2026
trials: 200
created a project: 90
invited a teammate: 20
activated means: the invite
interviews: none
```""",
    """**Activation note**
The gap is the invite. 90 created a project. 20 invited someone. Activated, by their definition, is 20 of 200.
No reason is in this note. Nobody was interviewed.
One week only. Not a redesign.
Next question, not a build: why the 70 who had a project did not invite. That question is open.""",
)

put(
    "pricing-page-note",
    "Check a pricing page against the plans and the limits they actually enforce.",
    "The public page says Pro includes unlimited exports. The product blocks an export at 5,000 rows. Jonah can edit the page. There is no competitor price in the file.",
    """```text
plan: Pro
page: unlimited exports
product: blocks at 5000 rows
discount on the page: none
editor: Jonah Park
competitor price: not in the file
```""",
    """**Page note**
Change 'unlimited exports' to 5,000 rows. The product blocks there.
Do not add a competitor's price. None is in the file.
No discount line. None was set.
Editor: Jonah. The page and the product have to match before the next ad runs.""",
)

put(
    "trial-to-paid",
    "Report trial-to-paid from the cohort dates in the export.",
    "August trials: 100 started, 18 paid, trial length 14 days, all finished. September trials started 1 to 14 September and are still inside 14 days. A slide blends them.",
    """```text
trial length: 14 days
August: 100 started, 18 paid, cohort closed
September 1-14: 80 started, still inside the trial
paid definition: a paid workspace, not a card added and removed
channel split: not exported
```""",
    """**Conversion**
August, closed: 18 of 100.
September 1-14: still open. Do not count them as lost or as converted.
Do not blend the months.
No channel split. None was exported.
Next cohort closes 28 September for the 14 September starts.""",
)

put(
    "plan-limit-note",
    "Write the limit a plan enforces, and the message the user sees when they hit it.",
    "Pro blocks an export at 5,000 rows. The message in the product still says 'You can export everything on Pro'. There is no overage price.",
    """```text
plan: Pro
limit: 5000 rows, then the export button stops
current message: You can export everything on Pro
overage price: none set
who changes the limit: Jonah
```""",
    """**Limit**
Pro blocks at 5,000 rows. The button stops. It does not bill an overage. None is set.

Message: This export stops at 5,000 rows on Pro. It does not say unlimited.
Who changes the limit: Jonah. The pricing page has to say the same number.""",
)

put(
    "net-retention-note",
    "Compute net retention only from the starting and ending revenue they provide for the same accounts.",
    "A board slide says NRR is 120 percent. The file has total MRR for two months and a list of new logos. It does not identify the same accounts at the start and the end.",
    """```text
slide: NRR 120 percent
file: August MRR 40500, September week MRR 42000
new logos: 6, revenue not split
same-account cohort: not in the file
expansion versus churn: not split
```""",
    """**Retention note**
Do not use 120 percent. The file is not a same-account cohort.
New logos do not belong in that ratio, and their revenue is not even split out.
Ending and starting totals are a company MRR change, not NRR.
What would make the number possible: the same accounts, August revenue and current revenue, with new logos excluded.
Until that sheet exists, the cell stays blank.""",
)

put(
    "security-answer-sheet",
    "Answer a security questionnaire from documents the company has, and leave the rest blank.",
    "A customer asked if Fieldnote has SOC 2. The folder has no report. A draft answer says 'yes, in progress'. Nobody has written that a audit is underway. Jonah is the only person who may send the sheet.",
    """```text
question: do you have SOC 2
documents: none
draft answer: yes, in progress
audit letter: not in the folder
sender: Jonah Park
secrets: none to paste
```""",
    """**Answer**
SOC 2: not in the file. Do not say yes. Do not say in progress. No letter says that.
Sender: Jonah. He does not forward the draft.
Other questions with no document get the same mark, not a guess.
No secrets in the sheet.""",
)

PACKS.append(pack(
    {"id": "entrepreneurship", "title": "Entrepreneurship", "summary": "Startup choices, discovery, and investor updates. Not a promise of funding.", "keywords": ["startup", "founder", "ideas", "saas", "mvp"]},
    """
startup-story | Startup Story | story note
job: Write the company story from the customer and the fact they can show, not from a borrowed pitch.
triggers: startup story; origin story; pitch narrative; what do we say we are
inputs: The customer; The fact they can show; The ask; Lines they copied from another pitch
steps: Name the customer. || Use one fact they can show. || Cut a line copied from another company. || Match the ask to the fact. || Do not add a market size they did not source. || Keep it to one paragraph and one proof.
anti: A copied pitch; An unsourced market size; A story with no customer
example: A draft says they are the Stripe of local shops and have a $4 billion market. They have four paying shops.
out: A story about the four shops, with the Stripe line and the market size cut.
related: idea-screen; investor-update

runway-choice | Runway Choice | runway note
job: State the runway choice from cash, burn, and the hire they are considering.
triggers: runway; how long is our cash; hire or wait; burn choice
inputs: Cash; Monthly burn; The hire cost; The date they care about
steps: Use their cash and burn. || Show months at the current burn. || Show months if the hire starts. || Do not treat a maybe receivable as cash. || Recommend one choice. || Do not promise a raise.
anti: A receivable counted as cash; A raise assumed; Burn without the hire shown separately
example: Cash is $180,000, burn is $30,000, and a hire would add $8,000. A customer might pay $40,000.
out: A note that keeps the $40,000 out and shows both runway figures.
related: runway-and-burn; cash-flow-forecast

first-ten-customers | First Ten Customers | customer list
job: List the first customers they can name, and the ones that are still wishes.
triggers: first customers; who will buy; design partners; early customer list
inputs: Names they have talked to; Who paid; Who said no; The offer
steps: Split paid, talking, and no. || A wish with no conversation is not a prospect. || Use their words for why someone paid. || Do not add logos. || Say what the offer was. || Count only rows they named.
anti: Logos they did not earn; A wish counted as a pipeline; A reason they invented
example: Four shops pay. Six names are on a wish list with no conversation. A deck says ten customers.
out: A list of four paying shops, and the six wishes marked as not customers.
related: design-partner-pilot; customer-discovery-sprint

design-partner-pilot | Design Partner Pilot | pilot note
job: Scope a pilot with the partner, the success test, and the end date.
triggers: design partner; pilot scope; paid pilot; first pilot
inputs: The partner; The success test; The end date; What is free
steps: Name the partner. || Write the test in a number they can observe. || Set the end date. || Say what is free and what is paid. || Do not call it a success before the date. || A pilot with no end is a finding.
anti: An open-ended free build; A success declared in week one; A partner who has not agreed
example: A shop agreed to try exports for 30 days. A draft calls the company validated.
out: A pilot with a 30-day end and no validated claim.
related: first-ten-customers; mvp-scope

idea-screen | Idea Screen | screen
job: Screen a business idea against the customer, the proof, and the reason to stop.
triggers: business idea; is this a business; idea screen; should we build this
inputs: The idea; The customer; Proof they have; The cost of a week of work
steps: Name the customer. || State the proof in hand. || If the proof is zero, say so. || Name one reason to stop. || Do not score it with a fake matrix. || Recommend a next test or a stop.
anti: A weighted score with no data; A market size as proof; A build decision from excitement
example: An idea for a permit app has no user and a week of build time they cannot spare.
out: A screen that says stop or talk to five owners first, with no score.
related: assumption-map; kill-the-idea

assumption-map | Assumption Map | assumption map
job: List the assumptions that would kill the idea if they are wrong, in the founder's words.
triggers: assumption map; what has to be true; leap of faith; riskiest assumption
inputs: The idea; Assumptions they stated; Which one they can test this week; Evidence already in hand
steps: Write assumptions as sentences that can be false. || Mark the one that kills the idea. || Match it to a test they can run this week. || Evidence in hand is labeled evidence. || Do not add a market assumption they did not state. || Leave the test result blank.
anti: A test result filled in early; A dozen assumptions and no killer; A survey of friends called proof
example: The killer assumption is that shop owners will pay $49 a month. They have not asked.
out: A map with that sentence as the killer and the test not yet run.
related: idea-screen; beachhead-market

beachhead-market | Beachhead Market | beachhead note
job: Pick the first market from the customers they can already reach.
triggers: beachhead; first market; who is the wedge; niche first
inputs: The segments they named; Who they can reach this month; Who pays today; A segment they should not chase yet
steps: Prefer the segment they can reach. || A paying customer beats a imagined segment. || Say who is not the beachhead. || Do not pick a segment because it is large. || Name the offer for that segment. || One beachhead.
anti: A beachhead they cannot reach; Two beachheads; A choice based on market size alone
example: They can talk to Airdrie shop owners this month. A draft targets every small business in Canada.
out: A beachhead of the shops they can visit, and Canada marked as not now.
related: idea-screen; first-ten-customers

kill-the-idea | Kill Criteria | kill note
job: Write the criteria that would stop the idea, before more money is spent.
triggers: kill criteria; when do we stop; walk away; stop the idea
inputs: The idea; The spend so far; The test; The result that means stop
steps: Write the stop line before the test if they can. || Use a result they can observe. || Include the spend they will not pass. || Do not move the line after a weak result. || Say who decides. || A kill note is allowed to say stop.
anti: A line moved after a miss; A vanity metric as the only test; No person who can stop it
example: They said they would stop if five owners would not pay. Five said no. A draft says try five more.
out: A note that records the stop, and does not add five more.
related: idea-screen; runway-choice
"""
))

put(
    "startup-story",
    "Write the company story from the customer and the fact they can show, not from a borrowed pitch.",
    "Mara's draft says Northline is the Stripe of local shops and that the market is $4 billion. She can show four paying shops in Airdrie and Calgary. The ask is a $15,000 tooling budget, not a round.",
    """```text
customer: independent shops, four paying
fact: 4 shops pay $49 a month, started June 2026
ask: $15000 tooling budget
lines copied: Stripe of local shops, $4 billion market, no source
```""",
    """**Story**
Four independent shops pay $49 a month to get their Saturday list off a whiteboard. That started in June 2026.

Ask: $15,000 for tooling. Not a round.

Cut: 'Stripe of local shops'. Cut: $4 billion. No source.
The proof is the four shops. The story does not get bigger than that.""",
)

put(
    "runway-choice",
    "State the runway choice from cash, burn, and the hire they are considering.",
    "Northline has $180,000 cash. Burn is $30,000 a month. A hire would add $8,000. A customer might pay $40,000. Mara wants to know if she can hire.",
    """```text
cash: 180000
monthly burn: 30000
hire: 8000 a month, not started
maybe receipt: 40000, not in the bank
date she cares about: 31 Mar 2027
```""",
    """**Runway**
Current burn: 180,000 / 30,000 = 6 months. That is the file, not a promise.
With the hire: 38,000 a month, under 5 months. Do not start the hire on this note.
The $40,000 stays out. It is not cash.
No raise is assumed.
Choice: wait. Revisit if the $40,000 arrives.""",
)

put(
    "first-ten-customers",
    "List the first customers they can name, and the ones that are still wishes.",
    "A deck says ten customers. Four shops pay. Six names are on a whiteboard. Mara has not spoken to those six. The offer is $49 a month.",
    """```text
paid: Harbor Goods, Cedar Clinic front desk, Lantern Inn shop, a fourth shop she named as Birch Books
wish list: 6 names, no conversation logged
offer: $49 a month
why Harbor pays: Saturday list, Mara's note of their words
```""",
    """**Customers**
Paying: four. Harbor Goods, Cedar Clinic front desk, Lantern Inn shop, Birch Books.
Harbor's reason, in her note: the Saturday list. Do not invent reasons for the other three.
The six names are not customers and not a pipeline. No conversation is logged.
The deck's ten is wrong. The count is four.""",
)

put(
    "design-partner-pilot",
    "Scope a pilot with the partner, the success test, and the end date.",
    "Harbor Goods agreed to try the export for 30 days starting 16 September. A draft calls Northline validated. Nothing is free beyond that export. They already pay $49.",
    """```text
partner: Harbor Goods, Diane Cho, agreed 14 Sep 2026
test: she uses the Saturday export on 20 Sep and 27 Sep
end: 16 Oct 2026
paid: $49 a month already
free: the export setup only
```""",
    """**Pilot**
Partner: Harbor Goods. End: 16 October 2026.
Test: she uses the export on 20 September and 27 September. Success is those two uses, not a feeling.
Paid: $49, already. Free: the setup only.
Do not call the company validated. The test has not happened.
If 16 October passes with no use, the pilot failed. It does not extend itself.""",
)

put(
    "idea-screen",
    "Screen a business idea against the customer, the proof, and the reason to stop.",
    "Mara's friend wants a permit app for every town. No owner has asked for it. A week of build would consume the only free week she has before the Harbor pilot.",
    """```text
idea: permit app for every town
customer named: none
proof: none
week cost: her only free week before the Harbor pilot, 16 Sep
friend's enthusiasm: high
```""",
    """**Screen**
Stop, or talk to five owners first. Do not build this week.
Customer: none named. Proof: none.
The week is already claimed by the Harbor pilot. That is the cost.
No score. A market size would not fix the empty customer.
Reason to stop: no owner has asked, and the week is not free.""",
)

put(
    "assumption-map",
    "List the assumptions that would kill the idea if they are wrong, in the founder's words.",
    "Mara says the idea dies if shop owners will not pay $49 a month. She has four who pay. She has not asked the six names on the whiteboard. A friend assumed the market is huge.",
    """```text
idea: Saturday list for independent shops
killer, her words: owners will not pay $49 a month
evidence: 4 pay
not tested: the 6 names with no conversation
friend's line: the market is huge
test she can run this week: ask 5 of the 6, yes or no on $49
```""",
    """**Assumptions**
Killer: owners will not pay $49 a month. Her sentence.
Evidence: four pay. That is evidence for those four, not for the six.
Test this week: ask five of the six for a yes or no on $49. Result: blank until she asks.
Not on this map: 'the market is huge'. She did not state it, and it is not the killer.""",
)

put(
    "beachhead-market",
    "Pick the first market from the customers they can already reach.",
    "Mara can visit shops in Airdrie and north Calgary this month. A draft says the beachhead is every small business in Canada because the market is larger.",
    """```text
can reach this month: shops in Airdrie and north Calgary, she can drive there
pays today: 4 shops, 3 in that drive
draft beachhead: every small business in Canada
offer: $49 Saturday list
```""",
    """**Beachhead**
Shops she can drive to in Airdrie and north Calgary. One beachhead.
Not now: every small business in Canada. Size is not the reason.
Offer for this segment: the $49 Saturday list. Do not add a second product to chase a bigger map.
Three of the four paying shops are already in this drive. That is the wedge.""",
)

put(
    "kill-the-idea",
    "Write the criteria that would stop the idea, before more money is spent.",
    "Before the week started, Mara said she would stop the permit-app idea if five owners would not pay. She asked five. All five said no. A note from her friend says ask five more.",
    """```text
idea: permit app
line she set: stop if 5 owners will not pay
result: 5 asked, 5 no, 18 Sep 2026
spend so far: one evening
friend: ask 5 more
who decides: Mara Chen
```""",
    """**Kill note**
Stop. The line was five noes. She has five noes.
Do not add five more. The line does not move after the miss.
Spend so far: one evening. Do not add the free week.
Who decides: Mara. The friend does not get a vote that rewrites the line.""",
)
