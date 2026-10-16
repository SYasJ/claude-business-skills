"""Shared fixtures. Puts scripts/ and source/ on the path so tests can import them."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

for extra in (ROOT / "scripts", ROOT / "source"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))


@pytest.fixture(scope="session")
def root() -> Path:
    return ROOT


@pytest.fixture(scope="session")
def skill_files() -> list[Path]:
    files = sorted((ROOT / "plugins").rglob("SKILL.md"))
    assert files, "no SKILL.md files found - run scripts/generate.py"
    return files


@pytest.fixture(scope="session")
def domains() -> list[str]:
    return sorted(p.name for p in (ROOT / "plugins").iterdir() if p.is_dir())


@pytest.fixture(scope="session")
def manifest() -> dict[str, str]:
    entries = {}
    for line in (ROOT / "MANIFEST.sha256").read_text().splitlines():
        line = line.strip()
        if line:
            digest, _, path = line.partition("  ")
            entries[path] = digest
    return entries


@pytest.fixture(scope="session")
def counts() -> dict:
    return json.loads((ROOT / "catalog" / "counts.json").read_text())
