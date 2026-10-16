"""MANIFEST.sha256 integrity.

install.py verifies this manifest before copying anything, so a stale or wrong
entry breaks installation on a clean clone. That has happened: an entry for a
deleted file survived in the manifest and failed the integrity check.
"""

from __future__ import annotations

import hashlib


def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_every_manifest_entry_points_at_a_real_file(root, manifest):
    missing = [p for p in manifest if not (root / p).exists()]
    assert not missing, f"manifest lists files that do not exist: {missing}"


def test_every_manifest_hash_matches_the_file(root, manifest):
    wrong = [p for p, digest in manifest.items() if _sha256(root / p) != digest]
    assert not wrong, f"manifest hash does not match file contents: {wrong}"


def test_every_skill_is_listed_in_the_manifest(root, manifest, skill_files):
    unlisted = [
        str(p.relative_to(root)) for p in skill_files if str(p.relative_to(root)) not in manifest
    ]
    assert not unlisted, f"SKILL.md files absent from the manifest: {unlisted}"


def test_manifest_is_not_empty(manifest):
    assert len(manifest) > 100


def test_no_crlf_in_hashed_files(root, manifest):
    """Git on Windows rewrites LF to CRLF unless .gitattributes forbids it.

    That changes the bytes, so every manifest hash mismatches and install.py
    refuses to run. .gitattributes pins eol=lf; this guards it.
    """
    crlf = [p for p in manifest if b"\r\n" in (root / p).read_bytes()]
    assert not crlf, f"CRLF line endings would break the manifest: {crlf[:5]}"


def test_gitattributes_pins_line_endings(root):
    attrs = root / ".gitattributes"
    assert attrs.exists(), ".gitattributes is required to keep LF on Windows clones"
    assert "eol=lf" in attrs.read_text()
