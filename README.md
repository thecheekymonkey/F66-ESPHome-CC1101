# F66 Ceiling Fan Controller

ESPHome controller for an F66 ceiling fan receiver using an ESP32-S3 DevKitC-1, CC1101 433.92 MHz transmitter and BME680 environmental sensor.

## Stable release

**v1.0.1 — Production Stable**

This is the current known-good release. RF behavior is unchanged from the hardware-verified v1.0.0 baseline; v1.0.1 aligns naming and documentation. It generates the reverse-engineered 30-bit RF frame and uses stateless Home Assistant dashboard controls so every press causes a transmission, even when Home Assistant already believes the requested state is active.

## Main features

- Generated RF packets; no literal waveform replay in production
- Fixed 20-bit prefix, 9-bit command and calculated even-parity bit
- Speeds 1–6, Power Off, Breeze, Reverse, Light On/Off and 1/2/4/8-hour timers
- ESPHome native fan entity retained for compatibility
- Dedicated stateless command buttons used by the dashboard
- BME680 temperature, pressure, humidity and gas-resistance sensors
- CC1101 diagnostics for frequency, symbol rate, repeat count and TX settling

## Installation

1. Copy `esphome/f66-controller.yaml` into your ESPHome configuration folder.
2. Ensure `wifi_ssid` and `wifi_password` exist in ESPHome `secrets.yaml`.
3. Validate and compile the configuration.
4. Flash the ESP32-S3.
5. Confirm the new button entities appear in Home Assistant.
6. Install Mushroom Cards through HACS if not already installed.
7. Confirm the Home Assistant entity IDs match your installation, following `docs/NAMING_CONVENTIONS.md`.
8. Add `home-assistant/mushroom-card.yaml` as a manual dashboard card.
9. Run the physical verification checklist in `docs/RELEASE_CHECKLIST.md`.

## Documentation

- `docs/PROTOCOL.md` — canonical RF specification
- `docs/COMMANDS.md` — verified command table and frames
- `docs/HARDWARE.md` — hardware and pin assignments
- `docs/ARCHITECTURE.md` — design decisions and limitations
- `docs/TESTING.md` — software and hardware tests
- `docs/VERSION_HISTORY.md` — project evolution and release mapping
- `docs/NAMING_CONVENTIONS.md` — canonical project, file, version and entity naming
- `AGENTS.md` — rules for AI coding agents and contributors
- `MIGRATION_INSTRUCTIONS.md` — safe process for updating an existing GitHub repository

## Important limitation

The fan receiver is one-way. Home Assistant receives no confirmation from the fan, and the OEM remote can change the physical state without Home Assistant knowing. Dashboard commands therefore use stateless buttons and should remain that way.
