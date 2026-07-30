# Reverse-Engineering History

## Goal

Replace an F66 433 MHz ceiling-fan handset with an ESP32-S3 and CC1101 so every original function could be exposed in Home Assistant.

## Investigation

Several approaches were tried:

1. Generic SmartRC-style decoding
2. Manual CC1101 register configuration
3. Normalised short/long timing reconstruction
4. Generated 29-bit command frames
5. A guessed thirtieth framing bit
6. Frequency and timing sweeps
7. Literal replay of a measured frame

The command payloads appeared consistent and repeatable, but generated transmissions did not operate the fan.

![Flipper Zero Spectrum Analyzer Measuring 433.92 MHz AM650](../images/FLIPPER%20SPECTRUM%20ANALYSER.jpg)


## Breakthrough

A test control named **RF Speed 1 Literal Measured** replayed the exact recorded pulse durations. It worked immediately.

That isolated the problem:

- the ESP32-to-CC1101 wiring was correct
- the carrier and modulation settings were correct
- the selected command was correct
- the generated framing reconstruction was wrong

Analysis of the raw captures then established the observed final bit for all 15 commands. It did not follow the previously assumed “inverse of the final data bit” rule.

## Engineering decision

Rather than invent an unproven decoder/encoder, the project adopted literal waveform replay.

This is less elegant than a fully characterised protocol, but it is the most faithful and testable implementation. The exact waveforms are small, deterministic, and verified against hardware.

## Result

The following controls were tested successfully:

- Power
- Fan
- Speed 1 through Speed 6
- Reverse/left (`R/L`)
- Timers: 1H, 2H, 4H and 8H
- Light On
- Light Off

Version 4.0.0 cleaned the working firmware without changing the waveform data and was then confirmed working.

## Lessons learned

- A plausible bitstream is not necessarily a valid over-the-air frame.
- Footer, parity, checksum, or framing assumptions must be verified experimentally.
- Literal replay is a legitimate production strategy when the protocol is only partly understood and the captured command set is small.
- Known-good RF timing data should be treated like a binary asset: preserve it exactly.
- Testing one isolated variable at a time was what revealed the real fault.
