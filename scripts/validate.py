#!/usr/bin/env python3
"""Validate Practice Skills structure and reject unsafe patterns.

The check is local and deterministic. It does not phone home.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILL_RED_FLAGS = [
    "ignore previous instructions",
    "paste your api key",
    "paste your password",
    "send me your password",
    "disable safety",
]
CODE_RED_FLAGS = [
    "eval(",
    "exec(",
    "os.system",
    "subprocess",
    "urllib",
    "requests",
    "socket",
    "base64.b64decode",
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None, "missing frontmatter"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unclosed frontmatter"
    block = text[4:end]
    if "<" in block or ">" in block:
        return None, "angle brackets in frontmatter"
    fields = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields, None


def main():
    errors = []
    skills = list((ROOT / "plugins").glob("*/skills/*/SKILL.md"))
    if len(skills) < 400:
        errors.append(f"expected at least 400 skills, found {len(skills)}")
    names = []
    for path in skills:
        text = path.read_text(encoding="utf-8")
        fields, problem = frontmatter(text)
        folder = path.parent.name
        names.append(folder)
        if problem:
            errors.append(f"{path}: {problem}")
            continue
        if fields.get("name") != folder:
            errors.append(f"{path}: name does not match folder")
        if not NAME_RE.match(folder) or len(folder) > 64:
            errors.append(f"{folder}: invalid skill name")
        description = fields.get("description", "")
        if not description or len(description) > 1024:
            errors.append(f"{folder}: bad description length")
        if "Yasir Jilani" not in text:
            errors.append(f"{folder}: missing author")
        if text.count("\n") > 500:
            errors.append(f"{folder}: SKILL.md exceeds 500 lines")
        lowered = text.lower()
        for snippet in SKILL_RED_FLAGS:
            if snippet in lowered:
                errors.append(f"{folder}: forbidden snippet {snippet}")
    if len(names) != len(set(names)):
        errors.append("duplicate skill folder names")
    marketplace = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    if marketplace.get("owner", {}).get("name") != "Yasir Jilani":
        errors.append("marketplace owner is not Yasir Jilani")
    for plugin in marketplace.get("plugins", []):
        if not (ROOT / plugin["source"]).is_dir():
            errors.append(f"marketplace source missing {plugin['source']}")
    code_files = list((ROOT / "plugins").glob("*/skills/*/scripts/*.py"))
    code_files.extend(path for path in (ROOT / "scripts").glob("*.py") if path.name != "validate.py")
    for script in code_files:
        source = script.read_text(encoding="utf-8").lower()
        for snippet in CODE_RED_FLAGS:
            if snippet in source:
                errors.append(f"{script.relative_to(ROOT)} contains {snippet}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {len(skills)} skills, marketplace, and installer surface.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
