# Architecture and Design Rules

## Generated packets, not replay

Early versions replayed captured pulse arrays. Production generates the packet from a fixed prefix, command value and calculated parity. This is easier to audit, maintain and test.

## One-way RF means optimistic state

The receiver provides no state feedback. Home Assistant can only remember commands sent by this controller. It cannot know about commands sent by the OEM remote or missed RF transmissions.

Consequences:

- Home Assistant state is not authoritative.
- Reverse cannot expose an absolute forward/reverse state because its RF command toggles direction.
- Light On and Light Off remain separate actions.
- The dashboard must not depend on a remembered state to decide whether to transmit.

## Stateless dashboard controls

Every human-facing RF action in the v1.0.0 dashboard calls an ESPHome template button through `button.press`.

This avoids suppression of repeated commands that can occur with:

- `fan.turn_off` when HA already shows Off;
- `fan.set_percentage` when the same speed is selected again;
- `fan.set_preset_mode` when Breeze is already selected;
- stateful timer selections.

The native fan and sleep-timer entities remain for compatibility and diagnostics, but the supplied dashboard does not use them for command buttons.

## Authority order

When project sources disagree, use this order:

1. Physical behavior verified on the fan
2. Known-good v1.0.0 release files
3. Captured RF evidence
4. Automated protocol vectors
5. Protocol documentation
6. Other repository code
7. AI-generated descriptions or comments
