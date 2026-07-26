# Contributing

Hardware verification is more valuable than speculative protocol changes.

When proposing a firmware change:

1. Preserve the original V4 waveform arrays unless the change is explicitly a new capture profile.
2. State the exact ESP32 and CC1101 hardware used.
3. Test all 15 commands against a real receiver.
4. Document any altered RF setting.
5. Do not describe an inferred checksum, address, or framing rule as confirmed without comparative captures.

For new fan profiles, include repeated captures of at least one identical button press and explain how the handset/receiver pair was identified.
