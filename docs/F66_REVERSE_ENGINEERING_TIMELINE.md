# F66 Reverse Engineering Timeline

## Overview

This document records the major milestones in reverse engineering the VonLuce F66 RF protocol. It complements the protocol specification by explaining how the protocol was derived and which findings were experimentally verified.

## Phase 1 – RF Identification

The original handheld remote was analysed to determine the radio characteristics.

Confirmed:

- Frequency: 433.920 MHz
- Modulation: ASK / OOK
- Symbol rate: 2400 baud
- Receiver bandwidth: 200 kHz

## Phase 2 – Packet Structure

Captured transmissions showed a fixed-length frame.

The packet format was determined to be:

- 20-bit fixed prefix
- 9-bit command
- 1 parity bit

Total frame length: 30 bits

## Phase 3 – Frame Validation

Known remote buttons were decoded repeatedly until every command generated identical frames.

Confirmed commands included:

- Fan speeds
- Fan Off
- Light On
- Light Off
- Breeze
- Reverse
- Sleep timers

Parity was verified as even parity across the complete frame.

## Phase 4 – ESPHome Implementation

A native ESPHome implementation was produced using:

- ESP32-S3
- CC1101
- Remote Transmitter (RMT)

The packet builder reconstructs frames from:

- 20-bit prefix
- 9-bit command
- calculated parity

rather than storing complete packets.

## Phase 5 – Production Verification

Known commands were verified against the spare receiver.

Confirmed working:

- Speed 1–6
- Fan Off
- Light On
- Light Off
- Breeze
- Reverse
- Timer 1h / 2h / 4h / 8h

## Phase 6 – Complete Command Sweep

A temporary command-stepper was added to the TEST-RF firmware.

Every value from 0 through 511 was transmitted using the verified production packet builder.

Results:

- 15 known commands responded.
- 497 remaining values produced no observable response during normal operation.

No protocol parameters were changed during testing.

## Conclusions

The known command table is considered complete for normal operation.

Future investigation, if required, should focus on:

- alternative prefixes
- pairing behaviour
- manufacturing/programming modes
- command sequences
- power-on windows

rather than further brute-force testing of the existing 9-bit command field.
