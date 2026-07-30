#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "command_vectors.json").read_text())
PREFIX = DATA["prefix"]


def build_frame(command: int) -> str:
    assert 0 <= command <= 0x1FF
    body = PREFIX + f"{command:09b}"
    parity = body.count("1") % 2
    return body + str(parity)


def main() -> None:
    assert len(PREFIX) == 20
    assert set(PREFIX) <= {"0", "1"}

    seen = set()
    for name, vector in DATA["commands"].items():
        command = vector["decimal"]
        assert command not in seen, f"Duplicate command: {name}={command}"
        seen.add(command)
        frame = build_frame(command)
        assert len(frame) == 30, name
        assert frame == vector["frame"], f"Vector mismatch: {name}"
        assert frame.count("1") % 2 == 0, f"Odd parity: {name}"
        assert int(vector["hex"], 16) == command, f"Hex mismatch: {name}"

    print(f"PASS: {len(seen)} command vectors, 30-bit frames, even parity")


if __name__ == "__main__":
    main()
