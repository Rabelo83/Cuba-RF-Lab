# Blueprints

<span class="status-badge status-warning">No approved blueprints yet</span>

The project is intentionally not jumping straight to final fabrication dimensions. Blueprints move through documented status levels.

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
- testing procedure
- revision history

If it has not been field tested, it must say:

```text
NOT FIELD VALIDATED
```

## Repository Locations

- [Draft blueprints](https://github.com/Rabelo83/ETECSA-RF-Lab/tree/main/blueprints/draft)
- [Approved blueprints](https://github.com/Rabelo83/ETECSA-RF-Lab/tree/main/blueprints/approved)
- [Antenna design folders](https://github.com/Rabelo83/ETECSA-RF-Lab/tree/main/antenna)
- [Coupler design folders](https://github.com/Rabelo83/ETECSA-RF-Lab/tree/main/coupler)

