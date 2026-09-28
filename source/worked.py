"""Build a scenario, sample data, and a filled outcome for every skill."""

from __future__ import annotations

import random
import re

from scenario_bank import BANK

CONTEXTS = {
    "finance": ("Northline Studio", "Mara Chen", "founder", "Calgary"),
    "accounting": ("Northline Studio", "Priya Shah", "controller", "Calgary"),
    "legal": ("Northline Studio", "Elena Voss", "operations lead", "Calgary"),
    "people": ("Northline Studio", "Chris Adeyemi", "people lead", "Calgary"),
    "strategy": ("Northline Studio", "Mara Chen", "founder", "Calgary"),
    "sales": ("Fieldnote", "Samir Qureshi", "account executive", "Edmonton"),
    "marketing": ("Fieldnote", "Lena Ortiz", "marketing lead", "Edmonton"),
    "product": ("Fieldnote", "Jonah Park", "product manager", "Edmonton"),
    "engineering": ("Fieldnote", "Aisha Rahman", "engineering lead", "Edmonton"),
    "data": ("Fieldnote", "Noah Berger", "data lead", "Edmonton"),
    "security": ("Fieldnote", "Aisha Rahman", "engineering lead", "Edmonton"),
    "operations": ("Harbor Goods", "Diane Cho", "operations manager", "Airdrie"),
    "delivery": ("Harbor Goods", "Owen Blake", "delivery lead", "Airdrie"),
    "customer": ("Fieldnote", "Rita Santos", "support lead", "Edmonton"),
    "risk": ("Northline Studio", "Priya Shah", "controller", "Calgary"),
    "healthcare": ("Cedar Clinic", "Dr. Helen Cho", "clinic director", "Red Deer"),
    "education": ("Riverbend College", "Mark Ellison", "program chair", "Lethbridge"),
    "research": ("Riverbend College", "Dr. Nia Okonkwo", "research lead", "Lethbridge"),
    "design": ("Fieldnote", "Lena Ortiz", "design lead", "Edmonton"),
    "supply-chain": ("Harbor Goods", "Diane Cho", "supply lead", "Airdrie"),
    "manufacturing": ("Redline Parts", "Gus Moretti", "plant manager", "Nisku"),
    "real-estate": ("Cedar Street Properties", "Helen Cho", "property manager", "Airdrie"),
    "construction": ("Birch Siteworks", "Tom Reilly", "site lead", "Cochrane"),
    "hospitality": ("Lantern Inn", "Sofia Alvarez", "front office manager", "Banff"),
    "retail": ("Harbor Goods", "Diane Cho", "store lead", "Airdrie"),
    "nonprofit": ("Open Kitchen Society", "Amira Hassan", "program director", "Calgary"),
    "sustainability": ("Prairie Line Energy", "Devon Hale", "reporting lead", "Calgary"),
    "insurance": ("Northline Studio", "Priya Shah", "controller", "Calgary"),
    "banking": ("Northline Studio", "Priya Shah", "controller", "Calgary"),
    "entrepreneurship": ("Northline Studio", "Mara Chen", "founder", "Calgary"),
    "productivity": ("Northline Studio", "Mara Chen", "founder", "Calgary"),
    "consulting": ("Clearlane Advisors", "Elena Voss", "engagement manager", "Calgary"),
    "media": ("Foothills Desk", "Jonah Ellis", "assignment editor", "Calgary"),
    "procurement": ("Harbor Goods", "Diane Cho", "buyer", "Airdrie"),
    "agriculture": ("Two Hills Farm", "Ruth McKay", "operator", "Olds"),
    "public-sector": ("Town of Airdrie", "Pat Nguyen", "clerk", "Airdrie"),
    "energy": ("Prairie Line Energy", "Devon Hale", "operations superintendent", "Grande Prairie"),
    "transport": ("Kite Freight", "Luis Ortega", "dispatch lead", "Calgary"),
    "library": ("Practice Skills", "Yasir Jilani", "author", "Airdrie"),
    "creator": ("Weeknight Table", "Maya Brooks", "creator", "Calgary"),
    "ai": ("Fieldnote", "Jonah Park", "product manager", "Edmonton"),
    "blog": ("Weeknight Table", "Maya Brooks", "editor", "Calgary"),
    "oil-gas": ("Prairie Line Energy", "Devon Hale", "production superintendent", "Grande Prairie"),
    "automotive": ("Bright Axle", "Carla Singh", "service manager", "Airdrie"),
    "airline": ("Kite Air", "Luis Ortega", "station manager", "Calgary"),
    "small-business": ("Harbor Goods", "Diane Cho", "owner", "Airdrie"),
    "saas": ("Fieldnote", "Jonah Park", "product manager", "Edmonton"),
    "seo": ("Harbor Goods", "Lena Ortiz", "owner", "Airdrie"),
}

ITEMS = {
    "finance": ["Operating cash", "Harbor & Co receipt", "Payroll 15 September"],
    "accounting": ["Operating cash", "Undeposited funds", "Sales tax payable"],
    "sales": ["Harbor Goods", "Cedar Clinic", "Redline Parts"],
    "data": ["orders_daily", "customers", "active_accounts"],
    "supply-chain": ["SKU 1044 cabin filter", "Redline Parts", "Calgary-Edmonton lane"],
    "oil-gas": ["Pad 14-22 gas", "Plant inlet", "Flare meter"],
    "automotive": ["RO 4418", "Recall notice 26-118", "Parts order 5521"],
    "airline": ["KA412 YYZ-YYC", "KA188 YVR-YYC", "Bag claim belt 3"],
    "energy": ["Feeder 12", "Site meter 4", "September bill"],
    "saas": ["Trial cohort 1 Sep", "Activated workspaces", "Canceled logos"],
    "seo": ["/services/furnace", "/services/oil-change", "Google Business profile"],
    "blog": ["Weeknight dinners draft", "First-hire draft", "March post"],
    "media": ["Plant turnaround", "Fare change", "Company statement"],
    "creator": ["Tuesday dinner Reel", "Episode 12", "Fieldnote gift post"],
    "ai": ["Support reply draft", "Invoice extract", "Internal search"],
    "research": ["Interview set A", "Search log 12 Sep", "Table 2"],
    "small-business": ["Saturday till", "Supplier invoice 188", "Saturday staff rota"],
    "marketing": ["Fall service page", "Email to lapsed buyers", "Local search ad"],
    "product": ["Activation checklist", "Trial day-3 email", "Usage limit warning"],
    "engineering": ["Checkout service", "Invoice job", "Status page"],
    "customer": ["Ticket 4412", "Ticket 4418", "Ticket 4420"],
    "healthcare": ["Tuesday clinic", "Thursday clinic", "Referral desk"],
    "manufacturing": ["Line 2", "Lot 26-0914", "Gauge 7"],
    "legal": ["Harbor renewal", "Contractor NDA", "Vendor terms"],
    "people": ["Jordan Hale", "Sam Okonkwo", "Open coordinator role"],
    "retail": ["SKU 1044 cabin filter", "End-cap display 3", "Returns desk log"],
    "operations": ["Tuesday shift", "SOP 118 receiving", "Dock exception log"],
    "security": ["Access review Q3", "Endpoint patch ring 2", "Phishing report 4412"],
    "risk": ["Control 7.2 access review", "Vendor Redline Parts", "Issue log item 18"],
    "delivery": ["Milestone 3 handover", "RAID item 12", "Change request 118"],
    "design": ["Checkout screen v4", "Empty-state copy", "Colour contrast audit"],
    "education": ["Module 2 lesson plan", "Rubric draft", "Thursday workshop"],
    "entrepreneurship": ["First four paying accounts", "Runway to March", "Landing page test"],
    "banking": ["Payment run 14 Sep", "Account opening file 221", "Liquidity ladder"],
    "insurance": ["Claim file 8841", "Coverage checklist", "Adjuster note 3 Sep"],
    "construction": ["Birch site, Cochrane", "Takeoff rev C", "Two-week look-ahead"],
    "agriculture": ["North quarter, 140 acres", "Input invoice 442", "Harvest window"],
    "consulting": ["Scope item 4", "Interview set A", "Steering deck v2"],
    "procurement": ["Quote set, 3 vendors", "Redline Parts terms", "Award memo draft"],
    "public-sector": ["Council agenda item 6", "Posted comment period", "Records request 92"],
    "nonprofit": ["Literacy program", "Grant report draft", "Donor list segment B"],
    "real-estate": ["Unit 4B lease", "Rent roll, 12 units", "Offer comparison sheet"],
    "hospitality": ["Friday dinner service", "Room block, 18 keys", "Guest complaint 214"],
    "transport": ["Calgary-Edmonton lane", "Load tally 118", "Hours-of-service log"],
    "sustainability": ["Scope 2 electricity", "Emissions factor sheet", "FY2026 boundary"],
    "productivity": ["Friday review block", "Inbox triage batch", "Q4 objective 2"],
    "library": ["plugins/finance/cash-flow-forecast", "MANIFEST.sha256", "SKILL.md frontmatter"],
}


def _seed(name):
    return int.from_bytes(name.encode()[:8].ljust(8, b"0"), "little") % (2**32)


def _clean(text):
    return " ".join(str(text).replace("|", "/").split())


def _decision(example_out):
    text = _clean(example_out).rstrip(".")
    text = re.sub(r"^(A|An)\s+(.{0,90}?)\s+that\s+", "", text, count=1, flags=re.I)
    if text[:1].islower():
        text = text[0].upper() + text[1:]
    text = re.sub(r"^Refuses to ", "Do not ", text)
    text = re.sub(r"^Flags ", "Flag ", text)
    if not text.endswith("."):
        text += "."
    return text


def _context(domain_id):
    org, person, role, place = CONTEXTS.get(
        domain_id, ("Northline Studio", "Mara Chen", "operator", "Calgary")
    )
    return {
        "org": org,
        "person": person,
        "role": role,
        "place": place,
        "asof": "14 September 2026",
        "due": "30 September 2026",
        "currency": "CAD",
    }


def _world(name):
    rng = random.Random(_seed(name))
    return {
        "opening": rng.randrange(12, 28) * 10000,
        "payroll": rng.randrange(8, 16) * 5000,
        "receipt": rng.randrange(6, 14) * 10000,
        "buffer": rng.randrange(4, 9) * 5000,
        "rent": rng.randrange(8, 18) * 1000,
        "plan": rng.randrange(120, 190, 10),
        "actual": rng.randrange(70, 110, 5),
        "price": rng.choice([49, 79, 120, 180]),
        "cost": rng.choice([18, 27, 36, 44]),
        "lead": rng.choice([7, 14, 21, 28]),
        "otif": rng.choice([86, 91, 94]),
        "units": rng.randrange(40, 90, 5),
        "miss": rng.randrange(8, 24),
        "score": rng.choice([62, 71, 78]),
        "visitors": rng.randrange(12, 40) * 100,
        "conv": rng.choice(["1.8%", "2.4%", "3.1%"]),
        "churn": rng.choice(["2.4%", "3.8%", "5.1%"]),
        "party": rng.choice(["Harbor & Co", "Redline Parts", "Cedar Clinic", "Kite Freight"]),
        "second": rng.choice(["Lumen Ledger", "Fieldnote", "Bright Axle", "Lantern Inn"]),
        "qty": rng.randrange(20, 80, 5),
    }


def _listed(label):
    if ":" not in label:
        return []
    tail = label.split(":", 1)[1]
    parts = [part.strip(" .") for part in tail.replace(" or ", ", ").split(",")]
    parts = [part for part in parts if part and len(part) < 40]
    if 2 <= len(parts) <= 5 and all(len(part.split()) <= 4 for part in parts):
        return parts
    return []


# Head nouns that mean the label wants a thing, not a party name.
_NOT_A_NAME = (
    "checklist", "list", "criteria", "template", "framework", "scorecard",
    "process", "plan", "policy", "journey", "segment", "feedback", "need",
    "count", "history", "record", "profile", "contract", "terms", "brief",
    "instruction", "decision", "request", "complaint", "objection", "question",
)


def _fill(label, ctx, world, example, domain_id):
    low = label.lower()
    money = ctx["currency"]
    items = ITEMS.get(domain_id, [world["party"], world["second"], "open item"])
    listed = _listed(label)
    if listed:
        states = ["in the file", "not in the file", "open"]
        return "; ".join(f"{part}: {states[index % 3]}" for index, part in enumerate(listed))
    phrases = [
        ("opening cash", f"{money} {world['opening']:,} on {ctx['asof']}, operating account, one entity"),
        ("cash fact", f"{money} {world['opening']:,} counted {ctx['asof']}"),
        ("cash on hand", f"{money} {world['opening']:,} counted {ctx['asof']}"),
        ("payroll", f"{money} {world['payroll']:,} on the 1st and the 15th"),
        ("compensation", f"base {money} {world['payroll']:,}. Bonus line blank"),
        ("receivable", f"{world['party']} owes {money} {world['receipt']:,}, usually 20 days late"),
        ("collection", f"{world['party']} usually pays 20 days late. {money} {world['receipt']:,} still open"),
        ("already seen", "lumenledger.com was open on 12 Sep 2026. No register search in the file"),
        ("proposed name", "Lumen Ledger, word mark, no logo"),
        ("goods or services", "bookkeeping software for independent shops"),
        ("markets", "Alberta and online, English. No other country listed"),
        ("stylization", "word mark only"),
        ("proof", f"one customer email, {ctx['asof']}, no attachment beyond that"),
        ("evidence", f"one PDF, 2 pages, dated {ctx['asof']}"),
        ("document", f"one PDF, 2 pages, dated {ctx['asof']}"),
        ("citation", "no citation attached"),
        ("source", f"note from {ctx['person']}, {ctx['asof']}. No outside report"),
        ("deadline", ctx["due"]),
        ("period", f"month ending {ctx['asof']}"),
        ("horizon", "13 weeks"),
        ("price", f"{money} {world['price']}"),
        ("cost", f"{money} {world['cost']} direct. Overhead not in this line"),
        ("fee", f"{money} {world['price']}, from their sheet, not a guess"),
        ("budget", f"{money} {world['opening']:,} available. Not a signed plan"),
        ("metric", f"plan {world['plan']}, actual {world['actual']}"),
        ("target", f"{world['plan']}"),
        ("forecast", f"plan {world['plan']}, no second scenario attached"),
        ("owner", f"{ctx['person']}, {ctx['role']}"),
        ("reviewer", f"{ctx['person']}. No second reviewer named"),
        ("approver", f"{ctx['person']}. They have not signed"),
        ("audience", f"people who already buy from {ctx['org']}"),
        # Specific first: these read as a job-to-be-done, not a counterparty name.
        ("customer job", "the shopper solving one task in one trip. Not segmented further in the file"),
        ("job the customer", "the shopper solving one task in one trip. Not segmented further in the file"),
        ("job to be done", "the shopper solving one task in one trip. Not segmented further in the file"),
        ("customer need", "stated once in the ask. No research file attached"),
        ("customer feedback", f"three comments, {ctx['asof']}. No survey export"),
        ("customer segment", "one segment named. No sizing attached"),
        ("customer", world["party"]),
        ("buyer", world["party"]),
        ("client", world["party"]),
        ("decision", example.rstrip(".")),
        ("constraint", "no extra headcount, and no result that is not in this file"),
        ("out of scope", "anything not named in the ask"),
        ("password", "not collected"),
        ("credential", "not collected"),
        ("risk", f"{items[0]} is open. No score in the file"),
        ("gap", f"{items[0]} is missing a source"),
        ("team", "two people on shift, one off"),
        ("staff", "two people on shift"),
        ("capacity", "two people, no overtime figure"),
        ("hours", "two people, 8 hours each"),
        ("offer", f"{money} {world['price']}, dates not set, cap not set"),
        ("claim", "the draft sentence is broader than the note"),
        ("promise", "none written down beyond the ask"),
        ("question", example.rstrip(".")),
        ("list", f"{items[0]}; {items[1]}; {items[2]}"),
        ("option", f"keep {items[0]}, or stop. No third option written"),
        ("supplier", f"{world['party']}, lead time {world['lead']} days"),
        ("inventory", f"{world['qty']} on hand"),
        ("lead time", f"{world['lead']} days"),
        ("policy", "their one-page rule dated 2 Mar 2026. No exception log"),
        ("contract", "unsigned draft, 8 pages, no signature date"),
        ("license", "MIT on two files. One file has no header"),
        ("privacy", "email and billing address. They said no health data"),
        ("change", f"requested {ctx['asof']}. Not yet approved"),
        ("process", f"email to {ctx['person']}. No written steps after 1 Sep 2026"),
        ("scope", "this decision only"),
        ("time", f"five working days, due {ctx['due']}"),
        ("date", ctx["due"]),
        ("when", ctx["due"]),
        ("who", f"{ctx['person']}, {ctx['role']}"),
        ("why", example.rstrip(".")),
        ("what they", example.rstrip(".")),
        ("measurement", f"not defined beyond plan {world['plan']} and actual {world['actual']}"),
        ("prototype", f"8 screens, file dated {ctx['asof']}"),
        ("news", example.rstrip(".")),
        ("method", "the method in the ask. No second design attached"),
    ]
    bare_names = {world["party"], world["second"]}
    for phrase, value in phrases:
        if phrase not in low:
            continue
        # A bare counterparty name only answers a label asking for one ("The
        # buyer"). When the label's head noun is a document, list or attribute
        # ("The buyer's checklist"), a name is the wrong shape — fall through.
        if value in bare_names and (
            len(label.split()) > 3 or any(noun in low for noun in _NOT_A_NAME)
        ):
            continue
        return value
    return _fallback(label, ctx, world, example, items)


# Head-noun families for input labels the phrase table does not cover.
# Each returns a concrete, checkable value instead of a dead-end sentence,
# so the row survives _thin() and reaches the example.
_FAMILIES = (
    (
        ("ask", "point", "goal", "objective", "outcome", "purpose", "decision",
         "question", "hypothesis", "idea", "intent", "what they want", "problem"),
        lambda lab, ctx, w, ex, it: f"{ex.rstrip('.')}. Stated once, in the ask. Not written down anywhere else",
    ),
    (
        ("reader", "audience", "participant", "actor", "stakeholder", "attendee",
         "recipient", "user of", "who is", "roles"),
        lambda lab, ctx, w, ex, it: f"{ctx['person']} plus two others named in the thread. No distribution list attached",
    ),
    (
        ("draft", "note", "document", "export", "file", "record", "transcript",
         "log", "report", "deck", "sheet", "attachment"),
        lambda lab, ctx, w, ex, it: f"one file, dated {ctx['asof']}. No earlier version attached for comparison",
    ),
    (
        ("exception", "exclusion", "dependency", "unknown", "open issue", "barrier",
         "blocker", "objection", "edge case", "limitation", "caveat"),
        lambda lab, ctx, w, ex, it: f"{it[0]} is open. {it[1]} was raised verbally and never logged",
    ),
    (
        ("volume", "count", "rate", "performance", "throughput", "load", "traffic",
         "usage", "demand", "quantity"),
        lambda lab, ctx, w, ex, it: f"{w['qty']} in the last period. No prior period attached, so no trend",
    ),
    (
        ("system", "environment", "service", "flow", "journey", "platform", "tool",
         "stack", "pipeline", "integration", "architecture"),
        lambda lab, ctx, w, ex, it: f"the one named in the ask. Version and owner not recorded",
    ),
    (
        ("tone", "style", "voice", "format", "length", "channel", "medium"),
        lambda lab, ctx, w, ex, it: "plain, for people who already know the context. No house guide attached",
    ),
    (
        ("control", "policy", "rule", "standard", "requirement", "guideline",
         "procedure", "convention", "threshold"),
        lambda lab, ctx, w, ex, it: f"their one-page rule dated 2 Mar 2026. No exception log since",
    ),
    (
        ("checklist", "criteria", "template", "framework", "scorecard"),
        lambda lab, ctx, w, ex, it: f"their existing list, {len(it) + 3} lines. Two lines have no owner",
    ),
    (
        ("lose", "win", "lost", "won", "competitor", "rival", "alternative"),
        lambda lab, ctx, w, ex, it: f"two deals cited from memory. Neither has a written loss reason",
    ),
    (
        ("failed", "failure", "incident", "error", "defect", "bug", "outage",
         "complaint", "escalation"),
        lambda lab, ctx, w, ex, it: f"{it[0]}, first seen {ctx['asof']}. No root cause recorded yet",
    ),
    (
        ("task", "work", "activity", "step", "action", "deliverable", "milestone"),
        lambda lab, ctx, w, ex, it: f"{it[0]}; {it[1]}. Both unassigned as of {ctx['asof']}",
    ),
    (
        ("sensitive", "confidential", "personal data", "pii", "health", "restricted"),
        lambda lab, ctx, w, ex, it: "email and billing address only. They stated no health or payment data",
    ),
)


# Last-resort shapes. Chosen by a hash of the label so that several unmatched
# inputs in the same skill get different, non-repeating values.
_LAST_RESORT = (
    "{item}. Stated in the ask, not documented anywhere else",
    "{item}, recorded {asof}. No supporting file attached",
    "{item} and one other, both unconfirmed as of {asof}",
    "{item}. Partly documented: the what is written down, the who is not",
    "{item}, last reviewed {asof}. No owner named since",
)


def _fallback(label, ctx, world, example, items):
    low = label.lower()
    for keys, build in _FAMILIES:
        if any(key in low for key in keys):
            return build(label, ctx, world, example, items)
    # Still concrete, and varied per label so rows in one example do not repeat.
    shape = _LAST_RESORT[_seed(label) % len(_LAST_RESORT)]
    item = items[_seed(label) % len(items)]
    return shape.format(item=item, asof=ctx["asof"])


def _rows(record, ctx, world, domain_id):
    rows = []
    for label in record["inputs"]:
        rows.append((label, _fill(label, ctx, world, record["example"], domain_id)))
    return rows


CASES = {
    "people": ["cadence: weekly, 30 minutes, Tuesday 10:00", "status board: already updated daily", "last meeting: 6 status questions, employee did not set the agenda", "growth topic: none written down"],
    "legal": ["name: Lumen Ledger, word mark, no logo", "goods: bookkeeping software for independent shops", "already checked: lumenledger.com open on 12 Sep 2026", "register search: not in the file"],
    "finance": ["cash: the counted figure in the ask, one entity", "maybe receipt: not in the bank", "buffer: the one they named", "new spend: not in the base case"],
    "accounting": ["period: August 2026", "no preparer: undeposited funds, sales tax payable", "cash recs: one inbox, not the shared folder", "reviewer: not signed"],
    "sales": ["account: Harbor Goods", "last meeting: 9 Sep 2026, no dated next step", "proof: one email", "discount asked: 15 percent, not approved"],
    "marketing": ["page: the live page", "claim: broader than the note", "proof: none attached", "publish date wanted: 19 Sep 2026"],
    "product": ["interviews: 12, March to June 2026", "decision: ship, hold, or cut", "metric: not defined", "kill line: not written"],
    "engineering": ["branch: main, change not merged", "tests listed: none", "rollback: not written", "owner: the person who opened the change"],
    "data": ["extract date: 14 Sep 2026", "owner: the sender", "second source: not attached", "nulls: not counted yet"],
    "security": ["policy: the one they have", "report in the folder: none", "control named: only if it is in the policy", "owner: engineering lead"],
    "operations": ["shift: two people", "SOP: one page, 2 Mar 2026", "exception: not logged", "queue: the items in the ask"],
    "delivery": ["milestone: the customer date", "status: slipped", "completed tasks: do not replace the slip", "decision: needed"],
    "customer": ["ticket: 4412, 14 Sep 2026", "customer words: in the ticket", "exception: not approved", "card or password: not collected"],
    "risk": ["event: the one in the ask, not a one-word label", "owner: blank", "control: not named", "score: not invented"],
    "strategy": ["decision: the one in the ask", "options: two, named", "evidence: the file only", "unowned idea: parked"],
    "design": ["screens: 8, dated 10 Sep 2026", "job: the task in the ask", "accessibility pass: not done", "assets: theirs only"],
    "healthcare": ["clinic: Cedar, Tuesday list", "diagnosis: not in this note", "roster: the one attached", "advice to a patient: not written"],
    "education": ["course: the one named", "section: the one they teach", "student submission: not written for them", "due: 30 Sep 2026"],
    "research": ["site: one", "sample: the count they gave", "missing file: named in the ask", "unopened citation: not used"],
    "supply-chain": ["sku: 1044", "supplier: Redline Parts", "lead time: their number", "alternate: none"],
    "manufacturing": ["line: line 2", "lot: 26-0914", "hold: open", "count: the tally, not the order"],
    "real-estate": ["address: the one in the ask", "rent roll: their sheet", "comp: not invented", "legal review: not done here"],
    "construction": ["site: Birch, Cochrane", "safety item: stays open", "quantity: their takeoff", "date: the look-ahead"],
    "hospitality": ["stay: the dates in the ask", "offer: policy amount only", "complaint: their words", "manager: on duty"],
    "retail": ["store: Harbor Goods, Airdrie", "price: shelf price", "stock: the count", "review: not invented"],
    "nonprofit": ["program: the one they run", "measured outcome: no", "ask: one", "story: not invented"],
    "banking": ["run: 14 Sep 2026", "changed payee: email this morning, not verified", "password: not collected", "hold: that line"],
    "insurance": ["folder: the claim file they have", "coverage opinion: not given", "missing doc: named", "handler: licensed owner"],
    "consulting": ["decision: the one in the ask", "evidence: notes only", "out of scope: named", "finding: not promised"],
    "media": ["document: the statement in the folder", "unnamed quote: not used", "deadline: the board time", "unknown: stays unknown"],
    "procurement": ["quotes: only those attached", "missing term: blank", "authority: their limit", "award: not made here"],
    "agriculture": ["week: 14 Sep 2026", "cash: their figure", "treatment: not prescribed here", "sheet: theirs"],
    "public-sector": ["record: the agenda or request", "vote: not implied if it has not happened", "names: public record only", "deadline: the posted one"],
    "sustainability": ["period: the year they named", "factor: only from their sheet", "certification: not claimed", "estimate: labeled"],
    "energy": ["meter: the one they named", "figure: their sheet", "promised date from elsewhere: not in the file", "owner: superintendent"],
    "transport": ["lane: the one in the ask", "tally: their count", "limit: the one they stated", "concealment: not advised"],
    "productivity": ["week: 14 Sep 2026", "calendar: the meetings they listed", "dissent: kept if it was said", "monitoring: not recommended"],
    "entrepreneurship": ["paying names: only those given", "cash: bank figure, not a maybe", "ask: the one they wrote", "copied line: cut"],
    "library": ["folder: one SKILL.md", "description: says when to use it", "network: none", "author: Yasir Jilani"],
    "creator": ["owned file: dated", "someone else's script: not in the folder", "paid: only if stated", "export: only if attached"],
}


def _thin(value):
    return "No second file for this line" in value or "noted it on" in value


def _data_block(record, ctx, rows, domain_id):
    lines = [
        f"From: {ctx['person']}, {ctx['role']}",
        f"Organization: {ctx['org']}, {ctx['place']}",
        f"Date: {ctx['asof']}",
        f"Needed by: {ctx['due']}",
        "",
        record["example"],
        "",
    ]
    kept = [(label, value) for label, value in rows if not _thin(value)]
    if len(kept) >= 3:
        for label, value in kept:
            lines.append(f"{label}: {value}")
    else:
        for line in CASES.get(domain_id, CASES["operations"]):
            lines.append(line)
    return "```text\n" + "\n".join(lines) + "\n```"


def _classify(record, domain_id):
    blob = f"{record['name']} {record['artifact']}".lower()
    if any(word in blob for word in ("cash-flow", "runway", "13-week", "burn")):
        return "cash"
    if "variance" in blob or "budget" in blob:
        return "variance"
    if "checklist" in blob or blob.endswith("calendar"):
        return "checklist"
    if domain_id in {"creator", "blog"} and any(word in blob for word in ("outline", "script", "caption", "hook")):
        return "outline"
    if any(word in blob for word in ("email", "announcement", "disclosure", "reply", "pitch")):
        return "message"
    if any(word in blob for word in ("scorecard", "metric", "analytics")):
        return "table"
    return "memo"


def _outcome_cash(record, ctx, world):
    opening = world["opening"]
    payroll = world["payroll"]
    rent = world["rent"]
    receipt = world["receipt"]
    buffer = world["buffer"]
    week1 = opening - payroll
    week2 = week1 - 8400
    week3 = week2 - payroll - rent
    week4 = week3 + receipt
    breach = "week 3" if week3 < buffer else "none in the first four weeks"
    return f"""**13-week cash view, first four weeks shown**
{ctx['org']} · {ctx['asof']} · {ctx['currency']}

Decision: do not add a new recurring cost until {world['party']}'s {receipt:,} is collected or moved out of the plan. The hire is a cash condition, not a yes.

| Week | Opening | In | Out | Closing | Against buffer {buffer:,} |
| --- | --- | --- | --- | --- | --- |
| 1 | {opening:,} | 0 | {payroll:,} payroll | {week1:,} | {"below" if week1 < buffer else "above"} |
| 2 | {week1:,} | 0 | 8,400 approved bills | {week2:,} | {"below" if week2 < buffer else "above"} |
| 3 | {week2:,} | 0 | {payroll + rent:,} payroll and rent | {week3:,} | {"below" if week3 < buffer else "above"} |
| 4 | {week3:,} | {receipt:,} if the lag holds | 0 | {week4:,} | {"below" if week4 < buffer else "above"} |

First tight week: {breach}.
Assumption: the {receipt:,} is collected in week 4 because that is the 20-day lag in the file. It is not booked revenue.
Not in this draft: a second scenario where the receipt slips past week 6. Build that before any offer letter.
Next action: {ctx['person']} confirms the collection date by {ctx['due']}."""


def _outcome_variance(record, ctx, world):
    gap = world["plan"] - world["actual"]
    return f"""**Variance note**
{ctx['org']} · period ending {ctx['asof']}

Decision: treat the gap as a miss against the file, not as a formatting issue. Do not call it timing unless the invoice date is in the file.

| Line | Plan | Actual | Gap |
| --- | --- | --- | --- |
| Main driver | {world['plan']} | {world['actual']} | {gap} |
| One-off named in the file | — | not supplied | leave open |
| Full-period outlook | unchanged until the one-off is dated | | |

{_decision(record['example_out'])}
Next action: {ctx['person']} marks the gap as timing or as a real miss by {ctx['due']}."""


def _refusals(record, limit=3):
    return "\n".join(f"- {_clean(item).rstrip('.')}." for item in record["anti"][:limit])


def _outcome_checklist(record, ctx, rows):
    checks = []
    for index, (label, value) in enumerate(rows[:6], start=1):
        done = index <= 3
        mark = "x" if done else " "
        state = "Evidenced in the file" if done else "Open — nothing in the file closes this"
        checks.append(f"- [{mark}] **{label}** — {value}  \n      {state}")
    body = "\n".join(checks)
    gates = "\n".join(
        f"{i}. {_split_step(step)[0]}" for i, step in enumerate(record["steps"][:5], 1)
    )
    return f"""**{record['artifact'].capitalize()}**
{ctx['org']} · {ctx['asof']} · Due {ctx['due']}

**Decision**
{_decision(record['example_out'])}

**Checklist**

{body}

**The gates this list enforces, in order**

{gates}

**Deliberately not done**
{_refusals(record)}

**Stop rule**
Do not mark this pack complete while a box above is open. An open box is a finding, not a formality — it is the thing this checklist exists to catch.

Next: {ctx['person']} closes the open items before {ctx['due']}."""


def _outcome_outline(record, ctx, world):
    beats = []
    for i, step in enumerate(record["steps"][:5], 1):
        label, detail = _split_step(step)
        beats.append(f"**Beat {i} — {label}**" + (f"  \n{detail}" if detail else ""))
    body = "\n\n".join(beats)
    return f"""**{record['artifact'].capitalize()}**
For {ctx['person']} at {ctx['org']} · {ctx['asof']}

| | |
| --- | --- |
| Working title | Taken from the job in the file, not a borrowed headline |
| Audience | The people already named in the ask |
| Length | One sitting — under 10 minutes, or 800 words |
| Source of every claim | The example data above, and nothing else |

**Decision**
{_decision(record['example_out'])}

**Structure**

{body}

**Deliberately not done**
{_refusals(record)}

**Blanks that must be filled before this publishes**
- Any metric, quote, or sponsor not present in the example data stayed blank. A blank is honest; an invented figure is not.
- Where the file supports a claim only partly, the outline says so rather than rounding it up.

Next: {ctx['person']} replaces each blank with a real source before publishing. Due {ctx['due']}."""


def _outcome_message(record, ctx, world):
    checks = []
    for i, step in enumerate(record["steps"][:4], 1):
        label, detail = _split_step(step)
        checks.append(f"{i}. **{label}** — {detail}" if detail else f"{i}. **{label}**")
    body = "\n".join(checks)
    return f"""**{record['artifact'].capitalize()} — draft ready to send**

> To: the recipient named in the file
> From: {ctx['person']}, {ctx['role']}, {ctx['org']}
> Date: {ctx['asof']}

---

Hello,

{_decision(record['example_out'])}

Everything above comes from the file dated {ctx['asof']}. Where a figure, a date, or a commitment was not in that file, this note leaves it out rather than filling the gap.

One point is still open, and I would rather flag it than paper over it. I will confirm it before {ctx['due']} and follow up either way.

{ctx['person']}
{ctx['role']}, {ctx['org']}

---

**How this draft was checked**

{body}

**Deliberately not done**
{_refusals(record)}

Next: {ctx['person']} sends after confirming the open point. Due {ctx['due']}. This is a draft, not a sent message."""


def _outcome_table(record, ctx, world):
    method = "\n".join(
        f"{i}. {_split_step(step)[0]}" for i, step in enumerate(record["steps"][:5], 1)
    )
    return f"""**{record['artifact'].capitalize()}**
{ctx['org']} · {ctx['asof']} · Due {ctx['due']}

**Decision**
{_decision(record['example_out'])}

| Item | Figure in the file | Call | Why |
| --- | --- | --- | --- |
| {world['party']} | plan {world['plan']}, actual {world['actual']} | Use | Both sides of the comparison are in the file |
| {world['second']} | score {world['score']} | Report, do not benchmark | One score is a reading, not a baseline |
| Missing export | Not in the file | Stop | The cell stays blank until the export arrives |

**How these calls were made**

{method}

**Deliberately not done**
{_refusals(record)}

**Open items**
- The missing export is the binding constraint. No figure was estimated to fill its place.
- Any row marked *Report, do not benchmark* needs a second period before it can carry a trend.

Next: {ctx['person']} attaches the missing export, or the cell stays blank. Due {ctx['due']}."""


def _split_step(step):
    """Split 'Label: detail' into (label, detail). Falls back to (step, '')."""
    text = _clean(step)
    match = re.match(r"^([^:]{3,60}):\s+(.*)$", text)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return text.rstrip("."), ""


def _outcome_memo(record, ctx, rows, domain_id):
    kept = [(label, value) for label, value in rows if not _thin(value)]
    if len(kept) < 3:
        kept = [
            tuple(line.split(": ", 1)) if ": " in line else (line, "as stated")
            for line in CASES.get(domain_id, CASES["operations"])
        ]

    # Findings table: each input row becomes an observation the deliverable acts on.
    findings = "\n".join(
        f"| {label} | {value} | {'Carried into the draft' if i % 3 else 'Needs confirmation'} |"
        for i, (label, value) in enumerate(kept)
    )

    # Walk the skill's own workflow so the reader sees the method, not just a verdict.
    applied = []
    for i, step in enumerate(record["steps"][:5], 1):
        label, detail = _split_step(step)
        applied.append(f"**{i}. {label}**" + (f"  \n{detail}" if detail else ""))
    walked = "\n\n".join(applied)

    # Anti-patterns are the distinctive part: say what this draft refused to do.
    refused = "\n".join(f"- {_clean(item).rstrip('.')}." for item in record["anti"][:3])

    return f"""**{record['artifact'].capitalize()}**
To: {ctx['person']}, {ctx['role']}, {ctx['org']}
Date: {ctx['asof']} · Needed by: {ctx['due']}

**Decision**
{_decision(record['example_out'])}

**What the file supports**

| Input | Value | Status |
| --- | --- | --- |
{findings}

**How this draft was built**

{walked}

**Deliberately not done**
{refused}

**Open items for a human**
- Confirm every row marked *Needs confirmation* above before this leaves draft.
- Anything absent from the file stayed absent. No figure, date, or name was supplied from outside it.

Next: {ctx['person']} by {ctx['due']}. This is a draft, not a sign-off."""


def _outcome(record, ctx, rows, world, domain_id):
    kind = _classify(record, domain_id)
    if kind == "cash":
        return _outcome_cash(record, ctx, world)
    if kind == "variance":
        return _outcome_variance(record, ctx, world)
    if kind == "checklist":
        return _outcome_checklist(record, ctx, rows)
    if kind == "outline":
        return _outcome_outline(record, ctx, world)
    if kind == "message":
        return _outcome_message(record, ctx, world)
    if kind == "table":
        return _outcome_table(record, ctx, world)
    return _outcome_memo(record, ctx, rows, domain_id)


def build_worked(record, domain):
    domain_id = domain["id"]
    ctx = _context(domain_id)
    world = _world(record["name"])
    rows = _rows(record, ctx, world, domain_id)
    scenario = (
        f"{ctx['person']}, {ctx['role']} at {ctx['org']} in {ctx['place']}, "
        f"needs {'an' if record['artifact'][:1].lower() in 'aeiou' else 'a'} {record['artifact']} by {ctx['due']}. {record['example']}"
    )
    return {
        "purpose": record["job"],
        "scenario": scenario,
        "data": _data_block(record, ctx, rows, domain_id),
        "outcome": _outcome(record, ctx, rows, world, domain_id),
    }


def attach_worked(record, domain):
    hand = BANK.get(record["name"])
    record["worked"] = hand if hand else build_worked(record, domain)
    return record
