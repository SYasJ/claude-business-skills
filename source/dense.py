"""Parse dense skill blocks into catalog records."""

from __future__ import annotations

from schema import skill


def _split(value, sep):
    return [part.strip() for part in value.split(sep) if part.strip()]


def parse_dense(text):
    records = []
    chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]
    for chunk in chunks:
        lines = [line.strip() for line in chunk.splitlines() if line.strip()]
        if lines[0].startswith("#"):
            continue
        try:
            name, title, artifact = [part.strip() for part in lines[0].split("|")]
        except ValueError as exc:
            raise ValueError(f"Bad header: {lines[0]}") from exc
        fields = {}
        for line in lines[1:]:
            key, sep, value = line.partition(":")
            if not sep:
                raise ValueError(f"{name}: missing colon in {line}")
            fields[key.strip()] = value.strip()
        for required in ("job", "triggers", "inputs", "steps", "anti", "example", "out"):
            if required not in fields:
                raise ValueError(f"{name}: missing {required}")
        steps = _split(fields["steps"], "||")
        if len(steps) < 5:
            raise ValueError(f"{name}: only {len(steps)} steps")
        records.append(
            skill(
                name,
                title,
                fields["job"],
                artifact,
                _split(fields["triggers"], ";"),
                _split(fields["inputs"], ";"),
                steps,
                _split(fields["anti"], ";"),
                fields["example"],
                fields["out"],
                related=_split(fields.get("related", ""), ";"),
                avoid=_split(fields.get("avoid", ""), ";"),
            )
        )
    return records


def pack(domain, text):
    return {"domain": domain, "skills": parse_dense(text)}
