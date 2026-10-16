"""install.py: path safety, tool targets, and a real install into a temp tree."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import install as installer
import pytest

EXPECTED_TOOLS = {
    "claude",
    "claude-project",
    "codex",
    "gemini",
    "agents",
    "project",
    "cursor",
    "windsurf",
    "opencode",
    "hermes",
    "openclaw",
    "openclaw-project",
    "langchain",
}


def test_every_documented_tool_resolves(tmp_path):
    for tool in EXPECTED_TOOLS:
        dest = installer.destinations(tool, tmp_path)
        assert dest, f"{tool} resolved to nothing"


def test_unknown_tool_is_rejected(tmp_path):
    with pytest.raises(SystemExit):
        installer.destinations("not-a-real-tool", tmp_path)


def test_all_returns_every_tool(tmp_path):
    assert set(installer.destinations("all", tmp_path)) >= EXPECTED_TOOLS


@pytest.mark.parametrize("bad", ["/", "/etc", "/usr/bin", "/System"])
def test_system_paths_are_refused(bad):
    with pytest.raises(SystemExit):
        installer.assert_safe_destination(Path(bad))


def test_hermes_and_openclaw_target_their_documented_paths(tmp_path):
    hermes = installer.destinations("hermes", tmp_path)["hermes"]
    assert hermes.parts[-2:] == (".hermes", "skills")
    openclaw = installer.destinations("openclaw", tmp_path)["openclaw"]
    assert openclaw.parts[-2:] == (".agents", "skills")


def test_manifest_verification_passes_on_a_clean_tree():
    assert installer.verify_tree()


def _run(root, *args):
    return subprocess.run(
        [sys.executable, "scripts/install.py", *args],
        cwd=root,
        capture_output=True,
        text=True,
    )


def test_dry_run_writes_nothing(root, tmp_path):
    out = _run(
        root, "--tool", "project", "--project", str(tmp_path), "--domain", "retail", "--dry-run"
    )
    assert out.returncode == 0, out.stderr
    assert not list(tmp_path.rglob("SKILL.md"))


def test_real_install_copies_the_domain(root, tmp_path):
    out = _run(root, "--tool", "project", "--project", str(tmp_path), "--domain", "retail")
    assert out.returncode == 0, out.stderr
    installed = list(tmp_path.rglob("SKILL.md"))
    assert installed, "install produced no files"
    expected = len(list((root / "plugins" / "retail" / "skills").iterdir()))
    assert len(installed) == expected


def test_install_without_a_domain_installs_nothing(root, tmp_path):
    """--domain all must be opt-in; a bare invocation must not dump 600 skills."""
    _run(root, "--tool", "project", "--project", str(tmp_path))
    assert not list(tmp_path.rglob("SKILL.md"))


def test_unknown_domain_fails(root, tmp_path):
    out = _run(
        root,
        "--tool",
        "project",
        "--project",
        str(tmp_path),
        "--domain",
        "nonexistent-domain",
        "--dry-run",
    )
    assert out.returncode != 0


@pytest.mark.parametrize("bad", ["/System", "/Library", "/Applications", "/System/Library/Foo"])
def test_macos_system_roots_are_refused(bad):
    with pytest.raises(SystemExit):
        installer.assert_safe_destination(Path(bad))


def test_ordinary_user_paths_are_allowed(tmp_path):
    """The system-root guard must not reject a project directory called 'system'."""
    installer.assert_safe_destination(tmp_path / "system" / "skills")
