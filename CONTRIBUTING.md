# Contributing

Skills in this repository are written by Yasir Jilani. A change is a text review, not a downloadable agent.

Do not edit `plugins/` by hand. The next `python3 scripts/generate.py` overwrites it. Edit `source/`, then generate.

## Folder structure

```text
plugins/supply-chain/
├── .claude-plugin/plugin.json
└── skills/dock-photo-note/
    └── SKILL.md
```

| Piece | Rule |
| --- | --- |
| Domain folder | An existing plugin id, such as `supply-chain` |
| Skill folder | Same string as the `name` field |
| Required file | `SKILL.md` |
| Optional | `references/`, `scripts/`, `assets/` |
| Not allowed | `README.md` inside a skill folder, network code, a skill nested inside `.claude-plugin/` |

`plugin.json` `author` is an object, `{ "name": "Yasir Jilani" }`, not a string.

## Naming

Use lowercase kebab-case. Letters, numbers, and single hyphens only. No leading, trailing, or double hyphen. 64 characters or fewer. The name is the job, not the company and not the date.

| Use | Do not use |
| --- | --- |
| `dock-photo-note` | `DockPhoto` |
| `dock-photo-note` | `dock_photo_note` |
| `dock-photo-note` | `supply-chain-dock-photo-note-for-harbor-goods` |
| `oil-gas` for a domain that already exists | a new domain for one skill |

The folder, the frontmatter `name`, and the example path must be the same string:

```text
plugins/supply-chain/skills/dock-photo-note/SKILL.md
examples/by-skill/supply-chain/dock-photo-note.md
```

## Format

Add the skill in `source/`, in the pack for that domain. One block, blank line before the next skill:

```text
dock-photo-note | Dock Photo Note | dock photo note
job: Record a dock photo against the PO line and the tally, without calling a short count theft.
triggers: dock photo; receiving photo; short shipment photo; OS&D photo
inputs: The PO; The tally; What the photo shows; Who took it
steps: Name the PO line. || State the counted quantity and the billed quantity. || Say only what the photo shows. || Do not call a short count theft. || Name who sends the note. || Hold the difference out of available stock.
anti: A theft claim from a short count; A photo of a different PO; Stock raised to match the bill
example: PO 5521 billed 40 filters. The tally is 32. The photo shows 32 boxes and an intact seal.
out: A note for 8 short, stock available 32, and no theft claim.
related: dock-exception-note
```

Then generate and validate:

```bash
python3 scripts/generate.py
python3 scripts/validate.py
```

The generated file starts like this. Do not put `<` or `>` in the frontmatter.

```markdown
---
name: dock-photo-note
description: "Record a dock photo against the PO line and the tally, without calling a short count theft. Use when the user mentions dock photo, receiving photo, short shipment photo, or OS&D photo, or asks for a dock photo note. Supply chain skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: supply-chain
---
```

The body is the procedure: when to use it, inputs, steps, and one example. The example file is separate and has four parts only:

1. What this is for
2. Scenario
3. Example data
4. Example outcome

Example data is the file a person would hand over. The outcome is the note they would send, not a sentence describing the note.

## Writing an example by hand

The generator writes an example for every skill from the `inputs`, `steps` and `anti` you supply. That is the default and it is fine for most skills.

When a skill deserves a fuller example — real figures, a reconciliation that does not balance, a table a reader can check — add it to `source/scenario_bank.py` instead. A skill listed there overrides its generated example and survives the next `generate.py`:

```python
put(
    "dock-photo-note",
    "Record a dock photo against the PO line and the tally.",
    "Scenario paragraph: who, where, what they need and by when.",
    """```text
PO 5521 ... the file a person would actually hand over
```""",
    """**Dock photo note**
...the note they would send, with the 32 and the 8 visible...""",
)
```

Use it for the skills a newcomer is most likely to open first. A hand-written example should show arithmetic, a table, or a refusal — something the generated version cannot.

## Collaboration example

Priya has a dock photo. Sam keeps the catalog consistent. They are not both editing `plugins/`.

1. Priya checks `catalog/SKILLS.md` for `dock-exception-note`. The new skill must not reuse that name.
2. She branches `add-dock-photo-note` and adds the block above to the supply-chain source. She does not open a second domain.
3. She runs generate and validate. The diff should show `source/`, `plugins/supply-chain/skills/dock-photo-note/SKILL.md`, the example file, and the catalog. A hand-edited `SKILL.md` with no source change is not a complete change.
4. Sam reviews the name, the folder match, and the example. He rejects it if the outcome says "a note that records the shortage" instead of showing the 32 and the 8.
5. After merge, either person can install just that domain:

```bash
python3 scripts/install.py --tool claude --domain supply-chain --dry-run
```

## Do not add

- Network calls, telemetry, license checks, or a `curl | sh` installer
- A skill that asks for a password, token, or card number
- Exploit steps, or instructions to deceive a customer, auditor, or colleague
- Invented citations, fake metrics, or a copied script
- A `README.md` inside a skill folder
