# Rules for AI Agents and Contributors

These rules apply to Antigravity, Gemini, Copilot and any other coding agent.

1. Read this file and every file under `docs/` before proposing changes. Follow `docs/NAMING_CONVENTIONS.md`.
2. Treat `releases/v1.0.0/` as the immutable hardware-verified baseline and `releases/v1.0.1/` as the current naming-aligned release.
3. Never edit `main` directly. Create a branch and show the full diff.
4. Never commit Wi-Fi passwords, API keys or secrets.
5. Do not alter the fixed prefix, command values, parity logic, bit order, pulse timings, frequency or repeat behavior without explicit human approval and new physical tests.
6. Do not replace generated packets with literal waveform replay.
7. Do not replace dashboard `button.press` actions with stateful fan, preset or select services.
8. Preserve separate Light On and Light Off commands.
9. Preserve Reverse as a stateless toggle command; do not claim its absolute state is known.
10. Keep experimental pairing or colour work outside production until physically verified.
11. Run `python3 tests/test_protocol.py` and `python3 scripts/check_release.py` after every change.
12. Validate and compile ESPHome when the environment supports it.
13. Do not claim hardware verification. Only the human operator can confirm physical fan behavior.
14. Update documentation and `CHANGELOG.md` with every approved release change, including naming-only changes.
15. Never delete legacy files during an audit. Move duplicates to an explicitly named archive only after human approval.

## Required workflow

1. Audit without modifying files.
2. Report conflicts with exact paths.
3. Propose a categorized plan: documentation, safe refactor, behavior change or unverified.
4. Wait for approval.
5. Apply only approved changes on a branch.
6. Run tests and provide results plus a full diff.
7. Wait for physical verification before merge or release tagging.
