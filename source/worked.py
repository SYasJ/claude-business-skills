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
    "airline": ["KA412", "KA188", "Station YYC"],
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
    for phrase, value in phrases:
        if phrase in low:
            return value
    return f"{items[0]}. {ctx['person']} noted it on {ctx['asof']}. No second file for this line."


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


def _outcome_checklist(record, ctx, rows):
    checks = []
    for index, (label, value) in enumerate(rows[:5], start=1):
        state = "open" if index > 3 else "in the file"
        checks.append(f"- [{ 'x' if state == 'in the file' else ' ' }] {label} — {state}. {value}")
    body = "\n".join(checks)
    return f"""**{record['artifact'].capitalize()}**
{ctx['org']} · {ctx['asof']}

{_decision(record['example_out'])}

{body}

Next action: {ctx['person']} closes the open items before {ctx['due']}. Do not mark the pack done while a box is open."""


def _outcome_outline(record, ctx, world):
    return f"""**{record['artifact'].capitalize()}**
For {ctx['person']} at {ctx['org']} · {ctx['asof']}

Working title: the job in the file, not a copied headline
Audience: the people already named in the ask
Length: one sitting, under 10 minutes or 800 words

1. Open with the situation in the file. Do not open with a claim the file does not support.
2. One point {ctx['person']} can show from their own notes.
3. A second point the audience can use this week. No borrowed script.
4. Close with one action and the source named in the file.

Decision: {_decision(record['example_out'])}
Leave out: any metric, quote, or sponsor that is not in the example data.
Next action: {ctx['person']} replaces any blank with a real source before publishing. Due {ctx['due']}."""


def _outcome_message(record, ctx, world):
    return f"""**Draft the reader can send**

{ctx['person']} — {ctx['org']}
{ctx['asof']}

Hello,

{_decision(record['example_out'])} This note uses only the facts in the file from {ctx['asof']}. It does not add a result, a quote, or a discount that was not supplied.

The open point is still open. I will confirm it before {ctx['due']}.

{ctx['person']}
{ctx['role']}, {ctx['org']}"""


def _outcome_table(record, ctx, world):
    return f"""**{record['artifact'].capitalize()}**
{ctx['org']} · {ctx['asof']}

Decision: {_decision(record['example_out'])}

| Item | Figure in the file | Call |
| --- | --- | --- |
| {world['party']} | plan {world['plan']}, actual {world['actual']} | use |
| {world['second']} | score {world['score']} | do not treat as a benchmark |
| Missing export | not in the file | stop, do not invent it |

Next action: {ctx['person']} attaches the missing export or the cell stays blank. Due {ctx['due']}."""


def _outcome_memo(record, ctx, rows, domain_id):
    kept = [(label, value) for label, value in rows if not _thin(value)]
    if len(kept) >= 3:
        used = "\n".join(f"- {label}: {value}" for label, value in kept)
    else:
        used = "\n".join(f"- {line}" for line in CASES.get(domain_id, CASES["operations"]))
    return f"""**{record['artifact'].capitalize()}**
To: {ctx['person']}, {ctx['role']}, {ctx['org']}
Date: {ctx['asof']}

**Decision**
{_decision(record['example_out'])}

**From the file**
{used}

Nothing in this draft was added from outside that file.
Next: {ctx['person']} by {ctx['due']}. This is not a sign-off."""


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
