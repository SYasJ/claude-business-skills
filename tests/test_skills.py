"""Every SKILL.md must satisfy the Agent Skills format and this repo's own rules."""

from __future__ import annotations

import re

import pytest

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Phrases a skill must never contain. The repo's security promise is that no
# skill asks for a credential or tells the agent to ignore its rules.
FORBIDDEN = (
    "ignore previous instructions",
    "ignore all previous",
    "disregard your instructions",
    "paste your api key",
    "paste your password",
    "enter your password",
    "share your seed phrase",
)


def _frontmatter(text):
    assert text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
    end = text.index("\n---\n", 3)
    block = text[4:end]
    fields = {}
    for line in block.splitlines():
        if line and not line.startswith((" ", "\t")) and ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields, block, text[end + 5 :]


@pytest.fixture(scope="module")
def parsed(skill_files):
    return [(p, *_frontmatter(p.read_text())) for p in skill_files]


def test_frontmatter_has_required_fields(parsed):
    for path, fields, _, _ in parsed:
        for key in ("name", "description", "license"):
            assert key in fields, f"{path} frontmatter is missing '{key}'"


def test_name_matches_directory(parsed):
    for path, fields, _, _ in parsed:
        assert fields["name"] == path.parent.name, (
            f"{path}: frontmatter name {fields['name']!r} != directory {path.parent.name!r}"
        )


def test_name_is_kebab_case(parsed):
    for path, fields, _, _ in parsed:
        assert NAME_RE.match(fields["name"]), f"{path}: {fields['name']!r} is not kebab-case"
        assert len(fields["name"]) <= 64, f"{path}: name longer than 64 characters"


def test_no_angle_brackets_in_frontmatter(parsed):
    """Angle brackets break YAML parsing in some Agent Skills clients."""
    for path, _, block, _ in parsed:
        assert "<" not in block and ">" not in block, f"{path}: angle bracket in frontmatter"


def test_description_is_substantial(parsed):
    """The description is the only thing loaded at startup - it has to carry its weight."""
    for path, fields, _, _ in parsed:
        assert len(fields["description"]) >= 40, f"{path}: description too short to route on"


def test_body_stays_under_the_line_budget(parsed):
    for path, _, _, body in parsed:
        assert body.count("\n") <= 500, f"{path}: body exceeds 500 lines"


def test_no_credential_or_jailbreak_language(parsed):
    for path, _, _, body in parsed:
        low = body.lower()
        for phrase in FORBIDDEN:
            assert phrase not in low, f"{path}: contains forbidden phrase {phrase!r}"


def test_every_skill_has_an_example(root, parsed):
    missing = []
    for path, fields, _, _ in parsed:
        domain = path.parents[2].name
        example = root / "examples" / "by-skill" / domain / f"{fields['name']}.md"
        if not example.exists():
            missing.append(str(example.relative_to(root)))
    assert not missing, f"skills with no example file: {missing}"


def test_generated_header_points_contributors_at_source(parsed):
    """plugins/ is generated; a contributor editing it loses their work."""
    for path, _, _, body in parsed:
        assert "GENERATED FILE" in body, f"{path}: missing the generated-file notice"
