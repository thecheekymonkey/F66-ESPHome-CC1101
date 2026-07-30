#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FW = (ROOT / "esphome/f66-controller.yaml").read_text()
CARD = (ROOT / "home-assistant/mushroom-card.yaml").read_text()
REL_FW = (ROOT / "releases/v1.0.1/f66-controller-v1.0.1.yaml").read_text()
REL_CARD = (ROOT / "releases/v1.0.1/mushroom-card-v1.0.1.yaml").read_text()

assert "Version : v1.0.1" in FW
assert FW == REL_FW, "Release firmware differs from active firmware"
assert CARD == REL_CARD, "Release dashboard differs from active dashboard"
assert "fan.turn_off" not in CARD
assert "fan.set_percentage" not in CARD
assert "fan.set_preset_mode" not in CARD
assert "select.select_option" not in CARD
assert CARD.count("perform_action: button.press") == 15

required = [
    "F66 Power Off", "F66 Speed 1", "F66 Speed 2", "F66 Speed 3",
    "F66 Speed 4", "F66 Speed 5", "F66 Speed 6", "F66 Breeze",
    "F66 Reverse Direction", "F66 Light On", "F66 Light Off",
    "F66 Timer 1 Hour", "F66 Timer 2 Hours", "F66 Timer 4 Hours",
    "F66 Timer 8 Hours",
]
for name in required:
    assert f'name: "{name}"' in FW, f"Missing firmware button: {name}"

codes = re.findall(r"command_code:\s*(\d+)", FW)
assert len(set(codes)) >= 15
print("PASS: release files match; all 15 dashboard commands are stateless")
