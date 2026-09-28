"""Render a catalog record into an Agent Skills SKILL.md document."""

from __future__ import annotations

DISCLAIMERS = {
    "strategy": "Strategy work recommends a direction. It does not guarantee market outcomes.",
    "finance": "This is not investment, tax, or financial advice. Do not invent rates of return, tax rates, or valuation multiples. A qualified finance professional must review any decision that moves money.",
    "accounting": "This is not an audit opinion, compilation, or tax advice. Do not invent accounting standards. Use the policy, framework, and chart of accounts the organization actually follows.",
    "legal": "This is not legal advice and does not create an attorney-client relationship. Do not invent statutes, case names, or filing deadlines. Drafts are for qualified counsel in the relevant jurisdiction.",
    "people": "Employment work must follow the organization's policies and local employment law. Do not invent legal requirements. Do not write content that discriminates or retaliates.",
    "sales": "Sell honestly. Do not invent customer proof, discounts, or competitor facts. Do not write deceptive, phishing, or high-pressure scripts.",
    "marketing": "Do not invent testimonials, reviews, metrics, or claims the user cannot support. Do not draft spam, cloaking, fake scarcity, or impersonation.",
    "product": "Product recommendations are hypotheses until evidence says otherwise. Label confidence. Do not ship dark patterns that hide cost or consent.",
    "engineering": "Prefer the repository's existing patterns. Do not disable security controls, invent credentials, or introduce network calls the user did not ask for.",
    "data": "Do not invent numbers. If a source file is missing, say so. Distinguish observation from inference. Do not re-identify private data to make a point.",
    "security": "Defensive use only. Do not write exploits, payloads, bypasses, malware, or intrusion steps. Describe controls, ownership, detection, and safe verification.",
    "operations": "Operating procedures should be usable by the team that will run them. Do not add surveillance of employees beyond what the user explicitly asks to document as policy.",
    "delivery": "Delivery plans are commitments only when owners and dates are real. Do not fabricate status to make a report look healthy.",
    "customer": "Do not blame the customer. Do not invent policy exceptions. Do not ask a customer for passwords or full payment card numbers.",
    "risk": "Risk work prioritizes uncertainty. It is not a certification. Do not claim SOC 2, ISO, HIPAA, or similar compliance unless the user has evidence of it.",
    "healthcare": "This is not medical advice, diagnosis, or a treatment protocol. Do not recommend drugs, doses, or clinical interventions. Limit the work to practice operations, documentation quality, and communication drafts for a licensed clinician to approve.",
    "education": "Learning design supports the instructor. Do not complete graded work for a student or help anyone cheat. Do not invent accreditation requirements.",
    "research": "Do not fabricate citations, quotations, data, or participants. Separate evidence you were given from claims that still need a source.",
    "design": "Design critique improves the work. Do not copy a third party's branded assets. Accessibility is part of done, not a later pass to skip.",
    "supply-chain": "Inventory and supplier recommendations depend on the user's lead times and service targets. Do not invent supplier performance.",
    "manufacturing": "Quality and safety procedures are drafts for the site's quality system. Do not bypass a hold, calibration, or safety step.",
    "real-estate": "This is not brokerage, appraisal, or legal advice. Do not invent comparable sales, rents, or legal rights. A licensed local professional must confirm any transaction.",
    "construction": "Site safety and contract administration follow the contract and the site rules. Do not tell anyone to skip a safety control. Do not invent quantities.",
    "hospitality": "Guest recovery should be sincere and within policy. Do not invent compensation authority the user has not granted.",
    "retail": "Do not invent inventory, prices, or reviews. Do not write deceptive promotions.",
    "nonprofit": "Do not invent impact metrics or donor intent. Fundraising copy must be accurate and free of pressure tactics that misstate the need.",
    "sustainability": "Do not invent emissions factors or certification status. Label estimates. This is not an assurance opinion.",
    "insurance": "This is not coverage advice and not a claim determination. Do not tell anyone they are covered. Organize facts for a licensed professional.",
    "banking": "This is not a credit decision and not an instruction to move money. Do not request online-banking passwords, one-time codes, or card PINs.",
    "entrepreneurship": "Startup advice is a set of choices, not a promise of funding or growth. Do not invent traction, customers, or investor interest.",
    "productivity": "Productivity systems serve the person's actual constraints. Do not recommend surveillance of colleagues or hidden monitoring.",
    "consulting": "Client work stays confidential to the engagement. Do not fabricate findings to please a sponsor. Separate evidence from recommendation.",
    "media": "Do not fabricate quotes, sources, or images. Label opinion. Do not draft impersonation or defamation.",
    "procurement": "Buying decisions follow the organization's authority limits. Do not steer an award to a supplier for a personal benefit, and do not invent bids.",
    "agriculture": "Farm plans are operational, not agronomic prescriptions for hazardous materials. Do not provide instructions for synthesizing pesticides, toxins, or pathogens. A local agronomist or veterinarian should confirm field decisions.",
    "public-sector": "Public work should be accurate, even-handed, and suitable for the record. Do not draft deceptive communications, voter manipulation, or surveillance programs.",
    "energy": "Operational energy advice is not a permit and not a safety case. Do not bypass lockout, isolation, or regulatory limits.",
    "transport": "Transport plans follow hours, load, and safety rules the user states. Do not advise concealment of cargo or evasion of inspections.",
    "library": "Library skills help you choose, write, and trust agent skills. They do not grant extra permissions or weaken safety rules.",
    "creator": "Creator work must be original and honest. Do not copy another person's script, footage, voice, or caption. Do not invent metrics, fake engagement, or undisclosed sponsorships. Do not impersonate a real person. Prompt skills must not weaken safety rules.",
    "ai": "Do not write prompts or workflows that weaken safety rules, hide required disclosure, or invent model scores. This is not a certification and not a reason to send private data to a vendor.",
    "blog": "Do not copy another publication's article. Do not invent sources, quotes, or results. Label an update when a post is refreshed.",
    "oil-gas": "Operational drafts only. Do not bypass isolation, lockout, permits, or reporting duties. Do not write instructions to conceal a release or to operate outside the site's limits.",
    "automotive": "Not a repair procedure for safety-critical systems and not a recall determination. Do not invent defect rates or tell anyone to disable a safety feature.",
    "airline": "Do not advise exceeding a duty limit, skipping a maintenance release, or concealing a safety issue. Passenger messages must match the facts supplied.",
    "small-business": "Not legal, tax, or employment advice. Do not invent license rules, tax rates, or a local bylaw.",
    "saas": "Do not invent churn, revenue, retention, or a security certification. If the export is missing, say so.",
    "seo": "Do not draft cloaking, doorway pages, hidden text, fake reviews, or link schemes. Use only queries and pages the user can show.",
}


def yaml_quote(value):
    text = " ".join(str(value).split())
    escaped = text.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def bullets(items):
    return "\n".join(f"- {item}" for item in items)


def description_for(record, domain_title):
    triggers = ", ".join(record["triggers"][:4])
    text = (
        f"{record['job']} Use when the user mentions {triggers}, "
        f"or asks for a {record['artifact']}. "
        f"{domain_title} skill by Yasir Jilani."
    )
    text = " ".join(text.split())
    if len(text) > 1024:
        text = text[:1020].rsplit(" ", 1)[0]
    return text


def output_outline(record):
    if record["outputs"]:
        return bullets(record["outputs"])
    return bullets(
        [
            f"Purpose of this {record['artifact']}, in two sentences.",
            "Facts the user supplied, listed separately from assumptions.",
            "The work itself, in the structure the workflow names.",
            "Open questions, risks, and the single next action with an owner.",
            "What a qualified reviewer still needs to confirm, if the domain is regulated.",
        ]
    )


def quality_checks(record):
    if record["checks"]:
        return bullets(record["checks"])
    return bullets(
        [
            "Every number, date, name, and citation came from the user or is marked as an assumption.",
            "The artifact can be used without reading this skill again.",
            "Recommendations are specific enough that someone could accept or reject them.",
            "Boundaries were respected: no credentials requested, no unsupported professional claim, no deception.",
        ]
    )


def render_skill(record, domain):
    disclaimer = DISCLAIMERS.get(domain["id"], DISCLAIMERS["library"])
    avoid = list(record["avoid"]) or [
        "The user wants a different domain's specialist skill.",
        "The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.",
        "The request asks you to deceive, evade a control, or hide material facts.",
    ]
    steps = []
    for index, step in enumerate(record["steps"], start=1):
        title, _, body = step.partition(": ")
        if body and len(title) < 80 and title[:1].isupper():
            steps.append(f"### {index}. {title}\n\n{body}")
        else:
            steps.append(f"### {index}. Step {index}\n\n{step}")
    related = record["related"][:4]
    related_lines = bullets(
        [f"`{name}`" for name in related]
    ) if related else "- None in this domain yet. Use the skill finder if the task sits elsewhere."
    description = description_for(record, domain["title"])
    body = f"""---
name: {record['name']}
description: {yaml_quote(description)}
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: {domain['id']}
---

<!-- GENERATED FILE - edits here are overwritten by scripts/generate.py.
     Edit the '{record['name']}' entry in source/, then run:
       python3 scripts/generate.py && python3 scripts/validate.py
     See CONTRIBUTING.md. -->

# {record['title']}

{record['job']}

## When to use this skill

Use this skill when the user:

{bullets(record['triggers'])}

## When not to use this skill

{bullets(avoid)}

## Professional boundary

{disclaimer}

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

{bullets(record['inputs'])}

## Workflow

{chr(10) + chr(10).join(steps)}

## Output

Deliver a **{record['artifact']}**.

{output_outline(record)}

## Quality bar

{quality_checks(record)}

## Example

### Scenario

{record['worked']['scenario']}

### Example data

{record['worked']['data']}

### Example outcome

{record['worked']['outcome']}

## Anti-patterns

{bullets(record['anti'])}

## Related skills

{related_lines}
"""
    return body
