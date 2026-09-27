from dense import pack
from scenario_bank import put

PACKS = []

PACKS.append(pack(
    {"id": "data", "title": "Data", "summary": "Contracts, lineage, freshness, and reconciliations from files the user has. No invented numbers.", "keywords": ["data", "warehouse", "pipeline", "metrics", "lineage"]},
    """
data-contract | Data Contract | data contract
job: Write the columns, grain, freshness, and owner a producer and a consumer can both use.
triggers: data contract; schema agreement; producer consumer contract; table contract
inputs: The table or file; The grain; The columns that must not be null; The freshness the consumer needs
steps: Name the grain in one sentence. || List required columns and which may be null. || Write the freshness as a clock time the producer can hit. || Name both owners. || Say what breaks the contract. || Do not add columns nobody produces.
anti: A contract with no grain; Freshness the producer never agreed; Hidden personal columns
example: Product wants active_accounts daily by 06:00. The job finishes at 09:30.
out: A contract that sets 10:00 or moves the job, and does not pretend 06:00 is true.
related: freshness-sla; metric-definition

pipeline-incident | Pipeline Incident | pipeline note
job: Write a pipeline failure from the log lines the user has, with the hold and the rerun owner.
triggers: pipeline failed; data job down; ETL incident; broken load
inputs: The job name; The error line they copied; What is stale; Who reruns it
steps: Quote the error they pasted. Do not invent a stack. || Say which table is stale and as of when. || State the hold: who should not use the table. || Name the rerun owner. || Separate a late file from a bad transform if the log shows which. || Do not include credentials from the log.
anti: A guessed root cause; A silent rerun; Credentials copied into the note
example: orders_daily failed at 05:12 with a missing file. The dashboard was still refreshed.
out: A note that marks orders_daily stale and stops the dashboard refresh.
related: data-contract; incident-postmortem

data-lineage | Data Lineage | lineage note
job: Trace a metric to the source tables the user can name, and stop where the trail stops.
triggers: data lineage; where does this number come from; metric source; column lineage
inputs: The metric; The tables they know; The transform they can point to; The gap
steps: Start at the metric definition they use. || Walk only to tables they named. || Mark the first hop you cannot show. || Do not draw a source you inferred from a column name. || Note if two jobs write the same column. || Give the owner one place to look next.
anti: A full map drawn from guesses; Ignoring a second writer; A lineage slide with no table names
example: active_accounts is said to come from the warehouse. Nobody can name the table.
out: A note that stops at the metric and lists the missing table as the open item.
related: metric-definition; data-dictionary

retention-schedule-data | Data Retention Schedule | retention note
job: Draft a retention note from the policy the user already has, not from a guessed law.
triggers: data retention; how long do we keep rows; retention schedule; delete old data
inputs: The datasets; The policy or contract clause they have; What they use the rows for; Who approves a delete
steps: List each dataset and the clause they cited. || If they have no clause, say the period is unset. || Do not invent a statute. || Separate a backup from the live table. || Name who may approve a delete. || Flag personal columns they pointed out.
anti: A seven-year rule copied from memory; Deleting without an owner; Ignoring backups
example: A draft says delete tickets after 90 days because a blog said so. Their contract is silent.
out: A note that leaves tickets unset and removes the blog rule.
related: records-retention; ai-data-note

warehouse-model | Warehouse Model Review | model review
job: Review a warehouse model for grain mistakes and double-counted joins.
triggers: warehouse model; star schema review; grain check; fact table review
inputs: The fact grain they claim; The joins; A sample of duplicate keys if they have one; The metric that looks wrong
steps: Restate the grain. || Check the join they showed for fan-out. || If they have duplicate keys, count them from their sample, do not invent a rate. || Say which metric moves if the grain is wrong. || Recommend a fix as a question for the modeler, not a silent rewrite. || Stop if they did not include the join.
anti: A new model drawn from scratch with no source; Ignoring a duplicate key sample; A guessed row count
example: active_accounts jumped after a join to a payments table that has many rows per account.
out: A review that flags the payments join as a fan-out risk and asks for a key count.
related: data-lineage; metric-definition

freshness-sla | Freshness SLA | freshness note
job: Set a freshness promise the job can meet, from the finish times the user has.
triggers: freshness SLA; data SLA; when is the table ready; late data
inputs: The last ten finish times if they have them; The time the consumer needs; The job owner; What happens if it is late
steps: Use their finish times. If they have fewer than five, say the promise is thin. || Set the promise after the slow runs, not at the average. || Name the consumer clock. || Say who is called when it misses. || Do not promise a time the job has already missed twice. || Write the exception path.
anti: A 6 a.m. promise on a 9 a.m. job; No owner for a miss; An average used as a guarantee
example: The consumer wants 06:00. Eight of the last ten runs finished after 09:00.
out: A promise of 10:30, or a job change, not 06:00.
related: data-contract; pipeline-incident

balance-reconciliation | Balance Reconciliation | reconciliation
job: Reconcile two extracts the user provides and list the rows that do not match.
triggers: reconcile two files; data reconciliation; tie-out; balance check
inputs: Both extracts; The key; The amount column; The as-of time
steps: Match on the key they named. || Sum both sides from the files. Do not type a total from memory. || List unmatched keys. || Separate a timing gap from a real break if the timestamps show it. || Stop if a key is missing. || Do not force a plug figure.
anti: A plug to make it balance; Matching on a name instead of the key; Ignoring one file
example: orders_daily and the billing export differ by $1,240 on 12 September. Three order ids are only on one side.
out: A tie-out that shows the $1,240 and the three ids, with no plug.
related: account-reconciliation-standard; data-quality-check

access-request-data | Data Access Request | access note
job: Triage an internal request for data the company already holds, against the approver they name.
triggers: data access request; who can see this table; internal data request; warehouse access
inputs: Who is asking; The table; Why; The approver role in their policy
steps: Record the asker, the table, and the why. || Check the approver they said their policy requires. || Do not grant access yourself. || Minimize columns. Ask if the whole table is needed. || Flag personal columns. || If the why is missing, the request waits.
anti: Access because someone is senior; A shared login; Approving your own request
example: An analyst wants the full tickets table, including addresses, for a vibe check.
out: A note that sends the request back for a real question and drops the address column from the ask.
related: access-review; ai-data-note
"""
))

put(
    "data-contract",
    "Write the columns, grain, freshness, and owner a producer and a consumer can both use.",
    "Product wants active_accounts on the dashboard by 06:00. Noah's job finished at 09:30 on eight of the last ten weekdays. They need a contract both sides can sign.",
    """```text
table: analytics.active_accounts
grain: one row per workspace per day
required columns: workspace_id, day, active_flag
nullable: none of those three
producer: Noah Berger
consumer: Jonah Park
job finish, last 10 weekdays: 09:12 to 09:41, two runs failed
consumer ask: 06:00 local
```""",
    """**Contract — analytics.active_accounts**
Grain: one row per workspace per day.
Required: workspace_id, day, active_flag. None null.
Freshness in this contract: ready by 10:00 America/Edmonton, or the dashboard shows the prior day.
Not in this contract: 06:00. The job does not finish then.
Breaks the contract: a null workspace_id, a day with two rows, or a finish after 10:00.
Owners: Noah produces. Jonah accepts the 10:00 clock or funds a faster job.
Next: both initial this by 30 September 2026. Until then the dashboard must not say 'live at 6'.""",
)

put(
    "pipeline-incident",
    "Write a pipeline failure from the log lines the user has, with the hold and the rerun owner.",
    "orders_daily failed this morning. Noah pasted one error line. The sales dashboard refreshed anyway and still shows yesterday's subtitle as today.",
    """```text
job: orders_daily
error line pasted: 15 Sep 2026 05:12 ERROR missing file s3://harbor/orders/2026-09-14.csv
table: analytics.orders_daily
last good load: 14 Sep 2026 05:40, covering 13 Sep
dashboard: refreshed 15 Sep 06:05, subtitle says 15 Sep
rerun owner: Noah Berger
credentials in the paste: none
```""",
    """**Pipeline note**
orders_daily is stale. Last good load covers 13 September, loaded 14 September 05:40.
Error on file: missing 2026-09-14.csv at 05:12. No other cause is in the paste.
Hold: do not use the dashboard figure labeled 15 September. The refresh did not bring new orders.
Rerun: Noah, after the file is actually there. Do not rerun against a missing path and call it fixed.
Next: Jonah changes the subtitle to the last good day before the 09:00 sales meeting.""",
)

put(
    "data-lineage",
    "Trace a metric to the source tables the user can name, and stop where the trail stops.",
    "Jonah asked where active_accounts comes from. Noah can point at a dbt model name and then the trail stops. The slide says 'the warehouse'.",
    """```text
metric: active_accounts, defined as workspaces with a login on that day
known hop: model fct_active_accounts, owner Noah
source tables named: none
second writer: unknown
slide text: "comes from the warehouse"
```""",
    """**Lineage note**
active_accounts is the count of workspaces with a login that day, per Jonah's definition.
Known hop: fct_active_accounts, owner Noah Berger.
Next hop: not in the file. Do not draw a source table from the column name.
The slide line 'the warehouse' is not a source.
Open: the table under the model, and whether any other job writes active_flag.
Next: Noah names that table before this metric is used in a board pack.""",
)

put(
    "retention-schedule-data",
    "Draft a retention note from the policy the user already has, not from a guessed law.",
    "A draft schedule says delete support tickets after 90 days because a blog recommended it. Fieldnote's customer contract in the folder does not mention ticket retention.",
    """```text
dataset: support.tickets
columns called out: email, home address on 6 of 14 sample rows
clause in the folder: customer contract 2026, no retention sentence
blog rule in the draft: 90 days
delete approver in their policy: privacy lead, role vacant
backups: nightly, kept 35 days, per Noah's note
```""",
    """**Retention note**
support.tickets: period unset. The contract in the folder has no clause. The 90-day blog line is removed.
Backups: 35 days, from Noah's note. A live-table delete would not clear those until they age out.
Personal columns in the sample: email, home address. That is a flag, not a delete order.
Approver: privacy lead. The role is vacant, so nobody can approve a delete from this note.
Next: counsel or the contract owner writes the period. This note does not invent one.""",
)

put(
    "warehouse-model",
    "Review a warehouse model for grain mistakes and double-counted joins.",
    "active_accounts jumped from 1,100 to 4,600 on 12 September after Noah joined the fact to payments. Payments has many rows per workspace. He has a 20-row sample.",
    """```text
claimed grain: one row per workspace per day
join added 12 Sep: payments on workspace_id
sample of 20 workspace-days: 17 have more than one payment row
metric before: 1,100 on 11 Sep
metric after: 4,600 on 12 Sep
modeler: Noah Berger
```""",
    """**Model review**
Do not use the 12 September active_accounts figure.

The claimed grain is one row per workspace per day. The payments join is many rows per workspace.
In the 20-row sample, 17 keys fan out. That is the sample, not a rate for the whole table.
The jump from 1,100 to 4,600 fits a fan-out. It is not proof of 3,500 new workspaces.
Fix to ask Noah for: count of workspace-days with more than one row, and a join that does not multiply the flag.
This review does not rewrite the model.""",
)

put(
    "freshness-sla",
    "Set a freshness promise the job can meet, from the finish times the user has.",
    "Jonah wants the dashboard to say data is ready at 06:00. Noah listed the last ten weekday finish times. Eight are after 09:00. Two failed.",
    """```text
job: fct_active_accounts
finish times: 09:12, 09:20, 09:41, failed, 09:18, 09:33, 09:15, failed, 09:28, 09:22
consumer need: 06:00 America/Edmonton
owner: Noah Berger
if late: dashboard should show the prior day, Jonah agrees
```""",
    """**Freshness note**
Do not promise 06:00. Eight finished runs landed between 09:12 and 09:41. Two failed.

Promise that matches the file: ready by 10:00, or show the prior day.
Call if it misses 10:00: Noah first, Jonah if the prior day is also missing.
The average is not the promise. The slow run is.
Next: Jonah changes the dashboard label. Noah does not sign 06:00.""",
)

put(
    "balance-reconciliation",
    "Reconcile two extracts the user provides and list the rows that do not match.",
    "Noah has two extracts for 12 September. orders_daily sums to $18,400. The billing export sums to $17,160. Three order ids appear on only one side.",
    """```text
as of: 12 Sep 2026
key: order_id
amount column: total_cad
orders_daily: 42 rows, sum 18400
billing export: 40 rows, sum 17160
only in orders_daily: 4412, 4418, 4420
only in billing: none
difference: 1240
```""",
    """**Tie-out — 12 September**
orders_daily $18,400. Billing $17,160. Gap $1,240. No plug.

| order_id | In orders_daily | In billing |
| --- | --- | --- |
| 4412 | yes | no |
| 4418 | yes | no |
| 4420 | yes | no |

The three ids are the unmatched set in these files. This note does not say why they are missing.
Do not refresh a revenue slide from orders_daily until Noah explains the three ids.
Next: Noah checks those ids by 16 September.""",
)

put(
    "access-request-data",
    "Triage an internal request for data the company already holds, against the approver they name.",
    "An analyst asked Noah for the full tickets table, including home addresses, to 'get a feel for the voice'. Their policy says the privacy lead approves personal columns. That role is vacant.",
    """```text
asker: Sam Okonkwo, analyst
table: support.tickets
why: get a feel for the voice
columns requested: all
personal columns in the table: email, home address
approver in policy: privacy lead
privacy lead: vacant
Noah's authority: he cannot approve his own pipeline, and he is not the privacy lead
```""",
    """**Access note**
Do not grant the full table.

The why is not a question the table can answer. Send it back.
If they return with a real question, drop email and home address unless the privacy lead approves. That role is vacant, so those columns wait.
Noah does not approve this. Seniority is not the approver.
A shared login is not an option in this note.
Next: Sam rewrites the why, or the request stays closed.""",
)

PACKS.append(pack(
    {"id": "blog", "title": "Blog and editorial", "summary": "Assignments, outlines, edits, and updates from sources the writer has. No copied articles.", "keywords": ["blog", "editorial", "post", "headline"]},
    """
blog-assignment | Blog Assignment | assignment
job: Assign a post with the reader, the question, the source, and the date.
triggers: blog assignment; post brief; assign an article; blog brief
inputs: The reader; The question; Sources already in hand; The due date
steps: Write the question the post answers. || Name the reader. || List sources they have. A post with no source does not get a date. || Set a due date they can hit. || Say what the post will not claim. || Do not assign a copied angle from another site.
anti: A due date with no source; A copied outline; A claim bigger than the notes
example: An editor wants a post on Calgary grocery prices by Friday. The writer has four receipts and no other source.
out: An assignment limited to those receipts, or no Friday date.
related: blog-outline; blog-source-note

blog-outline | Blog Outline | outline
job: Outline a post from the assignment and the notes, with headings the writer can draft from.
triggers: blog outline; post structure; article outline; heading plan
inputs: The assignment; The notes; The length; What must be cited
steps: Open with the question. || One heading per point they have notes for. || Mark a heading with no note as a hole. || Put the sources under the headings. || Close with what the reader can do. || Do not add a study you did not read.
anti: Headings with no notes; A fake study; An outline of someone else's post
example: The grocery post has notes for three receipts and a blank heading called 'the provincial trend'.
out: An outline that drops the trend heading until a source exists.
related: blog-assignment; blog-edit

blog-edit | Blog Edit | edit note
job: Edit a draft against the notes, and mark claims that the notes do not support.
triggers: edit this post; blog edit; line edit; claims check
inputs: The draft; The notes; The assignment; Words they must not add
steps: Check each factual sentence against the notes. || Mark unsupported sentences. Do not replace them with your own facts. || Cut repetition. || Keep the writer's voice. || Confirm the close matches the assignment. || Do not add a product pitch that was not assigned.
anti: New facts inserted by the editor; A tone rewrite that changes a number; Ignoring the notes
example: A draft says groceries are up 18 percent. The notes have four receipts and no index.
out: An edit that cuts the 18 percent and leaves the receipt totals.
related: blog-source-note; blog-outline

blog-refresh | Blog Refresh | update note
job: Update an old post with what changed, and label the update.
triggers: update this post; refresh an article; blog update; evergreen edit
inputs: The old post; What changed; The new source; The date of the old claims
steps: List claims that are now wrong or undated. || Replace only what the new source supports. || Put an update line with the date at the top. || Do not leave a stale price unlabeled. || Say what you could not recheck. || Keep the original date as well as the update date.
anti: A silent change of a number; A new claim with no source; Deleting the original date
example: A 2024 post still says a permit costs $50. The writer has a 2026 fee sheet at $75.
out: An update line and a $75 figure tied to the fee sheet, with the 2024 date kept.
related: blog-edit; content-refresh-seo

blog-series | Blog Series | series plan
job: Plan a series where each post can stand alone and the writer has notes for each part.
triggers: blog series; content series; multi-part post; series plan
inputs: The parts; Notes for each; The publishing days; The reader
steps: Cut parts that have no notes. || Make each post useful alone. || Order them by what the reader needs first. || Set dates the writer can hit. || Name the internal links. || Do not promise a part that is not sourced.
anti: A five-part promise with notes for two; Cliffhangers that hide the answer; Copied series titles
example: A four-part small-business series has notes for pricing and hiring only.
out: A two-part plan, with the other parts unscheduled.
related: blog-assignment; content-calendar

blog-source-note | Blog Source Note | source note
job: List what the post may cite, and what has to come out.
triggers: blog sources; fact check a post; citation check; what can we cite
inputs: The claims; The links or notes; What is behind a login; What is someone else's wording
steps: Match each claim to a note. || A claim with no note comes out. || Do not cite a page you cannot open. || Mark wording that is too close to another article. || Separate their receipts from a public dataset. || Do not invent a citation.
anti: A citation to a page they did not open; A lifted paragraph; A dataset they do not have
example: The draft cites a StatCan table the writer has not opened, plus four receipts they do have.
out: A note that allows the receipts and pulls the StatCan sentence.
related: citation-hygiene; blog-edit

blog-distribution | Blog Distribution | distribution note
job: Say where a finished post goes, based on channels the writer actually has.
triggers: distribute this post; blog promotion; where to share a post; republish
inputs: The live URL; Channels they control; A partner who has agreed; Places they must not paste the whole post
steps: List channels they control. || Put the link, not a full copy, on channels that are not theirs. || A partner share needs a yes already in the file. || Do not buy reposts. || Match the disclosure if the post is paid. || Set one day, not a spam burst.
anti: Pasting the full post onto someone else's site; A partner named without a yes; Bought shares
example: A plan says email the list, post the full text in a Facebook group they do not run, and tag a grocer who has not agreed.
out: A note that keeps the email and cuts the group paste and the unagreed tag.
related: blog-assignment; newsletter-editor

blog-title-pack | Blog Title Pack | title options
job: Write title options that the draft can support, with no borrowed viral headline.
triggers: blog titles; headline options; post title; H1 options
inputs: The draft's actual result; Words they will not use; The search query if they have one; The title they hoped to copy
steps: Write options from the result in the draft. || Cut a title that promises a number the draft does not have. || If a query is in the file, use it only if the draft answers it. || Reject a copied viral headline. || Give three options, not thirty. || Pick one and say why.
anti: A title with a fake percent; A copied headline; A title that answers a different post
example: They want 'Grocery prices up 18 percent in Calgary' and the draft only has four receipts.
out: Three titles about those receipts, and a no on the 18 percent title.
related: blog-edit; headline-check
"""
))

put(
    "blog-assignment",
    "Assign a post with the reader, the question, the source, and the date.",
    "Maya wants a Friday post on Calgary grocery prices. She has four receipts from 10 to 14 September and no index, no StatCan table, and no store permission.",
    """```text
reader: Calgary home cooks who shop once a week
question: what did one kitchen spend on food this week
sources in hand: 4 receipts, 10-14 Sep 2026, food total $52
not in hand: a price index, a store comment, another household
due asked: Friday 19 Sep 2026
will not claim: a city trend
```""",
    """**Assignment**
Question: what did this kitchen spend on food in the week of 14 September?
Reader: a Calgary home cook comparing their own week, not a policy audience.
Sources: the four receipts. Food total $52. Pharmacy line excluded.
Due: 19 September, only if the post stays inside those receipts.
Not assigned: a city trend, a store ranking, a percent change.
If the draft grows past the receipts, the date slips. Do not fill the hole with an unread table.""",
)

put(
    "blog-outline",
    "Outline a post from the assignment and the notes, with headings the writer can draft from.",
    "Maya has the assignment and the four receipts. She also sketched a heading called 'the provincial trend' with no note under it.",
    """```text
assignment: one kitchen, week of 14 Sep, $52 food
notes: Co-op $18.40, Co-op $22.10, market $11.50, pharmacy excluded
length: 700 words
blank heading: the provincial trend
must cite: each receipt date
```""",
    """**Outline**
H1: What this kitchen spent on food, week of 14 September

H2: The four stops — notes exist
H2: What was not food — pharmacy line, notes exist
H2: The $52 total — her sum, notes exist
H2: What this does not show — one kitchen, one week

Cut: 'the provincial trend'. No note, no heading.
Close: the reader can lay their own receipts next to this. They cannot learn a city rate from it.
Each receipt date goes under the first H2.""",
)

put(
    "blog-edit",
    "Edit a draft against the notes, and mark claims that the notes do not support.",
    "Maya's draft is 680 words. One sentence says grocery prices in Calgary are up 18 percent. The notes have the four receipts and no index.",
    """```text
draft sentence: "Grocery prices in Calgary are up 18 percent this year."
notes: four receipts, food total $52, dates 10-14 Sep 2026
assignment: one kitchen, no city trend
other sentences: match the receipts
voice: hers, short
```""",
    """**Edit note**
Cut: "Grocery prices in Calgary are up 18 percent this year." The notes do not have a percent or a city index. Do not replace it with a different percent.

Keep: the four stops, the pharmacy exclusion, the $52, the dates.
Do not add a provincial comparison to fill the cut.
The close still has to say this is one kitchen. If that sentence is missing, add her words, not a new fact.
Word count is fine. The 18 percent is the block.""",
)

put(
    "blog-refresh",
    "Update an old post with what changed, and label the update.",
    "A March 2024 post on Harbor Goods' site still says a sidewalk-display permit is $50. Diane has a 2026 town fee sheet that says $75. She wants the post updated without pretending it was always $75.",
    """```text
old post: 12 Mar 2024, "Sidewalk display permit: $50"
new source: town fee sheet, effective 1 Jan 2026, display permit $75
what she could not recheck: the inspection wait time, still written as "about a week"
update date: 20 Sep 2026
```""",
    """**Update**
Add at the top: Updated 20 September 2026. The fee below was corrected. The 12 March 2024 date stays on the post.

Replace $50 with $75, tied to the fee sheet effective 1 January 2026.
Leave the inspection sentence, and mark it unchecked: "about a week" was not on the 2026 sheet.
Do not delete the 2024 date. Do not write that the fee was always $75.""",
)

put(
    "blog-series",
    "Plan a series where each post can stand alone and the writer has notes for each part.",
    "Diane wants a four-part series for Harbor Goods: pricing, hiring, taxes, and ads. She has notes on her own prices and on the one hire she made. She has no tax notes and no ad results.",
    """```text
reader: a shop owner in Airdrie
parts asked: pricing, first hire, taxes, ads
notes: price list 2026, hire notes for Sam in June
no notes: tax, ads
days she can publish: Tuesday
```""",
    """**Series**
Two posts. The other two are not scheduled.

| Part | Standalone promise | Date |
| --- | --- | --- |
| What she charges, from the 2026 list | a reader can compare a price | Tue 23 Sep |
| The June hire, hours and wage she recorded | a reader sees one real hire | Tue 30 Sep |

Taxes and ads: no notes, no date, no 'part 3 of 4' tease.
Each post makes sense if the reader never sees the other.""",
)

put(
    "blog-source-note",
    "List what the post may cite, and what has to come out.",
    "The grocery draft cites a StatCan table Maya has not opened, and four receipts she has on the counter.",
    """```text
claim: food total $52 — source: her receipts
claim: pharmacy excluded — source: her note
claim: Calgary food up 4.2 percent — source line says StatCan, table not opened
wording: one paragraph is close to a news brief she saved
login-only PDF: not in the folder
```""",
    """**Source note**
May cite: the four receipts and her pharmacy note.
Pull: the 4.2 percent sentence. The table was not opened.
Pull: the paragraph that tracks the saved news brief. Rewrite from her receipts or cut it.
Do not add the login-only PDF. It is not in the folder.
No replacement citation gets invented in this note.""",
)

put(
    "blog-distribution",
    "Say where a finished post goes, based on channels the writer actually has.",
    "The grocery post is live. A plan says email Maya's list, paste the full text into a neighbourhood Facebook group she does not run, and tag a grocer who has not replied.",
    """```text
url: weeknighttable.example/week-of-14-sep
channels she controls: her email list, 420 people, her Instagram
partner yes: none
group: neighbourhood Facebook group, she is not a moderator
grocer: no reply to her 12 Sep note
paid: no
```""",
    """**Distribution**
Email the list once, with the link.
Instagram: the link and the $52 line she can support. Not the full post pasted as a new article.
Do not paste the full text into the Facebook group.
Do not tag the grocer. There is no yes.
One day, 21 September. Not a burst across groups she does not run.""",
)

put(
    "blog-title-pack",
    "Write title options that the draft can support, with no borrowed viral headline.",
    "Maya hoped to title the post 'Grocery prices up 18 percent in Calgary'. The draft does not contain 18 percent. It contains $52 and four receipts.",
    """```text
draft result: $52 food, four receipts, one kitchen, week of 14 Sep
query in a notebook: calgary grocery prices
title she hoped to copy: a news headline about an 18 percent jump
words she will not use: crisis, shocking
```""",
    """**Titles**
1. What I spent on food this week: $52
2. Four receipts, one Calgary kitchen, week of 14 September
3. This is not a grocery index

Use 1. It is the number in the draft.
No on 'Grocery prices up 18 percent in Calgary'. The draft cannot support it.
The notebook query is not a reason to promise a city answer. The post does not answer that query.""",
)
