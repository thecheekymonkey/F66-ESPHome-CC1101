# Instructions to Update the Existing GitHub Repository

## 1. Back up first

- Download a ZIP of the current GitHub repository.
- Record the current `main` commit hash.
- Create a backup branch such as `backup-before-f66-v1`.
- Do not let an AI agent work directly on `main`.

## 2. Give Antigravity this package

Copy the complete contents of this package into a new working branch, for example:

```bash
git checkout -b f66-v1-repository-rebuild
```

Do not overwrite unknown files silently. Existing files must first be inventoried and compared.

## 3. First Antigravity prompt: audit only

```text
Read AGENTS.md, README.md and every file under docs/.
Do not modify any file.
Inventory the current repository and compare it with this v1.0.1 package.
Identify duplicates, conflicts, missing documentation, changed RF constants,
changed entity IDs and any dashboard action that does not use button.press.
Report exact file paths and classify each issue as documentation only,
safe refactor, behavior change or unverified. Do not implement anything.
```

## 4. Review the audit

Reject any proposal that changes verified RF behavior without a clear reason and a new physical-test plan. Preserve potentially useful old material under `archive/legacy/` rather than deleting it.

## 5. Second Antigravity prompt: controlled update

```text
Apply only the approved audit changes on the current branch.
Use `releases/v1.0.0` as the immutable hardware-verified behavior baseline and `releases/v1.0.1` as the current naming-aligned release. Follow `docs/NAMING_CONVENTIONS.md`.
Do not change RF constants, command values, parity, pulse timings or stateless
dashboard actions. Preserve unknown or experimental material under archive/legacy.
Run python3 tests/test_protocol.py and python3 scripts/check_release.py.
Run ESPHome validation and compilation if available.
Return the full diff and all test output. Do not merge and do not create a tag.
```

## 6. Human checks

- Review the complete diff.
- Flash the resulting firmware to the controller.
- Complete `docs/RELEASE_CHECKLIST.md`.
- Confirm repeated presses work for every command.

## 7. Merge and release

After all checks pass:

```bash
git add .
git commit -m "Release F66 controller v1.0.1"
git push -u origin f66-v1-repository-rebuild
```

Create a pull request. After human review and physical testing, merge it and then:

```bash
git checkout main
git pull
git tag -a v1.0.1 -m "F66 Ceiling Fan Controller v1.0.1 production stable"
git push origin v1.0.1
```

Create a GitHub Release for `v1.0.1` and attach the two files from `releases/v1.0.1/`. Keep the existing `v1.0.0` release unchanged.
