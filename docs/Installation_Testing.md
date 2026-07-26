# Installation and Test Checklist

## Before flashing

- Confirm the board is an ESP32-S3 DevKitC-1.
- Confirm the CC1101 module is suitable for 433 MHz.
- Verify every connection against `Hardware.md`.
- Power the CC1101 from 3.3 V.
- Put Wi-Fi credentials in `secrets.yaml`.

## ESPHome validation

Use the normal ESPHome workflow for your installation:

```bash
esphome config firmware/F66-production-v4.yaml
esphome run firmware/F66-production-v4.yaml
```

The exact commands may differ if ESPHome is running as a Home Assistant add-on or container.

## First boot

Expected entities include:

- Controller Status
- RF Status
- RF Transmission Profile
- RF Frequency
- RF CC1101 Symbol Rate
- RF Repeat Count
- RF TX Settling
- the 15 remote buttons
- Restart Ceiling Fan Controller

Expected RF status after boot:

```text
READY - literal captured frames
```

## Functional test

With the intended fan powered, test in this order:

- [ ] Power
- [ ] Fan
- [ ] Speed 1
- [ ] Speed 2
- [ ] Speed 3
- [ ] Speed 4
- [ ] Speed 5
- [ ] Speed 6
- [ ] R/L
- [ ] 1H
- [ ] 2H
- [ ] 4H
- [ ] 8H
- [ ] Light On
- [ ] Light Off

Keep the verified defaults during this test.

## Recommended Home Assistant Dashboard Card (Native Tile Grid)

Add this YAML snippet to your Home Assistant Dashboard to create a 3-column remote control tile card matching the physical handset:

```yaml
type: vertical-stack
title: F66 Ceiling Fan Controller
cards:
  - type: entity
    entity: text_sensor.active_fan_state
    name: Current Status
    icon: mdi:fan-clock

  - type: grid
    columns: 2
    square: false
    cards:
      - type: tile
        entity: button.power
        name: Power
        icon: mdi:power
      - type: tile
        entity: button.fan
        name: Fan
        icon: mdi:fan

  - type: grid
    columns: 3
    square: false
    cards:
      - type: tile
        entity: button.speed_1
        name: Speed 1
      - type: tile
        entity: button.speed_2
        name: Speed 2
      - type: tile
        entity: button.speed_3
        name: Speed 3
      - type: tile
        entity: button.speed_4
        name: Speed 4
      - type: tile
        entity: button.speed_5
        name: Speed 5
      - type: tile
        entity: button.speed_6
        name: Speed 6

  - type: grid
    columns: 3
    square: false
    cards:
      - type: tile
        entity: button.r_l
        name: Reverse (F/R)
        icon: mdi:rotate-3d-variant
      - type: tile
        entity: button.light_on
        name: Light On
        icon: mdi:lightbulb-on
      - type: tile
        entity: button.light_off
        name: Light Off
        icon: mdi:lightbulb-off

  - type: grid
    columns: 4
    square: false
    cards:
      - type: tile
        entity: button.1h
        name: 1H Timer
      - type: tile
        entity: button.2h
        name: 2H Timer
      - type: tile
        entity: button.4h
        name: 4H Timer
      - type: tile
        entity: button.8h
        name: 8H Timer
```


## Failure checks

If no controls work:

- verify 3.3 V and ground
- check SCK/MOSI/MISO/CS wiring
- confirm GDO0 is on GPIO14
- confirm the module is a 433 MHz CC1101
- inspect ESPHome logs for CC1101 initialisation errors
- test at close range
- check the antenna

If only some controls fail, restore the original V4 file and compare its SHA-256 with the value in the README. Partial failures usually suggest that waveform data or button-to-frame mapping was changed.
