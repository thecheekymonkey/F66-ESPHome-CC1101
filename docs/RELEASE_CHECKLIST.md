# v1.0.1 Release Checklist

## Repository

- [ ] Existing GitHub repository backed up
- [ ] Current commit hash recorded
- [ ] Work performed on a new branch
- [ ] Legacy files preserved under `archive/legacy/`
- [ ] No secrets committed

## Software

- [ ] `python3 tests/test_protocol.py` passes
- [ ] `python3 scripts/check_release.py` passes
- [ ] ESPHome configuration validates
- [ ] ESPHome firmware compiles
- [ ] Dashboard YAML loads without missing entities

## Device

- [ ] ESP32-S3 boots
- [ ] CC1101 initializes
- [ ] BME680 sensors update
- [ ] Every button creates an RF transmission log
- [ ] All 15 verified RF commands work physically
- [ ] Repeated identical commands transmit and work

## Release

- [ ] Version is `1.0.0` in firmware and documentation
- [ ] Full diff reviewed by a human
- [ ] Pull request merged only after physical verification
- [ ] Git tag `v1.0.1` created
- [ ] GitHub release created using `releases/v1.0.1/`
