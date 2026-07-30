# F66 RF Protocol

This document is the canonical protocol description for the verified controller.

## Radio profile

- Frequency: **433.920 MHz**
- Modulation: **ASK/OOK**
- CC1101 symbol rate setting: **2400 baud**
- CC1101 filter bandwidth: **200 kHz**
- Output power: **10 dBm setting**
- Default repeats: **4**
- TX settling delay: **1000 µs**

## Frame structure

Each transmitted frame contains exactly **30 bits**, sent most-significant bit first:

| Bits | Width | Meaning |
|---|---:|---|
| 0–19 | 20 | Fixed receiver/address prefix |
| 20–28 | 9 | Command value |
| 29 | 1 | Even-parity bit |

Fixed prefix:

```text
00000101011001011101
```

The command is masked to 9 bits (`0x000`–`0x1FF`).

### Canonical Command Values

| Function | Decimal | Hex | Frame | Parity |
|---|---:|---:|---|---:|
| Power Off | 401 | `0x191` | `000001010110010111011100100011` | 1 |
| Speed 1 | 488 | `0x1E8` | `000001010110010111011111010000` | 0 |
| Speed 2 | 456 | `0x1C8` | `000001010110010111011110010001` | 1 |
| Speed 3 | 425 | `0x1A9` | `000001010110010111011101010010` | 0 |
| Speed 4 | 393 | `0x189` | `000001010110010111011100010011` | 1 |
| Speed 5 | 362 | `0x16A` | `000001010110010111011011010100` | 0 |
| Speed 6 | 330 | `0x14A` | `000001010110010111011010010101` | 1 |
| Breeze | 267 | `0x10B` | `000001010110010111011000010111` | 1 |
| Reverse Direction | 299 | `0x12B` | `000001010110010111011001010110` | 0 |
| Light On | 244 | `0x0F4` | `000001010110010111010111101000` | 0 |
| Light Off | 307 | `0x133` | `000001010110010111011001100110` | 0 |
| Timer 1 hour | 149 | `0x095` | `000001010110010111010100101011` | 1 |
| Timer 2 hours | 338 | `0x152` | `000001010110010111011010100101` | 1 |
| Timer 4 hours | 433 | `0x1B1` | `000001010110010111011101100010` | 0 |
| Timer 8 hours | 464 | `0x1D0` | `000001010110010111011110100001` | 1 |


## Parity

The final bit makes the number of `1` bits across the complete 30-bit frame even.

Implementation rule:

```text
parity = popcount(prefix + command) mod 2
```

Therefore:

- an odd number of ones before parity produces parity `1`;
- an even number of ones before parity produces parity `0`.

## Pulse encoding

Each bit consists of a positive pulse followed by a negative space:

| Bit | Positive pulse | Negative space |
|---|---:|---:|
| 0 | 380 µs | 1100 µs |
| 1 | 1100 µs | 380 µs |

The last bit uses a **6000 µs negative inter-frame gap** instead of its normal space.

The complete frame is repeated four times by default.

## Bit order

- Prefix: bit 19 down to bit 0
- Command: bit 8 down to bit 0
- Parity: final bit

## Source of truth

The implementation in `esphome/f66-controller.yaml`, the vectors in `tests/command_vectors.json`, and physically verified fan behavior must agree. A change to any protocol constant requires updated tests and fresh physical verification.
