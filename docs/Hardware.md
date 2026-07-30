# Hardware

## Controller

- ESP32-S3 DevKitC-1
- CC1101 RF module
- BME680 environmental sensor

## Pin assignments

### CC1101 SPI

| Signal | ESP32-S3 pin |
|---|---|
| SCLK | GPIO12 |
| MOSI | GPIO11 |
| MISO | GPIO13 |
| CS | GPIO10 |
| RF data / remote transmitter | GPIO14 |

### BME680 I²C

| Signal | ESP32-S3 pin |
|---|---|
| SDA | GPIO4 |
| SCL | GPIO5 |
| Address | `0x77` |

## Radio configuration

- Frequency: 433.92 MHz
- ASK/OOK modulation
- 2400 baud symbol-rate setting
- 200 kHz filter bandwidth
- Output-power setting: 10

Use a suitable 433 MHz antenna and a stable power supply. Confirm the CC1101 module voltage requirements before wiring; do not assume all breakout boards tolerate 5 V logic or supply.
