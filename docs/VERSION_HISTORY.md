# Version History

The older filenames were laboratory iteration numbers, not formal semantic releases. They are preserved unchanged under `archive/legacy/`.

| Legacy file | Milestone |
|---|---|
| `TEST-RF-v2-generated-test.yaml` | Early generated-packet testing |
| `TEST-RF-v3-generated-suite.yaml` | Expanded generated command suite |
| `TEST-RF-v4-generated-only.yaml` | Generated-only implementation |
| `TEST-RF-v5-parity-BME680.yaml` | Correct parity and BME680 integration |
| `TEST-RF-v6-compact-packet-builder.yaml` | Compact packet builder |
| `TEST-RF-v7-clean-layout.yaml` | Layout and entity cleanup |
| `TEST-RF-v8-native-entities.yaml` | Native Home Assistant entities |
| `F66-PRODUCTION-from-TEST-RF.yaml` | Production migration |
| `F66-PRODUCTION-v8.1-power-off-fix.yaml` | Dedicated stateless Power Off button |
| `F66-PRODUCTION-v8.2-all-stateless-controls.yaml` | All dashboard RF controls made stateless |

## Formal releases

### v1.0.0 — Production Stable

- Known-good behavior from legacy v8.2
- Formal semantic versioning begins
- Generated 30-bit packets with even parity
- All 15 verified commands included
- All dashboard RF actions use stateless buttons
- Protocol vectors and contributor rules added

Future versions:

- `1.0.x`: fixes that do not intentionally add protocol features
- `1.x.0`: backward-compatible features
- `2.0.0`: incompatible architecture, entity naming or protocol changes

### v1.0.1 — Naming and Documentation Alignment

- RF behavior unchanged from v1.0.0
- Current firmware comments no longer refer to the TEST-RF laboratory rig
- Canonical file, release, project and Home Assistant naming documented
- Installation-specific Home Assistant entity IDs explicitly identified
- Active and release files aligned to the same version convention
