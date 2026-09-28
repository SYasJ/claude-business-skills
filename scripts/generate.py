#!/usr/bin/env python3
"""Generate the Practice Skills tree from source records.

This script only writes files inside the repository. It does not use the
network, install packages, or read credentials.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(SOURCE))

from render_skill import render_skill  # noqa: E402
from worked import attach_worked  # noqa: E402

PACK_MODULES = [
    "pack_growth",
    "pack_market",
    "pack_product",
    "pack_engineering",
    "pack_flow",
    "pack_run",
    "pack_care",
    "pack_practice",
    "pack_fields",
    "pack_supply",
    "pack_world",
    "pack_sectors",
    "pack_creator",
    "pack_more",
]
DOMAIN_MODULES = [
    "d01_strategy",
    "d02_finance",
    "d03_accounting",
    "d04_legal",
    "d05_people",
]
VERSION = "1.0.0"
AUTHOR = "Yasir Jilani"
REPOSITORY = "https://github.com/SYasJ/claude-business-skills"
HOMEPAGE = "https://syasj.github.io/claude-business-skills/"
LOCAL_TOOLS = {
    "cash-flow-forecast": (
        "A stdlib script is bundled at `scripts/cashflow_check.py`. "
        "It rolls a CSV of `week,inflow,outflow` forward from an opening balance you pass with `--opening`. "
        "It does not fetch bank data, rates, or credentials. Example: "
        "`python3 scripts/cashflow_check.py weeks.csv --opening 100000 --buffer 25000 --json`. "
        "For the assumption log format, see [references/assumptions.md](references/assumptions.md)."
    ),
    "prioritization-rice": (
        "A stdlib script is bundled at `scripts/rice_score.py`. "
        "It scores a CSV of `item,reach,impact,confidence,effort` that you already filled in. "
        "It does not invent reach or confidence. Example: `python3 scripts/rice_score.py items.csv --json`."
    ),
    "raid-log": (
        "A stdlib script is bundled at `scripts/raid_lint.py`. "
        "It checks a CSV of `type,item,owner,date,status` for missing owners and dates. "
        "It does not update a project system. Example: `python3 scripts/raid_lint.py raid.csv --json`."
    ),
}


def load_packs():
    packs = []
    for name in DOMAIN_MODULES:
        module = __import__(name)
        packs.append({"domain": module.DOMAIN, "skills": module.SKILLS})
    for name in PACK_MODULES:
        module = __import__(name)
        packs.extend(module.PACKS)
    return merge_packs(packs)


def merge_packs(packs):
    order = []
    by_id = {}
    for pack in packs:
        domain_id = pack["domain"]["id"]
        if domain_id not in by_id:
            by_id[domain_id] = pack
            order.append(pack)
            continue
        by_id[domain_id]["skills"].extend(pack["skills"])
        keywords = by_id[domain_id]["domain"].setdefault("keywords", [])
        for word in pack["domain"].get("keywords", []):
            if word not in keywords:
                keywords.append(word)
    return order


def validate(packs):
    errors = []
    seen = {}
    for pack in packs:
        domain_id = pack["domain"]["id"]
        if domain_id in {item["domain"]["id"] for item in packs if item is not pack}:
            pass
        for record in pack["skills"]:
            name = record["name"]
            if name in seen:
                errors.append(f"duplicate skill name {name}")
            seen[name] = domain_id
            if len(name) > 64 or "--" in name or name.startswith("-") or name.endswith("-"):
                errors.append(f"bad name {name}")
            if not all(ch.islower() or ch.isdigit() or ch == "-" for ch in name):
                errors.append(f"name characters {name}")
            if len(record["steps"]) < 5:
                errors.append(f"{name} has too few steps")
            if len(record["anti"]) < 3 or len(record["triggers"]) < 3:
                errors.append(f"{name} missing triggers or anti-patterns")
    domain_ids = [pack["domain"]["id"] for pack in packs]
    if len(domain_ids) != len(set(domain_ids)):
        errors.append("duplicate domain id")
    if errors:
        raise SystemExit("Catalog errors:\n- " + "\n- ".join(errors))
    return seen


def filter_related(record, known):
    record["related"] = [name for name in record["related"] if name in known and name != record["name"]]
    return record


def sha256(path):
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main():
    packs = load_packs()
    known = validate(packs)
    catalog = []
    manifest_lines = []
    for pack in packs:
        domain = pack["domain"]
        domain_dir = ROOT / "plugins" / domain["id"]
        plugin = {
            "name": domain["id"],
            "version": VERSION,
            "description": domain["summary"],
            "author": {"name": AUTHOR},
            "license": "MIT",
            "homepage": HOMEPAGE,
            "repository": REPOSITORY,
            "keywords": domain.get("keywords", []),
        }
        write(domain_dir / ".claude-plugin" / "plugin.json", json.dumps(plugin, indent=2) + "\n")
        for record in pack["skills"]:
            filter_related(record, known)
            attach_worked(record, domain)
            body = render_skill(record, domain)
            if body.count("\n") > 500:
                raise SystemExit(f"{record['name']} exceeds 500 lines")
            if "<" in body.split("---", 2)[1] or ">" in body.split("---", 2)[1]:
                raise SystemExit(f"{record['name']} has angle brackets in frontmatter")
            skill_dir = domain_dir / "skills" / record["name"]
            if record["name"] in LOCAL_TOOLS:
                body = body.rstrip() + "\n\n## Optional local tool\n\n" + LOCAL_TOOLS[record["name"]] + "\n"
            skill_path = skill_dir / "SKILL.md"
            write(skill_path, body)
            catalog.append(
                {
                    "name": record["name"],
                    "title": record["title"],
                    "domain": domain["id"],
                    "domain_title": domain["title"],
                    "summary": record["job"],
                    "artifact": record["artifact"],
                    "triggers": record["triggers"],
                    "example": record["example"],
                    "example_out": record["example_out"],
                }
            )
            write(ROOT / "examples" / "by-skill" / domain["id"] / f"{record['name']}.md", render_example(record, domain))
    catalog.sort(key=lambda item: (item["domain"], item["name"]))
    write(ROOT / "catalog" / "skills.json", json.dumps(catalog, indent=2) + "\n")
    write(ROOT / "catalog" / "SKILLS.md", render_catalog(packs, catalog))
    write(ROOT / "examples" / "INDEX.md", render_example_index(catalog))
    marketplace = {
        "name": "yj-skills",
        "owner": {"name": AUTHOR},
        "description": (
            f"Independent Agent Skills library by {AUTHOR}. "
            f"{len(catalog)} practice skills across {len(packs)} domains for Claude and other Agent Skills clients. "
            "Not affiliated with Anthropic. No telemetry, no remote installer, no license server."
        ),
        "plugins": [],
    }
    for pack in packs:
        domain = pack["domain"]
        marketplace["plugins"].append(
            {
                "name": domain["id"],
                "source": f"./plugins/{domain['id']}",
                "description": domain["summary"],
                "version": VERSION,
                "author": {"name": AUTHOR},
                "category": domain["id"],
                "keywords": domain.get("keywords", []),
            }
        )
    write(ROOT / ".claude-plugin" / "marketplace.json", json.dumps(marketplace, indent=2) + "\n")
    for path in sorted((ROOT / "plugins").rglob("*")):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_file():
            rel = path.relative_to(ROOT).as_posix()
            manifest_lines.append(f"{sha256(path)}  {rel}")
    write(ROOT / "MANIFEST.sha256", "\n".join(manifest_lines) + "\n")
    counts = {pack["domain"]["id"]: len(pack["skills"]) for pack in packs}
    write(
        ROOT / "catalog" / "counts.json",
        json.dumps({"skills": len(catalog), "domains": len(packs), "by_domain": counts}, indent=2) + "\n",
    )
    print(f"Generated {len(catalog)} skills in {len(packs)} domains")


def render_example(record, domain):
    worked = record["worked"]
    return f"""# {record['title']}

`{record['name']}`

## What this is for

{worked['purpose']}

## Scenario

{worked['scenario']}

## Example data

{worked['data']}

## Example outcome

{worked['outcome']}
"""


def render_example_index(catalog):
    lines = [
        "# Separate examples",
        "",
        "One file per skill. Each file has the situation, the sample data, and a sample outcome.",
        "",
    ]
    current = None
    for item in catalog:
        if item["domain"] != current:
            current = item["domain"]
            lines.append(f"## {item['domain_title']}")
            lines.append("")
        lines.append(f"- [{item['title']}](by-skill/{item['domain']}/{item['name']}.md)")
    lines.append("")
    return "\n".join(lines)


def render_catalog(packs, catalog):
    lines = [
        "# Skills catalog",
        "",
        f"Every skill in Claude Code Business Skills, grouped by domain. "
        f"Author: {AUTHOR}. Version {VERSION}.",
        "",
        f"[Repository]({REPOSITORY}) · [Website]({HOMEPAGE}) · "
        f"[Examples]({REPOSITORY}/blob/main/examples/INDEX.md)",
        "",
        "Install a domain. Do not load every skill unless you mean to pay the description cost.",
        "",
        "```bash",
        "python3 scripts/install.py --tool claude --domain finance",
        "```",
        "",
    ]
    by_domain = {}
    for item in catalog:
        by_domain.setdefault(item["domain"], []).append(item)
    titles = {pack["domain"]["id"]: pack["domain"]["title"] for pack in packs}
    summaries = {pack["domain"]["id"]: pack["domain"]["summary"] for pack in packs}
    for domain_id in sorted(by_domain):
        lines.append(f"## {titles[domain_id]}")
        lines.append("")
        lines.append(summaries[domain_id])
        lines.append("")
        lines.append("| Skill | What it produces |")
        lines.append("| --- | --- |")
        for item in by_domain[domain_id]:
            lines.append(f"| `{item['name']}` | {item['artifact']} |")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
