#!/usr/bin/env python3
"""Install Practice Skills onto this machine.

Local copy only. This installer does not use the network, does not execute
skill scripts, does not request credentials, and does not need a license key.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_SUFFIXES = {".md", ".py", ".json", ".txt", ".svg"}
FORBIDDEN_PARTS = {
    "etc",
    "usr",
    "bin",
    "sbin",
    "system32",
    "syswow64",
    "windows",
}


def sha256(path):
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def load_manifest():
    manifest_path = ROOT / "MANIFEST.sha256"
    if not manifest_path.exists():
        raise SystemExit("MANIFEST.sha256 is missing. Refusing to install an unverifiable tree.")
    entries = {}
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, _, rel = line.partition("  ")
        entries[rel] = digest
    return entries


def verify_tree():
    entries = load_manifest()
    mismatches = []
    for rel, expected in entries.items():
        path = ROOT / rel
        if not path.is_file() or path.is_symlink():
            mismatches.append(f"missing {rel}")
            continue
        if sha256(path) != expected:
            mismatches.append(f"hash mismatch {rel}")
    if mismatches:
        raise SystemExit("Integrity check failed:\n- " + "\n- ".join(mismatches[:20]))
    return entries


def destinations(tool, project):
    home = Path.home()
    project = project.resolve()
    mapping = {
        "claude": home / ".claude" / "skills",
        "claude-project": project / ".claude" / "skills",
        "codex": home / ".codex" / "skills",
        "gemini": home / ".gemini" / "skills",
        "agents": home / ".agents" / "skills",
        "project": project / ".agents" / "skills",
        "cursor": project / ".cursor" / "skills",
        "windsurf": project / ".windsurf" / "skills",
        "opencode": project / ".opencode" / "skills",
        # Hermes Agent reads ~/.hermes/skills as its source of truth.
        "hermes": home / ".hermes" / "skills",
        # OpenClaw discovers ~/.agents/skills and <workspace>/.agents/skills;
        # these are aliases so the tool name in the command matches the docs.
        "openclaw": home / ".agents" / "skills",
        "openclaw-project": project / ".agents" / "skills",
        # LangChain deepagents takes a directory of skill folders:
        #   create_deep_agent(..., skills=["./skills/"])
        "langchain": project / "skills",
    }
    if tool == "all":
        return mapping
    if tool not in mapping:
        raise SystemExit(f"Unknown tool {tool}")
    return {tool: mapping[tool]}


def assert_safe_destination(path):
    resolved = path.resolve()
    parts = {part.lower() for part in resolved.parts}
    if parts & FORBIDDEN_PARTS:
        raise SystemExit(f"Refusing to write into a system path: {resolved}")
    if resolved == Path(resolved.anchor):
        raise SystemExit(f"Refusing to use a drive root as destination: {resolved}")


def skill_dirs(domains):
    plugins = ROOT / "plugins"
    found = []
    if not domains or domains == ["all"]:
        domain_paths = sorted(p for p in plugins.iterdir() if p.is_dir())
    else:
        domain_paths = []
        for name in domains:
            path = plugins / name
            if not path.is_dir():
                raise SystemExit(f"Unknown domain {name}. See catalog/SKILLS.md.")
            domain_paths.append(path)
    for domain in domain_paths:
        skills = domain / "skills"
        if not skills.is_dir():
            continue
        for skill in sorted(p for p in skills.iterdir() if p.is_dir()):
            if not (skill / "SKILL.md").is_file():
                raise SystemExit(f"Missing SKILL.md in {skill}")
            found.append(skill)
    return found


def iter_files(skill_dir):
    for path in sorted(skill_dir.rglob("*")):
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise SystemExit(f"Refusing symlink in skill tree: {path}")
        if not path.is_file():
            continue
        if path.suffix.lower() not in ALLOWED_SUFFIXES:
            raise SystemExit(f"Refusing unexpected file type: {path}")
        yield path


def install(skills, dest, dry_run):
    copied = []
    for skill in skills:
        target = dest / skill.name
        for source in iter_files(skill):
            relative = source.relative_to(skill)
            outfile = target / relative
            copied.append(str(outfile))
            if dry_run:
                continue
            outfile.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, outfile)
    return copied


def main():
    parser = argparse.ArgumentParser(description="Install Yasir Jilani Practice Skills locally.")
    parser.add_argument("--tool", default="claude", help="claude, claude-project, codex, gemini, agents, project, cursor, windsurf, opencode, hermes, openclaw, openclaw-project, langchain, or all")
    parser.add_argument("--domain", action="append", default=[], help="Domain id to install. Repeatable. Default: none, so the full library is not installed by accident. Use --domain all to opt in.")
    parser.add_argument("--project", default=".", help="Project directory for project-scoped tools")
    parser.add_argument("--dry-run", action="store_true", help="Print the copy plan and write nothing")
    parser.add_argument("--skip-verify", action="store_true", help="Skip MANIFEST.sha256 verification. Not recommended.")
    args = parser.parse_args()
    if not args.domain:
        raise SystemExit(
            "No domain selected. Install one practice area, for example:\n"
            "  python3 scripts/install.py --tool claude --domain finance\n"
            "Use --domain all only if you intend to install every skill."
        )
    if not args.skip_verify:
        verify_tree()
    skills = skill_dirs(args.domain)
    project = Path(args.project)
    plan = {}
    for tool, dest in destinations(args.tool, project).items():
        assert_safe_destination(dest)
        copied = install(skills, dest, args.dry_run)
        plan[tool] = {"destination": str(dest), "files": len(copied), "skills": len(skills)}
        print(f"{tool}: {len(skills)} skills, {len(copied)} files -> {dest}")
    receipt = {
        "author": "Yasir Jilani",
        "dry_run": args.dry_run,
        "domains": args.domain,
        "tools": plan,
        "network": False,
        "credentials_requested": False,
    }
    if not args.dry_run:
        receipt_path = Path.cwd() / "install-receipt.json"
        receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {receipt_path}")
    print("Install plan is local only. No packages were downloaded and no skill script was executed.")


if __name__ == "__main__":
    main()
