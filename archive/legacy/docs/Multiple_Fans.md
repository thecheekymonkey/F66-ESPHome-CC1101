# Multiple Fan Support

## Current status

Version 4.0.0 contains the verified captures from one F66 handset/receiver pair.

Two additional fans are expected for other rooms. Their remotes must be measured before assuming that all F66 products use the same RF address or command set.

## Why different fans must be tested

If every receiver accepted the same fixed frames, nearby fans could respond together. The product must therefore distinguish installations somehow. Plausible mechanisms include:

- an address field embedded in the fixed command
- a factory-programmed command/address table
- a DIP-switch or solder-link configuration
- an undocumented learn/pairing sequence
- another receiver-side selection mechanism

No mechanism has yet been proven.

## Recommended commissioning procedure

For each new fan:

1. Label the handset and receiver by room before installation.
2. Keep only the fan under test powered where possible.
3. Capture the same simple control from each handset, preferably Speed 1.
4. Capture that control multiple times to confirm that it is stable.
5. Compare the raw timings and decoded bit patterns with the original capture.
6. Capture all 15 commands if the command set differs.
7. Create a separate firmware profile for that room.
8. Test for cross-control with the other fans powered.

## Likely firmware direction

If each remote has a unique fixed address, future firmware can store one 15-frame profile per fan. A single ESP32/CC1101 may then expose separate Home Assistant entities for each room, subject to RF range and simultaneous-transmission considerations.

Until those captures exist, multi-fan support remains planned rather than claimed.
