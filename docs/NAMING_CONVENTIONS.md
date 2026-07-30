# Naming Conventions

These names are canonical from v1.0.1 onward.

## Project and release names

- Project display name: `F66 Ceiling Fan Controller`
- Repository name: `f66-ceiling-fan-controller`
- ESPHome node name: `f66-ceiling-fan-controller`
- ESPHome friendly name: `F66 Ceiling Fan Controller`
- Git tag format: `vMAJOR.MINOR.PATCH`, for example `v1.0.1`
- Release folder format: `releases/vMAJOR.MINOR.PATCH/`
- Release firmware filename: `f66-controller-vMAJOR.MINOR.PATCH.yaml`
- Release dashboard filename: `mushroom-card-vMAJOR.MINOR.PATCH.yaml`

Do not use `PRODUCTION`, `STABLE`, `TEST-RF`, or ad-hoc suffixes in current release filenames. Those names remain only in `archive/legacy/` to preserve history.

## Active files

The current editable files always use version-neutral names:

- `esphome/f66-controller.yaml`
- `home-assistant/mushroom-card.yaml`

A release is made by copying those files into its versioned folder without changing behavior.

## Home Assistant entities

ESPHome entity display names begin with `F66`, for example:

- `F66 Power Off`
- `F66 Speed 1`
- `F66 Timer 1 Hour`
- `F66 Temperature`

The supplied dashboard currently targets the entity IDs verified in the production Home Assistant installation:

- Device prefix: `bedroom_f66_ceiling_fan_controller`
- Example: `button.bedroom_f66_ceiling_fan_controller_f66_power_off`

Home Assistant may create different entity IDs on another installation. Entity IDs are installation-specific and are not protocol constants. Before installing the dashboard elsewhere, confirm the actual IDs in **Settings → Devices & services → Entities** and update only the `entity:` and `entity_id:` values in the dashboard YAML.

Do not rename the ESPHome node or its entities in an existing installation unless a Home Assistant migration is planned, because doing so can create new entity IDs and break dashboards or automations.

## Command labels

Use these exact human-facing labels:

- Light On
- Light Off
- Power Off
- Speed 1 through Speed 6
- Breeze
- Reverse Direction
- Timer 1 Hour
- Timer 2 Hours
- Timer 4 Hours
- Timer 8 Hours

## Versioning rules

Semantic versioning is used:

- Patch: documentation, naming, tests, or bug fixes that do not intentionally change the protocol or user-facing command set.
- Minor: backward-compatible features.
- Major: incompatible changes, protocol redesign, or entity naming changes that require migration.

`v1.0.0` remains the first production-stable hardware-verified baseline. `v1.0.1` aligns naming and documentation while preserving RF behavior.
