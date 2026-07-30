# Changelog

## [1.0.1] - 2026-07-30

### Changed

- Standardized the project name as `F66 Ceiling Fan Controller`
- Standardized release tags, folders and filenames
- Removed obsolete TEST-RF wording from current production comments
- Documented canonical Home Assistant labels and installation-specific entity IDs
- Added `docs/NAMING_CONVENTIONS.md`
- Preserved RF behavior and command values from v1.0.0

## [1.0.0] - 2026-07-30

### Added

- Formal production-stable release
- Canonical RF protocol documentation
- Verified command vectors
- Stateless ESPHome button for every dashboard RF action
- Home Assistant Mushroom dashboard using `button.press`
- Automated protocol and release consistency tests
- AI-agent and contributor governance rules
- Preserved legacy development history

### Architecture

- Production continues to generate packets instead of replaying captured waveforms.
- Native optimistic fan/select entities remain available, but the supplied dashboard does not depend on their state to trigger RF commands.
