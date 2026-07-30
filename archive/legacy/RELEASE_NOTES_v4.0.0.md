# F66 Ceiling Fan Controller v4.0.0

This is the first production release of the ESPHome F66 ceiling-fan controller.

## Confirmed hardware

- ESP32-S3 DevKitC-1 N16R8
- CC1101 433 MHz module
- F66 handset/receiver system, FCC ID 2A6TK-F66

## Verified controls

Power, Fan, Speed 1–6, R/L, 1H, 2H, 4H, 8H, Light On and Light Off.

## Implementation

The firmware transmits literal RF waveforms captured from the original remote. This was selected after generated protocol frames failed despite apparently correct command values.

## Production improvements

- cleaner naming and comments
- INFO-level logging
- streamlined maintenance interface
- GPIO4 and GPIO5 reserved for future BME680 support
- no changes to the verified waveform data

## Known limitations

- one-way RF commands provide no receiver state feedback
- multi-fan addressing has not yet been characterised
- BME680 support is planned but not included
