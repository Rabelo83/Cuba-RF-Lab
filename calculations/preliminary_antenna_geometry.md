# Preliminary Antenna Geometry Seeds

Status: pre-simulation geometry worksheet

Date: 2026-08-09

These dimensions are for simulation setup only. They are not optimized, not matched, not field validated, and not approved blueprints.

Generated from:

`calculations/preliminary_antenna_geometry.py`

## Assumptions

- Free-space speed of light: 299792458 m/s.
- Yagi elements are full tip-to-tip element lengths.
- Yagi seeds use simple wavelength-scaled starting ratios, not an optimized design.
- LPDA seed uses tau = 0.86 and sigma = 0.16 only as a starting point.
- Biquad seeds list key dimensions; the full wire path still needs an EM model.
- Conductor diameter, boom coupling, feed gap, balun, matching, phone-coupler interaction, and nearby metal are not solved here.
- Simulations should sweep conductor diameters of 4 mm, 6 mm, and 8 mm where practical.

## Required Simulation Sweeps

| Candidate family | Minimum frequency sweep | Required check points |
| --- | --- | --- |
| 900 MHz Yagi | 880-960 MHz | 900, 925, 945, 960 MHz |
| 1800 MHz Yagi | 1710-1880 MHz | 1710, 1800, 1840, 1880 MHz |
| Broadband LPDA | 800-2200 MHz | 800, 900, 1800, 2100, 2200 MHz |
| 1800 MHz biquad | 1710-1880 MHz | 1710, 1800, 1840, 1880 MHz |
| 2100 MHz biquad | 1920-2170 MHz | 1920, 2100, 2170 MHz |

The passive architecture must consider both phone receive and phone uplink behavior because an ordinary phone still transmits normally into the cellular network. This project does not design active amplifiers or repeaters.

## Candidate Summary

| Candidate | Target MHz | Elements | Longest element mm | Boom / width mm | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| Y900_5EL_SEED | 900 | 5 | 173.2 | 266.5 | Compact 900 MHz class Yagi seed |
| Y900_7EL_SEED | 900 | 7 | 173.2 | 349.8 | Higher-gain 900 MHz class Yagi seed |
| Y1800_5EL_SEED | 1800 | 5 | 86.6 | 133.2 | Compact 1800 MHz class Yagi seed |
| Y1800_7EL_SEED | 1800 | 7 | 86.6 | 174.9 | Higher-gain 1800 MHz class Yagi seed |
| LPDA_800_2200_SEED | 800 | 9 | 178.0 | 142.6 | LPDA seed, tau=0.86, sigma=0.16, 9 elements |
| BIQUAD_1800_SEED | 1800 | 3 | 83.3 | 0.0 | Biquad seed dimensions; use full wire geometry in EM model |
| BIQUAD_2100_SEED | 2100 | 3 | 71.4 | 0.0 | Biquad seed dimensions; use full wire geometry in EM model |

## Y900_5EL_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| reflector | 0.0 | 173.2 |
| driven | 66.6 | 163.2 |
| director_1 | 133.2 | 154.9 |
| director_2 | 199.9 | 151.6 |
| director_3 | 266.5 | 148.2 |

## Y900_7EL_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| reflector | 0.0 | 173.2 |
| driven | 60.0 | 163.2 |
| director_1 | 113.3 | 154.9 |
| director_2 | 166.6 | 151.6 |
| director_3 | 223.2 | 148.2 |
| director_4 | 286.5 | 144.9 |
| director_5 | 349.8 | 141.6 |

## Y1800_5EL_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| reflector | 0.0 | 86.6 |
| driven | 33.3 | 81.6 |
| director_1 | 66.6 | 77.4 |
| director_2 | 99.9 | 75.8 |
| director_3 | 133.2 | 74.1 |

## Y1800_7EL_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| reflector | 0.0 | 86.6 |
| driven | 30.0 | 81.6 |
| director_1 | 56.6 | 77.4 |
| director_2 | 83.3 | 75.8 |
| director_3 | 111.6 | 74.1 |
| director_4 | 143.2 | 72.4 |
| director_5 | 174.9 | 70.8 |

## LPDA_800_2200_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| element_1_800mhz | 0.0 | 178.0 |
| element_2_930mhz | 28.5 | 153.1 |
| element_3_1082mhz | 53.0 | 131.7 |
| element_4_1258mhz | 74.0 | 113.2 |
| element_5_1463mhz | 92.2 | 97.4 |
| element_6_1701mhz | 107.7 | 83.7 |
| element_7_1977mhz | 121.1 | 72.0 |
| element_8_2299mhz | 132.7 | 61.9 |
| element_9_2674mhz | 142.6 | 53.3 |

## BIQUAD_1800_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| square_side | 0.0 | 41.6 |
| reflector_spacing | 0.0 | 20.8 |
| minimum_reflector_width | 0.0 | 83.3 |

## BIQUAD_2100_SEED

| Element | Position mm | Length or key dimension mm |
| --- | ---: | ---: |
| square_side | 0.0 | 35.7 |
| reflector_spacing | 0.0 | 17.8 |
| minimum_reflector_width | 0.0 | 71.4 |

## Simulation Acceptance Criteria

Before any candidate moves beyond concept, record:

- realized gain at required check points
- S11 or return loss across the sweep
- VSWR across the sweep
- feed-point impedance
- front-to-back ratio
- horizontal and vertical radiation patterns
- half-power beamwidth
- conductor diameter sensitivity
- +/- 1 mm and +/- 3 mm dimensional error sensitivity
- likely feed and balun complexity
- estimated net passive-chain improvement using `calculations/desktop_link_budget_scenarios.md`
- estimated material and fabrication cost risk

## Current Engineering Read

The first models should be simple Yagis first because they are easier to reason about and fabricate. LPDA should be simulated as a band-uncertainty hedge, not as the default winner. Biquad should be treated as a compact high-band experiment, not a 900 MHz blackout-resilience solution.
