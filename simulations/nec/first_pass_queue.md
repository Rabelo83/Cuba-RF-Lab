# NEC First-Pass Simulation Queue

Status: queue ready, solver not installed locally

Date: 2026-08-09

Local check on 2026-08-09 did not find `xnec2c`, `nec2c`, or `openEMS` installed. This file defines the first simulation pass so a solver can be installed later without changing the engineering target.

## Input Geometry

Use:

- `calculations/preliminary_antenna_geometry.py`
- `calculations/preliminary_antenna_geometry.md`
- `data/processed/antenna_candidate_first_pass.csv`

All values are pre-simulation seeds only. They are not final dimensions.

## Simulation Order

| Priority | Candidate | Reason |
| ---: | --- | --- |
| 1 | Y900_5EL_SEED | Primary lower-band, simpler and cheaper than 7-element version. |
| 2 | Y1800_5EL_SEED | Compact LTE Band 3 candidate; useful cost/size comparison. |
| 3 | Y900_7EL_SEED | Tests whether extra 900 MHz gain margin is worth size and tolerance cost. |
| 4 | Y1800_7EL_SEED | Tests whether high-band passive-chain margin can beat phone-at-RF-location. |
| 5 | LPDA_800_2200_SEED | Band-uncertainty hedge; must prove complexity is justified. |
| 6 | BIQUAD_1800_SEED | Simple compact high-band reference. |
| 7 | BIQUAD_2100_SEED | Secondary high-band reference for broadband awareness. |

## Frequency Sweeps

| Candidate family | Sweep | Check points |
| --- | --- | --- |
| 900 MHz Yagi | 880-960 MHz, 5 MHz step | 900, 925, 945, 960 MHz |
| 1800 MHz Yagi | 1710-1880 MHz, 10 MHz step | 1710, 1800, 1840, 1880 MHz |
| LPDA | 800-2200 MHz, 25 MHz step | 800, 900, 1800, 2100, 2200 MHz |
| 1800 MHz biquad | 1710-1880 MHz, 10 MHz step | 1710, 1800, 1840, 1880 MHz |
| 2100 MHz biquad | 1920-2170 MHz, 10 MHz step | 1920, 2100, 2170 MHz |

## Material/Tolerance Sweeps

Run each practical wire/tube antenna with:

- conductor diameter: 4 mm, 6 mm, 8 mm for Yagi and LPDA where practical
- conductor diameter: 2 mm, 3 mm, 4 mm for biquad wire
- element length error: nominal, +1 mm, -1 mm, +3 mm, -3 mm
- element spacing error: nominal, +1 mm, -1 mm, +3 mm, -3 mm
- feed gap/matching assumption documented separately

## Required Outputs

For each candidate, save a summarized result in `simulations/results/` with:

- solver and version
- model file path
- target frequency sweep
- realized gain at required check points
- S11 or return loss
- VSWR
- feed-point impedance
- front-to-back ratio
- horizontal pattern
- vertical pattern
- half-power beamwidth
- polarization
- efficiency estimate
- construction tolerance sensitivity
- feed and matching notes
- net passive-chain estimate after coax, connector, matching, passive-coupler, and miscellaneous losses
- comparison against phone-at-RF-location

## Stop Conditions

Stop advancing a candidate if simulation shows:

- poor match that cannot be solved with a simple, low-cost feed
- gain too low to survive the passive-chain losses
- beamwidth too narrow for practical aiming by non-specialists
- construction tolerance too tight for ordinary tools
- material or feed complexity too high for low-cost public fabrication

Any candidate that fails should remain documented; failed candidates help prevent repeated work.
