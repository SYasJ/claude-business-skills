"""catalog/, marketplace.json and plugin.json must agree with what is on disk."""

from __future__ import annotations

import json

PLUGIN_FIELDS = {
    "name",
    "version",
    "description",
    "author",
    "license",
    "homepage",
    "repository",
    "keywords",
}


def test_counts_match_the_tree(root, counts, skill_files, domains):
    assert counts["skills"] == len(skill_files)
    assert counts["domains"] == len(domains)


def test_by_domain_counts_are_right(root, counts, domains):
    for domain in domains:
        on_disk = len(list((root / "plugins" / domain / "skills").iterdir()))
        assert counts["by_domain"][domain] == on_disk, f"{domain} count is wrong"


def test_skills_json_lists_every_skill(root, skill_files):
    entries = json.loads((root / "catalog" / "skills.json").read_text())
    assert len(entries) == len(skill_files)


def test_every_domain_has_a_valid_plugin_json(root, domains):
    for domain in domains:
        path = root / "plugins" / domain / ".claude-plugin" / "plugin.json"
        assert path.exists(), f"{domain} has no plugin.json"
        data = json.loads(path.read_text())
        assert set(data) >= PLUGIN_FIELDS, (
            f"{domain} plugin.json missing {PLUGIN_FIELDS - set(data)}"
        )
        assert data["name"] == domain
        assert isinstance(data["author"], dict), "author must be an object, not a string"


def test_marketplace_lists_every_domain(root, domains):
    data = json.loads((root / ".claude-plugin" / "marketplace.json").read_text())
    listed = {p["name"] for p in data["plugins"]}
    assert listed == set(domains), f"marketplace drift: {listed ^ set(domains)}"


def test_catalog_markdown_lists_every_skill(root, skill_files):
    """The catalog is the published index; a skill missing from it is invisible."""
    text = (root / "catalog" / "SKILLS.md").read_text()
    missing = [p.parent.name for p in skill_files if f"`{p.parent.name}`" not in text]
    assert not missing, f"skills absent from catalog/SKILLS.md: {missing[:10]}"


def test_no_stale_skill_counts_in_docs(root, counts):
    """A renamed or regrown library leaves old totals behind in prose."""
    total = str(counts["skills"])
    for name in ("README.md", "SECURITY.md", "catalog/SKILLS.md"):
        text = (root / name).read_text()
        for stale in ("437 skills", "587 skills", "594 skills"):
            assert stale not in text, f"{name} still says {stale} (should be {total})"
