"""The generator must be deterministic and its output must already be committed.

plugins/, examples/, catalog/ and MANIFEST.sha256 are all generated from
source/. If a contributor edits source/ and forgets to regenerate, or edits
plugins/ directly, the tree drifts. This catches both.
"""

from __future__ import annotations

import shutil
import subprocess
import sys


def _git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True)


def test_generated_tree_is_committed(root):
    """Regenerating must produce no diff. If this fails, run scripts/generate.py."""
    if not shutil.which("git") or _git(root, "rev-parse", "--git-dir").returncode != 0:
        import pytest

        pytest.skip("not a git checkout")

    before = _git(root, "status", "--porcelain")
    if before.stdout.strip():
        import pytest

        pytest.skip("working tree is dirty; cannot distinguish generator drift")

    gen = subprocess.run(
        [sys.executable, "scripts/generate.py"], cwd=root, capture_output=True, text=True
    )
    assert gen.returncode == 0, gen.stderr

    after = _git(root, "status", "--porcelain")
    assert not after.stdout.strip(), (
        "scripts/generate.py changed files that are committed differently.\n"
        "Run: python3 scripts/generate.py && git add -A\n"
        f"Changed:\n{after.stdout}"
    )


def test_validate_script_passes(root):
    out = subprocess.run(
        [sys.executable, "scripts/validate.py"], cwd=root, capture_output=True, text=True
    )
    assert out.returncode == 0, out.stdout + out.stderr


def test_related_skills_all_exist(root, skill_files):
    """A 'related' pointer at a skill that was renamed or removed is a dead link."""
    import re

    names = {p.parent.name for p in skill_files}
    dead = []
    for path in skill_files:
        text = path.read_text()
        match = re.search(r"## Related skills\n(.*?)(?:\n## |\Z)", text, re.S)
        if not match:
            continue
        for ref in re.findall(r"`([a-z0-9-]+)`", match.group(1)):
            if ref not in names:
                dead.append(f"{path.parent.name} -> {ref}")
    assert not dead, f"related-skill pointers at skills that do not exist: {dead}"
