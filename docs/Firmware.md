# Firmware Guide

## Release file

`firmware/F66-production-v4.yaml`

Version 4.5.0 is the production build enhanced with active state tracking and Home Assistant UI polish.

## Structure

The firmware contains:

- ESP32-S3 and network configuration
- SPI and CC1101 configuration
- ESPHome remote transmitter and receiver
- four runtime RF tuning values (categorized under `config`)
- status entities (`Controller Status`, `RF Status`, `RF Profile` categorized under `diagnostic`)
- `Active Fan State` text sensor for live state summary (`ON | Speed 3 | Forward | Timer: 1H | Light: ON`)
- one queued transmission script and one state update script
- 15 literal frame arrays
- 15 Home Assistant button entities with MDI icons
- one restart button
- comments reserving GPIO4/GPIO5 for future I²C use

## Immutable section

The arrays named `frame_0` through `frame_14` are verified waveform assets. Do not:

- round their timings
- replace them with nominal 380/1110 µs symbols
- regenerate them from the documented command values
- remove the measured inter-frame gaps
- change their order

A refactor is acceptable only if an automated comparison confirms that every signed timing value remains identical.

## Runtime tuning

The verified defaults are:

- 433.920 MHz
- 2400 baud
- four repeats
- 1000 µs TX settling

The select entities are retained to aid diagnosis with clone CC1101 modules and are categorized as `config` entities in Home Assistant. They reset to the verified defaults after restart because `restore_value` is disabled.

## Receive mode

After boot and after every transmission, the firmware returns the CC1101 to RX mode. Raw receive dumping remains enabled because it is useful for future handset captures. Production logging is set to INFO.

## Home Assistant state tracking model

Version 4.5.0 introduces a software state tracking model using ESPHome global variables (`state_power`, `state_speed`, `state_dir_forward`, `state_timer_hours`, `state_light`). Whenever a command button is pressed via Home Assistant or ESPHome, the state model updates immediately and publishes a formatted summary to the `Active Fan State` text sensor (`text_sensor.active_fan_state`).

## Future BME680

GPIO4 and GPIO5 are reserved for SDA and SCL. BME680 support should be introduced in a later, separately tested release. It must not modify the existing SPI or CC1101 pin assignments.

