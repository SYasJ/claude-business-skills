# Practice Skills

This repository is an Agent Skills library by Yasir Jilani. It is not an Anthropic product.

When working in this repo:

- Install or recommend one domain, not the full library, unless the user asks for every skill.
- Do not add network calls, credential prompts, or remote installers.
- Do not write exploits, evasion steps, or deceptive customer copy into a skill.
- Regulated drafts stay drafts. Do not invent laws, rates, diagnoses, or coverage decisions.
- Keep `SKILL.md` under 500 lines. Put long notes in `references/`.
- After changing `source/`, run `python3 scripts/generate.py` and `python3 scripts/validate.py`.
- The installer is `python3 scripts/install.py`. Never replace it with a `curl | sh` command.
