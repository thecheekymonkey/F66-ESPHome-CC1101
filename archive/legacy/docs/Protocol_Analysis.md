# Protocol Analysis

## Confirmed radio configuration

| Property | Value |
|---|---|
| Carrier frequency | 433.920 MHz |
| Modulation | ASK/OOK |
| CC1101 symbol rate | 2400 baud |
| Filter bandwidth | 200 kHz |
| Output power | +10 dBm |
| Repeated frames | 4 |

Measured pulse families were approximately:

- short pulse: 380 µs
- long pulse: 1110 µs
- inter-frame gap: approximately 6.0–6.7 ms in the retained captures

The production firmware deliberately preserves the individual measured timings rather than replacing them with idealised values.

## Commands recovered during analysis

The following 29-bit values were associated with the controls. The final captured framing bit is listed separately because it is not reliably derived as the inverse of the last command bit.

| Function | Command | Captured final bit |
|---|---:|---:|
| Power | `0x0ACBB91` | 1 |
| Fan | `0x0ACBB0B` | 1 |
| Speed 1 | `0x0ACBBE8` | 0 |
| Speed 2 | `0x0ACBBC8` | 1 |
| Speed 3 | `0x0ACBBA9` | 0 |
| Speed 4 | `0x0ACBB89` | 1 |
| Speed 5 | `0x0ACBB6A` | 0 |
| Speed 6 | `0x0ACBB4A` | 1 |
| R/L | `0x0ACBB2B` | 0 |
| 1H | `0x0ACBA95` | 1 |
| 2H | `0x0ACBB52` | 1 |
| 4H | `0x0ACBBB1` | 0 |
| 8H | `0x0ACBBD0` | 1 |
| Light On | `0x0ACBAF4` | 0 |
| Light Off | `0x0ACBB33` | 0 |

## Important conclusion

The command values alone were not sufficient to reproduce a working transmission. A generated waveform using a guessed framing rule failed, while replaying the measured frame worked.

The final bit is therefore documented as observed data, not as a proven checksum, parity bit, inverse bit, or logical footer. The complete protocol structure remains partially unresolved.

## Production representation

Each button maps to one array of 60 signed pulse durations:

- positive values represent the active level
- negative values represent the inactive level
- each array includes the final inter-frame gap
- the selected array is appended four times by default

The arrays in the production YAML are the verified source of truth.

## Raw Flipper Zero captures

Raw SubGHz pulse captures (`.sub`) recorded with a Flipper Zero are preserved in the [`subghz/`](../subghz) directory:

- `subghz/ALL BUTTONS SEQUENTIALLY.sub`: Master capture of all 15 remote functions in sequence.
- `subghz/SPEED 1 BUTTON.sub`: Dedicated single-press capture of Speed 1.
- `subghz/SEQUENCE README.txt`: Chronological button mapping index.

## Addressing


Only one original handset/receiver pair has been fully captured. The common prefix visible in the recovered values may contain an address, family identifier, or fixed protocol field, but this has not yet been proven.

Captures from the two additional fan handsets will be compared before documenting an address layout.
