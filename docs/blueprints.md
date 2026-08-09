# Blueprints

<span class="status-badge status-warning">No approved blueprints yet</span>

The project is intentionally not jumping straight to final fabrication dimensions. Blueprints move through documented status levels.

Blueprints are not only technical drawings. A public-ready blueprint must also show how the design can be built at low cost, repaired, and adapted with locally available materials.

## Status Levels

| Status | Meaning |
| --- | --- |
| CONCEPT | Idea or topology under discussion. |
| CALCULATED | Key dimensions and assumptions calculated. |
| SIMULATED | Modeled with documented tool, geometry, and assumptions. |
| PROTOTYPE | Built or ready for prototype construction. |
| FIELD_TESTED | Tested in real conditions with stored measurements. |
| APPROVED | Reviewed design with required evidence and limitations. |

## Current Blueprint State

| Area | Current Status | Public Note |
| --- | --- | --- |
| Broadband LPDA | CONCEPT | Preliminary numbers are not approved build data. |
| 1800 MHz Yagi | CONCEPT | Depends on LTE Band 3 availability during useful outage windows. |
| 900 MHz Yagi | CONCEPT | Depends on local low-band blackout measurements. |
| Passive phone coupler | CONCEPT | Needs fixture design and repeatable position sweeps. |

For plain-language build paths, use [Keep It Simple](keep-it-simple.md). That section avoids RF math and shows only the simple blueprint, materials, and build/test steps for each project path.

For antenna topology selection, use [Antenna Selection](antenna-selection.md). The LPDA is one candidate only, not the default winner.

## Public Blueprint Rule

Every public blueprint must include:

- title
- version
- status
- author or AI
- date
- assumptions
- target bands
- materials
- dimensions
- RF calculations
- simulation method and results
- expected impedance or matching behavior
- mechanical notes
- construction tolerance
- weatherproofing
- limitations
- production cost estimate
- required versus optional parts
- local substitutes
- repair notes
- testing procedure
- revision history

Antenna blueprints must also include topology comparison against competing antenna candidates and a written selection reason in `DECISIONS.md`.

If it has not been field tested, it must say:

```text
NOT FIELD VALIDATED
```

## Repository Locations

- [Draft blueprints](https://github.com/Rabelo83/Cuba-RF-Lab/tree/main/blueprints/draft)
- [Approved blueprints](https://github.com/Rabelo83/Cuba-RF-Lab/tree/main/blueprints/approved)
- [Antenna design folders](https://github.com/Rabelo83/Cuba-RF-Lab/tree/main/antenna)
- [Coupler design folders](https://github.com/Rabelo83/Cuba-RF-Lab/tree/main/coupler)
