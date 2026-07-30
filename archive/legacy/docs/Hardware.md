# Hardware and Wiring

## Tested platform

- **Microcontroller:** ESP32-S3 DevKitC-1 N16R8
- **Radio:** CC1101 module intended for the 433 MHz band
- **Fan remote:** F66, FCC ID 2A6TK-F66
- **Target fan product:** VonLuce 52-Inch Ceiling Fan with Dimmable Light ([Amazon UK link](https://www.amazon.co.uk/dp/B0D6VMZ47L), ASIN `B0D6VMZ47L`)


## Pin assignment

| Function | ESP32-S3 pin | CC1101 pin |
|---|---:|---|
| SPI clock | GPIO12 | SCK |
| SPI MOSI | GPIO11 | MOSI/SI |
| SPI MISO | GPIO13 | MISO/SO |
| Chip select | GPIO10 | CS/CSN |
| Transmit signal | GPIO14 | GDO0 |
| Receive signal | GPIO9 | GDO2 |
| Power | 3V3 | VCC |
| Ground | GND | GND |

This is the wiring used by the verified firmware. Do not alter it while validating the release.

![ESP32-S3 DevKitC-1 with CC1101 Prototype](../images/ESP32%20PROTOTYPE.jpg)

![CC1101 Wireless Module Pinout & Schematic](../images/C1101%20PINOUT.png)


## Reserved I²C pins

The production firmware reserves:

- GPIO4 — SDA
- GPIO5 — SCL

These pins are intended for a future BME680 environmental sensor. No I²C component is enabled in version 4.0.0.

## Power and signal levels

The ESP32-S3 and CC1101 use 3.3 V logic. The radio module must not be powered from 5 V unless the specific board explicitly includes suitable regulation and level shifting.

Use short SPI wiring where practical. Poor grounding, long jumper wires, weak 3.3 V supplies, and unsuitable antennas can all reduce RF reliability.

## CC1101 board variations

Low-cost modules are sold with different crystal frequencies, RF matching networks, pin orders, and antenna arrangements. Confirm that the module is intended for 433 MHz and check the printed pin labels rather than relying on the physical order shown in online photographs.

## Installation location

A ceiling-fan controller may be placed near mains wiring. The ESP32 and CC1101 are low-voltage electronics and must be housed, powered, and separated from mains conductors appropriately. This repository does not provide a mains power-supply design.
