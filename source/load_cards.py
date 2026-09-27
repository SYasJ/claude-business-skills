"""Load compact skill cards from text blocks."""

from __future__ import annotations

from schema import skill


def parse_cards(text, defaults=None):
    defaults = defaults or {}
    records = []
    blocks = []
    current = []
    for line in text.splitlines():
        if line.startswith("== ") and line.endswith(" =="):
            if current:
                blocks.append(current)
            current = [line]
        else:
            if current:
                current.append(line)
    if current:
        blocks.append(current)
    for block in blocks:
        header = block[0][3:-3].strip()
        name, _, title = header.partition(" | ")
        fields = {
            "triggers": [],
            "inputs": [],
            "steps": [],
            "anti": [],
            "related": [],
            "avoid": [],
            "outputs": [],
            "checks": [],
        }
        mode = None
        scalar = {}
        for line in block[1:]:
            if not line.strip():
                mode = None
                continue
            if line.startswith("  - ") and mode:
                fields[mode].append(line[4:].strip())
                continue
            if ":" in line and not line.startswith(" "):
                key, _, value = line.partition(":")
                key = key.strip()
                value = value.strip()
                if key in fields:
                    mode = key
                    if value:
                        fields[key].append(value)
                else:
                    mode = None
                    scalar[key] = value
                continue
            if mode in ("job", "example", "example_out", "artifact"):
                scalar[mode] = (scalar.get(mode, "") + " " + line.strip()).strip()
        data = {**defaults, **scalar}
        records.append(
            skill(
                name.strip(),
                title.strip(),
                data["job"],
                data["artifact"],
                fields["triggers"],
                fields["inputs"],
                fields["steps"],
                fields["anti"],
                data["example"],
                data["example_out"],
                related=fields["related"],
                avoid=fields["avoid"],
                outputs=fields["outputs"],
                checks=fields["checks"],
            )
        )
    return records
