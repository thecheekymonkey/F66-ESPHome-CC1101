# Changelog

All notable project changes are documented here.

## [4.5.0] - 2026-07-26

### Added

- Active Fan State tracking model and summary text sensor (`text_sensor.active_fan_state`)
- Custom Material Design icons (`mdi:`) for all 15 primary remote controls
- Stock Home Assistant Native Tile Grid dashboard card YAML configuration
- Entity categorization (`config` and `diagnostic`) for clean Home Assistant device presentation

### Changed

- Updated version banner to 4.5.0

## [4.0.0] - 2026-07-26


### Added

- Production project naming and version banner
- Reserved GPIO4/GPIO5 documentation for future BME680 I²C support
- GitHub-ready documentation and release structure
- Flipper Zero raw `.sub` captures and button sequence documentation (`subghz/`)
- Photographic documentation of handset, prototype setup, spectrum analyzer, pinout, and HA dashboard (`images/`)


### Changed

- Logger reduced from DEBUG to INFO
- Status entities renamed for production use
- Firmware cleaned for release

### Removed

- RF profile restore button
- CC1101 reinitialisation button

### Verified

- All 15 original remote functions tested successfully
- Literal waveform data retained from the working V3 firmware

## [3.0.0] - 2026-07-26

### Added

- Literal replay of all measured F66 remote frames
- Runtime controls for frequency, symbol rate, repeats and TX settling

### Fixed

- Replaced the unsuccessful generated-frame implementation
- Preserved the actual captured final framing behaviour

## [1.x–2.x] - Experimental

- Protocol decoding experiments
- Generated waveform tests
- Framing hypotheses
- Frequency and timing sweeps
