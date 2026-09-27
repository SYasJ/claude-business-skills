from dense import pack
from scenario_bank import put

PACKS = []

PACKS.append(pack(
    {"id": "media", "title": "Media and communications", "summary": "Newsroom assignments, source logs, and headlines that do not invent quotes.", "keywords": ["news", "newsroom", "headline", "editorial", "media"]},
    """
news-assignment | News Assignment | assignment
job: Assign a story with the question, the sources already in hand, and what is not known.
triggers: news assignment; story brief; assign a reporter; news budget item
inputs: The question; Sources in hand; The deadline; What must not be implied
steps: Write the question, not the conclusion. || List sources they have. || Mark what is unknown. || Set a deadline that matches the sources. || Say what the story will not claim if a source is missing. || Do not assign a version that needs a quote they do not have.
anti: A conclusion assigned as the story; A deadline with no source; An implied wrongdoing
example: A desk wants a story that a plant 'cut safety' by Friday. The only source is a company statement about a turnaround.
out: An assignment about the turnaround dates in the statement, not a safety verdict.
related: source-log-news; editorial-brief

source-log-news | Source Log | source log
job: Log who said what, when, and whether it was on the record.
triggers: source log; who said this; on the record; news sources
inputs: The notes; Whether each person was on the record; Documents; What was not confirmed
steps: One row per source. || Mark on the record, background, or not for use, as the reporter noted. || A quote with no name and no note does not go in the story. || Separate a document from a recollection. || Do not upgrade background to on the record. || Record who did not call back.
anti: A quote with no source; Background used as a named quote; A document they do not have
example: A sentence is attributed to 'a worker' and the notebook says the person would not be named.
out: A log that keeps the sentence out of the named story.
related: news-assignment; citation-hygiene

headline-check | Headline Check | headline check
job: Check a headline against the story's sourced facts.
triggers: headline check; does this hed work; news headline; front-page line
inputs: The headline; The sourced facts; The words that overclaim; The editor's deadline
steps: Underline every factual word in the headline. || Match each to a sourced sentence. || Cut a number, cause, or blame the story does not have. || Offer two headlines that match. || Do not write a clever line that adds a fact. || If the story is thin, say the headline has to be thin.
anti: A cause the story does not prove; A number not in the copy; Blame in the hed only
example: The hed says the plant cut safety staff. The story only has turnaround dates.
out: A hed about the dates, and a no on the staffing claim.
related: news-assignment; blog-title-pack

right-of-reply | Right of Reply | reply note
job: Record what a person was asked, what they answered, and the deadline they were given.
triggers: right of reply; comment request; fair comment; response deadline
inputs: The specific claim they were asked about; When they were asked; What they replied; The deadline
steps: Write the claim in the words that will be published. || Record the ask time and the deadline. || Record the reply verbatim or say they did not reply. || Do not paraphrase a no-comment into agreement. || If the deadline has not passed, the story does not say they refused. || Keep the note with the story.
anti: A no-comment turned into agreement; A deadline that already passed before the ask; A vague 'we reached out'
example: The company was asked at 16:00 for a 17:00 deadline about a staffing cut the story cannot source.
out: A note that the ask was too late and the claim is not ready.
related: news-assignment; interview-prep-comms

live-blog-update | Live Update | live update
job: Add one timestamped update from a new sourced fact, without mixing it into older items.
triggers: live blog; news update; developing story; timestamped update
inputs: The new fact; The source; The time; What is still unconfirmed
steps: Time-stamp the update. || Attribute the new fact. || Do not merge it into an older item so the time looks earlier. || Say what is still unconfirmed. || Correct an earlier item in a new line, do not silently change it. || Stop if the fact has no source.
anti: A silent edit of an old timestamp; An unconfirmed line written as fact; No source
example: At 14:10 a spokesperson confirms the turnaround starts Monday. An earlier item guessed Sunday.
out: A 14:10 update with the Monday date, and a correction line for the Sunday guess.
related: correction-note; news-assignment

desk-handoff | Desk Handoff | handoff
job: Hand a story to the next shift with what is confirmed, what is open, and who owns the next call.
triggers: desk handoff; shift handoff news; story handoff; night desk note
inputs: What is confirmed; What is open; The next call; The deadline
steps: Lead with confirmed facts. || List open questions. || Name the next person to call and whether they have already been called. || Do not leave a quote half-checked. || Pass documents by name. || Say what the next shift must not publish yet.
anti: A handoff that is only enthusiasm; An open quote treated as checked; No owner for the next call
example: The day desk hands off a staffing-cut story with no document and no reply logged.
out: A handoff that blocks publication until a source is in the log.
related: source-log-news; shift-handover

embargo-check | Embargo Check | embargo note
job: Check whether an embargo still applies and who agreed to it.
triggers: embargo; can we publish; press embargo; release time
inputs: The document; The embargo time; Who agreed; The clock now
steps: Record the embargo time in the zone they stated. || Say whether this desk agreed. || If they did not agree, do not invent an obligation, and do not help break a confidence they do hold. || If the time has passed, say so. || Do not publish early to beat a competitor if they agreed. || Name the owner of the decision.
anti: Publishing early after agreeing; A guessed embargo; No time zone
example: A release says 10:00 ET Tuesday. The desk agreed. It is 07:30 MT Tuesday.
out: A note that 07:30 MT is 09:30 ET, so the embargo has not lifted.
related: news-assignment; pr-pitch

news-budget | News Budget | budget note
job: Rank stories the desk can staff today from the sources they have, not from the stories they wish they had.
triggers: news budget; story list; what leads; rundown
inputs: The candidates; The sources for each; The staff on shift; The slot count
steps: Cut stories with no source. || Match the rest to the people on shift. || Put the best-sourced story first, not the loudest topic. || Say what slips. || Do not staff a story with a person who is not on the shift. || Leave a slot empty rather than fill it with an unsourced item.
anti: A lead with no source; A full rundown nobody can report; A wish list called a budget
example: Five stories are on the board. Two have documents. Three reporters are on shift.
out: A budget with two stories staffed and three cut.
related: news-assignment; editorial-calendar-newsroom
"""
))

put(
    "news-assignment",
    "Assign a story with the question, the sources already in hand, and what is not known.",
    "The desk wants a Friday story that Prairie Line 'cut safety' at a plant. The only document is a company statement that a turnaround starts Monday 22 September and lasts ten days.",
    """```text
question the desk wrote: did the plant cut safety staff
document: company statement, 15 Sep 2026, turnaround starts 22 Sep, ten days, no staffing figures
other sources: none
deadline asked: Friday 19 Sep 17:00
must not imply: a safety verdict
reporter: Jonah Ellis
```""",
    """**Assignment**
Question: what dates did the company state for the turnaround, and what did the statement not say?
Source: the 15 September statement only.
Not assigned: a safety-staff verdict. There is no figure and no worker on the record.
Deadline: 19 September only for a story that stays inside the statement.
If a second source arrives, this assignment is rewritten. It is not expanded in the draft.""",
)

put(
    "source-log-news",
    "Log who said what, when, and whether it was on the record.",
    "Jonah's notebook has a company statement and a sentence from a person who said they would not be named and would not be quoted.",
    """```text
source 1: Prairie Line statement, 15 Sep 2026, on the record as a document, turnaround 22 Sep, ten days
source 2: person at the gate, 15 Sep 16:40, said "do not quote me and do not name me"
callback: spokesperson, left message 15 Sep 17:10, no reply
document not in hand: any staffing list
```""",
    """**Source log**
| Source | Status | Use |
| --- | --- | --- |
| 15 Sep statement | document | dates only |
| Gate conversation 16:40 | not for use | out |
| Spokesperson | no reply | do not write 'declined' |

The unnamed sentence does not go in the story.
No staffing list, so no staffing claim.""",
)

put(
    "headline-check",
    "Check a headline against the story's sourced facts.",
    "The copy desk wrote 'Plant cuts safety staff before 10-day shutdown'. The story only has the 22 September start and the ten-day length from the statement.",
    """```text
headline: Plant cuts safety staff before 10-day shutdown
sourced: turnaround starts 22 Sep 2026, ten days, company statement 15 Sep
not sourced: safety staff, cuts, blame
deadline: 19 Sep 16:00
```""",
    """**Headline check**
No. 'Cuts safety staff' is not in the story.

Options that match:
1. Company says plant turnaround starts 22 September
2. Statement: ten-day turnaround from Monday

Use 1. It is the date in the document.
Do not add a cause to make the line sharper.""",
)

put(
    "right-of-reply",
    "Record what a person was asked, what they answered, and the deadline they were given.",
    "An editor wants to write that the company refused to comment on a staffing cut. The ask went out at 16:00 for a 17:00 deadline, and the story cannot source the cut.",
    """```text
claim they would be asked about: a safety-staff cut
ask sent: 15 Sep 2026 16:00
deadline given: 15 Sep 17:00
reply: none by 17:00
can the story source the cut: no
```""",
    """**Reply note**
Do not write that they refused, and do not publish the cut.

The ask gave one hour, at the end of the day, about a claim the story cannot source.
No reply by 17:00 is not a refusal in this note. The deadline was not a fair window, and the claim is not ready.
Next: if the story becomes the turnaround dates only, a comment on staffing is unnecessary.""",
)

put(
    "live-blog-update",
    "Add one timestamped update from a new sourced fact, without mixing it into older items.",
    "At 11:00 the live blog guessed the turnaround might start Sunday. At 14:10 a spokesperson confirmed Monday 22 September. Jonah needs the update line.",
    """```text
earlier item: 11:00, "may start Sunday", no source named
new fact: spokesperson, on the record, 14:10, starts Monday 22 Sep, ten days
still unconfirmed: staffing, cause, which units
clock zone: America/Edmonton
```""",
    """**Update — 14:10**
A spokesperson said on the record that the turnaround starts Monday 22 September and is planned for ten days.

Still unconfirmed: staffing, cause, which units. Do not add them here.

Correction: the 11:00 item guessed Sunday and named no source. It stands as a bad item. Do not edit it into Monday. Point readers to this line.""",
)

put(
    "desk-handoff",
    "Hand a story to the next shift with what is confirmed, what is open, and who owns the next call.",
    "Jonah is leaving at 18:00. The night desk has one editor. The staffing-cut version has no document. The statement version is ready.",
    """```text
confirmed: statement dates, 22 Sep start, ten days
open: staffing, no document, spokesperson has not replied
next call: none queued
night staff: one editor, no reporter
must not publish: the staffing-cut version
```""",
    """**Handoff**
Publishable: the statement dates only, if the night editor wants a brief.
Not publishable: any staffing-cut line.
Open: spokesperson reply. Nobody is queued to call again tonight.
Do not leave the night editor to 'find a worker'. That source is not in the log.
Documents: the 15 September statement, in the story folder.""",
)

put(
    "embargo-check",
    "Check whether an embargo still applies and who agreed to it.",
    "A utility release is embargoed until 10:00 ET Tuesday. The desk agreed in writing on Monday. It is 07:30 in Calgary on Tuesday. An editor wants to post now.",
    """```text
embargo: 10:00 ET, Tuesday 16 Sep 2026
desk agreed: yes, email 15 Sep 18:04
now: 07:30 America/Edmonton, Tuesday 16 Sep
ET offset they stated: ET is 2 hours ahead of MT
decision owner: Jonah Ellis
```""",
    """**Embargo note**
Do not post.

07:30 MT is 09:30 ET. The embargo they agreed to lifts at 10:00 ET, which is 08:00 MT.
The desk agreed. Early is not available.
Owner: Jonah. Post at or after 08:00 MT if the story is ready, not before.""",
)

put(
    "news-budget",
    "Rank stories the desk can staff today from the sources they have, not from the stories they wish they had.",
    "Five items are on the board. Two have documents. Three reporters are on shift, and one is already out on a fire briefing. Four slots are open on the site.",
    """```text
candidates: plant turnaround (statement in hand), fare change (airline PDF in hand), school board rumor (no source), shop-fire follow (reporter out), council land vote (agenda PDF, no vote yet)
staff: 3 reporters, 1 already on the fire
slots: 4
```""",
    """**Budget**
Staff two. Leave the other slots empty.

| Story | Source | Who |
| --- | --- | --- |
| Turnaround dates | statement | Jonah |
| Fare change | airline PDF | second reporter |

Not today: the school rumor, the land vote that has not happened, a second fire story. The reporter is already out and has not filed.
A full rundown is not the goal. An empty slot is better than an unsourced item.""",
)

PACKS.append(pack(
    {"id": "seo", "title": "Search", "summary": "Query maps, intent, and index notes from pages and data the user can show. No cloaking or fake reviews.", "keywords": ["seo", "search", "keywords", "local"]},
    """
keyword-map | Keyword Map | query map
job: Map queries to pages the user already has, using only queries they exported or listed.
triggers: keyword map; query mapping; which page for this query; SEO map
inputs: The queries they listed; The pages; The page that already answers each; Queries with no page
steps: One query, one page. || If two pages answer it, pick the one they want and say the other should not compete. || A query with no page is a gap, not a reason to invent a page today. || Do not add queries from memory. || Mark intent in their words. || Do not recommend hidden text or a doorway page.
anti: Queries they did not list; Two pages aimed at one query; A doorway page
example: Harbor Goods has a furnace page and an oil-change page. They listed eight queries. Two match no page.
out: A map of the six matches and a gap list of two, with no new doorway URLs.
related: search-intent; seo-content-brief

technical-seo-note | Technical SEO Note | technical note
job: Turn crawl findings the user exported into a fix list a developer can accept or reject.
triggers: technical SEO; crawl errors; index issues; site audit
inputs: The export; The template they use; Who deploys; What they will not change this month
steps: Use rows from the export. || Group by template, not by every URL. || Cut findings they said are out of scope. || Do not invent a ranking lift. || Name the owner. || Separate a blocked page from a slow page if the export shows which.
anti: A ranking promise; Findings not in the export; A rewrite of the whole site
example: A crawl of 40 URLs shows 12 furnace pages missing a title and the blog blocked by a test noindex.
out: A fix list for the title template and a note to remove the test noindex, with no traffic promise.
related: index-coverage; technical-design-doc

search-intent | Search Intent | intent note
job: Say what the searcher is trying to do, from the query and the page the user has.
triggers: search intent; what does this query want; intent mismatch; query vs page
inputs: The query; The page; What the page actually answers; What the searcher likely needs done
steps: Restate the query. || Say what the page answers in one sentence. || If those differ, say mismatch. || Recommend a change to the page or a different query. || Do not stuff the query into a page that answers something else. || Use their wording for the job-to-be-done.
anti: Query stuffing; A mismatch ignored; Intent copied from a tool they did not run
example: The query is 'furnace repair Airdrie'. The page is a brand story with no service area and no phone.
out: A note that the page does not answer the query until the service facts are on it.
related: keyword-map; local-seo-note

internal-links | Internal Link Plan | link plan
job: Plan internal links from pages that exist to pages that answer the next question.
triggers: internal links; site links; link plan; related pages
inputs: The source pages; The target pages; The anchor words they will use; Pages they do not want linked
steps: Link only to URLs they listed. || Anchors must match the target, not a keyword they wish they ranked for. || Do not add a link on every paragraph. || Skip pages they marked no. || Say which links are in the body, not the footer spam block. || Do not recommend buying links or a link scheme.
anti: A link scheme; Anchors that misstate the target; Links to URLs that are not theirs
example: The furnace page should point to the oil-change page with the anchor 'emergency plumber'.
out: A plan that rejects that anchor and uses words that match the oil-change page.
related: keyword-map; information-architecture

content-refresh-seo | Search Refresh | refresh note
job: Decide whether an old URL should be updated, from the query and the stale claim.
triggers: update this URL; content refresh SEO; stale page; refresh versus new URL
inputs: The URL; The query; The stale sentence; The new fact they can source
steps: Keep the URL if the query still matches the page's job. || Replace the stale sentence only with the sourced fact. || Put the update date. || A new URL is for a new job, not for a date change. || Do not add a city or a price they cannot source. || Do not cloak the old content for bots.
anti: A new URL for the same job; A silent price change; Cloaking
example: The permit page ranks for a query they still want, and the fee is wrong.
out: A refresh of the same URL, with the new fee and the date, not a second URL.
related: blog-refresh; keyword-map

local-seo-note | Local SEO Note | local note
job: Check a local listing and a location page against the name, address, and phone the user uses.
triggers: local SEO; Google Business; NAP; location page
inputs: The name, address, and phone they use; The listing as they see it; The location page; Hours
steps: Compare name, address, and phone. || Note mismatches. Do not 'fix' them with a different address. || Hours must match the door. || Do not invent reviews or ask for fake ones. || Categories must match the work they do. || Say who edits the listing.
anti: Fake reviews; A listing address they do not occupy; A category for work they do not do
example: The listing says open Sunday. The shop is closed Sunday. The phone matches.
out: A note to change Sunday hours and to leave the phone alone.
related: search-intent; keyword-map

serp-gap | SERP Gap | gap note
job: Compare the user's page to what they can see on the results page, without inventing ranks.
triggers: SERP gap; why are we not ranking; results page review; competitor page
inputs: The query; Their page; What they personally see on the results page; What they will not copy
steps: Describe only the results they looked at, with the date. || Do not invent a rank or a search-volume number. || Say what those pages answer that theirs does not. || Recommend a factual gap to fill, not a copy. || Do not copy another site's text. || If they did not look, say so.
anti: A fake rank; A copied paragraph; Volume numbers from memory
example: They looked at the query and their page has no city and no hours. They did not record a rank.
out: A gap note about city and hours, with no rank claim.
related: keyword-map; local-seo-note

index-coverage | Index Coverage | index note
job: Read an index export and say which URLs are out and why the export says so.
triggers: index coverage; not indexed; coverage report; pages not in search
inputs: The export; The URLs they care about; A noindex they know about; Who can change the template
steps: Count from the export. || Group by the reason in the export. || A test noindex they know about is a finding, not a mystery. || Do not promise indexation. || Name the owner of the template. || Ignore URLs they said do not matter.
anti: A promise that a page will rank once indexed; Reasons not in the export; Panic over URLs they do not care about
example: 30 blog URLs are excluded by a noindex left on from a March test.
out: A note to remove that noindex, with no ranking promise.
related: technical-seo-note; blog-refresh
"""
))

put(
    "keyword-map",
    "Map queries to pages the user already has, using only queries they exported or listed.",
    "Diane listed eight queries for Harbor Goods. The site has a furnace page and an oil-change page. Two queries match neither.",
    """```text
pages: /services/furnace, /services/oil-change
queries she listed 18 Sep 2026:
furnace repair Airdrie -> furnace page
furnace tune-up Airdrie -> furnace page
emergency furnace Airdrie -> furnace page
oil change Airdrie -> oil-change page
synthetic oil change -> oil-change page
oil change price -> oil-change page
plumber Airdrie -> no page
roof repair -> no page
```""",
    """**Query map**
| Query | Page |
| --- | --- |
| furnace repair Airdrie | /services/furnace |
| furnace tune-up Airdrie | /services/furnace |
| emergency furnace Airdrie | /services/furnace |
| oil change Airdrie | /services/oil-change |
| synthetic oil change | /services/oil-change |
| oil change price | /services/oil-change |

Gaps, not new doorway URLs: plumber Airdrie, roof repair. She does not do that work. Do not make pages for them.
Do not point furnace queries at the oil-change page.""",
)

put(
    "technical-seo-note",
    "Turn crawl findings the user exported into a fix list a developer can accept or reject.",
    "A crawl of 40 Harbor Goods URLs on 18 September shows 12 service URLs with an empty title and every /blog URL marked noindex. Diane says the blog block was a March test.",
    """```text
export: 40 URLs, 18 Sep 2026
empty title: 12 URLs, all under /services/
noindex: 9 URLs, all under /blog/
out of scope this month: a redesign
deploy owner: her contractor, Sam, Fridays
```""",
    """**Fix list**
1. Title template on /services/. 12 URLs, one template, not 12 projects.
2. Remove the March test noindex on /blog/. 9 URLs.

Not this month: a redesign.
No ranking lift is claimed. The export does not show ranks.
Owner: Sam, Friday deploy. Diane checks one service URL and one blog URL after.""",
)

put(
    "search-intent",
    "Say what the searcher is trying to do, from the query and the page the user has.",
    "The query Diane cares about is 'furnace repair Airdrie'. The furnace page tells the shop's origin story and does not list the city, the phone, or what a repair visit includes.",
    """```text
query: furnace repair Airdrie
page: /services/furnace
page answers: how the shop started in 2014
searcher job: find someone who will come fix a furnace in Airdrie
phone on the home page: 403-555-0148
phone on this page: absent
```""",
    """**Intent note**
Mismatch. The query asks for a repair in Airdrie. The page answers a brand story.

Do not stuff the query into the origin paragraph.
Add, if she can stand behind it: the city, the phone that is already on the home page, and what a repair visit includes. She has not written the visit scope. Leave that blank rather than inventing a promise.
Until those facts are on the page, this URL does not answer the query.""",
)

put(
    "internal-links",
    "Plan internal links from pages that exist to pages that answer the next question.",
    "Diane wants the furnace page to link to oil changes. A draft anchor says 'emergency plumber'. The oil-change page is about oil changes. She does not want a link to the blog test.",
    """```text
source: /services/furnace
target she wants: /services/oil-change
anchor in the draft: emergency plumber
blog: /blog/*, noindex, do not link
other target: none
```""",
    """**Link plan**
One body link, not a footer dump.

From /services/furnace to /services/oil-change.
Anchor: oil changes, or synthetic oil change. Not 'emergency plumber'. That is a different job, and she has no plumber page.
No links to /blog/ while the test noindex is on.
No links to other domains.""",
)

put(
    "content-refresh-seo",
    "Decide whether an old URL should be updated, from the query and the stale claim.",
    "The page /permits/sidewalk still ranks for a query Diane wants. It says the fee is $50. The 2026 fee sheet says $75. Someone suggested a new URL so the old one can stay.",
    """```text
url: /permits/sidewalk
query she still wants: sidewalk display permit Airdrie
stale sentence: fee is $50
new fact: town fee sheet, 1 Jan 2026, $75
new URL suggested: /permits/sidewalk-2026
```""",
    """**Refresh note**
Keep /permits/sidewalk. The query is the same job.
Replace $50 with $75 and cite the fee sheet. Add: updated 20 September 2026.
Do not make /permits/sidewalk-2026. A new URL is a new job. This is not one.
Do not show the old fee to people and the new fee to crawlers. One page, one fee.""",
)

put(
    "local-seo-note",
    "Check a local listing and a location page against the name, address, and phone the user uses.",
    "Harbor Goods' door is closed Sunday. The listing Diane looked at on 18 September says open Sunday 10 to 4. The phone matches. The listing category is 'plumber'.",
    """```text
name on the door: Harbor Goods
address: 18 Centre Ave, Airdrie
phone: 403-555-0148
listing hours: Sun 10:00-16:00
door hours: closed Sunday, Mon-Sat 08:00-17:00
listing category: plumber
work they do: furnace and oil change
who can edit: Diane
```""",
    """**Local note**
Change Sunday to closed. The door is the source.
Leave the phone. It matches.
Change the category off plumber. She does not do that work. Use a category that matches furnace or auto service only if the listing offers that exact label. If she is unsure of the label, she picks it in the product, not in this note.
Do not ask anyone for a fake review.
Editor: Diane.""",
)

put(
    "serp-gap",
    "Compare the user's page to what they can see on the results page, without inventing ranks.",
    "Diane searched 'furnace repair Airdrie' on 18 September and looked at the top three results she saw. She did not write down a rank for her own page. Those three pages show a city, a phone, and hours. Hers does not.",
    """```text
query: furnace repair Airdrie
date looked: 18 Sep 2026
her page has: origin story
pages she saw: three local service pages with city, phone, hours
her rank: not recorded
volume: not in any export
will not copy: their wording
```""",
    """**Gap note**
No rank. She did not record one. No volume. None was exported.

Gap she can see: those pages state city, phone, and hours. Her furnace page does not.
Fill with her own facts: Airdrie, 403-555-0148, Mon-Sat 08:00-17:00, closed Sunday.
Do not copy their sentences. Do not add a review count she does not have.""",
)

put(
    "index-coverage",
    "Read an index export and say which URLs are out and why the export says so.",
    "Diane exported coverage on 18 September. 30 URLs are excluded. 9 are the blog, reason noindex. The other 21 are old tag URLs she says do not matter.",
    """```text
export date: 18 Sep 2026
excluded: 30
reason noindex: 9, all /blog/
reason crawled not indexed: 21, all /tag/
she cares about: the 9 blog URLs
she does not care about: /tag/
template owner: Sam
known test: blog noindex added in March
```""",
    """**Index note**
The 9 blog URLs are out because of noindex. That matches the March test. Remove it.
The 21 tag URLs are in the export and out of scope. Do not spend the month on them.
This note does not say the blog will rank after the tag is removed. Indexing is not a rank.
Owner: Sam. Diane rechecks one blog URL after the Friday deploy.""",
)

PACKS.append(pack(
    {"id": "research", "title": "Research", "summary": "Search logs, consent, and claims that stay inside the evidence. No invented citations.", "keywords": ["research", "evidence", "consent", "replication"]},
    """
source-search-log | Search Log | search log
job: Log the searches and the dates so a review can see what was looked for.
triggers: search log; literature search; what did we search; database log
inputs: The databases; The query strings; The dates; What was not searched
steps: Record each database, query, and date. || Record zero results as zero. || Do not add databases they did not open. || Note filters. || Say who ran it. || A log is not a review.
anti: A database listed that was not opened; A dropped zero; No date
example: A draft methods section lists three databases. The notebook shows two, one of them with zero hits.
out: A log of the two searches, including the zero, and the third name removed.
related: literature-review-plan; citation-hygiene

consent-script | Consent Script | consent script
job: Draft the words a participant hears before they agree, from the study facts the user has.
triggers: consent script; participant consent; verbal consent; information sheet
inputs: What the person will be asked to do; What is recorded; How they can stop; What the user cannot promise
steps: Say the task and the time. || Say what is recorded. || Say they can stop. || Do not promise confidentiality the design cannot keep. || Do not hide a risk they named. || This is a draft for the ethics owner, not an approval.
anti: A promise of anonymity the recording breaks; Hidden recording; A script that is also the ethics approval
example: Interviews will be recorded and the script says nobody will know who spoke.
out: A script that says the recording exists and names who will hear it.
related: ethics-review-prep; interview-guide-research

replication-check | Replication Check | replication note
job: Check whether a result can be rerun from the files the user has.
triggers: replication; can we rerun this; reproducibility check; data for a result
inputs: The result; The data file; The steps they wrote down; The missing piece
steps: Match the result to a file. || Walk the steps they wrote. || Stop at the first missing file or parameter. || Do not fill a missing parameter with a plausible one. || Say rerunnable or not, from this folder. || Name what would make it rerunnable.
anti: A plausible parameter treated as the original; A pass with a missing file; A new analysis called a replication
example: Table 2 cannot be rerun. The analysis script points to a CSV that is not in the folder.
out: A note that Table 2 is not rerunnable until that CSV is produced.
related: data-availability; research-memo

data-availability | Data Availability | availability statement
job: Write a data-availability statement that matches the files they can actually share.
triggers: data availability; what data can we share; availability statement; open data note
inputs: The files; What contains personal data; The repository they will use; What they cannot share
steps: Name files they will deposit. || Hold files they said contain personal data. || Do not write 'available on request' if they have no process. || Give the repository only if it exists. || Match the statement to the files, not to a journal template. || Say who approves a later request.
anti: A template statement; Personal data in the deposit; A repository that does not exist
example: A draft says data are in dba_ripple. No deposit exists. Two files have names and phone numbers.
out: A statement that the deposit is not up, and those two files are not in the share set.
related: replication-check; consent-script

reviewer-response | Reviewer Response | response draft
job: Draft a response to reviewer comments from the changes the authors actually made.
triggers: reviewer response; respond to reviewers; revision letter; peer review reply
inputs: The comments; The changes made; The comments they will not follow; The page or line they can cite
steps: Answer the comment they received, not a softer version. || Point to the change they made. || If they did not change it, say so and why. || Do not invent a new analysis to please a reviewer. || Do not insult the reviewer. || Keep each reply next to its comment.
anti: A fake new experiment; A reply to a comment they were not sent; A rude rebuttal
example: Reviewer 2 asked for a second dataset. The authors did not collect one.
out: A reply that says the dataset was not collected, with no invented table.
related: research-memo; claim-limit-note

claim-limit-note | Claim Limit | claim note
job: Limit a sentence to what the study design can support.
triggers: overclaim; limit this sentence; what can we conclude; claim check
inputs: The sentence; The design; The sample; The outcome they measured
steps: Restate the design in one line. || Cut words that say cause if they ran an association. || Cut words that say people in general if the sample is one site. || Do not add a policy recommendation the study did not test. || Offer a replacement sentence. || Keep the limit next to the claim.
anti: Cause language on an association; A national claim from one site; A policy line with no test
example: A sentence says the workshop caused employment. The study asked 20 people at one site how confident they felt.
out: A sentence about confidence at that site, with cause and employment removed.
related: research-memo; evidence-table
"""
))

put(
    "source-search-log",
    "Log the searches and the dates so a review can see what was looked for.",
    "A methods draft says Nia searched PubMed, Scopus, and Web of Science on 2 September. Her notebook shows PubMed and Scopus only. Scopus returned zero hits. Web of Science is not in the notebook.",
    """```text
who: Dr. Nia Okonkwo
date in the draft: 2 Sep 2026
PubMed: query "small shop hiring interview", 42 hits, notebook page 3
Scopus: same query, 0 hits, notebook page 3
Web of Science: not in the notebook
filters: English, 2018-2026, written on page 3
```""",
    """**Search log**
| Database | Date | Query | Hits |
| --- | --- | --- | --- |
| PubMed | 2 Sep 2026 | small shop hiring interview | 42 |
| Scopus | 2 Sep 2026 | small shop hiring interview | 0 |

Filters: English, 2018-2026.
Web of Science comes out of the methods draft. It was not opened.
Zero stays in the log. A log is not a review.""",
)

put(
    "consent-script",
    "Draft the words a participant hears before they agree, from the study facts the user has.",
    "Nia will record 30-minute interviews. Two researchers will hear the audio. A draft script says nobody will know who spoke.",
    """```text
task: one interview, 30 minutes, about hiring
recorded: audio
who hears it: Nia and one co-researcher
stop: they can stop at any time, recording deleted if they ask before publication
cannot promise: that a quote will be unrecognizable to their own staff
ethics owner: the college board, not this script
```""",
    """**Words they hear**
This is a 30-minute interview about hiring. I will record audio.
Nia Okonkwo and one co-researcher will hear it. I cannot promise your staff would not recognize a detailed story.
You can stop at any time. If you ask before publication, the recording is deleted.
This script is not the ethics approval. The board still has to accept the study.

**Removed**
"Nobody will know who spoke." The recording and the small staff make that false.""",
)

put(
    "replication-check",
    "Check whether a result can be rerun from the files the user has.",
    "Table 2 in Nia's draft cites analysis.R and interviews.csv. The R script is in the folder. The CSV is not. A README mentions a cutoff of 0.5 that is not in the script.",
    """```text
result: Table 2, 20 interviews, mean confidence 3.4
script in folder: analysis.R
file the script reads: interviews.csv
interviews.csv in folder: no
cutoff 0.5: in the README, not in the script
```""",
    """**Replication note**
Table 2 is not rerunnable from this folder.
The script is here. interviews.csv is not. Stop there.
Do not type 0.5 into the script from the README and call it replicated.
What would make it rerunnable: the CSV the script names, unchanged, and a note if 0.5 was ever used.
This is not a new analysis.""",
)

put(
    "data-availability",
    "Write a data-availability statement that matches the files they can actually share.",
    "A journal template in the draft says the data are in Zenodo. Nia has not created a deposit. Two spreadsheets have participant names and phone numbers.",
    """```text
files: codebook.pdf, interview-guide.pdf, contacts.xlsx, raw-notes.xlsx
personal data: names and phones in contacts.xlsx and in a column of raw-notes.xlsx
repository: none created
later requests: Nia will answer, no process written
template line: "Data are available in Zenodo"
```""",
    """**Availability statement**
Do not use the Zenodo line. No deposit exists.
Not for deposit: contacts.xlsx, and the name and phone column in raw-notes.xlsx.
codebook.pdf and interview-guide.pdf can be deposited once a repository exists.
Until then the statement is: these two files are not yet in a repository. Personal-data files are not in the share set.
'Available on request' is not in this statement. There is no written process.""",
)

put(
    "reviewer-response",
    "Draft a response to reviewer comments from the changes the authors actually made.",
    "Reviewer 2 asked for a second dataset from another town. Nia did not collect one. She did add a sentence limiting the claim to one site.",
    """```text
comment: collect a comparison dataset from a second town
change made: paragraph 4 now says one site, 20 interviews
change not made: no second dataset
line to cite: paragraph 4, revision 18 Sep 2026
tone: direct
```""",
    """**Response**
Reviewer 2 asked for a second dataset. We did not collect one. We cannot add a table we do not have.

What changed: paragraph 4 now limits the claim to this site and these 20 interviews (revision 18 September 2026).
What did not change: the sample. A second town is future work, not this paper.
No new experiment is described.""",
)

put(
    "claim-limit-note",
    "Limit a sentence to what the study design can support.",
    "The draft says the hiring workshop caused employment. The study was 20 interviews at one shop about how confident people felt after the workshop. No jobs were tracked.",
    """```text
sentence: "The workshop caused employment."
design: interviews, one site, no comparison group
sample: 20 staff, June 2026
measured: self-rated confidence, 1 to 5
not measured: jobs, wages, offers
```""",
    """**Claim note**
Do not say the workshop caused employment. Jobs were not measured. The design cannot support cause.

Replacement: At this shop, 20 people rated their confidence after the workshop. This is not a finding about employment, and it is not a finding about other shops.
Keep that limit in the same paragraph as any confidence number.
No policy line. None was tested.""",
)
