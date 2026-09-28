<p align="center">
  <img src="docs/assets/banner.svg" alt="594 Claude Code Agent Skills for business work across 48 domains" width="880">
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href="https://github.com/SYasJ/claude-practice-skills/stargazers"><img src="https://img.shields.io/github/stars/SYasJ/claude-practice-skills?style=flat" alt="GitHub Stars"></a>
  <a href="https://github.com/SYasJ/claude-practice-skills/blob/main/catalog/SKILLS.md"><img src="https://img.shields.io/badge/skills-594-brightgreen" alt="594 Skills"></a>
  <a href="https://github.com/SYasJ/claude-practice-skills/blob/main/catalog/SKILLS.md"><img src="https://img.shields.io/badge/domains-48-orange" alt="48 Domains"></a>
</p>

<h1 align="center">Claude Code Business Skills</h1>

<p align="center"><strong>594 Agent Skills for real business work — finance, ops, engineering, HR, legal, and 43 more domains.<br>Install one command. Works in Claude Code, Cursor, Gemini CLI, Codex, and any Agent Skills–compatible tool.</strong></p>

---

## What it does

You drop a skill into Claude Code. When you describe a task that matches, Claude loads the skill and follows it — step by step, with guardrails. You get consistent output that shows its work.

**Before:** "Help me with the bank reconciliation" → generic advice.  
**After (with `bank-reconciliation` skill):** Claude reconciles book to bank, flags the unexplained $400 gap, classifies the three old deposits-in-transit as needing a decision, and refuses to plug the difference.

> The skill tells Claude: no plugs, classify everything, flag items older than the threshold, propose entries as drafts only — not post them.

## Quick install

```bash
git clone https://github.com/SYasJ/claude-practice-skills.git
cd claude-practice-skills
python3 scripts/install.py --tool claude --domain finance
```

That copies each skill in the `finance` domain to `~/.claude/skills/`. Claude Code loads a skill when the task matches its description. No server. No API key. No network call during install.

Preview before installing:

```bash
python3 scripts/install.py --tool claude --domain finance --dry-run
```

Install multiple domains:

```bash
python3 scripts/install.py --tool claude --domain finance --domain accounting --domain people
```

## What it looks like in practice

### Finance · `cash-flow-forecast`
```
You: build the 13-week cash forecast from these invoices

Claude: [loads cash-flow-forecast skill]
Week 1: Opening $180,000 | Receipts $62,400 | Disbursements $74,100 | Closing $168,300
Week 2: Opening $168,300 | Receipts $48,200 | Disbursements $81,600 | Closing $134,900
...
Week 7 hits the $40,000 buffer. Review before week 5.
Assumptions: collections lag 21 days; payroll on the 15th and last Friday.
These are projections, not a guarantee.
```

### Engineering · `incident-postmortem`
```
You: the draft postmortem says Alex was careless

Claude: [loads incident-postmortem skill]
Removed: "Alex was careless"
Contributing factor: branch protection was not enabled on main — any
push could deploy without review.
Action: enable branch protection (owner: Aisha, due 28 Sep 2026)
This postmortem does not assign blame to an individual.
```

### Accounting · `bank-reconciliation`
```
You: the rec has an unexplained difference and three old DITs

Claude: [loads bank-reconciliation skill]
Statement balance:  $97,820
Outstanding checks: ($5,070) — checks #2241, #2242
Adjusted bank:      $92,750
Book balance:       $94,350
Adjustments:        ($1,200) — NSF + bank fee
Adjusted book:      $93,150
Unexplained gap:    $400     ← needs investigation before sign-off

DITs older than 30 days (3 items, $11,700): recommend inquiry,
not automatic reversal.
```

## Supported tools

| Tool | Flag | Skills land in |
| --- | --- | --- |
| Claude Code (global) | `--tool claude` | `~/.claude/skills/` |
| Claude Code (project) | `--tool claude-project --project .` | `.claude/skills/` |
| Cursor | `--tool cursor --project .` | `.cursor/skills/` |
| Gemini CLI | `--tool gemini` | `~/.gemini/skills/` |
| Codex CLI | `--tool codex` | `~/.codex/skills/` |
| Windsurf | `--tool windsurf --project .` | `.windsurf/skills/` |
| OpenCode | `--tool opencode --project .` | `.opencode/skills/` |
| Generic agents | `--tool agents` | `~/.agents/skills/` |

## Domains

| Domain | Skills | What it covers |
| --- | ---: | --- |
| Engineering | 27 | Design docs, code review, incidents, releases, ADRs |
| Marketing | 24 | Positioning, campaigns, claims you can support |
| Finance | 23 | Cash, runway, margin, management packs |
| People | 23 | Hiring, reviews, comp bands, onboarding |
| Data | 23 | Contracts, lineage, freshness, governance |
| Strategy | 22 | Choices, board memos, OKRs, operating cadence |
| Sales | 20 | Discovery, qualification, proposals, sequences |
| Product | 20 | PRDs, briefs, experiments, roadmaps |
| Legal | 18 | Contract triage and counsel briefs |
| Accounting | 17 | Close, reconciliations, controls, audit prep |
| Research | 17 | Questions, evidence, consent, claim limits |
| Supply chain | 17 | Demand, inventory, OTIF, dock exceptions |
| Security | 16 | Controls and incident response. No exploits |
| Operations | 16 | SOPs, capacity, service levels |
| Customer | 14 | Journeys, recovery, health scores, escalations |
| Delivery | 14 | Charters, status, RAID, change control |
| Manufacturing | 14 | Quality, CAPA, schedule, traceability |
| Entrepreneurship | 14 | Runway, first customers, idea screens |
| Design | 13 | Critique, UX writing, handoff, accessibility |
| Education | 12 | Lessons, rubrics, workshops, assessments |
| Healthcare ops | 12 | Clinic flow and documentation quality |
| Media | 12 | Assignments, source logs, headlines, corrections |
| Creator | 43 | Video outlines, sponsorship, scripts, community |
| AI | 10 | Use cases, evals, review gates, cost control |
| SEO | 8 | Query maps, intent, local listings, briefs |
| Oil and gas | 8 | Production, nominations, site safety notes |
| Airline | 8 | Delays, duty checks, station opens |
| Automotive | 8 | Service lane, recalls, DVI, handovers |
| Small business | 8 | Owner cash, first hire, local offers |
| SaaS | 8 | Weekly metrics, activation, pricing page |
| Blog | 8 | Assignments, edits, titles, source checks |
| Energy | 8 | Tariffs, bills, curtailment, isolation |
| Retail | 11 | Promotions, listings, cart recovery, loyalty, planogram |
| + 15 more | — | Agriculture, banking, construction, consulting… |

Full list: [catalog/SKILLS.md](catalog/SKILLS.md)

## Skill format

Each skill is a folder with one `SKILL.md` file:

```
plugins/finance/skills/cash-flow-forecast/
└── SKILL.md
```

```markdown
---
name: cash-flow-forecast
description: "Build a 13-week direct cash forecast from collections and
  commitments, not accrual revenue. Use when the user mentions 13-week
  cash, cash forecast, or when do we run out of money."
license: MIT
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: finance
---

## When to use
...

## Workflow
...

## Quality bar
...
```

Claude loads a skill when the task description matches. You can also invoke directly: `/cash-flow-forecast`.

## Why the guardrails matter

Every skill in a regulated domain (finance, legal, HR, medical, tax) tells Claude to:
- Draft for a qualified human to review, not self-sign
- Use only the data the user supplied — no invented numbers
- State what is missing rather than filling in a gap
- Label output as a draft, not a final deliverable

This is not a legal, tax, medical, or investment advice product.

## Trust

| Promise | How to verify |
| --- | --- |
| No telemetry | Read `scripts/install.py` — it copies files, nothing else |
| No remote calls during install | No `curl` pipeline in these docs |
| Files match the manifest | `python3 scripts/validate.py` |
| Author is visible in every skill | Every SKILL.md says Yasir Jilani |
| Not an Anthropic product | This README says so, on purpose |

## Claude Code marketplace

```bash
/plugin marketplace add YOUR_GITHUB_USER/claude-practice-skills
/plugin install finance@yj-skills
```

The marketplace name is `yj-skills`. Each domain is one plugin.

## Repository layout

```
plugins/<domain>/skills/<skill-name>/SKILL.md   ← install these
examples/by-skill/<domain>/<skill-name>.md       ← one example per skill
catalog/SKILLS.md                                ← full index
scripts/install.py                               ← installer
scripts/validate.py                              ← hash check
source/                                          ← source for the generator
```

`plugins/` is what you install. `source/` is what you edit if you want to add skills. Run `python3 scripts/generate.py` to rebuild `plugins/` from `source/`. You do not need to run the generator to install.

Contributing, naming rules, and how to add a skill: [CONTRIBUTING.md](CONTRIBUTING.md)

## License

MIT. Copyright 2026 Yasir Jilani.
