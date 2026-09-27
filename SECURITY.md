# Security

Practice Skills is an independent library by Yasir Jilani. It is not affiliated with Anthropic, and it is not a hosted service.

## What this repository will not do

- It does not phone home, collect telemetry, or require an account.
- It does not ask for passwords, API keys, tokens, seed phrases, or payment cards.
- The installer copies local files. It does not download or pipe a remote script into a shell.
- Skill scripts use the Python standard library only. They do not open sockets.
- Skills are workflows. They are not a license to give legal, medical, tax, investment, or coverage advice.
- Defensive security skills do not include exploits, payloads, or bypasses.
- Nothing in this tree should be read as an official Claude product.

## Check the tree before you install

From the repository root:

```bash
python3 scripts/validate.py
python3 scripts/install.py --tool claude --domain finance --dry-run
```

`validate.py` checks skill format and rejects skill text that asks you to paste credentials or ignore safety rules. `MANIFEST.sha256` lists every plugin file. The installer verifies those hashes unless you pass `--skip-verify`.

## Install one domain

Each installed skill adds its name and description to the agent's startup context. Install the domain you need:

```bash
python3 scripts/install.py --tool claude --domain finance
```

Do not install all 437 skills unless you have decided the context cost is worth it.

## Reporting a problem

If you find a skill that asks for secrets, hides a network call, or gives a regulated conclusion as if it were licensed advice, remove that skill and send a note to the maintainer before publishing a fix. Do not "fix" it by adding a remote dependency.
