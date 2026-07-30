# F66 Ceiling Fan Controller v4.5.0

This production release enhances the ESPHome F66 ceiling-fan controller with active state tracking, custom UI icons, and clean Home Assistant dashboard tile grid layout support.

## Confirmed hardware & product listing

- ESP32-S3 DevKitC-1 N16R8
- CC1101 433 MHz module
- F66 handset/receiver system (FCC ID **2A6TK-F66**)
- Target Fan: **VonLuce 52-Inch Ceiling Fan** ([Amazon UK B0D6VMZ47L](https://www.amazon.co.uk/dp/B0D6VMZ47L))

## Version 4.5.0 Key Highlights

- **Active Fan State Tracking Model:** Provides a live state text sensor in Home Assistant (`ON | Speed 3 | Forward | Timer: 1H | Light: ON`).
- **Custom Material Design Icons:** Added crisp `mdi:` icons for all 15 primary remote buttons.
- **Clean Entity Categorization:** Grouped diagnostic and RF tuning controls (`config` and `diagnostic`) to keep the primary device card clutter-free.
- **Stock Home Assistant Native Tile Grid:** Included copy-paste dashboard card configuration matching the 3-column physical remote handset layout without requiring any extra HACS plugins.
- **Flipper Zero SubGHz Dumps:** Raw `.sub` capture files included for direct Flipper Zero transmission.
- **Strict RF Rules Preserved:** 100% untouched literal waveform timing data.

## Verified controls

Power, Fan, Speed 1–6, R/L (Forward/Reverse), 1H, 2H, 4H, 8H, Light On, and Light Off.
