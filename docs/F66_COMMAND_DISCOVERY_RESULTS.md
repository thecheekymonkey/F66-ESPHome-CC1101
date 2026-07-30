# F66 RF Command Discovery Results

## Status

Command exploration complete.

The complete 9-bit command space (0 through 511) was tested on the spare F66 receiver using the existing, verified ESPHome/CC1101 transmission path.

Only the 15 already-known commands produced a response. All other command values were ignored by the receiver during normal operation.

## Test Hardware

- ESP32-S3 DevKitC-1
- CC1101 at 433.920 MHz
- ASK/OOK modulation
- Existing ESPHome `send_f66` packet builder
- Spare F66 fan receiver/controller
- Native Home Assistant test controls

The test harness reused the same RF path as the working production-style controls. Known commands such as Light On and Light Off continued to work during testing, confirming that the transmitter, packet builder, radio settings, and receiver were operational.

## Test Method

A temporary Home Assistant command-stepper was added to the TEST-RF ESPHome configuration.

The tester provided:

- A command number selector covering 0 through 511
- Send Current Command
- Previous Command
- Next Command
- A one-click step-and-transmit control

Each command used the existing F66 frame builder:

- Fixed 20-bit receiver/address prefix
- 9-bit command field
- Even parity
- 30-bit total frame
- Existing pulse timings
- Existing repeat count
- Existing CC1101 configuration

No protocol constants were changed during the command sweep.

## Confirmed Commands

| Decimal | Hex | Function |
|---:|---:|---|
| 149 | `0x095` | Timer 1 hour |
| 244 | `0x0F4` | Light On |
| 267 | `0x10B` | Breeze |
| 299 | `0x12B` | Reverse Direction |
| 307 | `0x133` | Light Off |
| 330 | `0x14A` | Speed 6 |
| 338 | `0x152` | Timer 2 hours |
| 362 | `0x16A` | Speed 5 |
| 393 | `0x189` | Speed 4 |
| 401 | `0x191` | Fan Off |
| 425 | `0x1A9` | Speed 3 |
| 433 | `0x1B1` | Timer 4 hours |
| 456 | `0x1C8` | Speed 2 |
| 464 | `0x1D0` | Timer 8 hours |
| 488 | `0x1E8` | Speed 1 |

## Result

The following user-facing functions are confirmed:

- Fan Off
- Speeds 1 through 6
- Breeze mode
- Reverse direction toggle
- Light On
- Light Off
- Sleep timers: 1, 2, 4, and 8 hours

No additional normal-operation functions were discovered.

The receiver appears to validate the command field against a fixed list of supported values and silently ignore all other 9-bit command values.

## Interpretation

This result strongly suggests that the F66 receiver does not expose a larger set of hidden features through unused values in the existing 9-bit command field.

Potential behaviours outside the scope of this sweep could still theoretically require:

- A different receiver/address prefix
- A special command sequence
- A long-press or repeated-command pattern
- A power-on or pairing window
- Factory or programming conditions

There is currently no evidence that any such behaviours are required for normal fan operation.

## Recommended Repository State

The 15 confirmed commands should remain the authoritative production command table.

The temporary command-stepper may be:

- Kept only in the isolated TEST-RF lab configuration for future investigation; or
- Removed after this result is committed.

It should not be added to the production controller unless a manual raw-command diagnostic is intentionally desired.

## Final Conclusion

The normal F66 command set is considered complete:

- 15 confirmed commands; no response from the remaining 497 values.
- Further brute-force testing of the same 9-bit command field is not recommended unless new evidence suggests a different prefix, sequence, or receiver mode.
