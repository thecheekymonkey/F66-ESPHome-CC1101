# Testing

## Automated tests

Run from the repository root:

```bash
python3 tests/test_protocol.py
python3 scripts/check_release.py
```

These tests verify frame length, prefix, command width, parity, unique command values, expected vectors and required stateless dashboard entities.

## ESPHome validation

With ESPHome installed:

```bash
esphome config esphome/f66-controller.yaml
esphome compile esphome/f66-controller.yaml
```

The Wi-Fi secrets must be available to ESPHome.

## Home Assistant checks

- Reload or restart ESPHome integration after flashing.
- Confirm all dedicated button entities exist.
- Confirm the Mushroom card shows no missing entities.
- Confirm every dashboard action calls `button.press`.

## Physical command test

Watch ESPHome logs and verify a `F66 TX:` line appears for every press.

Test each command once, then test repeated identical presses:

- Power Off twice while HA already displays Off
- Each speed twice
- Breeze twice
- Each timer twice
- Light On twice
- Light Off twice
- Reverse twice, noting that two presses should return physical direction to its starting direction

A release is not hardware-verified until a human completes these tests on the actual fan.
