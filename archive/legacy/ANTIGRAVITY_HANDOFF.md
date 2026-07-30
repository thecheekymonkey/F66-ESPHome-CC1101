# Antigravity Handoff

This folder is ready to be published as a new GitHub repository.

## Confirmed facts

- Product: F66 ceiling-fan remote, FCC ID 2A6TK-F66
- Fan Listing: VonLuce 52-Inch Ceiling Fan ([Amazon UK B0D6VMZ47L](https://www.amazon.co.uk/dp/B0D6VMZ47L))
- Hardware: ESP32-S3 DevKitC-1 N16R8 plus CC1101

- Production firmware: `firmware/F66-production-v4.yaml`
- Version: 4.5.0
- Status: every exposed control tested successfully
- Firmware SHA-256: `ef5f8cb16de8fbe65880108bb56e23ac9aa63a31ef7f5afe36b04988c73dcab0`
- Licence selected: MIT
- BME680: planned only; GPIO4/GPIO5 reserved, not enabled
- Multi-fan addressing: not yet determined

## Do not change before first publication

1. Do not alter any `frame_0` through `frame_14` timing values.
2. Do not regenerate the waveforms from the documented command values.
3. Do not claim multi-fan compatibility.
4. Do not claim that the final framing bit algorithm is understood.
5. Do not add BME680 code to the 4.5.0 release.
6. Do not expose Wi-Fi credentials or a real `secrets.yaml`.

## Suggested repository name

`F66-ESPHome-CC1101`

## Suggested description

> Home Assistant control for an F66 433 MHz ceiling fan using ESPHome, ESP32-S3 and CC1101, with verified literal RF replay.

## Publishing order

1. Create a public GitHub repository named `F66-ESPHome-CC1101`.
2. Upload the complete contents of this directory, preserving paths.
3. Use `main` as the default branch.
4. Make the commit:

   ```text
   Release verified F66 ESPHome controller v4.5.0
   ```

5. Confirm GitHub renders the root README correctly.
6. Create a release tag:

   ```text
   v4.5.0
   ```

7. Create a GitHub release titled:

   ```text
   F66 Ceiling Fan Controller v4.5.0
   ```

8. Use the contents of `RELEASE_NOTES_v4.5.0.md` as the release description.
9. Attach `firmware/F66-production-v4.yaml` to the release.
10. Do not publish any local `secrets.yaml`, build directory, or ESPHome credentials.


## Included optional assets

- [x] Photographs of handset, ESP32 prototype setup, spectrum analyzer, and HA dashboard (`images/`)
- [x] CC1101 wiring schematic & pinout diagram (`images/C1101 PINOUT.png`)
- [x] Raw Flipper `.sub` captures and button press sequence (`subghz/`)
- [ ] Captures from the two additional handsets
- [ ] The GitHub username/credit line
- [ ] Enclosure and power-supply details


## Final integrity check

Before publishing, verify:

```bash
sha256sum firmware/F66-production-v4.yaml
```

Expected:

```text
ef5f8cb16de8fbe65880108bb56e23ac9aa63a31ef7f5afe36b04988c73dcab0
```
