# Verified F66 Commands

All commands below were carried into the production-stable firmware and treated as physically verified in this project conversation.

| Function | Decimal | Hex | Parity | Full 30-bit frame |
|---|---:|---:|---:|---|
| Power Off | 401 | `0x191` | 1 | `000001010110010111011100100011` |
| Speed 1 | 488 | `0x1E8` | 0 | `000001010110010111011111010000` |
| Speed 2 | 456 | `0x1C8` | 1 | `000001010110010111011110010001` |
| Speed 3 | 425 | `0x1A9` | 0 | `000001010110010111011101010010` |
| Speed 4 | 393 | `0x189` | 1 | `000001010110010111011100010011` |
| Speed 5 | 362 | `0x16A` | 0 | `000001010110010111011011010100` |
| Speed 6 | 330 | `0x14A` | 1 | `000001010110010111011010010101` |
| Breeze | 267 | `0x10B` | 1 | `000001010110010111011000010111` |
| Reverse Direction | 299 | `0x12B` | 0 | `000001010110010111011001010110` |
| Light On | 244 | `0x0F4` | 0 | `000001010110010111010111101000` |
| Light Off | 307 | `0x133` | 0 | `000001010110010111011001100110` |
| Timer 1 hour | 149 | `0x095` | 1 | `000001010110010111010100101011` |
| Timer 2 hours | 338 | `0x152` | 1 | `000001010110010111011010100101` |
| Timer 4 hours | 433 | `0x1B1` | 0 | `000001010110010111011101100010` |
| Timer 8 hours | 464 | `0x1D0` | 1 | `000001010110010111011110100001` |

## Command semantics

- **Power Off** is an absolute off command, not a toggle.
- **Reverse Direction** is a toggle; the controller cannot know the resulting absolute direction.
- **Light On** and **Light Off** are separate commands and must not be replaced by a Home Assistant toggle.
- Speeds and timers must remain directly callable even when the same command is pressed repeatedly.

Any pairing or light-colour captures remain experimental until separately decoded, documented and physically tested. They are not part of v1.0.0.
